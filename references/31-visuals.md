# 31 — Visuals: charts, image SEO and social images

Make charts that people and AI can both read, audit and optimize images, and set Open Graph and social images.

**Inputs:** the draft (`content/drafts/<slug>.md`) or page URL, the data behind a chart (with sources), the site's brand colours and font, `site-profile.md`
**Outputs:** per chart in `content/drafts/<slug>-charts/`: `<chart-name>.html` (or `.svg`), `<chart-name>.csv`, and the text layer pasted into the draft; image findings in `audits/YYYY-MM-DD-audit.md` (or `audits/YYYY-MM-DD-image-audit.md` for a quick task); optimized files in a new folder next to the originals

## When to use / skip

- **Charts:** when a page has data that answers "which is better", "how has X changed" or "how does X work". Add a chart only when it carries data, explains a process or proves a claim. Decorative graphics add nothing.
- **Image audit:** core for image-heavy sites (portfolio, e-commerce, publisher; 02-site-types §1); light elsewhere.
- **Social images:** every indexable page that gets shared (home, posts, products, landing pages).
- Not here: hero image as an LCP problem (20-technical-audit), `ImageObject`/`Dataset` property details (21-schema), product image feeds (51).

## Procedure A: a chart AI can read

**Core idea: AI cites text, not pixels.** The chart is for people; the heading, summary, table, CSV and Dataset markup are what machines read.

1. **Get the data and its source.** Ask for: data (or approve research), the point the chart makes, where it will live, and the comparison type. Every number needs a source with date; no source, no chart. Synthesis from several sources: list each.
2. **Pick the chart type.**

| Data pattern | Chart | Value for AI answers |
|---|---|---|
| A vs B vs C | Comparison bar | Very high ("which is better") |
| Rankings or scores | Horizontal bar | Very high (ranked lists) |
| Change over time | Line | High ("how has X changed") |
| Part of a whole | Donut/pie, max 5 segments | Medium |
| Multi-criteria | Radar, always with a table | Medium |
| Process or decision | Flowchart / decision tree | High ("how does X work") |
| Feature comparison | Matrix/checklist table | Very high (direct extraction) |

3. **Build it.** Preferred: inline SVG in the HTML (text stays crawlable). Alternatives: a Mermaid diagram for Markdown sites, a chart-library config for interactive charts, or an exported WebP/SVG file. SVG rules:
   - All labels as `<text>` elements, never converted to paths.
   - Root `<svg role="img" aria-labelledby="t1 d1">` with `<title id="t1">` and `<desc id="d1">`.
   - Inline the SVG (not `<img src>`) when you want its text crawlable.
   - Contrast ≥3:1 for marks, ≥4.5:1 for text; never use colour alone to carry meaning (add labels or patterns).
4. **Apply the design rules** (below).
5. **Write the text layer** (below) and the **HTML data table**.
6. **Add Dataset markup** (below); validate per 21-schema.md.
7. **Name and caption the file:** descriptive hyphenated filename, conclusion-style alt text, `<figure>` + `<figcaption>`.
8. **Visual QA:** open the HTML file in any browser and check the QA table; fix and re-check. If you cannot render, ask the user to open it and send a screenshot, or say "visual QA not done".
9. **Link it:** link the chart from related posts with an anchor stating the finding; on a standalone data page, link back to the guides and comparisons that use it.

### Design rules

