# 60 — Measurement, monitoring and reporting

How to measure search and AI visibility with free sources (Search Console, GA4, PageSpeed/CrUX, Bing Webmaster, a manual AI visibility tracker), catch regressions and content decay, and report monthly.

**Inputs:** `site-profile.md`, `research/prompts.csv`, `research/keywords.csv`, `tracking/change-log.md`, `tracking/baselines/`, earlier `reports/`
**Outputs:** `tracking/baselines/YYYY-MM-DD-<page-slug>.json` (or `.md`), `tracking/ai-visibility-log.csv`, `reports/YYYY-MM-report.md`, re-check entries in `tracking/change-log.md`, refresh candidates for 30-content-creation.md

## When to use / skip

- **Use** in Monitor and report mode, at the end of every full audit with data access, before and after every live change (03 §4), and on the 30/60/90-day schedule (§12).
- **Light** for landing pages (02 routing): one baseline, Search Console basics, a 5–10 prompt AI panel.
- **Skip** data sections you have no access to; write "not measured" and say which access would unlock them.

## Procedure

1. List available sources (§1) and record them in the Site Profile.
2. Pull the standard views (§2–§6) for the period; label every number with its source (core rules §1).
3. Run the drift compare (§7) for key URLs and anything changed since the last report.
4. Run the AI visibility panel (§8) and AI referral check (§9).
5. Run decay detection (§10); send refresh candidates to 30.
6. Compare against KPIs (§11), write the monthly report (§13), set re-check dates (§12).

## 1. Data sources

| Source | Gives | Access needed |
|---|---|---|
| Google Search Console (GSC) | Clicks, impressions, CTR, position, indexing, CWV, AI feature impressions (2–3 day lag, ~16 months) | Verified property (Domain property via DNS preferred) |
| GA4 | Sessions by channel, landing pages, key events, AI-assistant traffic | Viewer role |
| PageSpeed Insights | Lighthouse lab + CrUX field data | None (API key optional) |
| CrUX API + History | p75 field metrics; 25 weekly periods | Free API key |
| Bing Webmaster Tools | Bing clicks/impressions, indexing, backlinks, IndexNow | Verified site (import from GSC) |
| AI visibility log | Mentions, citations, share of voice in AI answers | Manual runs (§8) |
| Paid tools (optional) | Rankings, AI share of voice, backlinks | If a paid SEO data tool is available (DataForSEO, Ahrefs, Semrush, SE Ranking, Moz…), use it and label the source; otherwise use the free methods here |

**Setup checklist** (first run): GSC Domain property verified · sitemap submitted in GSC and Bing · Bing site imported from GSC · GA4 key events defined (forms, calls, sign-ups, purchases) · GSC linked to GA4 (optional) · GA4 AI channel visible (§9). Never store API keys or passwords in the workspace (core rules §9.4).

## 2. Search Console

**UI steps (no code needed):**

1. **Performance → Search results**: date range last 3 months; tick Clicks, Impressions, CTR, Position. Use **Compare** for period-over-period. Export (top right) to Sheets/CSV.
2. Tabs **Queries** and **Pages**: export both. Filter Query "contains" brand name to split **branded vs non-branded**.
3. **Quick wins** (core rules §4): queries in that position range with above-median impressions for the site → improve title/meta, answer-first section, internal links (30, 13).
4. **Pages (indexing) report**: count Indexed vs Not indexed; open each reason (crawled not indexed, duplicate without canonical, excluded by noindex, 404, redirect). Compare with the sitemap count.
5. **URL Inspection** (top bar) for key URLs: indexed?, Google-selected vs user-declared canonical, last crawl, crawled as mobile. "Test live URL" shows rendered HTML.
6. **Sitemaps**: status, discovered URL count, errors.
7. **Core Web Vitals** report: URL groups Poor / Needs improvement / Good by mobile and desktop.
8. **Generative AI performance** report *(perishable, verified 2026-08)*: impressions only for AI Overviews and AI Mode by page, country, device, date. No clicks or queries. AI Mode clicks and impressions are already counted inside normal Performance totals, so "classic vs AI" can't be split cleanly from totals.

