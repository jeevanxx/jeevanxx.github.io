#!/usr/bin/env python3
"""
Builds the auto-generated parts of the portfolio. Run by GitHub Actions
(.github/workflows/auto-update.yml) on every push, every Monday, and on demand.

  1. certificates/index.json + certificates/previews/*.jpg
     from every PDF or image in the certificates/ folder (+ optional details.json)
  2. Jeevan-J-Shine-Resume.pdf
     from resume-template.html, with Projects filled from GitHub + projects.json
     and Certificates filled from step 1. Only re-rendered when the content changes.

Usage:  python scripts/build.py [--repos-json FILE]   (FILE = saved GitHub API response, for offline testing)
Needs:  pdftoppm (poppler-utils), Python packages: playwright, pypdf
"""
import argparse, datetime as dt, hashlib, html, json, os, re, subprocess, sys, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
USER = "jeevanxx"
CERT_DIR = ROOT / "certificates"
PREVIEW_DIR = CERT_DIR / "previews"
RESUME_PDF = ROOT / "Jeevan-J-Shine-Resume.pdf"
RESUME_HASH = ROOT / ".resume-hash"
IMAGE_EXT = {".jpg", ".jpeg", ".png", ".webp"}
DOC_EXT = {".pdf"} | IMAGE_EXT
esc = html.escape


def log(*a):
    print("[build]", *a, flush=True)


def pretty(name):
    return re.sub(r"\s+", " ", re.sub(r"[-_]+", " ", name)).strip().title()


def parse_date(s):
    for fmt in ("%d %b %Y", "%d %B %Y", "%Y-%m-%d", "%b %Y", "%B %Y", "%Y"):
        try:
            return dt.datetime.strptime(s.strip(), fmt).date()
        except (ValueError, AttributeError):
            pass
    return None


def git_date(path):
    try:
        out = subprocess.run(["git", "log", "-1", "--format=%cs", "--", str(path)], cwd=ROOT,
                             capture_output=True, text=True, check=True).stdout.strip()
        return dt.date.fromisoformat(out) if out else None
    except Exception:
        return None


