# timlouiswilken.github.io

Personal website of Tim-Louis Wilken, served by GitHub Pages at <https://timlouiswilken.github.io>.
Plain HTML and CSS, no framework, no build tool beyond one Python script.

## Layout

| Path | What it is |
|---|---|
| `index.html` | The home page: hero, live forecast widget, project cards, experience, education. Hero, experience and education are edited here directly. |
| `build.py` | Single source of truth for the **projects**. It holds a `PROJECTS` list and generates the project cards in `index.html` (between the `PROJECTS:START/END` markers) and one page per project in `projects/`. |
| `projects/*.html` | Generated project pages. Do not edit by hand; edit `build.py` and rebuild. |
| `style.css` | All styling. Colours and fonts are CSS variables at the top (`--accent`, `--font-sans`, …). |
| `images/profile.jpg` | Portrait (metadata stripped). |
| `images/projects/` | Project images. Each card uses one image; project pages can add a gallery. |
| `cv.pdf` | CV download, built from `cv_src/cv.tex`. |
| `favicon.svg` | Tab icon. |

## Editing projects

Each entry in `PROJECTS` in `build.py` is a dictionary:

| Key | Meaning |
|---|---|
| `slug` | File name of the project page (`projects/<slug>.html`). |
| `title`, `year` | Title, and the small year label shown on the project page (cards show no year). |
| `image`, `alt` | Card image in `images/projects/` and its alt text. |
| `contain` | `True` shows the whole image with padding (charts); otherwise the image fills the frame and is cropped. |
| `position` | CSS `object-position` for cropped images, e.g. `"center 75%"`. |
| `metric` | Alternative to an image: `("340 GW", "caption")` renders a large number instead. |
| `detail_image`, `detail_natural` | Optional separate image for the project page; `detail_natural: True` shows it at full height. |
| `card` | Two to three sentences on the card. |
| `summary` | One sentence under the title of the project page. |
| `tags` | Small labels. |
| `links` | List of `("Label", "https://…")`, shown on the card and the page. |
| `cta` | Optional `("Button text", "https://…")`, rendered as a prominent button on the page. |
| `body` | Paragraphs on the project page. |
| `highlights` | Bullet list "Highlights". |
| `caveats` | Optional bullet list "Limitations". |
| `gallery` | Optional list of `("file.png", "caption")`, shown below the text. |

The order of the list is the order of the cards. After any change:

```bash
python3 build.py
```

## Live forecast widget

The card under the hero fetches `https://timlouiswilken.github.io/gb-dayahead-forecast/data/latest.json`
(the day-ahead forecast published every morning by the online forecasting pipeline;
code and methodology in [gb-dayahead-research](https://github.com/TimLouisWilken/gb-dayahead-research))
and `history.json` (realised daily errors). It draws the day's hourly point forecast with the 90 % band
and shows day average, peak, low and the mean realised MAE of the last seven days against the naive forecast.
If the feed is unavailable the card stays hidden. The code is in the last `<script>` block of `index.html`.

## Preview locally

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

Use a server rather than opening the file directly, otherwise the live widget cannot fetch the JSON.

## CV

`cv_src/cv.tex` is a copy of the current CV (Times New Roman via `fontspec`, so it needs XeLaTeX or tectonic):

```bash
cd cv_src && tectonic cv.tex && cp cv.pdf ../cv.pdf
```

## Deploy

The repository is `TimLouisWilken/TimLouisWilken.github.io`; GitHub Pages serves the `main` branch root.
Every push to `main` is live within about a minute.

```bash
python3 build.py
git add -A && git commit -m "Update" && git push
```

## Conventions

- British English, no em dashes in running text, a space before units and percent (`93 %`, `50 MW`).
- Images: PNG for charts, JPEG for photos, longest side about 1,600 px, metadata stripped.
- Every project card links to code or a live demo where one exists; links are shown as text, not hidden behind titles.
