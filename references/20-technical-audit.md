# 20 — Technical audit

Find everything that stops search engines and AI systems from crawling, rendering, indexing and fast-loading the site, and turn it into a prioritized fix list.

**Inputs:** `seo-workspace/<domain>/site-profile.md` (type, platform, size tier, flags), the site URL, optional Search Console access.
**Outputs:** `seo-workspace/<domain>/audits/YYYY-MM-DD-audit.md` (Technical and Performance sections), `seo-workspace/<domain>/audits/YYYY-MM-DD-fix-list.md`, generated `sitemap.xml` when asked.

Thresholds (titles, URLs, Core Web Vitals, sitemaps, touch targets, images) live in core rules §4. AI crawler policy is in core rules §7 and is checked in 22-ai-search-readiness.md. Schema validation is in 21-schema.md. Image SEO (alt text, formats, file sizes) is in 31-visuals.md; here images matter only as the LCP element.

## When to use / skip

- **Core for every site type** (02-site-types.md §1). Landing pages: light run (one URL, steps 3, 6, 7, 9, 10 only).
- **Staging / dev flag**: run the pre-launch checklist (§10) instead of flagging `noindex`, auth or blocked bots as errors (core rules §9.3).
- **Login-gated**: audit public pages only; say so.
- **Skip** sitemap generation for one-page sites; skip pagination checks when no paginated lists exist.

## Procedure

1. **Plan the crawl by size tier** (tier from 01-intake §3c). Use the table in §1. Write the sample list into the audit file before fetching.
2. **Fetch the basics**: `/robots.txt`, every sitemap it declares (or `/sitemap.xml`, `/sitemap_index.xml`), the home page, and the sample pages. Record HTTP status, final URL after redirects, and response headers for each.
3. **robots.txt mechanics** (§2). AI bot groups: hand over to 22 §1.
4. **Indexability and canonicals** (§3) on every sampled page.
5. **Status codes and redirects** (§4): follow every redirect chain to the end.
6. **Raw vs rendered HTML** (§5) on the home page and one page per template.
7. **Core Web Vitals** (§6): run PageSpeed Insights for the home page and the top template pages, mobile first (60-measurement.md §4); diagnose with LCP subparts, INP causes, CLS causes.
8. **Mobile and above the fold** (§7).
9. **Security and HTTPS** (§8): passive signals only.
10. **Single-page deep check** (§9) on the 1–5 most important pages (home, top money page, top article).
11. **Sitemaps** (§11): audit; generate if missing or broken and the user wants one.
12. **URL structure, pagination, internal reach** (§12).
13. **Score and prioritize**: Technical and Performance categories of SEO Health (core rules §2), only over what was measured. Assign priority levels (core rules §2) and apply the relevance check (core rules §3).

### 1. Crawl strategy by size tier

All tiers: polite crawl rate (core rules §8), follow at most 3 redirect hops, respect robots.txt, 30 s timeout, back off on 429, never spoof a bot user agent (core rules §8).

| Tier | What to fetch |
|---|---|
| XS | Every URL (sitemap + links from home) |
| S | Every template plus every key page; all URLs if time allows |
| M | 3–5 URLs per template (home, category, product/article, service, location, blog index, paginated page 2) plus top 20 pages (Search Console if available); stop near 150 fetches |
| L | Sampling by section, one section at a time (stop near 300 fetches); Search Console Pages report is the primary data |
| XL | Template sampling only; focus on index coverage, crawl budget, faceted URLs, log files if offered; say a full crawl is out of scope |

- Identify templates by URL pattern (`/blog/*`, `/products/*`) and layout.
- If a paid crawler or SEO data tool is available (Screaming Frog, Sitebulb, DataForSEO, Ahrefs, Semrush, SE Ranking, Moz…), use its export and label the source; otherwise use the sample method.
- If you can run code: `node scripts/aeo-audit.mjs <url> --max-pages=15 --out=seo-workspace/<domain>/audits/YYYY-MM-DD-aeo-audit.json` crawls up to N pages (default 10, max 30) and checks titles, meta, canonical, H1, noindex, links and robots. Its scoring belongs to 22.

### 2. robots.txt mechanics