# ---------------------------------------------------------------- certificates
def build_certificates():
    details = {}
    if (CERT_DIR / "details.json").exists():
        details = json.loads((CERT_DIR / "details.json").read_text(encoding="utf-8"))
    files = [p for p in CERT_DIR.iterdir() if p.is_file() and p.suffix.lower() in DOC_EXT]
    groups = {}
    for p in files:
        groups.setdefault(p.stem.lower(), []).append(p)

    PREVIEW_DIR.mkdir(exist_ok=True)
    certs = []
    for stem, items in groups.items():
        pdf = next((p for p in items if p.suffix.lower() == ".pdf"), None)
        img = next((p for p in items if p.suffix.lower() in IMAGE_EXT), None)
        main = pdf or img
        if pdf and img:
            preview = img                      # an image with the same name is the preview
        elif pdf:
            preview = PREVIEW_DIR / f"{pdf.stem}.jpg"
            if not preview.exists():
                log("rendering preview for", pdf.name)
                subprocess.run(["pdftoppm", "-jpeg", "-jpegopt", "quality=82", "-r", "80", "-f", "1", "-l", "1",
                                "-singlefile", str(pdf), str(preview.with_suffix(""))], check=True)
        else:
            preview = img
        d = details.get(main.name) or details.get(main.stem) or {}
        date = parse_date(d.get("date", "")) if d.get("date") else None
        date = date or git_date(main) or dt.date.fromtimestamp(main.stat().st_mtime)
        certs.append({
            "file": f"certificates/{main.name}",
            "preview": preview.relative_to(ROOT).as_posix(),
            "title": d.get("title") or pretty(main.stem),
            "type": d.get("type", "Certificate"),
            "date": d.get("date") or date.strftime("%d %b %Y").lstrip("0"),
            "sortDate": date.isoformat(),
            "issuer": d.get("issuer", ""),
            "place": d.get("place", ""),
            "id": d.get("id", ""),
            "description": d.get("description", ""),
            "tags": d.get("tags", []),
        })
    # remove previews whose PDF was deleted
    keep = {c["preview"] for c in certs}
    for p in PREVIEW_DIR.glob("*.jpg"):
        if p.relative_to(ROOT).as_posix() not in keep:
            p.unlink()
    certs.sort(key=lambda c: (c["sortDate"], c["title"]), reverse=True)
    (CERT_DIR / "index.json").write_text(json.dumps(certs, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    log(f"{len(certs)} certificate(s)")
    return certs


# ---------------------------------------------------------------- projects
def gh_get(url):
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json", "User-Agent": "portfolio-build"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def short_url(u):
    return re.sub(r"^https?://(www\.)?", "", u).rstrip("/")


def build_projects(cfg, repos_json=None):
    repos = json.loads(Path(repos_json).read_text()) if repos_json else gh_get(
        f"https://api.github.com/users/{USER}/repos?per_page=100&sort=pushed")
    notes, pinned, hide = cfg.get("notes", {}), cfg.get("pinned", []), set(cfg.get("hide", []))
    out = []
    for r in repos:
        if r.get("fork") or r.get("archived") or r["name"] in hide or r["name"].lower() == f"{USER}.github.io":
            continue
        n = notes.get(r["name"], {})
        bullets = n.get("resume") or ([n["description"]] if n.get("description") else []) or (
            [r["description"]] if r.get("description") else [])
        if not bullets:                        # no description anywhere -> leave it off the resume
            continue
        live = n.get("liveUrl") or r.get("homepage") or (
            f"https://{USER}.github.io/{r['name']}/" if r.get("has_pages") else "")
        tech = n.get("tech")
        if not tech:
            try:
                tech = list((gh_get(r["languages_url"]) if not repos_json else {}).keys())[:5]
            except Exception:
                tech = []
            tech = tech or ([r["language"]] if r.get("language") else [])
        out.append({"name": r["name"], "title": n.get("title") or pretty(r["name"]), "bullets": bullets,
                    "tech": tech, "live": live, "repo": r["html_url"], "pushed": r.get("pushed_at", "")})
    rank = lambda p: pinned.index(p["name"]) if p["name"] in pinned else len(pinned)
    out.sort(key=lambda p: p["pushed"], reverse=True)
    out.sort(key=rank)
    for ex in sorted(cfg.get("resumeExtras", []), key=lambda e: e.get("position", 99)):
        out.insert(min(ex.get("position", 99), len(out)), {
            "title": ex["title"], "bullets": ex.get("resume", []), "tech": ex.get("tech", []),
            "live": ex.get("url", ""), "status": ex.get("status"), "label": ex.get("label", "")})
    return out


def project_html(p):
    if p.get("status"):
        tag = f' <span class="tag" style="color:#7746e1;background:#efe8ff">{esc(p["status"])}</span>'
    elif p.get("live") and p.get("repo"):
        tag = ' <span class="tag">LIVE</span>'
    else:
        tag = ""
    link = p.get("live") or p.get("repo")
    right = (f'<a class="meta link" href="{esc(link)}">{esc(short_url(link))}</a>' if link
             else f'<span class="meta">{esc(p.get("label", ""))}</span>')
    lis = "".join(f"<li>{esc(b)}</li>" for b in p["bullets"])
    tech = f'\n    <div class="tech"><b>Tech:</b> {esc(", ".join(p["tech"]))}</div>' if p["tech"] else ""
    return (f'  <div class="item">\n    <div class="row"><span class="title">{esc(p["title"])}{tag}</span>{right}</div>\n'
            f'    <ul>{lis}</ul>{tech}\n  </div>\n')


def cert_html(c):
    title = c["title"] + (f' — {c["type"]}' if c.get("type") and c["type"] != "Certificate" else "")
    sub = " · ".join(x for x in [c.get("issuer"), c.get("place"), f'ID: {c["id"]}' if c.get("id") else ""] if x)
    sub = f'\n    <div class="sub">{esc(sub)}</div>' if sub else ""
    return (f'  <div class="item">\n    <div class="row"><span class="title">{esc(title)}</span>'
            f'<span class="meta">{esc(c["date"])}</span></div>{sub}\n  </div>\n')


# ---------------------------------------------------------------- resume
def render_pdf(html_text, out_pdf):
    from playwright.sync_api import sync_playwright
    from pypdf import PdfReader
    tmp = ROOT / ".resume-build.html"
    try:
        with sync_playwright() as pw:
            browser = pw.chromium.launch()
            page = browser.new_page()
            for size in ("8.9pt", "8.7pt", "8.5pt", "8.3pt"):
                tmp.write_text(html_text.replace("</style>", f":root{{--fs:{size}}}</style>", 1), encoding="utf-8")
                page.goto(tmp.as_uri(), wait_until="networkidle")
                page.evaluate("document.fonts.ready")
                page.pdf(path=str(out_pdf), format="A4", print_background=True, prefer_css_page_size=True)
                if len(PdfReader(str(out_pdf)).pages) == 1:
                    browser.close()
                    return True
            browser.close()
            return False
    finally:
        tmp.unlink(missing_ok=True)


def build_resume(projects, certs, cfg):
    template = (ROOT / "resume-template.html").read_text(encoding="utf-8")
    projects = projects[: cfg.get("resumeMaxProjects", 6)]
    certs = certs[:4]
    fill = lambda ps: (template.replace("<!--PROJECTS-->\n", "".join(project_html(p) for p in ps))
                               .replace("<!--CERTIFICATES-->\n", "".join(cert_html(c) for c in certs)))
    digest = hashlib.sha256(fill(projects).encode()).hexdigest()   # fingerprint of the full content
    if RESUME_PDF.exists() and RESUME_HASH.exists() and RESUME_HASH.read_text().strip() == digest:
        log("resume unchanged")
        return
    while True:
        if render_pdf(fill(projects), RESUME_PDF) or len(projects) <= 3:
            RESUME_HASH.write_text(digest + "\n")
            log(f"resume rebuilt with {len(projects)} projects, {len(certs)} certificate(s)")
            return
        log("resume longer than one page; dropping the last project")
        projects = projects[:-1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repos-json")
    args = ap.parse_args()
    cfg = json.loads((ROOT / "projects.json").read_text(encoding="utf-8"))
    certs = build_certificates()
    projects = build_projects(cfg, args.repos_json)
    log("resume projects:", ", ".join(p["title"] for p in projects))
    build_resume(projects, certs, cfg)


if __name__ == "__main__":
    sys.exit(main())
