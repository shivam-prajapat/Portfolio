# Shivam Kumar — Portfolio

Static, responsive portfolio in a warm editorial style with ink-dark AI project diagrams, coral signal accents, and teal data paths. The page is plain HTML, CSS, and JavaScript; it has no build step or runtime dependency. Google Fonts are loaded when a network connection is available, with local system fallbacks.

## Preview

Open `index.html` in a browser. For a local server, run `python -m http.server 8000` from this folder and visit `http://localhost:8000`.

## Photo assets

- `assets/shivam-portrait.webp` — cropped and lightly color-corrected from the supplied seated portrait.
- `assets/shivam-event.webp` — resized and lightly color-corrected from the supplied event photo.
- `scripts/prepare_photos.py` records the non-generative crop and tonal adjustments. To regenerate, pass the original files with `--portrait` and `--event` arguments.

The Gemini-generated portrait was not included because its synthetic appearance and watermark conflict with the request to keep the face authentic. The two natural photos are used without generative face edits.

## Content and link notes

The supplied résumé provides project stacks and reported performance figures. The Bluestock experience is expanded and its three reported outcomes are prominent; education details remain in the résumé. The Multiple Disease Prediction System demo URL was already present as a clickable résumé link and is retained on the site. The other featured projects link to their source repositories. GitHub repository pages could not be fetched in this environment, so the site uses the exact repository URLs supplied by Shivam. Project visuals remain conceptual and no clinical validation is claimed.

Design references and limitations are recorded in [portfolio-creative-direction.md](portfolio-creative-direction.md). Razorpay content informed the problem-to-build-to-impact narrative; the supplied Pinterest short links were inaccessible to the reference viewer.
