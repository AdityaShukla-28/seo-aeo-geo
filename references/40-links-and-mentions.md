# 40 — Links and mentions

Analyze the backlink profile honestly, then find and act on ethical link and brand-mention opportunities that help classic rankings and AI citations.

**Inputs:** `seo-workspace/<domain>/site-profile.md`, `brand-dna.md`, `research/competitors.md`, `research/prompts.csv`, `research/community.md` (language mining from 11), any link export the user can provide.
**Outputs:** `seo-workspace/<domain>/audits/YYYY-MM-DD-backlinks.md` (profile analysis), `seo-workspace/<domain>/plan/backlink-plan.md` (from `templates/backlink-plan.md`), outreach drafts from `templates/outreach-templates.md`.

## When to use / skip

| Situation | Do |
|---|---|
| Full audit | Part A (profile analysis), light |
| GEO focus, SaaS, agency, publisher, marketplace, e-commerce | Part A + Part B in depth (core in 02-site-types.md) |
| Local business | Part A light; local citations and reviews live in 50-local.md; use Part B for local PR and "best of" lists |
| Portfolio, docs, landing page | Light: profiles, a few relevant directories and communities; skip heavy campaigns |
| New site (under ~10 pages, few links) | Skip Part A scoring (not enough data); go straight to Part B |
| Ranking drop after a link-related manual action | Part A §A6 (disavow) first |

Entity setup (Organization/Person, `sameAs`, Wikidata, knowledge panel, review-platform profiles) is owned by 10-brand-and-entity.md. Community language mining is owned by 11-demand-research.md. This file covers participation, not mining.

---

## Part A — Backlink profile analysis

### A1. Pick data sources and label confidence

Use every source you can reach. Label each metric with its source and confidence (core rules §1).

| Source | Access | Gives | Confidence |
|---|---|---|---|
| Paid link index (any: DataForSEO, Ahrefs, Semrush, SE Ranking, Majestic, Moz paid…) | Paid account | Referring domains, anchors, new/lost, authority, spam signals, any domain | 1.0 |
| Verification fetch (open the linking page, look for `href` to the site) | Free | Link exists / removed / nofollow, for known URLs only | 0.95 |
| Google Search Console → Links report | Free, verified own site | Top linking sites, top linked pages, top anchor text (sampled; no quality metrics) | 0.90 for existence |
| Moz free tier / free verified-site tiers of paid tools (e.g. Ahrefs Webmaster Tools) | Free signup *(limits perishable)* | Authority score, linking domains, anchors, spam score | 0.85 |
| Bing Webmaster Tools → Backlinks | Free, verified own site | Linking URLs, anchors, comparison with other domains | 0.70 |
| Single-metric rank sources (Open PageRank and similar) | Free | One rank number, no links or anchors | 0.60 |
| Common Crawl web graph | Free, public | Domain-level rank/presence only; no anchors, no page-level data | 0.50 |

Free sources capture a minority of all links but most of the strong ones; for sites with a few hundred links they show much of what matters (directional, source study). Known biases: they favor popular sites, truncate long tails, lag by weeks to months, and own-site tools only cover verified properties. **Referring domains matter more than raw backlink counts.**

### A2. Collect seven factors

| # | Factor | Weight | Good | Warning | Critical |
|---|---|---|---|---|---|
| 1 | Referring domain count (vs. 3 competitors) | 20 | At or above competitor median | 50–100% of median | Under 50% of median |
| 2 | Domain quality distribution | 20 | Links from several authority tiers, relevant niches, target-market countries | Skewed to low tier | Mostly irrelevant countries or niches (≥80%: network signal) |
| 3 | Anchor text naturalness | 15 | Within benchmarks below | One type out of range | Exact match >15% |
| 4 | Toxic link ratio | 20 | Few or no high-risk patterns | Several medium-risk patterns | High-risk patterns present at scale |
| 5 | Link velocity trend (needs dated data) | 10 | Growing or stable | Slow decline | >20% loss per quarter, or sudden spike |
| 6 | Follow / nofollow ratio | 5 | >60% follow | 40–60% | <40% |
| 7 | Geographic relevance | 10 | Mostly target market | Mixed | Mostly unrelated countries |

Also check **domain concentration**: no single domain should supply >5% of links (warning >10%, critical >25%). Raw counts like "100 referring domains" mean little alone; compare to competitors in `research/competitors.md`.

**Anchor benchmarks** (share of referring-domain anchors):

