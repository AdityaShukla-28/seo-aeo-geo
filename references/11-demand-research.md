# 11 — Demand research

Find what people search for (keywords), what they ask AI assistants (prompts) and the words they use (community language), then group keywords the way search engines group them (SERP overlap).

**Inputs:** `brand-dna.md`, `research/competitors.md`, `site-profile.md`; Search Console query export if available; any paid SEO tool export the user provides.
**Outputs:** `seo-workspace/<domain>/research/keywords.csv`, `research/prompts.csv`, `research/community.md` (templates in `templates/`); category criteria and cited sources appended to `research/competitors.md`.

---

## When to use / skip

| Site type (02-site-types.md) | Scope |
|---|---|
| Local, E-com, SaaS, Publisher, Agency, Docs, Marketplace | Full: Parts A–D |
| Portfolio (◐) | Name and "name + role" keywords, 5–10 "who is / best <role> in <city>" prompts; skip clustering |
| Landing page (◐) | The one target query, its close variants and objection questions; skip clustering |
| Quick task needing only a few keywords | Part A steps 1–4 only, no CSV unless asked |

Rough candidate counts before pruning: Landing 5–15 · Portfolio 10–20 · Local 30–80 · others 60–150. After pruning, quality beats count.

---

## Procedure

### Part A: Keywords → `keywords.csv`

1. **Pick 3–5 seed terms** from `brand-dna.md`: the category, main products/services, the problem solved, plus location for local businesses. Use customer words, not internal jargon.
2. **Start with real data if you have it.**
   - Search Console (Queries report, last 3–16 months): every query with impressions is proven demand. Queries with impressions in the quick-win and striking-distance position ranges (core rules §4) are the quickest wins. Label `metric_source` = `gsc`. (How to connect and export: 60-measurement.md.)
   - Paid SEO data: if a paid SEO data tool is available (DataForSEO, Ahrefs, Semrush, SE Ranking, Moz…), use it for volume, difficulty and competitor keyword gaps, and label the source; otherwise use the free methods below.
3. **Discover candidates with free methods.** Run each seed through:

   | Method | How | Typical finds |
   |---|---|---|
   | Autocomplete (manual) | Type the seed plus modifiers into a search box and note suggestions: `for`, `vs`, `best`, `how to`, `without`, `free`, `alternative`, `price`/`cost`, `near me`, `review`, `template`, `examples`, `for beginners` | Long-tail and use-case variants |
   | People Also Ask | Search the seed, `how to choose <seed>`, `is <seed> worth it`; note every question | Questions (go to Part B as prompts if conversational) |
   | Related searches | Bottom of the results page | Journey steps before and after |
   | Competitor pages | `site:<competitor>` + their navigation, category and blog topics; `<competitor> vs`, `<competitor> alternative` | Gaps and comparison terms |
   | Problem / job terms | `how to <job the product does>`, `<pain> fix`, `<task> checklist` | Problem-aware keywords |
   | Community language | From Part C | Real phrasing, slang |
   | Site and sales language | Ask the user for top sales/support questions and review excerpts | Buyer objections |

   Observe autocomplete and PAA by hand (or through a SERP data API). **Never scrape Google endpoints with a fake browser user agent** (core rules §8). If your search tool shows no autocomplete, ask the user to type the seeds in their own browser and paste what appears.

4. **Keep the keyword as people type it.** Head terms (1–3 words) usually anchor pillars. Longer phrases (4–6 words) are valid spoke targets **when there is evidence of demand** (autocomplete, PAA, GSC impressions). Full conversational questions ("what's the best X for a 5-person team") belong in `prompts.csv`, not here.

5. **Validate and prune.** Keep a keyword only if it has at least one demand signal and passes the relevance check:

   | Evidence (count how many) | Strong | Weak |
   |---|---|---|
   | Volume > 0 from a labeled paid tool, or GSC impressions | ✔ | |
   | Appears in autocomplete or PAA | ✔ | |
   | Pages dedicated to the exact topic rank on page 1 | ✔ | |
   | Discussed in forum threads | | ✔ |
   | Only appears in your own brainstorm | | ✘ drop |

   - Drop confirmed zero-volume terms from a paid tool.
   - **Relevance rule**: drop anything the site cannot credibly serve with its real products, services or expertise (core rules §3).
   - Keep navigational keywords only for the user's own brand.