| Element | Rule |
|---|---|
| Colours | Max 3 per chart: one accent for the key data point (the brand's primary colour), greys for the rest; red only for negative/risk, green only for positive change; white or page background, never a coloured chart background |
| Type | One font family (the site's body font or `system-ui, sans-serif`). Title 18–20 px bold · subtitle 14–15 px · axis 11–12 px · data labels 12–13 px semibold · source 11 px muted |
| Layout | No border or box; generous padding; 640–800 px wide; viewBox about 680 px wide with ≥20 px clear on every side |
| Gridlines | Remove them and the value axis when values are labelled on the bars; faint horizontal lines only when >10 points; never vertical gridlines on bar charts; baseline 1 px |
| Labels | Values directly on or beside bars/points; legend only when unavoidable (bottom, horizontal) |
| Title | An **action title**: a full sentence stating the takeaway ("Updated pages earned more citations in 2025"), never "Chart 1" or a topic label |
| Annotations | 1–2 thin-line callouts at most; if it needs more, simplify the chart |
| Source line | Always, small, below: `Source: [Org], [Year]. N=[sample]. [1-line method].` |
| Never | 3D, gradients, shadows, decorative icons, rainbow palettes, pie >5 segments, radar without table |

### Text layer (required for every chart)

| Piece | Where | Rule |
|---|---|---|
| Takeaway heading | H2 on a standalone data page, H3 inside an article | States the finding with a number |
| Key finding summary | Directly above the chart | 40–60 words, names the subject (no "it"/"this"), ≥1 number, stands alone: "[Subject] [did X] by [number]. Based on [method] of [N items] from [dates], … [One practical implication]." |
| Source and method line | Directly below | Org, year, sample, date range, 1-sentence method |
| "What this means" | After the chart | 2–3 sentences: interpretation, who should act and how, one named comparison point |
| HTML data table | After the chart | See below |
| CSV download | Under the table | `<a href="<chart-name>.csv" download>Download the data (CSV)</a>` |

Data table rules: `<figure>` + `<figcaption>`, `<table>` with `<caption>`, `<thead>`, `<tbody>`, `<th scope="col">` / `<th scope="row">`; units in headers, not cells; values identical to the chart; in the server HTML, not injected by JavaScript.

### Dataset JSON-LD

Use the `Dataset` template in 21-schema.md. Fill: `name` (takeaway heading), `description` (key finding summary), `temporalCoverage` (`YYYY-MM/YYYY-MM`), `variableMeasured` (`PropertyValue` with `name` and `unitText`), `creator` (the site's Organization `@id`), `datePublished`, `distribution` (`DataDownload`, `text/csv`, CSV URL), `image` (chart URL). **`license`: ask the owner** which licence the data is published under (e.g. all rights reserved, CC BY 4.0); never set one by default. If the data is someone else's, credit the original creator and don't claim it as your dataset; omit Dataset markup for third-party data you merely re-chart unless the owner confirms the rights.

### Visual QA

| Issue | Look for |
|---|---|
| Overflow | Labels or callouts past the right or top edge of the viewBox |
| Clipping | Data labels cut off above the tallest bar or below the baseline |
| Overlap | Labels colliding, especially many horizontal bars |
| Misalignment | Labels not centred on their bars/points |
| Axis mismatch | Bar lengths not matching the values or scale |
| Readability | Text too small at real size; low contrast; dark mode turns text invisible |

Fixes: shorten text, break long callouts into `<tspan>` lines (wrap above ~200 px), increase viewBox height rather than squeezing.

## Procedure B: image SEO audit

1. **List images** on each page sampled (size tier sampling: 01 §3c): `src`, served format, bytes, `alt`, `width`/`height`, `loading`, `fetchpriority`, `srcset`/`sizes`, filename, above or below the fold.
2. **Judge the served file, not the URL extension.** Many CDNs and plugins serve WebP/AVIF from a `.jpg` URL. Check the response `Content-Type` (browser dev tools → Network, or fetch with an `Accept: image/avif,image/webp` header). Can't fetch the image → "format not measured"; don't guess from the extension. Never suggest a replacement URL you have not confirmed returns 200.
3. **Check each item:**

| Check | Pass rule |
|---|---|
| Alt text | Present on meaningful images, describes the image, length per core rules §4; `alt=""` for decoration (don't flag those). No "image", filenames or keyword lists |
| Charts and infographics | Alt states the conclusion, not "bar chart"; the full data is in a table on the page |
| File size | Within the hero / content / thumbnail targets in core rules §4 |
| Format | WebP or AVIF (core rules §4); SVG for logos, icons, diagrams; JPEG/PNG only as `<picture>` fallback |
| Dimensions | `width` and `height` attributes or CSS `aspect-ratio` on every image (prevents CLS) |
| Responsive | `srcset` + `sizes` for content wider than ~400 px |
| Loading | `loading="lazy"` + `decoding="async"` below the fold; never lazy-load the LCP image, give it `fetchpriority="high"` (core rules §4). A JS lazy-loader (`data-src`, `lazyload` class) is not a missing attribute; note it |
| Filename | Lowercase, hyphenated, descriptive (`blue-running-shoes.webp`, not `IMG_1234.jpg`) |
| Context | Image sits near text that explains it; captions where useful |
| Delivery | Large image sites: CDN with caching headers |
| CSS/JS images | Important images (products, charts) as `<img>`, not CSS backgrounds |

4. **Rank fixes** by bytes saved and LCP impact; LCP image first. Priority levels per core rules §2.

What matters for image search: alt text, filename, surrounding page text and speed. Embedded IPTC creator/copyright fields only affect display and attribution in image results, not ranking; EXIF camera data and IPTC keywords are ignored. Optional extras: licence info via `ImageObject` (21) for photographers and stock sellers; AI-generated product images in a merchant feed need the IPTC digital-source-type label *(perishable, verified 2026; see 51-ecommerce)*.

## Procedure C: optimization pipeline

Work on copies in a new folder; keep originals. **Tools (any one is enough):** ImageMagick 7 (`magick`), `cwebp`/`avifenc` (libwebp, libavif), `exiftool` for metadata, or Node with the `sharp` package. All run on Windows, macOS and Linux.

1. **Check tools:** `magick -version`, `cwebp -version`, `exiftool -ver`, `node -v`.
2. **Resize** to the largest size actually displayed (×2 for high-density screens at most).
3. **Convert** (single files; same syntax in PowerShell and bash):
   ```
   magick input.jpg -resize 1200x -quality 82 output-1200.webp
   magick input.jpg -resize 800x  -quality 82 output-800.webp
   magick input.jpg -resize 400x  -quality 82 output-400.webp
   cwebp -q 82 -metadata all input.jpg -o output.webp
   avifenc -q 60 input.jpg output.avif
   ```
   Batch with Node (`npm i sharp`, save as `optimize.mjs`, run `node optimize.mjs <in-folder> <out-folder>`):
   ```js
   import sharp from 'sharp'; import fs from 'node:fs'; import path from 'node:path';
   const [inDir, outDir] = process.argv.slice(2); fs.mkdirSync(outDir, { recursive: true });
   for (const f of fs.readdirSync(inDir).filter(f => /\.(jpe?g|png)$/i.test(f))) {
     const base = path.parse(f).name;
     for (const w of [400, 800, 1200]) {
       await sharp(path.join(inDir, f)).resize({ width: w, withoutEnlargement: true })
         .webp({ quality: 82 }).toFile(path.join(outDir, `${base}-${w}.webp`));
     }
   }
   ```
4. **Metadata (optional):** check with `exiftool -IPTC:all -XMP:all file.webp`; add creator/copyright only with the owner's details. WebP holds XMP, not IPTC; `exiftool` maps it.
5. **Verify** sizes against core rules §4 and compare visually with the original.
6. **Write the HTML:**
   ```html
   <picture>
     <source type="image/avif" srcset="shoe-400.avif 400w, shoe-800.avif 800w" sizes="(max-width: 600px) 100vw, 800px">
     <source type="image/webp" srcset="shoe-400.webp 400w, shoe-800.webp 800w" sizes="(max-width: 600px) 100vw, 800px">
     <img src="shoe-800.jpg" alt="Blue trail running shoe, side view" width="800" height="600" loading="lazy" decoding="async">
   </picture>
   ```
   On a CMS, use its built-in image optimisation or plugin instead (03-platforms).

## Procedure D: Open Graph and social images

Sizes *(perishable; re-check each platform's docs before quoting)*:

| Use | Size / ratio | Notes |
|---|---|---|
| Open Graph / link preview (most platforms) | 1200×630 px (1.91:1) | Treat 1200×630 as the minimum; keep text and logo in the centre safe area |
| Large-image card on X | Use the same 1200×630 file | Set `twitter:card` = `summary_large_image` |
| Blog hero | 16:9 | Also feeds Discover (≥1200 px wide, 02-site-types §6) |
| Schema/article image | Provide 16:9, 4:3 and 1:1 crops | Listed in Article markup (21) |
| Social square | 1:1 (e.g. 1080×1080) | |
| Pinterest | 2:3 (e.g. 1000×1500) | |
| Favicon / app icon | 512×512 source; export 32×32 and 180×180 | Simple mark, readable at 16 px |

Tags on every shareable page (absolute HTTPS URLs; page-specific image where possible, site default otherwise):

```html
<meta property="og:title" content="…">
<meta property="og:description" content="…">
<meta property="og:url" content="https://example.com/page">
<meta property="og:type" content="article">
<meta property="og:image" content="https://example.com/images/page-og-1200x630.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="…">
<meta name="twitter:card" content="summary_large_image">
```

Use JPEG or PNG for `og:image` if a target platform does not show WebP previews. Check with each platform's own link-preview or sharing debugger.

## Output format

**Chart package** (per chart):
```
1. Takeaway heading: <h2|h3>…</h2|h3>
2. Key finding summary (40–60 words)
3. Chart: inline SVG / Mermaid / config — file: content/drafts/<slug>-charts/<chart-name>.html
4. Source and method line
5. What this means (2–3 sentences)
6. HTML data table
7. CSV: <chart-name>.csv
8. Dataset JSON-LD (licence: <owner's answer>)
9. Image metadata — filename, alt text (conclusion), figcaption
10. Visual QA: passed / not done (why)
```

**Image audit:**
```
IMAGE AUDIT — <domain> — YYYY-MM-DD (source: crawl | manual | user-provided)
| Metric | Count | Status |
| Images checked | 48 | – |
| Missing alt (meaningful images) | 9 | High |
| Over size target | 14 | Medium |
| Not WebP/AVIF (served format) | 11 | Medium |
| No width/height | 6 | Medium |
| LCP image lazy-loaded | 1 | High |
| Pages without og:image | 3 | Medium |
Fix list (largest savings first): | Image | Page | Bytes | Served format | Issues | Fix | Est. saving |
Not measured: <what and why>
```

## Fallbacks and "not measured"

- **No fetch:** ask for page source or a list of image URLs with sizes (browser dev tools → Network → filter "Img"); mark served format and bytes "not measured" if not given.
- **Can't run code:** do conversions in the CMS's image settings or any free in-browser image compressor, one image at a time; write the HTML by hand.
- **Can't render charts:** deliver the SVG and ask the user to open the file in any browser and confirm or screenshot; mark visual QA "not done".
- **No data source for a chart:** don't make the chart; suggest a table of sourced facts or original research the business could run.
- **No brand colours:** use a neutral grey palette with one blue accent and say so.