| Anchor type | General range | Over-optimization signal |
|---|---|---|
| Branded (name, domain) | 30–50% (local services 45–60%, SaaS 40–55%) | Under 15% |
| Naked URL | 15–25% | — |
| Generic ("click here", "website") | 10–20% | — |
| Exact-match keyword | 3–10% | Over 15% |
| Partial-match keyword | 5–15% | Over 25% |
| Long-tail / natural sentence | 5–15% | — |

These are review heuristics, not Google rules.

### A3. Data-sufficiency gate (mandatory)

1. Count factors with at least one real data source.
2. **4 or more factors:** compute a 0–100 Backlink Health score. Re-weight over measured factors only. When sources mix, weight each factor score by its source confidence: `score = Σ(factor_score × confidence × weight) ÷ Σ(confidence × weight)`.
3. **Fewer than 4 factors:** write `Backlink Health: INSUFFICIENT DATA (n/7 factors measured)` and show only the factor results you have, each with its source.
4. **Only Common Crawl or a single-metric rank source:** give **no number of any kind** (no score, no "approximate" score). Write `Not assessed`, and report the rank/presence data as low-confidence context.
5. Never let a missing factor read as "weak profile". Lack of data is not a finding.

### A4. Toxic and risky patterns

| Risk | Patterns |
|---|---|
| **High (flag)** | Known link networks / PBNs; hacked pages with pharma, casino or adult injections; spun or auto-generated pages; link farms (pages with thousands of outbound links); exact-match anchors from many unrelated domains; site-wide footer/sidebar links from unrelated sites (paid-link pattern); doorway pages; deindexed or penalized domains; new domains (under 30 days) with hundreds of outbound links |
| **Medium (review by hand)** | Reciprocal patterns across 10+ domains; expired domains repurposed for links; pages with >50 outbound links or under 100 words; low-quality guest-post networks; article directories; unrelated niche; language mismatch; >50 links from one domain; >90% outbound link ratio |
| **Low (monitor, usually ignore)** | Social bookmarks at scale; forum profile links; press-release syndication; coupon aggregators; generic directories; blog comments; scraper sites; nofollow-only domains |

**Velocity red flags:** ~10× normal new links in a week (possible negative SEO: investigate); 50%+ links lost in a month (check Search Console → Manual actions, and whether linking pages died); no new links for 3+ months (content attracts none: see Part B); all new links from one TLD or country (coordinated activity).

Most low-quality links are simply ignored by Google. Report them; don't panic the owner.

### A5. Pages and gaps

1. **Top linked pages**: which pages earn links (link magnets) → make more like them; feed them internal links to money pages (13-strategy-and-plan.md).
2. **Linked 404s**: pages that return 404 but have backlinks → 301 to the closest live page (20-technical-audit.md). Usually the fastest win.
3. **Competitor gap**: domains linking to ≥2 competitors but not to the site = prospects. Domains linking to both = existing relationships. Domains linking only to the site = advantage to protect. Needs a paid index or both properties in Bing WMT; otherwise do a manual gap: search `"competitor name" -site:competitor.com` and list editorial pages that mention competitors but not the brand.
4. **Lost links** (only with dated data or a saved list): re-verify; a page that answers 5xx or 403/429 is "could not check", not "lost"; a JavaScript-rendered page whose link you can't see is "unconfirmed", not "removed".

### A6. Disavow: only in clear cases

Disavow only when **one** of these is true:
- Search Console shows a **manual action for unnatural links to your site**, or
- There is clear evidence of links the site (or a past SEO vendor) bought or built through a scheme, or
- A large, ongoing negative-SEO spam attack that is plainly hurting the site.

Do **not** disavow: ordinary low-quality or low-authority links, nofollow links, a small number of spam links, or links you merely dislike. A wrong disavow can remove helpful links.

Process: try removal first (ask the linking site), then build a UTF-8 `.txt` file of `domain:example.com` lines with `#` comment lines (date, reason), and have the owner upload it in Search Console's disavow tool (Bing WMT has its own). For a manual action, follow with a reconsideration request describing what was cleaned up. Log it in `tracking/change-log.md`.

---

## Part B — Earning links and mentions

AI assistants recommend brands that appear across many independent, relevant sources. Mentions without links still count for GEO; links still count for SEO. Every tactic below must pass core rules §8 (no buying links, no undisclosed promotion, no fake reviews, no link schemes).

### B1. Set constraints