6. **Classify intent** (12-search-intent.md refines it from the live SERP):

   | `intent` | Signals |
   |---|---|
   | `informational` | how, what, why, guide, examples, ideas |
   | `commercial` | best, top, review, vs, alternative, comparison |
   | `transactional` | buy, price, pricing, book, hire, quote, near me, free trial |
   | `navigational` | a brand or product name, login |

7. **Assign `priority`.** Difficulty scales differ between tools; never mix tools in one column, and treat the bands as directional.

   | `priority` | With a labeled difficulty score (0–100) | Without one (estimate from the SERP, mark "SERP estimate" in `notes`) |
   |---|---|---|
   | `easy-win` | 0–15 | Page 1 shows forums, thin or outdated pages, small sites, few exact-match titles |
   | `target` | 16–50 | Mixed page 1: some strong brands, some beatable pages |
   | `hard` | >50 | Page 1 dominated by major brands, publishers or marketplaces |
   | `authority` | Any | Broad term worth covering for topical depth; ranking not expected soon |

8. **Record SERP features** you observed (pipe-separated, see column table). Leave empty if not checked; write `none` if checked and none appeared.

### Part B: AI prompts → `prompts.csv`

9. **Understand the difference.** Prompts are full natural-language questions (usually 5–15+ words) with context and constraints: budget, team size, location, use case. People ask follow-ups. One keyword can map to many prompts.
10. **Discover prompts across 8 query types.** Aim for 30–80 raw prompts (Local 10–20, Portfolio 5–10), then dedupe.

    | `query_type` | Patterns |
    |---|---|
    | `definition` | What is X? How does X work? Difference between X and Y? |
    | `recommendation` | Best X for <use case/audience>? Which X should I choose? Top X in <year/city>? |
    | `comparison` | A vs B, which is better? X alternatives? How does A compare to B? |
    | `evaluation` | Is X worth it? Pros and cons of X? X problems? Can I trust X? |
    | `how-to` | How to <solve problem>? How to choose X? Step-by-step <task>? |
    | `cost` | How much does X cost? X pricing? Is X worth the investment? |
    | `landscape` | Which companies do X? Leaders in X? X competitors? |
    | `use-case` | Can X be used for <scenario>? How is X used in <industry>? Will X replace Y? |

    Sources: PAA questions, community threads (Part C), review sites, the user's sales and support questions, competitor comparison pages, and follow-up suggestions shown inside AI assistants.

11. **Assign `tier`** (business value):
    - `buy` — "who should I use / what's best": the brand can be named as an option.
    - `solve` — "how do I do this": the brand's method or product is the solution.
    - `learn` — "what is X": the brand is cited as an expert source.
    Guideline mix: ~20% buy, ~40% solve, ~40% learn (adjust to the goal; local businesses skew to buy).

12. **Score `citability` and `competition`.**

    | `citability` | Meaning |
    |---|---|
    | `high` | The answer needs specific sources: recommendations, comparisons, prices, data, local options |
    | `medium` | Answerable from general knowledge but sources are often cited |
    | `low` | Answered from general knowledge alone (basic definitions) |

    | `competition` | Meaning |
    |---|---|
    | `none` | No good page answers it |
    | `low` | Only small blogs or thin pages |
    | `medium` | Decent content from known brands |
    | `hard` | Dominated by major brands, publishers or reference sites |

13. **Derive `priority`:** `buy` or `solve` + `high` citability + `none`/`low` competition → `easy-win`; any tier + `high` citability + `medium`/`hard` competition → `target`; `low` citability → `skip`; use judgment in between. Keep `skip` rows: they record what not to chase.
14. **Write a concrete `brand_mention_mechanism`.** How exactly would the brand appear in the answer? Good: "listed in top-5 alongside <A> and <B> because our comparison table is cited", "our pricing page quoted for cost range in <city>". Bad: "builds awareness".
15. **Map the category.** While researching, list 8–12 criteria assistants and reviewers use to judge options in this category (price, integrations, certifications, warranty, response time…) and 10–15 sources they cite (review sites, associations, publications, directories). Append both to `research/competitors.md` (format in 10-brand-and-entity.md).
16. **Sort** rows: buy/easy-win, buy/target, solve/easy-win, solve/target, learn/easy-win, learn/target, then all `skip`. The AI visibility panel in 60-measurement.md is built from these rows.

