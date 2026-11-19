# 22 — AI search readiness (AEO + GEO audit)

Check whether answer engines and AI assistants can reach, read, trust and quote the site, and compute the AI Search Readiness score with the weights in core rules §2.

**Inputs:** `seo-workspace/<domain>/site-profile.md`, `seo-workspace/<domain>/brand-dna.md`, `research/prompts.csv` (if 11 ran), findings from 20 (rendering, CWV) and 21 (schema).
**Outputs:** AI Search Readiness section in `seo-workspace/<domain>/audits/YYYY-MM-DD-audit.md`; AI fixes in `audits/YYYY-MM-DD-fix-list.md`; optional `seo-workspace/<domain>/audits/YYYY-MM-DD-aeo-audit.json`.

Google's position (perishable; date in core rules §10): optimizing for AI Overviews and AI Mode is still SEO; no special files, chunking or AI-only markup are needed (core rules §5). Most items below are SEO fundamentals viewed through an AI lens. Never promise citations or traffic.

## When to use / skip

- Core for every site type (02-site-types.md §1); headline score for AEO and GEO focus.
- Focus **AEO**: use the AEO weights (core rules §2). Docs/developer sites: llms.txt and Markdown delivery are Medium priority; Low elsewhere (core rules §5).
- Agent readiness (§10) is optional: run it for SaaS, stores, booking sites, docs, or when asked.
- Staging sites: blocked bots are expected (core rules §9.3); list them in the pre-launch checklist (20 §10).

## Procedure

1. **Collect**: `/robots.txt`, `/llms.txt`, sitemap, the home page and 3–5 key pages (top money page, top article or guide, about, a product/service page). Fetch raw HTML; get rendered HTML too if possible (20 §5).
2. **Optional script** (Node 18+): `node scripts/aeo-audit.mjs https://example.com --max-pages=15 --out=seo-workspace/<domain>/audits/YYYY-MM-DD-aeo-audit.json`. It crawls up to N pages (default 10, max 30), runs 16 checks, and lists `pagesForReview` (home + richest pages with title, headings, text excerpt, schema, dates, author). Use its results as **inputs** to §7; don't report its own 0–100 "foundational" or "provisional" score as the headline. Manual fallback: do §1–§6 by reading the pages.
3. **AI crawler access** (§1).
4. **Firewall/CDN check** (§2).
5. **Visibility without JavaScript and snippet controls** (§3, §4).
6. **Content rubric**: score the 6 dimensions per reviewed page (§5), rationale before score.
7. **Authority and multimodal inputs** (§6), mostly from 10, 21, 31, 40.
8. **Compute the score** (§7) and coverage. Grade per core rules §2.
9. **Fixes**: AI-specific fix list (§9b); writing fixes go to 30-content-creation.md, entity fixes to 10-brand-and-entity.md, platform how-to to 03-platforms.md.
10. **Optional**: agent readiness (§10); llms.txt (§8) if missing and relevant.

### 1. AI crawler access (robots.txt)

Bot names, jobs and defaults: core rules §7 (do not keep a second list).

1. For each bot in that table, find the group that applies: the most specific `User-agent` group naming it; only if none names it, the `*` group. A named group does not inherit `*` rules.
2. Read whether `/` or key paths are disallowed for that bot.
3. Report **three separate lines**, never merged:
   - **Search bots** (OAI-SearchBot, Claude-SearchBot, PerplexityBot, Googlebot, Bingbot, Applebot): any blocked → **Critical** unless the owner chose it on purpose.
   - **User-triggered fetchers** (ChatGPT-User, Claude-User, Perplexity-User): blocked → High. Note they may not follow robots.txt fully.
   - **Training bots** (GPTBot, ClaudeBot, Google-Extended, Applebot-Extended, CCBot, Bytespider, Meta-ExternalAgent): blocked or allowed = **Info**, an owner decision. If no decision is recorded in site-profile.md, ask; never score it.
4. Match the claim to the bot:

| Claim | Check | Not evidence |
|---|---|---|
| Can appear in Google Search, AI Overviews, AI Mode | Googlebot | Google-Extended |
| Can be cited in ChatGPT search | OAI-SearchBot | GPTBot |
| Can be cited in Claude's search | Claude-SearchBot | ClaudeBot |
| Can be used for Gemini app grounding and training | Google-Extended | Googlebot |
| Can appear in Copilot / Bing | Bingbot | — |

5. Watch for: `User-agent: *` + `Disallow: /` (blocks every bot without its own group); a 5xx on robots.txt (compliant bots treat the site as blocked); bot names with version suffixes (`GPTBot/1.1`), which strict parsers may skip.
6. Fix with `templates/robots-ai.txt` (search bots allowed, training block left commented as an **OWNER DECISION**). Platform-specific editing: 03-platforms.md.

Script note: `aeo-audit.mjs` fails `ai-bot-access` only when a search/user bot is blocked and reports training-bot blocks as info. It reads one `User-agent` line per group and does not apply `*` rules to AI bots, so check by hand when several `User-agent` lines share one group or when `*` is disallowed.

### 2. Firewall and CDN bot blocking

robots.txt can allow a bot that the firewall still blocks. Signs: fetches return 403, a challenge or CAPTCHA page; the CDN dashboard has an "AI bots" block, "bot fight" mode or aggressive rate limits (Cloudflare, Wordfence, Sucuri, AWS/Vercel WAF).