**Data caveats:** query rows omit anonymized low-volume queries, so never sum query rows as site totals (use the chart totals). A logging error made **impressions, CTR and position unreliable from 2025-05-13 to 2026-04-27** (clicks fine, no backfill) *(perishable, verified 2026-04)*: say so when a comparison spans that window.

**Optional API** (Search Analytics `POST https://www.googleapis.com/webmasters/v3/sites/{siteUrl}/searchAnalytics/query`; URL Inspection `POST https://searchconsole.googleapis.com/v1/urlInspection/index:inspect`). Without code, use the "Try this API" panel on each method's Google docs page (signs in with the user's account).

```json
{ "startDate": "2026-08-01", "endDate": "2026-10-31", "dimensions": ["page", "query"],
  "type": "web", "rowLimit": 25000, "startRow": 0 }
```

Quotas *(perishable)*: Search Analytics ~1,200 queries/min per site; URL Inspection 2,000/day and 600/min per site. Page with `startRow`; for exact totals omit `query`/`page` dimensions.

## 3. GA4

1. **Reports → Acquisition → Traffic acquisition**, primary dimension "Session default channel group": note Organic Search, AI assistants, Referral, Direct sessions and key events.
2. **Engagement → Landing page**, add filter channel = Organic Search: top organic landing pages with key events.
3. Compare periods (date picker → Compare). Export via Share → Download.
4. Key events, not sessions, prove the goal (02 KPIs). No key events → goal KPI "not measured"; recommend setting them up.
5. EU sites: consent mode lowers recorded sessions; compare trends, not raw counts vs GSC clicks.

Optional API: GA4 Data API `runReport` (`landingPage`, `sessionDefaultChannelGroup`, `sessionSource`; `sessions`, `keyEvents`); token quota ~25,000/day per property *(perishable)*.

## 4. PageSpeed and Core Web Vitals

Thresholds: core rules §4. Field data (CrUX) beats lab data (Lighthouse).

1. Open `https://pagespeed.web.dev/` (or the API URL below in a browser) for the home page and one URL per key template, **mobile first**.
2. Record field p75 LCP, INP, CLS (label `CrUX (field)`) and the Lighthouse performance score (label `PageSpeed (lab)`). "No data" in the field section means too little Chrome traffic: use lab data and say so.
3. Trends: CrUX History gives 25 weekly p75 values; use `formFactor: PHONE` (an all-devices view can hide a mobile failure).

```text
https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https%3A%2F%2Fexample.com%2F&strategy=mobile
```

```python
# CrUX field data; set CRUX_API_KEY first (PowerShell: $env:CRUX_API_KEY="..."; macOS/Linux: export CRUX_API_KEY=...)
import json, os, urllib.request
body = json.dumps({"origin": "https://example.com", "formFactor": "PHONE"}).encode()
url = "https://chromeuxreport.googleapis.com/v1/records:queryRecord"  # use :queryHistoryRecord for 25-week history
req = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json",
                             "X-Goog-Api-Key": os.environ["CRUX_API_KEY"]})
print(urllib.request.urlopen(req).read().decode())
```

Notes: in the PageSpeed API JSON, field p75 values are in `loadingExperience.metrics` (`originLoadingExperience` = whole site; `CUMULATIVE_LAYOUT_SHIFT_SCORE` is CLS × 100) and lab values in `lighthouseResult.audits`; record `lighthouseResult.lighthouseVersion`. A CrUX 404 means not enough traffic, not an auth error. CLS p75 comes back as a string. Diagnosis and fixes live in 20.

## 5. Indexing

| Situation | Method |
|---|---|
| A few new or fixed URLs | GSC URL Inspection → "Request indexing" (small daily limit; use for key pages only) |
| Many URLs | Accurate sitemap with real `lastmod`, resubmitted in GSC and Bing |
| Bing, Yandex, Naver, Seznam, Yep | **IndexNow** (not used by Google) *(perishable, core rules §10)* |
| Job postings, livestream videos | Google Indexing API: officially only JobPosting and BroadcastEvent pages, 200 publish requests/day default. Never use it for ordinary pages |