| Check | Pass | Severity if failing |
|---|---|---|
| Reachable | `/robots.txt` returns 200 (or 404 = no rules). A 5xx makes compliant crawlers treat the whole site as blocked; Google treats 429 like a server error | Critical (5xx) |
| No accidental site block | No `Disallow: /` in `User-agent: *` on a live site | Critical |
| Resources crawlable | CSS, JS, images and fonts needed to render are not disallowed | High |
| Correct tool for the job | `noindex` is not attempted via robots.txt (unsupported). A page blocked in robots.txt cannot show its `noindex` | High |
| Group selection | Bots that have their own group get the needed `Disallow` lines repeated there (core rules §7) | Medium |
| Sitemap line | `Sitemap: https://…/sitemap.xml` with an absolute URL | Low |
| Private areas | Admin, cart, account protected by login, not only by robots.txt | Medium |

Googlebot reads only the first 2 MB of an HTML file *(perishable, verified 2026-09)*: keep main content and JSON-LD near the top and avoid huge inline scripts or base64 images.

### 3. Indexability and canonicals

| Check | How | Pass |
|---|---|---|
| Meta robots / `X-Robots-Tag` | Read `<meta name="robots">`, `<meta name="googlebot">` and the response header | No `noindex` on pages meant to rank; intentional `noindex` on thank-you, internal search, cart, filters |
| Canonical present and absolute | `<link rel="canonical">` | One per page, absolute URL, self-referencing on indexable pages |
| Canonical consistency | Compare canonical with final URL, `og:url`, sitemap URL, internal links, hreflang | All point to the same version (https, www or not, trailing slash) |
| No conflicts | Canonical points to a 200, indexable page; never canonical + `noindex` together | — |
| Duplicates | Same content on http/https, www/non-www, trailing slash, parameters, print versions | One version answers 200; others 301 to it |
| Index check | `site:` (approximate) or Search Console Pages / URL Inspection | Key pages indexed; note "Crawled – not indexed" patterns |
| Thin templates | Word count vs coverage floors (core rules §4) | Flag for 30-content-creation.md |

After a canonical fix, Google can take up to about two weeks to re-cluster duplicates *(perishable, verified 2026-09)*; don't call the fix failed earlier.

### 4. Status codes and redirects

- Permanent move: 301/308 straight to the final URL, max 1 hop (core rules §4). 302/307 only when truly temporary.
- Removed for good: 410 or 404 with a helpful page; redirect only to a genuinely equivalent page.
- Soft 404 ("not found" or empty page answering 200) → real 404. Meta refresh or JS redirects → server-side 301.
- Loops, chains and redirects to 404 on key pages: Critical. Internal links to redirects or 404s: update to the final URL.
- 5xx on sample pages: Critical; recheck twice before reporting.

Google does not render JavaScript on non-200 pages: anything injected by JS on an error page is invisible.

### 5. JavaScript rendering: raw vs rendered HTML