- Without owner confirmation: report only what a normal fetch shows. Never send requests with a spoofed bot user agent (core rules §8).
- With the owner: review the CDN/WAF settings and server logs for real search-bot hits (verified by the vendor's published IP ranges or reverse DNS). Allow **verified** search bots, not user-agent strings.
- Keep CAPTCHAs and challenges off content pages. **Never weaken a security rule without the owner's OK** (core rules §7).
- Logs or dashboard not available → "not measured".

### 3. Content visible without JavaScript

Many AI crawlers read raw HTML only. Using the raw-vs-rendered comparison (20 §5), check on each reviewed page that the main answer text, headings, internal links and JSON-LD are in the raw HTML. Main text only after JS = **Critical** for AI access (fix: SSR/SSG via 03-platforms.md).

### 4. Snippet and AI-use controls

| Control | Effect | Rule |
|---|---|---|
| `noindex` (meta or `X-Robots-Tag`) | Out of Google entirely, so out of AI Overviews | Critical on pages meant to be found |
| `nosnippet`, `max-snippet:0` | No snippet, so no use in AI Overviews/AI Mode answers | High on key pages; remove only with owner OK (may be intentional) |
| `data-nosnippet` on elements | That text is excluded from snippets and AI answers | Fine for boilerplate; flag if it wraps the main answer |
| `noai`, `noimageai` | Non-standard; honoured by some tools only | Ask the owner before removing (core rules §7) |
| Search Console "Search generative AI" setting *(perishable, verified 2026-09)* | Site-level include/exclude for Google's AI features; not a ranking or training control | If excluded, ask whether that is intended |

### 5. Content rubric (score each reviewed page 0–5)

Score only what you read. Write 1–2 sentences of evidence first, then the number, then a key finding under 14 words. Average across pages (weight the home page and top money page double if the site has few pages).

| Dimension | 0–1 | 2–3 | 4–5 |
|---|---|---|---|
| **Answer readiness**: can a direct answer to the page's main question be found fast? | Promotional or navigational only; talks around topics | Some answers, buried below the intro; a few definition-first sections | Answers lead the sections; direct answer block under question headings (core rules §4); common questions covered |
| **Quotability**: can a self-contained passage be lifted and still make sense? | One dense block or interactive-only; every passage needs context | Some standalone paragraphs and lists; many "as mentioned above" | Self-contained passages naming their subject; tables, numbered steps, definition paragraphs |
| **Evidence density**: specific, sourced facts? | Vague claims ("industry-leading") | Some numbers and named sources, sparse | Numbers, dates, named and linked sources, verifiable metrics throughout |
| **Content depth**: enough substance to fully answer? | Placeholder or a few sentences | Covers the main points, misses sub-topics or examples | Complete coverage, sub-topics, examples, data; a go-to reference for its scope (coverage floors: core rules §4) |
| **Freshness**: current enough to cite with confidence? | No dates, or clearly outdated facts | Dated but stale, or no "last updated" | Visible "Last updated", `dateModified`, current references, active maintenance |
| **Structural clarity**: does the HTML read cleanly? | No headings, walls of text, non-semantic markup | Headings present but inconsistent or skipped | One H1, clean H2/H3 outline, semantic HTML (`main`, `article`, lists, tables), little boilerplate noise |

If the script's `heuristicIntelligenceSignals` differ from your score × 20 by more than ~25 points on a dimension, re-read that page and confirm your score is grounded in what is there.

### 6. Authority and multimodal inputs

Take these from other modules; if a module didn't run, mark the item "not measured".

| Input | Source module | 5 = | 0 = |
|---|---|---|---|
| Author/creator identity | 30 / 10 | Named authors with bio pages and real credentials where readers expect them | Anonymous content on topics that need expertise |
| Entity consistency | 10, 21 | Organization/Person with stable `@id` and full sameAs; same name and one-line description on site and profiles | No entity markup, conflicting names or descriptions |
| Third-party presence | 10, 40 | Independent mentions, genuine reviews on relevant platforms, directory/Wikidata presence where eligible | No independent mentions found |
| Image alt quality | 31 | Descriptive alt on content images, `alt=""` on decoration (core rules §4) | Most images without alt |
| Charts and data visuals | 31 | Text summary + HTML table/CSV next to every chart | Key data only inside images |
| Video | 31, 21 | Transcript or summary on page, VideoObject | Video with no text equivalent |
| Social preview | 31 | `og:title`, `og:description`, `og:image` on key pages | Missing |

### 7. AI Search Readiness score (one method)

Score every item 0–5. **Check items** use the share of reviewed/crawled pages that pass: score = 5 × pass share (one decimal). **N/A** items (e.g. no video on the site) and **not measured** items are left out of the maths.

| Category (weight, core rules §2) | Item | Inner weight | Scored from |
|---|---|---|---|
| **Citability and answer readiness (25)** | Answer readiness | 3 | Rubric |
| | Quotability | 3 | Rubric |
| | Evidence density | 2 | Rubric |
| | Content depth | 2 | Rubric (script `text-depth` as a hint) |
| **Structure (20)** | Structural clarity | 3 | Rubric |
| | One H1 and no skipped heading levels | 2 | Checks `h1`, `heading-hierarchy` (average) |
| | Title and meta description present and fitting | 1 | Checks `title`, `meta-description` |
| | Internal links | 1 | Check `internal-links` |
| | Valid structured data with fitting types | 2 | Checks `schema`, `schema-types` + 21 validation (types allowed by core rules §6 only; HowTo never counts) |
| **Authority and brand (20)** | Freshness | 2 | Rubric |
| | Author/creator identity | 2 | §6 |
| | Entity consistency | 2 | §6 |
| | Third-party presence | 2 | §6 |
| **Technical access (20)** | Search bots allowed (robots.txt) | 4 | §1: all allowed 5 · only user fetchers blocked 3 · any search bot blocked 0 |
| | Main content in raw HTML | 3 | §3 |
| | Indexable, correct canonical | 3 | Checks `indexability`, `canonical` |
| | No unwanted `nosnippet`/`noai` | 2 | Check `ai-meta-tags`, §4 |
| | Firewall/CDN lets verified bots in | 2 | §2 (often not measured) |
| | Speed (CWV pass, core rules §4) | 1 | 60 §4 data: all good 5 · one needs improvement 3 · any poor 0 |
| | Discovery: sitemap with true `lastmod`, feed for blogs | 1 | 20 §11, check `rss-feed` (feed N/A for non-blogs) |
| | llms.txt at root | 0.5 | §8: valid 5 · present but invalid 2 · missing 0 |
| **Multimodal (15)** | Image alt quality | 2 | §6, check `image-alt` |
| | Charts and data visuals | 1 | §6 (N/A if none) |
| | Video | 1 | §6 (N/A if none) |
| | Social preview | 1 | Check `og` |

Maths:

1. Category % = Σ(inner weight × score) ÷ Σ(inner weight × 5) × 100, over measured items.
2. A category counts only if items holding at least half its inner weight were measured; otherwise it is "not measured".
3. **AI Search Readiness** = Σ(category % × category weight) ÷ Σ(weights of counted categories). Use 35/20/20/20/5 for AEO focus (core rules §2).
4. **Coverage** = Σ(category weight × share of its inner weight measured) ÷ 100.
5. Grade with core rules §2 (A–F; do not use plus/minus grades). Critical findings are listed at the top whatever the score.

Example: Citability 62%, Structure 80%, Authority 45%, Technical 90%, Multimodal not measured → (62×25 + 80×20 + 45×20 + 90×20) ÷ 85 = 69 → **C**, coverage ≤ 85%.

### 8. llms.txt (optional, low priority)

Priority per core rules §5. Google Search ignores it; some AI tools and Lighthouse's agentic audit read it.

1. Place it at the **site root only**: `https://example.com/llms.txt` (not only in `/.well-known/`). Serve 200 with `text/plain` or `text/markdown`; a soft 404 (HTML page answering 200) counts as missing.
2. Format (llmstxt.org community proposal): one `# Site name` H1 (required) · a `>` one-line summary · short notes · `## Section` headings each with a list of `- [Page name](absolute URL): one-line note` · optional `## Optional` section for skippable links. Lighthouse's check needs the H1, at least one Markdown link and 50+ characters.
3. List 10–40 of the most useful canonical pages (docs, pricing, about, key guides, policies). No marketing slogans, no instructions to AI systems.
4. Docs sites may add `/llms-full.txt` (full text of key pages) and `.md` versions of pages.
5. Start from `templates/llms.txt`; update it when key pages change.

### 9. Platform notes *(perishable, verified 2026-09)*

| Surface | What feeds it | Focus |
|---|---|---|
| Google AI Overviews / AI Mode | Google's index (Googlebot); page must be indexed and snippet-eligible | Classic SEO plus answer-first passages; AI Mode cites a broader set of pages than the top results (directional) |
| Gemini app | Google index; Google-Extended controls use for Gemini grounding/training | Treat Google-Extended as an owner decision (core rules §7) |
| ChatGPT search | OAI-SearchBot index; ChatGPT-User for live fetches | Entity presence and authoritative third-party sources |
| Perplexity | PerplexityBot index; Perplexity-User | Community and review sources are cited often (directional) |
| Claude | Claude-SearchBot; Claude-User | Same fundamentals |
| Copilot | Bing index (Bingbot) | Bing Webmaster Tools, IndexNow (60-measurement.md) |

AI answers vary by run, place and account; measure visibility as a trend (core rules §1.5; tracking in 60-measurement.md).

### 9b. AI-specific fixes (priority order)

| Finding | Priority | Fix (owner module) |
|---|---|---|
| Search bot blocked in robots.txt or firewall | Critical | robots template; verified-bot allowlist with owner OK (03) |
| Main content only after JavaScript | Critical | SSR/SSG or prerender key templates (03) |
| Unintended `noindex`/`nosnippet` on key pages | High | Remove after owner confirms (03) |
| No direct answers / not quotable | High | Answer-first rewrite, question headings, self-contained passages (30) |
| Entity unclear (no Organization/Person, no sameAs, inconsistent bios) | High for GEO | Entity setup (10), markup (21) |
| No dates or fake freshness | Medium | Visible "Last updated" + `dateModified` on real updates (core rules §4) |
| Facts without sources | Medium | Cite primary sources (30, 32) |
| Charts/video without text | Medium | Text layer (31) |
| No llms.txt | Medium (docs) / Low | §8 |
| No feed on a blog | Low | RSS/Atom with `<link rel="alternate">` (33 step 10) |

FAQ sections help answer engines; FAQPage markup is optional (core rules §5). Never recommend HowTo.

### 10. Agent readiness (optional, advanced)

AI agents that browse and act read pages through screenshots, the DOM and the **accessibility tree**. Treat this as accessibility + performance + access policy; never promise gains.

1. **Lighthouse Agentic Browsing** *(perishable, verified 2026-09)*: add `&category=AGENTIC_BROWSING` to the PageSpeed API URL (60-measurement.md §4), or run `npx lighthouse@latest https://example.com --only-categories=agentic-browsing --output=json --output-path=agentic.json` (Node 22.19+). Report the result as a fraction **X/N** with the Lighthouse version and date, never as a percentage. Counted audits: accessibility tree (an axe rule subset), CLS, llms.txt, and, when present, WebMCP schema validity, WebMCP form coverage and `ai-catalog.json`. Manual fallback: the PageSpeed website, or DevTools → Lighthouse.
2. **Accessibility tree** (manual, DevTools Accessibility pane): real `<button>` and `<a href>` (no clickable `div`s) · every input labelled · icon buttons have names · no invisible overlays over controls · no hover-only menus or focus traps · no CAPTCHA on content · confirmation messages stay visible · CLS within core rules §4.
3. **Markdown delivery** (optional, docs/SaaS): `.md` alternates linked with `<link rel="alternate" type="text/markdown">`, or the same URL answering `Accept: text/markdown` with `Vary: Accept`. Same content as the HTML; never switch content by user agent (cloaking).
4. **WebMCP** (W3C community draft, Chrome trial): only for sites with real forms or transactions, as an enhancement. Tools must call the same handlers as the UI, and purchases, sends and deletes keep a human confirmation step.
5. **Content-Signal** robots line (e.g. `search=yes, ai-input=yes, ai-train=no`): a stated preference with no confirmed effect; ask the owner before adding, and repeat it inside every named group.

## Output format

```markdown
## AI Search Readiness — <domain> — YYYY-MM-DD
Score: XX/100 (grade X) · coverage XX% · focus: GEO/AEO/All
Pages reviewed: <list> (crawl / aeo-audit.mjs)

| Category | Weight | Score % | Items not measured |
|---|---|---|---|
| Citability and answer readiness | 25 | | |
| Structure | 20 | | |
| Authority and brand | 20 | | |
| Technical access | 20 | | |
| Multimodal | 15 | | |

AI crawler access (robots.txt, date checked):
- Search bots: allowed / blocked: <names>
- User-triggered fetchers: ...
- Training bots: <allowed/blocked> — owner decision: <recorded / ask>
Firewall/CDN: <finding or "not measured">
Without JavaScript: main content <present/missing> in raw HTML

### Content rubric
| Dimension | Score 0–5 | Evidence | Key finding |

### Fixes
| # | Priority | Finding | Fix | Owner module | How we'll verify |

### Agent readiness (if run)
Lighthouse Agentic Browsing X/N (Lighthouse vX, date) · accessibility-tree issues · notes

### Not measured
- <item> — reason — what would unlock it
```

## Fallbacks and "not measured"

| Situation | Do this |
|---|---|
| Can't fetch | Ask for robots.txt text, raw HTML of key pages and llms.txt; score only those |
| Can't run code | Do §1–§6 by reading; skip the script |
| No access to firewall/CDN or logs | §2 = "not measured" (item dropped from the maths) |
| Modules 10/31/40 not run | Matching §6 items = "not measured"; say which module would unlock them |
| Robots.txt answers 429 or times out | "Not tested", never "allowed" |
| No search ability | Platform notes stay general; AI visibility tests belong to 60 |