### Part C: Community language → `community.md`

This is the only place community mining happens. It is **read-only research** for language, pain points and prompt discovery. Replying, posting and participation rules are in 40-links-and-mentions.md.

17. **Write three search buckets** before searching: **problem** (pains, jobs to be done), **solution** (category, best, alternatives), **competitor** (reviews, complaints, migrations).
18. **Run 15–40 searches** across the bucket terms, for example:
    - `site:reddit.com <pain>` · `site:reddit.com <pain> recommendation` · `site:reddit.com best <category>`
    - `site:reddit.com <category> vs <alternative>` · `site:reddit.com <competitor> review` · `site:reddit.com <competitor> alternative`
    - `site:quora.com <question>` · `<category> forum` · `<audience role> <pain>`
    - Low-star (1–3) reviews of competitors on the type's review platforms (10-brand-and-entity.md step 11)
    Add market-specific communities (regional forums, language-specific subreddits, niche Discord/Slack groups with public archives).
19. **Extract per thread or repeated theme:** community, theme, pain in plain words, exact phrasing (short quote), what the asker wants (recommendation / comparison / troubleshooting / workflow), brands mentioned together, unanswered questions, link. Do not record usernames or personal details.
20. **Score each theme 1–3** on pain intensity, repeatability (recurring vs one-off) and content fit (could a page, comparison, checklist or tool answer it). Label: `content-now` (score ≥7 and you can answer it), `build-asset` (strong theme, needs data or a tool first), `monitor`, `skip`. Note communities where participation might fit as a hand-off to 40.
21. **Feed the other files:** new phrases → `keywords.csv` (`discovery_source` = `community`); questions → `prompts.csv`; complaints about competitors → differentiation notes in `brand-dna.md`.

### Part D: Cluster keywords by SERP overlap

22. **Collect the top 10 organic URLs** for each keyword (ignore ads, snippets, PAA, panels). Normalize: drop protocol, `www`, trailing slash, tracking parameters. Cache results; reuse them for every pair.
23. **Reduce the work.** Pre-group by intent and head term; compare pairs only inside groups, plus the top keyword of each group across groups. Assume long-tail variants of the same head term with the same intent share a cluster, and spot-check about 20% of those assumptions.
24. **Down-weight ubiquitous domains** (Wikipedia, Reddit, YouTube, Amazon, major directories) that appear in most results, or exclude them before counting.
25. **Count shared URLs and apply:**

    | Shared URLs in top 10 | Relationship | Action |
    |---|---|---|
    | 7–10 | Same page | One page targets both; the higher-demand keyword is primary |
    | 4–6 | Same cluster | Same cluster; separate pages only if intents or demand differ clearly |
    | 2–3 | Related | Adjacent clusters; plan cross-links |
    | 0–1 | Separate | Different clusters, or out of scope |

    Tie-break scores of 3–4: same domains but different pages → closer; same intent → same cluster; one keyword with ~10× the demand → its own page; when unsure, same cluster, separate pages. Different SERP features (local pack vs featured snippet) mean different page types even with overlap.
26. **Pick one pillar per cluster:** broadest term, highest demand, most overlaps. Name clusters in kebab-case. Fill `cluster` and `is_pillar`.
27. **Web search is approximate** (core rules §1.4): results vary by session, location and personalization. Run important keywords twice and use the most common set. Without any search access, cluster by intent + head term and add "text-based cluster, not SERP-verified" to `notes`.

---

## Output format

### `keywords.csv` columns (exact header, this order)

`keyword,volume,kd,metric_source,intent,priority,cluster,is_pillar,serp_features,discovery_source,notes`