1. **Raw HTML**: view source (`view-source:` in the browser) or fetch without running scripts.
2. **Rendered HTML**: browser DevTools → Elements (copy outer HTML), or the free Rich Results Test / Search Console URL Inspection "View tested page" (shows Google's rendered HTML and screenshot). Manual fallback: disable JavaScript in the browser and reload.
3. Compare in a table:

| Element | Raw | Rendered | Problem if different |
|---|---|---|---|
| `<title>`, meta description | | | Google may use either |
| Meta robots | | | `noindex` in raw HTML may be honoured even if JS removes it |
| Canonical | | | Conflicting canonicals: Google may pick either |
| H1 and main text (word count) | | | Content invisible to AI crawlers that don't run JS |
| Internal links (`<a href>`) | | | Links added only by JS or via `onclick` may not be crawled |
| JSON-LD | | | JS-injected structured data is processed late; keep Product/Offer server-side |

4. Verdict: **SSR/SSG** (all present raw) = pass. **Hybrid** (shell raw, content JS) = High. **CSR only** (empty `<div id="root">`) = Critical for public pages. Dynamic rendering = technical debt, recommend SSR/SSG (fix how-to per framework in 03-platforms.md).
5. Infinite scroll and "load more" need real paginated URLs with `<a href>` links behind them.

### 6. Core Web Vitals diagnosis

Thresholds: core rules §4. Field data (CrUX) beats lab data; never mention FID.

Run the tools (PageSpeed Insights, CrUX, field vs lab, no-field-data handling): 60-measurement.md §4. Then diagnose with the tables below.

**LCP: find the slow subpart** (LCP = TTFB + resource load delay + resource load duration + element render delay):

| Subpart | Rough healthy share (web.dev guidance) | Typical causes | Fixes |
|---|---|---|---|
| TTFB | ~40% | Slow server, no caching, redirects, no CDN | Page/edge caching, CDN, fewer redirects, faster hosting |
| Resource load delay | <10% | LCP image found late (CSS background, JS-inserted, lazy-loaded) | `<img>` in HTML, `fetchpriority="high"`, preload, never lazy-load it (core rules §4) |
| Resource load duration | ~40% | Heavy image, no responsive sizes, slow third-party host | Compress, WebP/AVIF, `srcset`, same-origin or CDN hosting (details in 31-visuals.md) |
| Element render delay | <10% | Render-blocking CSS/JS, web fonts, client-side rendering, A/B-test scripts hiding the page | Inline critical CSS, `defer`/`async` JS, `font-display: swap`, SSR |

**INP: find the slow interaction**: long main-thread tasks (>50 ms) from big JS bundles, heavy event handlers, third-party tags (chat, ads, tag managers, heatmaps), large DOM (roughly >1,500 nodes), layout thrashing, synchronous storage or XHR. Fixes: split and defer JS, yield to the main thread, remove unused tags, debounce handlers, reduce DOM size, use CSS for animations.

**CLS: find what moves**: images, video and iframes without `width`/`height` or `aspect-ratio`; ads and embeds without reserved space; banners or consent bars injected above content; web fonts swapping metrics (use `size-adjust` or matching fallback fonts); content inserted after load. Fixes: reserve space, put injected UI in overlays or at the bottom, preload key fonts.

SPA note: CrUX counts hard navigations only; route changes in single-page apps are not reflected *(perishable, verified 2026-09)*.

### 7. Mobile and above the fold

Google indexes with a smartphone crawler; the risk is lost content, not exclusion.

- [ ] Viewport meta `width=device-width, initial-scale=1` present.
- [ ] Check at 375×812 (phone) and 1366×768 (laptop), plus 768×1024 if tablets matter: DevTools device mode, a real phone or user screenshots.
- [ ] No horizontal scrolling; text readable without zoom (~16 px base is practice, not a rule); no overlapping or cut-off elements.
- [ ] H1 and the primary call to action visible without scrolling on mobile.
- [ ] Touch targets meet core rules §4; tap-to-call on local sites; menu works without hover.
- [ ] **Parity**: mobile has the same main content, headings, links, structured data, title, meta and robots tags as desktop.
- [ ] No intrusive interstitials (full-screen pop-ups on arrival, consent walls); small banners and legal dialogs are fine.
- [ ] Key content visible on load, not only inside tabs or accordions.

### 8. Security and HTTPS (passive only)

- **HTTPS**: http → https 301, valid certificate not near expiry. Broken HTTPS = Critical (HTTPS itself is only a light ranking signal). Mixed content (`http://` scripts, images, iframes) = High.
- **Headers** (HSTS, CSP, `X-Content-Type-Options`, frame protection, `Referrer-Policy`): security hygiene, Low for SEO, not ranking signals.
- **Back-button hijacking** (scripts trapping the Back button): Google spam policy *(perishable, verified 2026-06)*, Critical.
- **Hacked signals**: `site:` results with foreign-language pharma/casino pages, odd redirects for search visitors: Critical; refer to the host or security team.

Software exposure: read only what a normal response shows (`Server`, `X-Powered-By` version, CMS generator tag). If a version looks outdated, tell the owner to confirm patch status with their host; say a version string alone is not proof. Request any other path or run any test **only after the user confirms they own or manage the site**, and never probe for vulnerabilities, fuzz or load-test (core rules §8).

### 9. Single-page deep check (manual checklist)

Mark each ✓ / ✗ / n/a with the evidence quoted. Thresholds from core rules §4.

| Area | Checks |
|---|---|
| Title and description | Title present · within core length range · unique · no duplicate `<title>` or duplicate meta tags · meta description present and within range · title topic reflected in the body · description matches the content |
| Headings | Exactly one H1 · no skipped levels in main content |
| Canonical and robots | Canonical present · not pointing elsewhere by mistake · `og:url` equals canonical · no unintended `noindex` (meta or header) · no unintended `nofollow` · no meta refresh redirect · hreflang includes self (if used, 52-international.md) |
| Document basics | `<!doctype html>` · charset declared and matching the header · `<html lang>` · viewport meta · no frames · no deprecated tags (`<font>`, `<center>`) · no placeholder text ("Lorem ipsum", "Sample page") |
| Images (performance view) | Width and height set · first/LCP image not lazy-loaded · alt present (quality: 31-visuals.md) |
| Links | Every link has text or an accessible name · no generic anchors ("click here", "read more") for key links · no links to `http://` versions · no mixed content |
| URL | Within core length guidance · no tracking/session parameters · lowercase · hyphens not underscores · ASCII or properly encoded · no `//` in the path |
| Size | HTML under 2 MB · DOM not excessively deep or wide (roughly >1,500 nodes is heavy) |
| Social and schema | `og:title`, `og:description`, `og:image` present · JSON-LD parses (validate with 21-schema.md §6) |
| Content | Word count vs coverage floor for its page type · not thin |

Judge context: `noindex` on a thank-you page is correct; thin content on a contact page is fine; two H1s rarely matter alone.

### 10. Staging and pre-launch

On staging, `noindex`, password protection and `Disallow: /` are **correct**. Instead of errors, deliver this checklist for launch day:

- [ ] Remove site-wide `noindex` (meta and `X-Robots-Tag`), staging `Disallow: /` and password protection on production; keep the staging host itself behind auth.
- [ ] Canonicals, hreflang, sitemap and `og:url` use the production domain.
- [ ] Migrations: 301 map from every old URL; test 20 sample redirects.
- [ ] Sitemap submitted in Search Console and Bing Webmaster Tools; analytics and verification tags present (60-measurement.md).
- [ ] Re-run §5–§9 on production within 48 hours.

### 11. Sitemaps (audit and generation)

**Audit:**

| Check | Severity if failing |
|---|---|
| Found via robots.txt or common paths; 200 and valid XML (gzip allowed) | High |
| Per-file limits (core rules §4); index used when over; no index inside an index | Critical |
| Only 200, indexable, canonical, https URLs (sample 20 per file) | High; Medium for redirects |
| `lastmod` in W3C format and true; all-identical values are not trusted | Low |
| Key pages missing, sitemap URLs not linked anywhere, URLs on another host | Medium |
| `priority`/`changefreq` (ignored by Google); image/video/news extensions valid (news = last 2 days only) | Info / Low |

**Generate** (only for real, indexable pages; quality gates for location and programmatic pages are in core rules §4 and 13-strategy-and-plan.md):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://example.com/</loc><lastmod>2026-11-01</lastmod></url>
  <url><loc>https://example.com/services/</loc><lastmod>2026-10-14</lastmod></url>
</urlset>
```

Split by type when large (`sitemap-pages.xml`, `sitemap-posts.xml`, `sitemap-products.xml`) and list the files in a `<sitemapindex>` with the same namespace. Prefer the platform's built-in sitemap (03-platforms.md) over a hand-made file that goes stale.

### 12. URL structure, pagination, internal reach

- URLs follow core rules §4; one consistent trailing-slash style; folder hierarchy mirrors the site structure.
- Parameter URLs (sort, filter, tracking) are canonicalized or kept out of the index (deep rules for stores in 51-ecommerce.md).
- Pagination: each page has crawlable `<a href>` links to the next pages and a self-referencing canonical (not canonical to page 1). `rel=next/prev` is not used by Google.
- Click depth and internal links per core rules §4; find orphan pages by comparing sitemap URLs with crawled links. Internal-link planning is in 13-strategy-and-plan.md.
- IndexNow for Bing and others: setup in 60-measurement.md.

## Output format

```markdown
## Technical audit — <domain> — YYYY-MM-DD
Crawl: <tier>, <N> URLs fetched (crawl), method: <sample/full/tool name>
Technical score: XX/100 (coverage XX%) · Performance score: XX/100 or "not measured"

| Area | Status | Key evidence (source) |
|---|---|---|
| robots.txt · Indexability · Redirects · JS rendering · Mobile · Security · Sitemaps · URLs (one row each) | pass/warn/fail | e.g. "canonical → http version on 12/40 pages (crawl)" |
| Core Web Vitals (mobile) | | e.g. LCP 3.1 s (CrUX field), INP 180 ms (CrUX field), CLS 0.02 (CrUX field) |

### Findings
| # | Priority | Finding (observation) | Why it matters | Fix (platform-specific, see 03) | Effort | How we'll verify |
|---|---|---|---|---|---|---|

### Not measured
- <item> — reason — access that would unlock it
```

The fix list (`YYYY-MM-DD-fix-list.md`) uses the developer format in 03-platforms.md.

## Fallbacks and "not measured"

| Missing ability | Do this |
|---|---|
| Can't fetch pages | Ask for view-source HTML of key pages, `robots.txt`, sitemap and mobile + desktop screenshots; status codes and redirects = "not measured" |
| Can't run code | PageSpeed website, DevTools, Rich Results Test rendered HTML, manual checklists above |
| No field data | Use lab values labelled `PageSpeed (lab)`; none at all → Performance "not measured", left out of the score |
| No Search Console | `site:` searches marked "approximate"; recommend connecting it |
| Large site, no crawler | Template sampling; state the share of URLs checked |
| No ownership confirmation | Normal-response security signals only |
