# 13 — Strategy and plan

Turn the research into a page plan (which pages to improve or create, how they link, in what order), a phased roadmap and measurable KPIs.

**Inputs:** `site-profile.md`, `brand-dna.md`, `research/keywords.csv`, `research/prompts.csv`, `research/community.md`, `research/competitors.md`, `research/serp-intent.md`, the latest `audits/` files, and a list of the site's indexable URLs (sitemap, crawl or Search Console).
**Outputs:** `seo-workspace/<domain>/plan/plan.csv`, `plan/roadmap.md` (templates in `templates/`).

---

## When to use / skip

| Site type (02-site-types.md) | Scope |
|---|---|
| Local, E-com, SaaS, Publisher, Agency, Docs, Marketplace | Full plan, clusters, roadmap |
| Portfolio (◐) | Small plan: home, about (identity hub), work index, one page per project, services/contact; no clusters unless they want to write |
| Landing page (–) | No plan.csv. If the user wants broader traffic, recommend splitting into a few real pages (home, pricing, FAQ, 2–3 use cases) and stop there |
| New site / pre-launch | Full plan; every row `action` = `create`; roadmap starts with foundations |

Plan only from research that exists. Do not invent keywords or prompts at this stage: if research is missing, run 11 first.

---

## Procedure

1. **Inventory existing pages.** List every indexable URL with its current main topic and, if Search Console is available, its top query, clicks and impressions (label `GSC`). Mark pages that are thin, outdated or duplicate (from the audit).
2. **Map research to pages.** For each keyword cluster from `keywords.csv`, find the existing page that already targets it (title/H1/URL/top GSC query). Outcomes:
   - One good match → `improve` (or `keep`).
   - Two or more pages competing for the same primary keyword (cannibalization) → `merge` into the strongest URL and redirect the rest, or differentiate their intents clearly.
   - No match → `create`.
3. **Group keywords and prompts into pages.** One page = one main topic, one dominant intent, 1–3 primary keywords that share a SERP (overlap 7+ means one page, 11-demand-research.md step 25), and 3–6 related prompts. Never one page per prompt. Typical groupings:
   - best / vs / alternatives → one `comparison` or `alternatives` page
   - how-to / workflow → `guide` or `use-case`
   - what is / how it works → `definition`
   - price / worth it / objections → `faq` (FAQ or trust page)
   - service or product category → `service`, `category` or `money`
4. **Choose the page type from the SERP**, not from preference: use the dominant type in `research/serp-intent.md` (12-search-intent.md step 5). Writing outlines per type are in 30-content-creation.md.
5. **Design hub-and-spoke clusters.**
   - Each cluster has one **pillar** (hub) targeting the cluster's pillar keyword: a broad guide for publishers/SaaS resources, a category page for stores, a service hub for local and agencies, a topic page for publishers.
   - **Spokes** cover one subtopic each, in more depth than the pillar does.
   - Size per pillar: 2–5 sub-topic groups, 2–4 spokes each (roughly 5–21 pages in total). Bigger means split into two pillars; smaller is fine for small sites.
   - Pages outside any cluster (home, pricing, contact) are `standalone`.
   - Coverage floors per page type: core rules §4. Length follows the topic, never a fixed target.
6. **Plan internal links** (record them in `parent_page_id` and `links_to`):

   | Link | Rule |
   |---|---|
   | Spoke → pillar | Mandatory, in body text |
   | Pillar → every spoke | Mandatory, in the section about that subtopic |
   | Spoke ↔ spoke, same cluster | 2–3 per page where genuinely related |
   | Spoke → other cluster | 0–1, only when there is a real bridge |
   | Spokes and guides → money page | At least one contextual link where the reader's next step is the product or service |
   | Existing strong pages → new pages | Add 1–3 links from pages that already get traffic (GSC top pages) |

   Floors from core rules §4 apply: every page ≥3 internal links in, within 3 clicks of home. Anchors: descriptive, the target keyword or a close variant; no single anchor text for more than ~40% of links to a page; never "click here". Breadcrumbs follow the URL hierarchy (schema in 21-schema.md).
7. **Prioritize** each page:

   | Priority | Use for |
   |---|---|
   | `p1` | Money pages and high-intent pages (`transactional`/`commercial`, `buy`/`solve` prompts with `easy-win`/`target`); existing pages with impressions that sit just off page 1 |
   | `p2` | Supporting spokes, comparisons for secondary competitors, trust pages |
   | `p3` | Authority and `learn` content, glossary, long-tail extras |

   Inside a priority, order by impact × confidence ÷ effort (core rules §2). Build pillars before their spokes; improving an existing page usually beats creating a new one. Every plan has at least one `p1`.