**IndexNow:** create a key (8–128 letters, digits or dashes), host it as `https://example.com/<key>.txt` containing only the key (hosted builders: 03 §2), then submit. Single URL (works in a browser):

```text
https://api.indexnow.org/indexnow?url=https%3A%2F%2Fexample.com%2Fnew-page&key=<key>
```

Batch: POST JSON `{"host":"example.com","key":"<key>","keyLocation":"https://example.com/<key>.txt","urlList":[...]}` to the same endpoint (up to 10,000 URLs). Many CMS plugins and CDNs can send IndexNow automatically (check docs). Submit only changed URLs.

## 6. Bing Webmaster Tools

1. Add the site by **importing from Search Console**.
2. **Search Performance**: clicks, impressions, CTR, position. Bing feeds Copilot answers, so pages missing from Bing can't be cited there.
3. **URL Inspection**, **Sitemaps**, **Site Scan** (free crawl audit), **Backlinks** (feeds 40), **IndexNow** (received URLs).
4. If the account shows an AI/Copilot citation report, log it as `Bing WMT` (perishable; check current Bing docs).

## 7. Regression baseline and drift rules

Capture a baseline **before** any change (03 §4), after each deploy, and monthly for key URLs (home, top 10 landing pages, one per template).

**Capture per URL:** status code · title · meta description · canonical · meta robots (+ `X-Robots-Tag`) · H1 list · H2 list · JSON-LD (types + full text) · Open Graph tags · CWV p75 (field if available) · Lighthouse performance score · hash or word count of main content. Site-level extras: robots.txt text, sitemap URL count, redirect map.

**Manual:** view source (or ask the user to paste it), copy the fields into a Markdown table, save as `tracking/baselines/YYYY-MM-DD-<page-slug>.md`. **If you can run code:** save the same fields as JSON plus SHA-256 hashes of body and JSON-LD. Normalize URLs before matching (lowercase host, no default port, UTM parameters or trailing slash).

**Compare rules** (severity maps to core rules §2 priority levels):

| # | Rule | Trigger | Level |
|---|---|---|---|
| 1 | Schema removed | Had JSON-LD, now none | Critical |
| 2 | Canonical changed | Different value after normalizing | Critical |
| 3 | Canonical removed | Had one, now missing | Critical |
| 4 | Noindex added | `noindex` now present | Critical |
| 5 | H1 removed | Had H1, now none | Critical |
| 6 | H1 rewritten | First H1 more than 50% different | Critical (confirm intent) |
| 7 | Title removed | Had title, now empty | Critical |
| 8 | Status to error | Was 2xx, now 4xx/5xx | Critical |
| 9 | Title changed | Text differs | High: check CTR in GSC over 2 weeks |
| 10 | Meta description changed | Text differs | High: monitor CTR |
| 11 | CWV regressed | Any p75 more than 20% worse | High |
| 12 | Lighthouse dropped | Performance score down 10+ points | High |
| 13 | Open Graph removed | Had OG tags, now none | High |
| 14 | Schema modified | JSON-LD text changed, still present | High: re-validate (21) |
| 15 | Schema added | None before, now present | Low: validate (21) |
| 16 | H2 structure changed | Count or text differs | Low |
| 17 | Content changed | Body hash differs | Low: review if nothing else fired |

FAQ/HowTo markup has no rich result to lose (core rules §5). Check the change log before raising an alarm; for an unintended Critical, roll back (03 §4 step 8) and open the owning module (20, 21, 30).

## 8. AI visibility tracker (free, manual)

AI answers vary by day, account, location and wording, so track trends from repeated runs, never single answers (core rules §1.5).

