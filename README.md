# Jeevan J Shine — Portfolio

Live at **https://jeevanxx.github.io**. Plain HTML + Tailwind CSS (compiled to `styles.css`), hosted free on GitHub Pages.

## What updates by itself (no code, no AI needed)

| What | How it updates |
|---|---|
| **Projects, stats, activity, coding-language bars** | Loaded live from GitHub every time someone opens the page. New public repos appear on their own. |
| **"Open app" button** | Appears when a repo has GitHub Pages on, or a link in its GitHub **About → Website** box. |
| **Certificates** | Upload a PDF or image into the `certificates` folder. It appears on the site and in the resume. |
| **Resume PDF** | Rebuilt by GitHub Actions after every change and every Monday, with your latest projects and certificates. |
| **Styles** | `styles.css` is recompiled automatically. |

The robot is `.github/workflows/auto-update.yml`. See it run in the **Actions** tab.
To run it right now: **Actions → Auto-update portfolio → Run workflow**.

## Everyday tasks (all on github.com, click the ✏️ pencil to edit a file, then "Commit changes")

- **Add a certificate:** open the `certificates` folder → **Add file → Upload files** → drop the PDF/image → **Commit changes**.
  The title comes from the file name (`python-basics-2027.pdf` → "Python Basics 2027").
  For a nicer title, date, issuer or ID, add an entry in `certificates/details.json`.
- **Change a project's title / description / live link, or the pinned order:** edit `projects.json`.
  A repo with no description anywhere is left off the resume (it still shows on the site).
- **Change your summary, education, skills or interests in the resume:** edit `resume-template.html`.
  (Projects and certificates in it are filled in automatically. Don't edit the PDF itself.)
- **Change website text (bio, timeline, skills):** edit `index.html` and search (Ctrl+F) for the words.
- **Change social links:** `socials` near the top of the `<script>` in `index.html`.
- **Profile photo:** replace `profile.jpg`.

Changes go live about 1–3 minutes after you commit (a little longer when the robot rebuilds the resume).

## Good to know
- GitHub pauses scheduled robots in repos with no commits for 60 days. It emails you first;
  just click **Enable workflow** on the Actions tab. Committing anything also keeps it active.
- The site itself never stops working, even if the robot is paused.
- Run the build locally (optional): `pip install playwright pypdf && python -m playwright install chromium`,
  install poppler (`pdftoppm`), then `python scripts/build.py`.

## Project thumbnails
Each project gets an illustrated thumbnail drawn in code. New repos get a generated one.
To use a real screenshot, put it in a `thumbnails/` folder and add `"thumbnail": "thumbnails/name.png"`
for that repo in the `notes` of `projects.json`.
