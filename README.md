# Jeevan J Shine — Portfolio

Personal portfolio site. Plain HTML + Tailwind CSS, compiled to `styles.css`.

## Styles (important)
Styling comes from `styles.css`, built from the Tailwind classes used in `index.html`.
If you add **new** Tailwind classes, rebuild it (needs Node.js):

```
npx tailwindcss@3 -c tailwind.config.js -i tailwind.input.css -o styles.css --minify
```

Theme colours, fonts and spacing live in `tailwind.config.js`.

## Preview locally
Open `index.html` in a browser, or run `node server.js` and visit http://localhost:3000

## What updates automatically
The **Projects**, **Activity**, **Languages** and stats sections load live from
GitHub (`github.com/jeevanxx`) every time someone opens the page.
New public repos appear on their own; forks are skipped.

## How to edit
Everything personal is in `SITE_CONFIG` at the top of the `<script>` in `index.html`:

- `github.pinned` — which repos show first, in order
- `github.hideRepos` — repo names to hide
- `projectNotes` — nicer titles/descriptions for repos (repos not listed use their GitHub description)
- `socials` — links shown in the hero and contact section

Text (bio, journey timeline, skills) is plain HTML in `index.html` — search for the words you want to change.

## Profile photo
Your photo is `profile.jpg` next to `index.html`. Replace that file to change it.

## Project thumbnails
Each project gets an illustrated thumbnail (drawn in code, follows the colour theme). New repos get a generated one automatically. To use a real screenshot, put it in a `thumbnails/` folder and add `thumbnail: 'thumbnails/name.png'` for that repo in `projectNotes`.