| Column | Required | Allowed values |
|---|---|---|
| `keyword` | yes | Lowercase search phrase, unique; questions longer than ~6 words go to prompts.csv |
| `volume` | no | Integer ≥0 monthly searches; empty if not measured |
| `kd` | no | Integer 0–100 difficulty; empty if not measured |
| `metric_source` | yes | `gsc` · `ahrefs` · `semrush` · `dataforseo` · `se-ranking` · `moz` · `keyword-planner` · `other-tool` · `not-measured` (must be `not-measured` when `volume` and `kd` are empty) |
| `intent` | yes | `informational` · `commercial` · `transactional` · `navigational` |
| `priority` | yes | `easy-win` · `target` · `hard` · `authority` |
| `cluster` | yes | kebab-case cluster name |
| `is_pillar` | yes | `true` · `false` (exactly one `true` per cluster) |
| `serp_features` | no | Pipe-separated: `ai-overview` · `featured-snippet` · `paa` · `local-pack` · `shopping` · `video` · `images` · `forums` · `news` · `knowledge-panel` · `none`; empty = not checked |
| `discovery_source` | yes | `gsc` · `paid-tool` · `autocomplete` · `paa` · `related-searches` · `community` · `competitor` · `site-copy` · `user` · `manual` |
| `notes` | no | Free text (e.g. "SERP estimate", "text-based cluster") |

### `prompts.csv` columns (exact header, this order)

`prompt,tier,query_type,citability,competition,priority,cluster,target_engines,brand_mention_mechanism,discovery_source,notes`

| Column | Required | Allowed values |
|---|---|---|
| `prompt` | yes | Lowercase natural-language question, ≥5 words, no trailing `?`, unique |
| `tier` | yes | `buy` · `solve` · `learn` |
| `query_type` | yes | `definition` · `recommendation` · `comparison` · `evaluation` · `how-to` · `cost` · `landscape` · `use-case` |
| `citability` | yes | `high` · `medium` · `low` |
| `competition` | yes | `none` · `low` · `medium` · `hard` |
| `priority` | yes | `easy-win` · `target` · `skip` |
| `cluster` | yes | kebab-case; reuse the keywords.csv cluster name when the topic is the same |
| `target_engines` | yes | Pipe-separated, ≥1: `chatgpt` · `perplexity` · `claude` · `gemini` · `copilot` · `ai-overview` · `ai-mode` |
| `brand_mention_mechanism` | yes | Concrete description (see step 14) |
| `discovery_source` | yes | `paa` · `community` · `autocomplete` · `review-site` · `competitor` · `sales-support` · `ai-observed` · `user` · `manual` |
| `notes` | no | Free text |

### CSV rules (both files)

- UTF-8, comma-delimited, header row first; quote any field containing a comma, quote or line break (`"` inside becomes `""`).
- Every row has exactly the header's number of fields; empty optional fields are written as nothing between commas.
- Enum values exactly as listed (lowercase, hyphenated). No duplicate `keyword` or `prompt`.
- The example rows in the templates are illustrative; replace them.

### `community.md`

Use `templates/community.md`: summary, language bank, pain points, comparison sets, unanswered questions, communities to watch (hand-off to 40), outputs fed to keywords/prompts.

### Chat summary

```
DEMAND RESEARCH: <domain>      (YYYY-MM-DD)
Keywords: 64 kept of 141 found · 9 clusters · metrics: gsc + not-measured (no paid tool)
Easy wins: <kw>, <kw>, <kw>
Prompts: 38 (buy 8 / solve 15 / learn 15) · 21 easy-win or target
Community: 12 themes · top pain: "<short quote>" (r/<sub>)
Clustering: SERP overlap on 40 keywords (approximate, built-in search); 24 text-based
Not measured: search volume, difficulty (no paid tool or Search Console)
```

## Fallbacks and "not measured"

| Missing ability | Do this |
|---|---|
| No search | Ask the user for seed topics, competitors and customer questions; build from site copy and their answers; `metric_source` = `not-measured`, clusters text-based |
| No Search Console, no paid tool | Volume and difficulty stay empty, `not-measured`; priority from SERP estimate (step 7) |
| Can run code + a SERP data API key in the environment | A script may pull autocomplete, PAA, related searches and SERP features per seed; read the key from an environment variable, never write it to files (core rules §9). Manual fallback: steps 3 and 22 |
| No AI assistant access | Prompts come from PAA, community and sales questions; `discovery_source` never `ai-observed` |
| No file access | Print each CSV in a fenced block, then `community.md` |