1. **Build the panel** from `research/prompts.csv` (11 owns prompt research): 20–50 prompts across clusters and tiers, including category prompts without the brand ("best X for Y"), problem prompts, comparison prompts, and 3–5 branded prompts ("Is <brand> good for…", "What is <brand>?"). Keep wording fixed month to month.
2. **Engines**: ChatGPT (search on), Perplexity, Gemini, Google AI Overviews / AI Mode, Copilot, Claude: whichever the audience uses.
3. **Conditions**: logged out or a fresh/temporary chat, memory and custom instructions off, same location and language each time. Record them.
4. **Runs**: at least 2 runs per prompt per engine per cycle, on different days if possible.
5. **Log** one row per prompt × engine × run in `tracking/ai-visibility-log.csv` (`templates/ai-visibility-log.csv`): date, engine, mode, location, prompt, cluster, run, brand_mentioned, brand_position (order among brands named; blank if absent), brand_cited (own URL in sources), cited_urls, sentiment (positive/neutral/negative/mixed), competitors_mentioned, accuracy_issue, notes.
6. **Score** for the period (label `AI visibility log, n = rows`):
   - Mention rate = rows with brand mentioned ÷ all rows
   - Citation rate = rows citing an own URL ÷ all rows
   - **Share of voice** = brand mentions ÷ (brand mentions + mentions of each tracked competitor), counting each brand once per row
   - Average position = mean brand_position where mentioned; positive share = positive ÷ mentioned
   - Split by engine and cluster; a prompt counts as "won" only if mentioned in every run.
7. **Act**: wrong facts → entity fixes (10); competitor-only prompts → content or comparison pages (30); third-party URLs that engines cite → mention opportunities (40); not cited despite a good page → AI readiness checks (22).

**Cadence:** full panel monthly, same week each month; re-run affected clusters 2–4 weeks after major content or entity changes. With fewer than ~100 rows, treat month-to-month moves under ~10 points as noise.

**Honesty:** if you run the prompts through your own web search instead of the consumer apps, label the engine "assistant web search (proxy)". If you can't reach the engines, give the user the prompt list and the CSV header to fill in and paste back.

## 9. AI referral traffic

1. GA4 **AI assistants** channel *(perishable, verified 2026-05)*: recognizes ChatGPT, Gemini, Claude, DeepSeek, Copilot and Grok; excludes Google AI Overviews/AI Mode (they arrive as Organic Search); Perplexity may land in Referral. Forward-only.
2. For full control, add an Exploration (or custom channel group) with session source matching this regex *(perishable referrer list, verified 2026-11)*:

```text
chatgpt\.com|chat\.openai\.com|perplexity\.ai|gemini\.google\.com|copilot\.microsoft\.com|claude\.ai|chat\.deepseek\.com|grok\.com|meta\.ai|you\.com
```

3. Also count `utm_source=chatgpt.com` (ChatGPT tags many outbound links).
4. Report AI sessions, key events and top AI landing pages. Many AI visits arrive without a referrer and count as Direct, so this undercounts: say so.
5. Optional: server or CDN logs show AI crawler hits (user agents in core rules §7); rising search-bot fetches of key pages are a leading indicator.

## 10. Content decay detection (feeds the refresh loop)

1. In GSC Performance → Pages, compare the **last 3 months vs the previous 3 months**; for seasonal sites also compare the same 3 months last year.
2. Only judge pages with enough data: at least 30 clicks (or 300 impressions on small sites) in the earlier period.
3. Flag a page as **decaying** when clicks fell 25% or more in both comparisons (not just seasonality).
4. Diagnose with the page's top queries:

| Pattern | Likely cause | Next step |
|---|---|---|
| Position down 2+ places | Competitors improved or page is outdated | Refresh (30): update facts, answer-first, depth, dates |
| Impressions flat, CTR down 20%+ | SERP changed (AI Overview, lost snippet, better competitor titles) | Check the SERP (12); rewrite title/meta; strengthen answer block |
| Impressions and position both down | Lost relevance or cannibalization | Check overlapping pages; merge + 301 (03) |
| Impressions down, position flat | Demand fell | Check Google Trends; usually leave |
| Page dropped from index | Technical | Inspect URL; fix via 20 |

5. Add decaying pages to the refresh list with the diagnosis; the rewrite procedure is in 30. After a refresh, log it in the change log and re-check at 30 and 60 days (§12). Also review money pages and top content every 3–6 months even without decay (core rules §4 Freshness).