8. **Apply the relevance check** (core rules §3) to every row: can this business credibly publish it, does it move the goal, and can the person implementing it actually do it in the time available? Cut rows that fail.
9. **Plan pages at scale** only when the plan calls for many similar pages from data (integrations, locations, glossary, listings, templates). Steps:
   1. **Data check**: each record has enough unique attributes to make a distinct page; flag near-duplicate records (>80% of fields the same) and stale data.
   2. **Template design**: separate static blocks (shared) from dynamic blocks (unique per record); hide sections when data is missing instead of printing empty or generic text; no "mad-libs" text where only the name changes.
   3. **Standalone-value test**: would this page be worth publishing if no similar page existed?
   4. **URL pattern**: lowercase, hyphenated slugs from the data, unique, no parameters (core rules §4 URL rule), e.g. `/integrations/<tool>`, `/glossary/<term>`, `/<service>/<city>`.
   5. **Linking**: a hub page per category linking every child; each child links to its hub and 3–5 related children by shared attributes; breadcrumbs.
   6. **Uniqueness and metadata**: measure unique body text against the rest of the set, and check that titles and descriptions are not one repeated pattern.
   7. **Rollout**: human-review a sample, publish in batches, watch indexing before the next batch; canonicals and sitemaps per 20-technical-audit.md.
   Uniqueness, warning, stop and batch numbers are in core rules §4 ("Pages at scale", "Location pages"). Safe at scale: integrations with real setup details, glossary terms with real definitions and examples, data pages with unique numbers, products with unique specs. Risky: city-swap pages, "best X for <industry>" without industry-specific substance, "<competitor> alternative" without real comparison data (core rules §8).
10. **Write `plan.csv`** (columns below) and validate it with the checklist.
11. **Write `roadmap.md`** from `templates/roadmap.md`: phases, owners, dates, KPI table. Fit the phases to the resources the user stated (Limits question in 01).
12. **Show the user** the top 10 rows and the phase plan; get approval before content work starts.
13. **After pages are built, run the cluster scorecard** (below) and update `status` in `plan.csv`.

### Site architecture by type (complements 02-site-types.md)

02 says what each type should prioritize; this table gives the URL skeleton and where hubs and spokes sit.

| Type | URL skeleton | Hubs (pillars) | Spokes | Pages at scale? |
|---|---|---|---|---|
| Portfolio | `/`, `/about`, `/work/<project>`, `/services`, `/writing/<post>` | `/work` | Project pages | No |
| Local | `/services/<service>`, `/areas/<area>`, `/about`, `/reviews`, `/faq`, `/contact` | Each service page | Cost, process, problem guides linking to the service | Area pages only with real local proof (gates in core rules §4) |
| E-commerce | `/collections/<category>/<sub>`, `/products/<handle>`, `/brands/<brand>`, `/guides/<topic>` | Category pages | Subcategories, products, buying guides linking to categories | Facets: 51-ecommerce.md |
| SaaS | `/features/<feature>`, `/integrations/<tool>`, `/solutions/<use-case or industry>`, `/pricing`, `/compare/<a-vs-b>`, `/alternatives/<competitor>`, `/customers/<story>`, `/resources/<guides, learn, templates>`, `/docs` | Feature and solution hubs, compare hub, resource topic hubs | Use cases, comparisons, guides, templates | Integrations, glossary, templates |
| Publisher | `/topics/<topic>`, `/<article-slug>`, `/authors/<name>`, `/about/editorial-policy` | Topic pages | Articles | Rarely; keep evergreen URLs free of dates |
| Agency / B2B | `/services/<service>`, `/industries/<industry>`, `/work/<case-study>`, `/team/<person>`, `/insights/<post>` | Service hubs | Case studies, process, cost guides; industry pages only with real experience | No |
| Docs | `/docs/<section>/<page>`, `/api/<resource>`, `/guides/<task>`, `/changelog` | Section index pages | Task pages | API reference from source; versions canonical to current |
| Marketplace | `/<category>/`, `/<category>/<location>/`, `/<listing>`, `/data/<report>` | Category and category×location hubs with real inventory | Listings, market data pages | Yes, gated (core rules §4) |
| Landing | `/` (+ `/pricing`, `/faq`, 2–3 use-case pages if split) | — | — | No |

### Cluster scorecard (after building)

| Metric | Target | How measured |
|---|---|---|
| Coverage | 100% of planned rows `published` | `status` column |
| Pillar links | 100% of spokes ↔ pillar | Crawl or manual check |
| Sibling links | ≥80% of planned `links_to` live | Crawl or manual check |
| Incoming links per page | Core rules §4 floor | Crawl |
| Orphan pages | 0 | Crawl vs sitemap |
| Cannibalization | 0 pages sharing a primary keyword | `target_keywords` + GSC queries |
| Visuals | ≥1 meaningful image or chart per spoke | Manual (31-visuals.md) |

---

## Output format

### `plan.csv` columns (exact header, this order)

