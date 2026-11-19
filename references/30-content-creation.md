# 30 — Content creation

Plan, write, score and refresh pages that rank, win answer boxes and get cited by AI assistants, without padding or invented facts.

**Inputs:** `site-profile.md`, `brand-dna.md`, `research/keywords.csv`, `research/prompts.csv`, `research/community.md`, `research/competitors.md`, `plan/plan.csv` (whatever exists)
**Outputs:** `content/briefs/<slug>.md`, `content/drafts/<slug>.md` (frontmatter + body), then `content/published/<slug>.md` after fact-check and approval

## When to use / skip

- **Use** for briefs, outlines, new pages of any type, comparison/alternatives pages, content-quality and E-E-A-T scores, rewrites and refreshes.
- **Light** for marketplaces (02-site-types §1): templates and category intros; pages at scale follow 13 and core rules §4.
- **Skip** blog clusters for one-page sites and portfolios unless the owner wants to write (core rules §3).
- Elsewhere: decay detection (60), research (11), SERP/intent (12), visuals (31), claim checks (32), code publishing (33).

## Procedure: brief → outline → draft → self-check → fact-check → publish

1. **Pick the target.** Take one row from `plan/plan.csv` (or the user's topic): primary keyword, 1–3 target prompts, page type, URL. If no research exists, run 11 first or ask the user for the keyword and audience.
2. **Choose mode.** *New page* (no URL yet) or *improve* (existing URL: fetch it, mark each section keep / strengthen / add / remove; never recommend a full rewrite when targeted fixes will do).
3. **Read the business.** Home page, sitemap and `brand-dna.md`. Apply the **website relevance rule**: every heading, subtopic, FAQ and claim must be something this business can credibly write about. Drop anything borrowed from competitors that the business does not offer. For hub/category pages, include every real child page from the sitemap, and invent none.
4. **Analyse the top results** (or reuse 12's SERP notes). Take the top 5 real competitors for the keyword. Skip aggregators, marketplaces, encyclopedias, forums, social and video platforms, government and news results that are not real business competitors. Score each 1–10 on Depth, Formatting, SEO, UX (total /40) and record the main gap. Mark search-based observations "approximate" (core rules §1.4).
5. **Find gaps.** Topic gaps (missing subtopics), depth gaps (covered thinly), quality gaps (outdated, no expert view, poor format). Rank by impact × competitive advantage ÷ effort.
6. **State the information gain** in one specific sentence: proprietary data, a real case with outcomes, expert or first-hand experience, an original framework or test. "More detail" or "better formatting" does not count. No gain → tell the user the page is unlikely to win and suggest what evidence to gather.
7. **Write the brief** with `templates/content-brief.md` → `content/briefs/<slug>.md`. Get the user's OK on keyword, angle and outline before drafting.
8. **Outline.** Use the page-type outline below. Per section: heading, word budget, format (paragraph, list, table, definition box), keyword guidance, "snippet target" if it is a question heading.
9. **Gather sources before writing.** Product facts from `brand-dna.md` only. External facts: primary sources (official docs, studies, government or standards bodies, recognised industry reports), recent where the topic changes. For each: claim, source name, date, URL. A number you cannot source is not used.
10. **Draft** with `templates/article-frontmatter.md` on top and pure content below (no notes, briefs or instructions in the body; H1 = `title`). Follow the writing standards below.
11. **Add visuals** only where they carry data, explain a process or prove a claim (31-visuals.md).
12. **Self-check** with the checklist below and score the draft (Content quality score). Fix anything that fails.
13. **Fact-check** with 32-fact-check.md. Fix every Critical item. YMYL pages: every claim (02-site-types §12).
14. **Publish** only after the owner approves: move to `content/published/`, then publish via the CMS (03-platforms.md) or code (33-publishing-in-code.md). Log it in `tracking/change-log.md` and add the target prompts to the AI visibility panel (60).

## Keyword and metadata placement

| Element | Rule |
|---|---|
| Primary keyword | In title tag (near the start), H1, slug, meta description, first 100 words. Not needed in every heading or paragraph; H1 plus 1–2 H2s is plenty. No density target; unnatural repetition is keyword stuffing (core rules §8). |
| Secondary keywords | 5–8 close terms and 10–15 related concepts, used naturally in body and H2/H3 where they fit. Synonyms are fine. |
| Title tag, meta description, H1, headings, URL | Lengths and rules in core rules §4. Primary keyword first, brand last, match the site's separator. Meta: active voice, specifics, a reason to click written for this page (not a stock CTA). |
| Image alt text | Describes the image (31-visuals.md). Not a keyword slot. |
| Internal links | Counts in core rules §4. Descriptive, varied anchors; link early when relevant; say whether the page is a hub (links down to cluster pages) or spoke (links up to its pillar) per 13. |

## Writing standards

1. **Answer first.** Each question heading is followed by a 40–60-word direct answer (core rules §4) that names its subject, works without the rest of the page and, where possible, contains one concrete fact or number.
2. **Self-contained passages** (core rules §4): no "as mentioned above", one idea per section.
3. **At least 2 quotable blocks** per page: 40–80-word passages an AI answer could lift whole (definition, verdict, key finding, "X is best for Y").
4. **Brand mention block** (commercial pages): one short standalone paragraph that says plainly why the brand belongs in the answer ("[Brand] is best for…", "Compared with [A] and [B], [Brand]…"). It must be true and supported by `brand-dna.md`. If the page cannot honestly support a brand mention, change the angle.
5. **Evidence.** Name sources inline ("According to [Source] ([year])…") and link the primary source. Quotes from named experts with their role. Label opinion as opinion.
6. **Experience.** Real scenarios, conditional advice ("if your team is X, choose Y"), trade-offs and limits ("this works for X; if Y, use Z instead"). First-hand photos, data and process where the business has them.
7. **Start from the prompt, not just the keyword:** the draft must directly answer each `target_prompts` entry. Use real user wording from `research/community.md` in headings and FAQs.
8. **Formatting:** short paragraphs (2–4 sentences), a list, table or callout every few hundred words, tables for comparisons, numbered lists for steps (never HowTo schema, core rules §5).
9. **Freshness:** visible "Last updated" and accurate dates (core rules §4). Add the year to the title only for time-sensitive topics.
10. **One clear CTA** at the end; no aggressive CTAs inside educational or competitor sections.

### GEO levers (directional, core rules §1.6)

Studies report that pages are cited more by AI answers when they include: quotations from named authoritative sources, specific statistics with source and date, in-text citations, answer-first sections, clear heading hierarchy, and recent updates. Apply them because they also help readers; never quote the study percentages to a client as fact, and never add quotes or numbers just to hit a count.

### Remove AI-sounding filler (editing pass)

- [ ] Openers like "In today's fast-paced world", "In the ever-evolving landscape", "Let's dive in".
- [ ] Empty verbs and hype: delve, unlock, unleash, elevate, leverage, seamless, robust, game-changing, revolutionary, best-in-class, industry-leading.
- [ ] Throat-clearing: "It's important to note that", "It's worth mentioning", "When it comes to".
- [ ] Closers: "In conclusion", "We hope this helped", a summary that repeats the intro.
- [ ] Stacked hedges ("may potentially help"), automatic groups of three, every paragraph the same shape.
- [ ] Vague claims ("studies show", "experts agree") → name the source or cut.
- [ ] Generic examples → replace with a specific role, company size, number or date.
- [ ] Hidden or invisible characters pasted from tools (zero-width spaces): remove.

## Content blocks and word budgets

Typical budgets per block. **The page total follows the topic and the coverage floor for its type (core rules §4); there is no 2,500-word floor, and you never pad.**

| Block | Budget | Notes |
|---|---|---|
| Introduction | 100–200 | Problem or outcome first; primary keyword in first 100 words; no greeting |
| Quick answer | 40–60 | H2 as the question; snippet target |
| Brand mention | 40–80 | Commercial pages only; must be true |
| Problem / context | 200–300 | 2–3 sourced numbers; concrete moments the problem hurts; chart if data (31) |
| Solution / comparison | 300–400 | What it does, then a 4–6-row comparison table, 3–5 capabilities framed as outcomes |
| How it works | 4–8 numbered steps | Action → result → why it matters; one real example |
| Scenarios / use cases | ≥3 scenarios | Per scenario: who (specific role and company type), problem, what matters most, recommended approach, evidence |
| Data and evidence | as needed | "[Claim with number]. According to [Source], [context] ([year])." Every number linked |
| FAQ (conditional) | 3–6 Q, answers 40–60 words (core rules §4 direct answer) | See FAQ rule |
| Conclusion | 100–150 | Before → after, one CTA |

**FAQ rule.** Include an FAQ only when the page targets question searches, readers have real objections, or you have 3–6 distinct questions the body does not already answer (from People Also Ask, `prompts.csv`, community threads). Required on FAQ/trust pages; usually useful on comparison and definition pages; skip on short product and landing pages and when it would repeat the body. Each answer stands alone. `FAQPage` markup is optional and earns no Google rich result (core rules §5).

## Page-type outlines

Pick the outline by `page_type`; don't force one shape on every page. Schema per type: 21-schema.md.

| page_type | Outline |
|---|---|
| `guide` | Intro · quick answer · problem/context · numbered steps · common mistakes · tools or solution (brand where relevant) · FAQ (optional) · conclusion |
| `comparison` (A vs B) | Intro · quick verdict (who should pick which) · evaluation criteria and method · comparison table · A in detail · B in detail · best-for breakdown · pricing with "as of" date · FAQ (usually) · conclusion |
| `alternatives` / roundup | Intro · quick list · how we chose (criteria, testing) · one section per option: summary, best for, pros, cons, price "as of" · comparison table · how to choose · FAQ · conclusion |
| `use-case` | Intro · quick answer · why this case is hard · how the product helps · role- or scenario-specific examples · proof (case data, quotes) · FAQ (optional) · conclusion |
| `definition` | Intro · definition block (40–60 words) · why it matters · how it works · examples · vs adjacent concepts · FAQ (usually) · conclusion |
| `service` | What the service is (definition box) · who needs it · how it works (steps) · cost or price range · outcomes and proof · why choose us (3–5 specifics) · FAQ · CTA with low-risk next step |
| `product-led` | Problem → workflow showing how the product solves it (real screenshots) → results → limits and when another approach fits → CTA |
| `case-study` | Outcome summary first (bold result) · client situation · challenge · approach (steps) · results with figures and timeline · takeaways · related service CTA. Only real, permitted client data. |
| `location` | Service in this place · local specifics (areas, conditions, regulations) · local team · local reviews and projects · local FAQ · NAP and booking. Uniqueness gates: core rules §4; local details: 50-local.md |
| `faq` (FAQ or trust page) | Direct answer to the core objection · evidence and trade-offs · alternatives · grouped Q&A (each 40–60-word answer) · CTA |
| `article` (news, opinion, general post) | Answer-first lede · context · body sections · sources · conclusion |

## Comparison and alternatives pages

**Title formulas** (lengths per core rules §4):
- A vs B: `[A] vs [B]: [Key Difference] ([Year])`
- Alternatives: `[N] Best [A] Alternatives in [Year] (Free and Paid)`
- Roundup: `[N] Best [Category] Tools in [Year], Compared`

Keyword patterns: `[A] vs [B]`, `[A] alternatives`, `best [category] tools`, `[A] vs [B] for [use case]`, `[A] vs [B] pricing`, `is [A] better than [B]`.

**Fairness rules** (core rules §8; non-negotiable):
1. Every competitor fact is verifiable from public sources and linked (their docs, pricing page, review sites).
2. Pricing and features carry "as of Month YYYY"; review quarterly or when a competitor ships a big change.
3. Disclose which product is yours, and the method (tested hands-on, docs review, user reviews).
4. Show criteria where competitors win; a table where you win every row is not credible to readers or AI.
5. Unknown data = "Not publicly available", never a guess. No false or misleading claims.
6. Include hidden costs (setup fees, per-seat pricing, overages) for all options, yours included.
7. Third-party ratings only with source link and date; never your own ratings of yourself.
8. Last row of the table: plain-language verdict ("Choose A if…, choose B if…").

Layout: summary verdict with CTA above the fold, CTA after the table and at the end, none inside competitor sections. Link related comparisons to each other, to feature pages and to migration case studies. Schema: no `Product` + `AggregateRating` for comparison pages; use what 21-schema.md and core rules §6 allow (often `Article`, optionally `ItemList` for roundups).

## E-E-A-T and quality

**Who / How / Why test** (from Google's helpful-content guidance): *Who* made it (visible byline, bio, credentials; required on YMYL)? *How* was it made (first-hand testing, original data, AI-assistance disclosed where readers would expect it)? *Why* does it exist (to help a reader, not to catch clicks or hit a word count)? Weak on all three = rewrite before publishing.

| Pillar | Strong signals |
|---|---|
| Experience | Original photos, screenshots, data, tests; specific anecdotes; before/after results; process shown |
| Expertise | Author credentials relevant to topic; correct terminology explained on first use; trade-offs, not just benefits; sourced claims |
| Authoritativeness | Author/brand cited or mentioned elsewhere, awards, publications, consistent topical history (entity work: 10) |
| Trust (most important) | Accurate sourced claims, dates, corrections, contact info, policies, disclosure of affiliation, no hype or deception |

Rate each pillar Strong / Moderate / Weak / None with evidence. YMYL: apply 02-site-types §12 and raise E-E-A-T findings one priority level.

AI-assisted content is fine with human review, original value and accurate facts. Low-quality markers: generic phrasing, no original insight, identical structure across pages, no author, errors. Unreviewed mass AI pages are banned (core rules §8).

### Content quality score (per page, 0–100)

This page-level score feeds the "Content quality" category of SEO Health (core rules §2). Grades per core rules §2.

| Category | Points | Full marks when |
|---|---|---|
| Intent and usefulness | 25 | Matches the dominant intent and page type (12); passes Who/How/Why; clear information gain |
| E-E-A-T | 25 | Trust 10, Experience 5, Expertise 5, Authority 5, using the pillar table |
| Answer readiness and structure | 20 | Direct answers under question headings, self-contained passages, ≥2 quotable blocks, clean heading levels, tables/lists where useful |
| Accuracy and sourcing | 20 | Every number and claim sourced; passes 32 with no Critical issues |
| Freshness and maintenance | 10 | Visible dates, current facts, no outdated references |

Score only what you could see; say "not measured" for the rest and show coverage (core rules §1.3).

## Self-check (before fact-check)

- [ ] Matches the approved brief; frontmatter complete (`templates/article-frontmatter.md`); H1 = `title`; no notes in body
- [ ] Title, meta, H1, headings, URL, internal links within core rules §4; primary keyword in its five places, no stuffing
- [ ] Every target prompt answered directly; quick answers 40–60 words; ≥2 quotable blocks; brand block true
- [ ] Comparison pages meet every fairness rule; FAQ only if it adds value
- [ ] Every statistic has source, date and link; no invented numbers, quotes or case results
- [ ] Filler pass done; length fits the topic, above the floor, nothing padded
- [ ] Content quality score at or above the grade the owner accepts (default B)

## Refreshing or rewriting an existing page

Decay detection lives in 60-measurement.md; this is the rewrite.

1. **Snapshot** the current page (HTML or CMS revision) and record its URL, title, meta, word count and, if available, GSC clicks, impressions, top queries and position for the last 3 months (source-labelled).
2. **Re-check intent** for the main queries (12). If the results now favour a different page type, change the format, not just the words.
3. **Compare** with the current top 5 results (step 4 above) and list new gaps.
4. **Mark each section** keep / strengthen / add / cut. Keep the URL; if two pages compete for the same query, merge into the stronger one and 301 the other (03 for redirects).
5. **Update facts:** replace outdated stats with the latest edition from the original source, re-verify prices and competitor details, fix broken links.
6. **Strengthen answers:** add quick answers under question headings that people now search, add real FAQs from new queries, add first-hand evidence.
7. **Keep what ranks:** don't remove sections that bring traffic for queries shown in GSC unless they are wrong.
8. **Dates:** change `date_modified` (and the visible "Last updated") only for substantive updates, never for cosmetic edits (core rules §4).
9. Run the self-check and 32 again; get approval; publish; log in `tracking/change-log.md` with a re-check date (30/60/90 days, 60-measurement.md).

## Output format

**Brief:** `templates/content-brief.md`. **Outline only** (when the user asks just for an outline): H1, slug, target length, and per-section heading, budget, format, snippet targets, keyword note and a 1–2-sentence writing note.

**Draft:** one Markdown file: frontmatter (`templates/article-frontmatter.md`) + body. **Score report:**

```
CONTENT QUALITY: <title> (<url>) — 78/100 (C), coverage 90% (not measured: author reputation)
Intent 20/25 · E-E-A-T 18/25 (Trust Strong, Experience Moderate, Expertise Strong, Authority Weak)
Answer readiness 16/20 (3 of 5 question H2s lack a direct answer) · Accuracy 16/20 · Freshness 8/10
Top fixes: 1) … 2) … 3) …
```

## Fallbacks and "not measured"

- **No fetch:** ask the user to paste the page or competitor text; otherwise write "competitor analysis not measured".
- **No search:** ask for top competitors and known questions; mark SERP, PAA and AI Overview notes "not measured".
- **No sources for a claim:** remove it or mark it "[NEEDS SOURCE]" for the owner; never fill it in.
- **No `brand-dna.md`:** ask the owner for product facts, pricing and proof points before writing product claims, or build the brand file first (10).
- **No file access:** output the brief, draft and score in chat as fenced blocks.
- **Search volume or difficulty:** if a paid SEO data tool is available (DataForSEO, Ahrefs, Semrush, SE Ranking, Moz…), use it and label the source; otherwise use the relative wording from core rules §1.2.