## 11. KPI sets per site type (where to measure the KPIs in 02)

| Type | Outcome KPI (source) | Leading indicators (source) | AI KPI (source) |
|---|---|---|---|
| Portfolio | Contact form submissions (GA4) | Name-query position and impressions (GSC) | "Who is <name>?" answer accuracy (AI log) |
| Local | Calls, directions, bookings (GBP Insights, GA4) | Local pack presence (manual or paid grid tool, 50); service-page clicks (GSC) | Mentions for "best <service> in <city>" (AI log) |
| E-commerce | Organic revenue and transactions (GA4) | Product/category impressions (GSC); Merchant Center clicks | SoV on "best X for Y" prompts (AI log) |
| SaaS | Organic sign-ups/demos (GA4) | BOFU page positions; branded query growth (GSC) | SoV on category prompts; AI-assistant sessions (GA4) |
| Publisher | Organic sessions, subscribers (GA4) | Discover clicks, impressions, decaying-page count (GSC) | Citation rate (AI log) |
| Agency | Organic leads (GA4) | Service/industry page positions (GSC) | Mentions for "best <service> agency" (AI log) |
| Docs | Docs sessions; support deflection (GA4, support tool) | Docs impressions (GSC) | Citations of docs URLs (AI log); AI-assistant sessions (GA4) |
| Marketplace | Inquiries/applications (GA4) | Indexed listing ratio (GSC Pages report vs sitemap) | Citations of data pages (AI log) |
| Landing | The one conversion (GA4) | Target-query position and CTR (GSC) | Brand description accuracy (AI log) |

## 12. Re-check schedule

| When | Check |
|---|---|
| Day 0–1 after a change | Live verification and drift compare (03 §4 step 7); request indexing for key URLs |
| Day 7 | URL Inspection for changed URLs; sitemap processed; no new Critical drift |
| Day 30 | Indexing report trend; CTR on pages with new titles/meta; canonical and redirect fixes settled (canonical clusters can take ~2 weeks) |
| Day 60 | Clicks/positions for changed pages vs baseline period; AI panel re-run for affected clusters |
| Day 90 | Light re-audit: recompute scores (core rules §2) on the same coverage and compare; update roadmap (13) |
| Monthly / quarterly | Monthly report (§13); full re-audit every 6–12 months or after a migration |

Write the dates into `tracking/change-log.md` and the Site Profile.

## 13. Monthly report

Write `reports/YYYY-MM-report.md` from `templates/monthly-report.md`: owner summary (5 plain lines) → KPIs vs last month and last year with source labels → search (GSC, branded vs non-branded, movers) → AI (§8 scores by engine, §9 sessions, GSC AI impressions) → technical (indexing, CWV, drift) → work done from the change log and its effect → decay/refresh list → next month's 3–5 priorities → not measured.

## Output format

```
MEASUREMENT SNAPSHOT: example.com · 2026-10 vs 2026-09
Search  Clicks 4,210 (+8%) · Impr 182k (+3%) · CTR 2.3% · Pos 18.4   [GSC]
Goal    Organic leads 37 (+5)                                         [GA4]
AI      Mention 34% · Citation 12% · SoV 21% (n = 120)  [AI visibility log] · AI sessions 96 [GA4]
CWV     Mobile LCP 2.9 s · INP 140 ms · CLS 0.04                      [CrUX (field)]
Drift   1 Critical (canonical changed on /pricing, unlogged)          [crawl]
Decay   4 pages → refresh list                                        [GSC]
Not measured: Bing (no access) · Next re-check: 2026-12-01
```

## Fallbacks and "not measured"

- **No GSC/GA4/Bing access**: mark those sections "not measured", give the user the UI steps above to export CSVs and paste them, and use only PageSpeed (no login needed) plus the AI panel.
- **Can't run code**: use the UI paths and browser URLs; skip API steps.
- **Can't fetch pages**: ask for view-source pastes for baselines; otherwise drift is "not measured".
- **Can't reach AI engines**: hand over the prompt panel and CSV header for the user to run.
- **New site**: no decay or trend data yet; capture baselines and the first AI panel as month zero.