Ask: channels already active (skip them), channels to avoid, weekly time budget, who will post (the AI only drafts; a human posts from their own account after reading the draft), and the target prompts from `research/prompts.csv`.

### B2. Find opportunities (real URLs only)

| Channel | How to find (search queries) | Typical action |
|---|---|---|
| Directories and review platforms (G2, Capterra, Product Hunt, Clutch, industry and regional directories) | `"[category]" directory submit`, `"[competitor]" site:g2.com` | Claim / submit listing; ask real customers for honest reviews (no gating) |
| "Best X" lists and roundups | `best [category] [year]`, `[competitor] alternatives` | Pitch the author with facts. A paid placement needs a visible sponsorship label **and** `rel="sponsored"` (or `nofollow`) on the link; a paid followed link is a link scheme (core rules §8) |
| Reddit | `site:reddit.com [pain point]`, `site:reddit.com [competitor] alternative`, `site:reddit.com best [category]` | Helpful, disclosed reply (B4) |
| Hacker News | `site:news.ycombinator.com "Ask HN" [problem]`; search hn.algolia.com | Show HN for something genuinely new and usable; comments with disclosure |
| Quora, Stack Exchange, niche forums, Discord/Slack communities | `site:quora.com "how to [problem]"`, `"[category]" forum OR community` | Answer the question; link only to the exact page that helps |
| GitHub awesome lists | `site:github.com "awesome-[category]"` | PR following the list's contribution guide |
| Podcasts and guest spots | `"[topic]" podcast "guest"`, podcast directories' search | Pitch 2–3 specific episode ideas (template) |
| Digital PR and original data | Journalist request services and hashtags (e.g. #journorequest) *(services change; verify)* | Answer only within real expertise; pitch data stories |
| Unlinked brand mentions | `"[brand]" -site:[domain]`, news search | Polite link request (template) |
| Syndication (Dev.to, Medium, Hashnode, LinkedIn articles) | — | Republish with a canonical link to the original where supported |
| Partners, integrations, suppliers, customers | Partner pages, "integrations", "customers" pages | Ask to be listed where a real relationship exists |
| Wikipedia | Check notability: independent reliable coverage | Never write or edit the brand's own article; propose sourced edits on the Talk page with a conflict-of-interest disclosure (entity work in 10) |

For each opportunity record: URL, last activity date, competitors mentioned, brand mentioned (yes/no), visible engagement (or "visibility unknown": never invent numbers), community rules that apply.

### B3. Score and prioritize

Score each 1–5 and weight:

| Factor | Weight | 5 means |
|---|---|---|
| GEO/SEO impact | 40% | Source AI answers or the target SERP already cite; relevant, editorial, followed or high-visibility |
| Effort (inverse) | 30% | Minutes, no special reputation needed |
| Relevance | 30% | Matches the brand's category and a target prompt or keyword exactly |

| Label | Rule | When |
|---|---|---|
| Quick Win | Weighted ≥4, effort score ≥4 | This week |
| High Value | Weighted ≥3.5, effort 2–3 | This month |
| Long Play | High impact, effort 1 (needs original research, notability, a track record) | Plan |
| Skip | Low impact, poor fit, or no way to help honestly | Record reason |

For community threads, also label the **motion**:

| Signal checked | Immediate | Build content first | Monitor | Skip |
|---|---|---|---|---|
| Pain intensity, recommendation/comparison/troubleshooting intent | Clear | Clear | Weak | None |
| Brand can help without forcing | Yes, with an existing page | Yes, but no good page yet | Unsure | No |
| Community active, rules allow mentions | Yes | Yes | Unknown | No / bans promotion |
| Recurring theme (not a one-off) | Any | Yes → create the guide (30-content-creation.md) | — | — |

Fit the plan to the stated time budget: if it is 30 minutes a week, Quick Wins must fit in 30 minutes.

### B4. Drafting rules for community replies (mandatory)

1. **Help first.** The reply must be useful even with the brand removed: answer, steps, data, trade-offs.
2. **Disclose every time** the brand, client or employer is mentioned: "Disclosure: I work at [brand]." No exceptions, no "where appropriate".
3. **Brand as one option**, not the headline. Name alternatives fairly when the asker would want them.
4. **Link to the specific page** that answers the question, never the home page; often no link is better.
5. **Match the venue**: technical depth for HN and Stack Exchange, structured answers for Quora, casual and direct for Reddit. No marketing language.
6. **Follow each community's rules**: read them first; respect self-promotion limits and account-age rules.
7. **Never**: post from multiple or bought accounts, ask anyone to upvote, astroturf "customer" posts, delete-and-repost, or reply to threads where the fit is forced (mark "Skip: no natural fit").
8. **Human posts it.** Deliver drafts for review; don't post on the user's behalf without explicit approval of each post.

Directory listings: draft title, short and long description, category, tags, submission URL and requirements. Show HN: honest title ("Show HN: X, a [what] for [who]"), what it does, what's new, how to try it free. Awesome-list PR: one-line entry in the list's format plus a short PR body.

### B5. Digital PR and original data

The most linkable and most AI-citable assets are things only the brand can publish:

| Asset | Examples | Requirements |
|---|---|---|
| Original data study | Survey, benchmark from anonymized product data, price index | Methodology page, sample size, dates, downloadable data (Dataset schema via 21-schema.md, charts via 31-visuals.md) |
| Free tool or calculator | Cost calculator, checker, template | Works without sign-up for the basic result |
| Expert commentary | Answers to journalist requests | Real named expert, claims checked (32-fact-check.md) |
| Annual/seasonal report | "State of [category] [year]" | Repeat yearly with the same method so the URL accrues links |

Pitch: one-sentence finding, why it matters to that outlet's readers, a chart, link to methodology. Never fabricate data, credentials or quotes.

### B6. Unlinked mentions

1. Search `"[brand]" -site:[domain]` (and product names, founder name) with a recent date filter; also news search.
2. Open each page; confirm there is no `href` to the domain.
3. Keep editorial, relevant, recent pages; skip forums, scrapers and pages where a link would be odd.
4. Send the short unlinked-mention template. One polite follow-up at most. Accept no.

### B7. Brand-mention monitoring (free methods)

| Method | Covers | Cadence |
|---|---|---|
| Google Alerts and Talkwalker Alerts on brand, product, founder, competitors | Web and news | As they arrive |
| Free keyword alert services for Reddit and HN (e.g. F5Bot) *(perishable)* | Communities | Daily digest |
| Reddit search sorted by New; hn.algolia.com | Communities | Weekly |
| `"[brand]" -site:[domain]` with date filter in Google and Bing | Web | Monthly |
| Search Console and Bing WMT links reports | New linking domains | Monthly |
| AI assistant answers to target prompts | GEO mentions | Monthly via 60-measurement.md |

Log notable mentions and outcomes in the plan's tracking table. Reply to criticism factually and politely, with disclosure.

---

## Output format

**Profile analysis** (`audits/YYYY-MM-DD-backlinks.md`):

```
# Backlink profile: <domain> (YYYY-MM-DD)
Backlink Health: <NN/100, coverage n/7> | INSUFFICIENT DATA (n/7) | Not assessed
Sources: <source (confidence)>, ...

| Factor | Result | Status | Source (confidence) |
|---|---|---|---|
| Referring domains | 140 vs competitor median 310 | warn | <tool> (1.0) |
| Anchors | branded 22%, exact 18% | fail | GSC Links (0.90) |
| ... | not measured | — | — |

Critical / High / Medium / Low findings (each: evidence, why it matters, fix, source)
Linked 404s to redirect: <url → target>
Competitor gap: top 20 prospect domains (or "not measured: needs a link index")
Disavow: not recommended | recommended because <manual action / scheme evidence>
Not measured: <what, and what access unlocks it>
```

**Opportunity plan**: `templates/backlink-plan.md`, saved to `plan/backlink-plan.md`. Drafts use `templates/outreach-templates.md`.

Before delivering: every metric has a source; no numeric score below the sufficiency gate; JS-rendered pages are "unconfirmed", not "removed"; every opportunity has a real URL; every draft that mentions the brand carries a disclosure line.

## Fallbacks and "not measured"

| Missing | Do instead |
|---|---|
| No link data at all | Skip the score ("Not assessed"); ask the owner to export Search Console → Links (top linking sites, top linked pages, anchors) as CSV, or connect Bing WMT; run Part B regardless |
| Can't fetch pages | Ask the user to open listed URLs and confirm the link and its `rel`; mark others "not verified" |
| No web search | Ask the user for competitor names, communities they know, and known mentions; draft templates and a channel checklist instead of a URL list; mark "opportunity list not measured" |
| Can't run code | Do everything manually; the weighted score is simple arithmetic you can show in a table |
| No dated data | Skip velocity and new/lost; say "point-in-time snapshot only" |
| New or tiny site | No score; Part B only, starting with directories, profiles, partners and one original-data asset |
