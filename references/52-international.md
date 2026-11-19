# 52 — International SEO

Make each language or country version findable by the right audience: correct hreflang, clean language/region targeting, real content parity, correct local formats, and translations a native speaker would accept.

**Inputs:** `seo-workspace/<domain>/site-profile.md` (markets and languages), crawl data from 20-technical-audit.md, `research/keywords.csv` per market if 11 ran.
**Outputs:** International section in `seo-workspace/<domain>/audits/YYYY-MM-DD-audit.md`; hreflang code (HTML, header or `hreflang-sitemap.xml`) and fixes in `audits/YYYY-MM-DD-fix-list.md`.

## When to use / skip

- Run only when the site has, or plans, more than one language or country version (02-site-types.md §1). Skip for landing pages.
- One language serving many countries with identical content: hreflang is optional; check only `<html lang>`, currency/format consistency and legal pages.
- Search engines per market (Naver, Baidu, Yandex, Seznam) and region-specific listing sites: 01-intake-and-detection.md §3d.
- Platform tools *(perishable: check each tool's current docs before advising)*:
  - **Shopify Markets**: outputs hreflang tags automatically per market; uses subfolders (`/en-gb/`) or separate domains/subdomains per market. Check the output instead of adding a second hreflang set.
  - **WPML / Polylang** (WordPress): add hreflang for linked translations; subfolder, subdomain or separate domain is a plugin setting. Check that untranslated pages aren't listed as alternates.
  - **Weglot**: adds hreflang and serves translations on subfolders or subdomains; confirm translations are in the server HTML, not swapped in by JavaScript.
  - **Webflow Localization**: generates locale subfolders and hreflang (can also go in the sitemap); check that each locale's canonical is self-referencing.
  - Subfolder vs subdomain choice and generic fix steps: §1 here and 03-platforms.md (safe changes).

## Procedure

1. **Inventory versions**: list every language/region version, its URL pattern, `<html lang>`, currency, and how hreflang is implemented (HTML `<link>`, HTTP header, sitemap, or none). Sample 5–10 page sets (home, top money pages, top articles).
2. **Check the structure** (§1). Flag automatic IP/language redirects.
3. **Validate hreflang** (§2, §3) for every sampled page set: build the matrix in the output format.
4. **Check canonical alignment** (§4).
5. **Generate or correct hreflang** (§5) with the method that fits the site size.
6. **Content parity** (§6) across versions.
7. **Locale formats** (§7) and **legal pages** (§8) per market.
8. **Machine-translation QA** (§9).
9. Prioritize (core rules §2) and apply the relevance check (core rules §3).

### 1. Structure and targeting

| Structure | Example | Strength | Cost |
|---|---|---|---|
| ccTLD | `example.de` | Strongest country signal | Separate domains to build and maintain; country-locked |
| Subfolder | `example.com/de/` | Shares domain strength; easiest to run | Weaker country signal on its own |
| Subdomain | `de.example.com` | Separate hosting possible | Often treated more separately than subfolders |
| URL parameter | `?lang=de` | — | Not recommended |

Rules:

- Google ignores geo meta tags and the old Search Console country setting was removed (2022). Signals that remain: ccTLD, hreflang (a hint, not a directive), local language, currency, addresses and phone numbers.
- Never force-redirect by IP or browser language. Show a dismissible language/country suggestion and keep a switcher visible on every page with links to the equivalent page (not to the home page).
- Every version must be crawlable: Googlebot crawls mostly from the US, so geo-blocking or auto-redirecting hides other versions.
- One language per URL. Don't mix translated and untranslated main content on one page.
- Right-to-left languages (Arabic, Hebrew, Persian, Urdu): `dir="rtl"` on `<html>` and mirrored layout.

### 2. hreflang codes

Format: `language` (ISO 639-1, lowercase) + optional `-Script` (ISO 15924) + optional `-REGION` (ISO 3166-1 alpha-2, uppercase by convention; matching is case-insensitive). Plus `x-default`.

| Valid | Invalid | Why |
|---|---|---|
| `en`, `en-GB`, `en-IN` | `en-UK` | The ISO country code is GB |
| `ja` | `jp` | `jp` is a country, not a language |
| `en` | `eng` | Three-letter ISO 639-2 codes are not accepted |
| `es-MX`, `es-AR` | `es-LA`, `en-EU` | Latin America and the EU are not ISO country codes |
| `zh-Hans`, `zh-Hant-TW` | `zh-CN` for Traditional script | Use script subtags when targeting a script |
| `de-CH` | `CH` | A region alone is invalid; language is always required (`be` = Belarusian) |

### 3. hreflang validation checklist

| Check | Rule | Severity if failing |
|---|---|---|
| Self-reference | Each page lists itself among its alternates | Critical |
| Return links | If A lists B, B lists A (full mesh across all versions) | Critical |
| Valid codes | §2 | High |
| Targets return 200 | No redirects, 404s, `noindex` or blocked URLs in any set | High |
| Exact URLs | Absolute, same protocol, same host style and trailing slash as the canonical | Medium |
| x-default | Present when a selector page or global fallback exists; one per set; included in return links | Medium |
| One method | HTML, header or sitemap; if two are used, they must agree exactly | Low (conflicts: High) |
| Unique per language-region | No two URLs for the same code in one set | High |
| In the raw HTML `<head>` | Not injected only by JavaScript; no invalid elements before it break `<head>` parsing | High |
| Matches `<html lang>` and content | Code matches the actual language of the page | High |

Manual method: for each sampled set, fetch every URL in it, copy its hreflang list into the matrix, and tick self, return, status and canonical. If a paid SEO crawler is available, use its hreflang report and label the source; otherwise use this sample method and state the share of pages checked.

### 4. Canonical alignment

- Hreflang goes only on canonical, indexable pages, and the hreflang URL equals that page's canonical.
- Each language version is **self-canonical**. Never canonicalize `/de/page` to `/page` (English): Google then drops the German version.
- Regional duplicates in the same language (`en-US`, `en-GB`, `en-AU` with near-identical text) are fine when each is self-canonical and linked by hreflang; localize prices, spelling, contact details and examples so each has a reason to exist.

### 5. Generation

Pick the method by size: HTML `<link>` tags for small sites (roughly under 50 versions per page); HTTP headers for PDFs and other non-HTML files; XML sitemap for large or cross-domain sites. Prefer the platform's own feature (03-platforms.md).

**HTML** (in `<head>` of every version, identical set on each):

```html
<link rel="alternate" hreflang="en-IN" href="https://example.com/en-in/pricing/" />
<link rel="alternate" hreflang="en-GB" href="https://example.com/en-gb/pricing/" />
<link rel="alternate" hreflang="de" href="https://example.com/de/preise/" />
<link rel="alternate" hreflang="x-default" href="https://example.com/pricing/" />
```

**HTTP header** (non-HTML files):

```
Link: <https://example.com/guide.pdf>; rel="alternate"; hreflang="en", <https://example.com/de/leitfaden.pdf>; rel="alternate"; hreflang="de"
```

**Sitemap** (each `<url>` lists the full set including itself):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>https://example.com/pricing/</loc>
    <xhtml:link rel="alternate" hreflang="en" href="https://example.com/pricing/"/>
    <xhtml:link rel="alternate" hreflang="de" href="https://example.com/de/preise/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://example.com/pricing/"/>
  </url>
  <url>
    <loc>https://example.com/de/preise/</loc>
    <xhtml:link rel="alternate" hreflang="en" href="https://example.com/pricing/"/>
    <xhtml:link rel="alternate" hreflang="de" href="https://example.com/de/preise/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://example.com/pricing/"/>
  </url>
</urlset>
```

Sitemap limits and rules: core rules §4 and 20-technical-audit.md §11. Cross-domain sets (`example.com` ↔ `example.de`) need return links on both domains; verify every domain in Search Console.

Steps: map equivalent pages across versions (by translated slug or a page ID, never by guess) → validate codes → generate the full set per page → check return links in the output → add x-default → re-validate (§3).

### 6. Content parity

For each page that should exist in every version, compare:

| Dimension | Acceptable difference | Severity if failing |
|---|---|---|
| Page exists in every declared version | None | High |
| Title and meta description localized (not left in the source language) | None | High |
| Structured data present and localized (`inLanguage`, prices, currency) | Same types and key properties | High |
| Section structure (H2/H3 count) | ±1 section | Medium |
| FAQ items | ±2 | Medium |
| Images present, alt text localized | Same count | Medium |
| Charts/tables present | Same | Low |
| Word count vs expected expansion | Within ±30% of the expected ratio (below) | Low |

Typical text length vs English (directional): German +25–35%, French/Spanish/Italian/Portuguese +15–25%, Dutch +10–20%, Japanese −10–25%, Korean −10–20%, Chinese −20–30%. A German page shorter than its English source probably lost content.

**Staleness**: compare `dateModified`/`lastmod` with the source version. Updated within 7 days of the source = fresh · 8–30 days = Low · 31–90 = Medium · over 90 = High.

**Parity score** (this module's sub-score; it does not change core rules §2 weights): page existence 30 + SEO elements (title, meta, schema) 30 + structure (sections, images, FAQ) 25 + freshness 15. Report per page set.

**Localization checks** (factual, not cultural guesses): local examples, prices and statistics instead of the source country's (no "80% of Americans" on a German page unless relevant) · correct legal references for the market · currency and units of the market (metric where used) · no untranslated buttons, navigation, alt text or schema text · one consistent formal/informal form of address, as set in brand-dna.md.

### 7. Locale formats

| Locale | Number | Date | Currency |
|---|---|---|---|
| en-US | 1,234.56 | MM/DD/YYYY | $1,234.56 |
| en-GB | 1,234.56 | DD/MM/YYYY | £1,234.56 |
| en-IN | 1,23,456.78 (lakh grouping) | DD/MM/YYYY | ₹1,23,456 |
| de-DE / de-AT | 1.234,56 | DD.MM.YYYY | 1.234,56 € |
| de-CH | 1’234.56 | DD.MM.YYYY | CHF 1’234.56 |
| fr-FR | 1 234,56 (space) | DD/MM/YYYY | 1 234,56 € |
| es-ES / it-IT / nl-NL / pt-BR | 1.234,56 | DD/MM/YYYY (nl: DD-MM-YYYY) | 1.234,56 € · R$ 1.234,56 |
| es-MX | 1,234.56 | DD/MM/YYYY | $1,234.56 MXN when ambiguous |
| ja-JP | 1,234 | YYYY/MM/DD or YYYY年MM月DD日 | ¥1,234 (no decimals) |
| ko-KR | 1,234 | YYYY. MM. DD. | ₩1,234 |
| zh-CN | 1,234.56 | YYYY年MM月DD日 or YYYY-MM-DD | ¥1,234.56 |

Phone numbers in international format with the country code (`+49 30 12345678`, `+91 98765 43210`). Address order follows the country (DE: street + number, postcode + city; JP: postcode first, then prefecture to street). When unsure, check the Unicode CLDR data for the locale.

Check prices, dates in posts and update stamps, copyright lines, and phone/address blocks on every version. A wrong format on a localized page = Medium; wrong currency on prices = High.

### 8. Legal and trust pages per market *(perishable, verified 2026-09; not legal advice, confirm with local counsel)*

| Market | Usually expected |
|---|---|
| Germany, Austria | Impressum (legal notice with company details), privacy policy under GDPR (DSGVO), withdrawal-right information for online sales |
| France | Mentions légales, privacy policy (GDPR), CGV (terms of sale) for shops |
| Other EU/EEA | GDPR privacy policy and cookie consent; 14-day withdrawal right information for consumer sales |
| UK | Privacy policy (UK GDPR), company details for registered companies |
| Japan | Disclosure under the Act on Specified Commercial Transactions (特定商取引法に基づく表記) for online sellers; APPI privacy policy |
| India | Privacy policy (DPDP Act 2023), grievance officer contact where required |
| US (California) | CCPA/CPRA privacy notice and opt-out where it applies |
| Brazil | LGPD privacy policy |

Each localized version links to its own market's pages, in the local language. Wrong-jurisdiction references (for example a California notice as the only privacy page on a German site) = High.

### 9. Machine-translation QA

Machine translation is acceptable when a fluent human reviews and corrects it. Unreviewed automated translation published at scale counts as scaled content abuse under Google's spam policies *(perishable, verified 2026-07)*; see core rules §8.

| Signal | Severity |
|---|---|
| Alternates whose body text is identical to the source (only the menu translated) | Critical |
| `<html lang>` does not match the body language, or is missing / `auto` | High / Medium |
| Translated meta descriptions far over the core length range (core rules §4) | Medium |
| Schema `inLanguage` missing or wrong | Medium |
| Untranslated product names or terms scattered in the body, wrong grammar or terminology | Low (heuristic; ask a native speaker) |
| In-browser translation widget used instead of real translated pages | Medium: widget text isn't a crawlable page |

Don't flag: clearly labelled machine-translated pages with limited scope, or translated UI strings. Low-value translated pages: `noindex` them individually rather than blocking whole sections.

## Output format

```markdown
## International — <domain> — YYYY-MM-DD
Versions: en (x-default), en-GB, de, fr · structure: subfolders · method: HTML hreflang
Page sets checked: N of M (crawl / sitemap)

| Page set | Version | URL | Self | Return | Canonical match | 200 | Code valid | Status |
|---|---|---|---|---|---|---|---|---|

| Page set | en | de | fr | Parity score |
|---|---|---|---|---|
| /pricing | ✓ | ✓ | missing | 55/100 |

### Findings
| # | Priority | Finding | Fix | Effort | How we'll verify |

### Generated hreflang
<HTML / header / sitemap block>

### Not measured
- <item> — reason — what would unlock it
```

## Fallbacks and "not measured"

| Situation | Do this |
|---|---|
| Can't fetch | Ask for the `<head>` of each version of 2–3 key pages and the sitemap; validate those only |
| Can't run code | Manual matrix (§3) in a table |
| No native speaker review possible | Mark translation quality "not measured"; list the heuristic signals found |
| No Search Console per market | Country performance and hreflang errors "not measured"; recommend connecting (60-measurement.md) |
| Legal requirements unclear | Say so and recommend local legal review; don't guess |