`page_id,priority,action,status,page_type,cluster,cluster_role,parent_page_id,links_to,section,subsection,title,url_slug,target_keywords,target_prompts,required_sections,why_it_matters,notes`

| Column | Required | Allowed values |
|---|---|---|
| `page_id` | yes | kebab-case, unique |
| `priority` | yes | `p1` · `p2` · `p3` |
| `action` | yes | `create` · `improve` · `merge` · `keep` · `redirect` |
| `status` | yes | `planned` · `briefed` · `drafted` · `published` · `updated` |
| `page_type` | yes | Content types with outlines in 30-content-creation.md: `guide` · `comparison` · `alternatives` · `use-case` · `definition` · `service` · `product-led` · `case-study` · `location` · `faq` · `article`. Structural types: `home` · `about` (identity hub, 10) · `money` (core product, feature or solution page) · `product` · `category` (51) · `listing-hub` · `tool` |
| `cluster` | conditional | kebab-case name from `keywords.csv`; empty only when `cluster_role` = `standalone` |
| `cluster_role` | yes | `pillar` · `spoke` · `standalone` (one `pillar` per cluster) |
| `parent_page_id` | conditional | `page_id` of the pillar; required for `spoke`, empty otherwise |
| `links_to` | no | Pipe-separated `page_id`s this page must link to besides its parent (siblings, money page, cross-cluster) |
| `section` | yes | `core` · `solutions` · `resources` · `shop` · `locations` · `company` · `docs` |
| `subsection` | conditional | Required when `section` = `resources`: `guides` · `comparisons` · `learn` · `blog` · `templates` · `tools`; empty otherwise |
| `title` | yes | Working title in plain language (final title rules in core rules §4) |
| `url_slug` | yes | Path starting with `/`, unique; for `improve`/`keep`/`merge` the existing URL |
| `target_keywords` | conditional | Pipe-separated; each value must exist in `keywords.csv` `keyword` (case-insensitive) |
| `target_prompts` | conditional | Pipe-separated; each value must exist in `prompts.csv` `prompt` (case-insensitive, `?` ignored). At least one of `target_keywords`/`target_prompts` is filled, except for `home`, `about` and `redirect` rows |
| `required_sections` | yes | Pipe-separated, ≥1: `direct-answer` · `comparison-table` · `who-this-is-for` · `how-it-works` · `steps` · `use-cases` · `pricing` · `specs` · `proof` · `objections` · `faqs` · `local-details` |
| `why_it_matters` | yes | Concrete business reason, ≥15 characters ("Owns the 'best X' cluster closest to purchase"), never "builds awareness" |
| `notes` | no | e.g. URLs merged into this page, data needed, owner |

Same CSV rules as 11-demand-research.md (quoting, field count, exact enums). Templates' example rows are illustrative.

### Validation checklist

- [ ] Header exact; every row has 18 fields
- [ ] `page_id` and `url_slug` unique
- [ ] Every keyword and prompt referenced exists in the research files
- [ ] Each cluster has exactly one `pillar`; every `spoke` has a `parent_page_id` that is that pillar
- [ ] `subsection` filled if and only if `section` = `resources`
- [ ] No two rows share a primary (first-listed) keyword
- [ ] At least one `p1`; every row passed the relevance check

### Roadmap and KPIs

`plan/roadmap.md` follows `templates/roadmap.md`. Default phases (shift to fit resources):

| Phase | Timing | Contents |
|---|---|---|
| 0. Foundations | Weeks 1–4 | Critical and High fixes from 20/21/22, tracking setup (60), entity setup (10), baselines |
| 1. Money pages | Weeks 3–8 | `p1` rows: improve existing money pages first, then create missing ones |
| 2. Clusters | Weeks 6–16 | Pillars, then spokes by priority; internal links as each page ships |
| 3. Authority | Months 3–9 | Original data, digital PR, reviews and profiles, community participation (40, 50) |
| 4. Scale and refresh | Months 6–12 | Gated pages at scale (if planned), refresh loop for decaying pages (60) |

KPI rules: every KPI has a source; baseline is the measured value on a stated date or "not measured"; targets are relative to the baseline (e.g. "+30% non-branded clicks"), never invented absolute numbers. Pick 4–7 KPIs that match the goal and type (02-site-types.md lists type KPIs). Measuring them is 60-measurement.md.

## Fallbacks and "not measured"

| Missing ability | Do this |
|---|---|
| No URL inventory | Ask for the sitemap URL or a page list; otherwise plan as a new site and mark every `action` as `create (unverified)` in `notes` |
| No Search Console | Prioritize by intent and research priority only; KPI baselines "not measured" until connected |
| No SERP check done | Use the page type implied by intent; add "page type not SERP-verified" in `notes` |
| No prompts.csv (SEO-only focus) | Leave `target_prompts` empty; keywords must then be filled |
| No file access | Print `plan.csv` and `roadmap.md` in fenced blocks |
