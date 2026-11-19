# 12 — Search intent and SERP analysis

Read the results page for a query to learn what searchers want, which page type wins, which answer format is expected, and whether a given page is the right kind of page for the query.

**Inputs:** `research/keywords.csv`, `research/prompts.csv`, `brand-dna.md`; for a ranking problem: the page URL and its target keyword.
**Outputs:** `seo-workspace/<domain>/research/serp-intent.md` (one block per keyword); `intent` and `serp_features` updated in `research/keywords.csv`; page-type decisions passed to 13-strategy-and-plan.md; page diagnoses added to the run's `audits/YYYY-MM-DD-audit.md`.

---

## When to use / skip

| Situation | Run |
|---|---|
| Strategy and plan | Pillar keywords and every `easy-win`/`target` keyword planned as a p1 page (usually 10–30 keywords, not the whole list) |
| Content creation | The page's primary keyword, before the brief (30-content-creation.md) |
| "Good page, but it doesn't rank" | Diagnosis: steps 1–11 for that page and keyword |
| Landing page | The one target query (● in 02-site-types.md) |
| Portfolio, docs (◐) | Name queries and the top 3–5 task queries only |
| Only branded queries matter | Skip |

## Limitation: web search is approximate

Built-in web search is not a real Google results page (core rules §1.4). Results change with location, language, device, history and time; ads, PAA and AI Overviews may be missing or different. Label every observation `approximate` unless it comes from a SERP data API or a screenshot the user took in the target market. Run important queries twice and keep what both runs agree on. Never state rankings as fact from one look.

Best sources, in order: (1) a SERP data API or paid SEO tool with location set to the market, labeled; (2) screenshots or copied results from the user, in a private window with the target location; (3) built-in web search, labeled `approximate`.

---

## Procedure

1. **Pick the keywords** (scope table above). Group near-identical keywords already merged by SERP overlap (11-demand-research.md Part D): analyze the primary one.
2. **Record the top 10 organic results.** For each: URL, site kind (brand / niche specialist / big publisher / platform), page type (step 3), format (long guide, list, comparison table, tool, video, category grid, product), visible date, and any rich result (stars, price, video thumbnail).
3. **Classify page types** using one label each:

   | Page type | Strongest signals | Above the fold must show |
   |---|---|---|
   | Tool / interactive | Inputs, calculator, generator, checker; "free <tool>" titles | The working tool |
   | Local | Address, map, hours, local pack in SERP, "near me" | Service + city, call and directions buttons, NAP |
   | Comparison | "vs", "best", "alternatives", tables, pros/cons, review sites ranking | Quick verdict + comparison table |
   | Product | Price, add to cart, specs, reviews, shopping results | Images, price, stock, buy button, rating |
   | Landing | Single offer, strong CTA, light navigation, branded SERP | Value proposition + primary CTA + proof |
   | Service | Process, case studies, credentials, quote/consult CTA | Service + outcome, consult CTA, proof |
   | Hybrid (education + product) | Teaching sections mixed with "try it" CTAs (common in SaaS) | Short answer + product bridge + dual CTA |
   | Article / guide | Byline, date, long body, TOC, PAA-heavy SERP | Direct answer or TL;DR, author, date |
   | Category / listing | Product or listing grid, filters | Intro line + grid + filters |

   If a page shows several, choose in this order: tool → local → comparison → product → landing → service → hybrid → category → article.

4. **Separate content competitors from platform results.** Encyclopedias, social and forum sites, marketplaces, directories and review sites, video platforms, government and academic sites rank on many queries but are not page-for-page rivals. Count them separately; they still tell you something:

   | Platform results on page 1 | What it means | Response |
   |---|---|---|
   | Forums (Reddit, Quora, niche boards) | Searchers want lived experience and honest opinions | Add first-hand experience, real examples, data; community work is 40-links-and-mentions.md |
   | Directories / review sites | Searchers compare providers on third-party sites | Be listed and accurate there (10, 40, 50) |
   | Marketplaces | Buying happens on marketplaces | 51-ecommerce.md marketplace section |
   | Video | Visual demonstration expected | Plan a video with transcript (31-visuals.md) |
   | Encyclopedias / dictionaries | Definitional intent | Short definition block; hard to win the top spot |

5. **Measure SERP consensus** on the content-competitor results: dominant page type share >60% = strong consensus (match it); 40–60% = mixed (match the leader, borrow from the runner-up); <40% = fragmented (room to differentiate; pick the type that best fits the business). Also note typical depth (light / medium / comprehensive), common schema types you can see as rich results, and media norms.
6. **Record SERP features and what they ask for:**

   | Feature | What it tells you | Build |
   |---|---|---|
   | Featured snippet: paragraph | Wants a concise definition | Direct answer block under a question heading (core rules §4) |
   | Featured snippet: list | Wants steps or a ranked list | Numbered or bulleted list under an H2 |
   | Featured snippet: table | Wants structured comparison | HTML table with clear column headers |
   | Featured snippet: video | Wants a demonstration | Video with chapters and transcript |
   | People Also Ask | Related doubts and next questions | Answer the top 3–6 on the page (question H2s or an FAQ section) |
   | AI Overview / AI Mode answer | Google's synthesis; cited sources are the trust set | Note which sources are cited and whether you are; answer-readiness checks in 22-ai-search-readiness.md |
   | Local pack | Local intent | Local page + Google Business Profile (50-local.md) |
   | Shopping / product grid | Purchase intent | Product or category page with product data (51-ecommerce.md) |
   | Top stories | Freshness matters | News or dated update content |
   | Knowledge panel | Entity query | Entity setup (10-brand-and-entity.md) |
   | Ads (top and bottom) | Commercial value; ad copy shows triggers and objections | Use themes for user stories (step 9) |
   | No snippet at all | Format not settled | Opportunity: structure the answer clearly |

   Write the observed features into `serp_features` in `keywords.csv`.
7. **Classify intent and journey stage.** Intent: informational, commercial, transactional, navigational; add "local" when the local pack or "near me" variants appear. Mixed intent → choose the dominant one and note the second. Stage: awareness (definitions, "what is"), consideration (how to choose, best, reviews), decision (vs, pricing, near me, buy). Update `intent` in `keywords.csv` if the SERP disagrees with the word-based guess.
8. **Detect page-type mismatch** (diagnosis or when mapping an existing page). Compare the page's type with the consensus:

   | Your page | SERP expects | Priority (core rules §2) | Fix |
   |---|---|---|---|
   | Article | Product / category pages | Critical | Target the keyword with a product or category page; turn the article into a supporting guide that links to it |
   | Article | Tool | Critical | Build the tool (even simple), keep the explanation below it |
   | Article | Local pages | Critical | Create a real local or service-area page (50-local.md) |
   | Article | Comparison | High | Restructure as a comparison with a table and verdict |
   | Product / landing | Informational guides | High | Create a guide that links to the product; don't force the product page to rank |
   | Landing | Tool | High | Add a working interactive element above the fold |
   | Service | Local results | Medium | Add location signals, local proof, LocalBusiness details |
   | Same type | — | Aligned | Work on depth, proof and UX instead |

   A technically perfect page of the wrong type rarely ranks. Fix the type before polishing anything else.
9. **Write 3–5 user stories from SERP evidence.** Format: *As a [persona], I want to [goal], because [driver], but I'm blocked by [barrier].* Each story cites its signals (a PAA question, ad theme, related search, snippet format). Stories span at least two journey stages.

   | Signal | Reveals |
   |---|---|
   | PAA themes: definitional / procedural / evaluative / comparative / risk | Knowledge gaps and stage |
   | Ad copy: "free plan", "trusted by 10,000", "set up in 5 minutes" | Barriers: commitment, trust, time |
   | Related searches adding "for small business", "pricing", "alternatives" | Narrowing, price focus, dissatisfaction |
   | "Is X safe / legit / a scam" | Skeptical; needs proof |
   | Many "vs" and "best" queries | Overwhelmed by choice; needs a clear recommendation |
   | "X not working" | Frustrated with the current solution |

   | Barrier | Page must provide |
   |---|---|
   | Information gap | Complete answer in the first screen |
   | Trust gap | Reviews, credentials, guarantees, named clients |
   | Comparison fatigue | Clear differentiation, "best for" guidance |
   | Price sensitivity | Visible pricing or ranges, value explanation |
   | Technical confusion | Steps, demo, screenshots |
   | Time pressure | Fast path to the result |

10. **Define 3–5 personas and check the page against each.** Every persona traces to a signal cluster (e.g. cost PAA → budget buyer; setup PAA → technical evaluator). For each persona rate the page Pass / Partial / Fail on:
    - **Relevance**: does it address this persona's goal specifically?
    - **Clarity**: can they find their answer within about 10 seconds (first screen, clear headings, tables)?
    - **Trust**: enough proof for this persona's doubts?
    - **Action**: an obvious next step for their stage?
    Fix the weakest persona first.
11. **Gap analysis (optional diagnostic sub-score, core rules §2 "Module sub-scores").** Rate the page against SERP norms: page type 0–15, content depth 0–15, UX (CTA clarity, first screen, mobile) 0–15, structured data vs visible rich results 0–15, media 0–15, authority/E-E-A-T signals 0–15, freshness 0–10. Report as "Intent alignment 58/100 (diagnostic, approximate SERP)". It never enters the headline scores directly.
12. **Sketch current vs proposed layout** when the page type or first screen is wrong. Current: list what the first screen and each section actually contain (with rough word counts). Proposed: the section order for the target type (step 3 table plus the outline in 30-content-creation.md). Be concrete: not "add a CTA" but "add 'Get a free quote' button under the H1, linking to /contact#quote"; not "add FAQs" but "answer these 4 PAA questions: …". Mobile first: the most important element must be in the first screen at 375 px width.
13. **For AI prompts (optional).** For the top 5–10 prompts, ask two assistants twice each (core rules §1.5) and note the answer shape (list of brands, steps, definition, table) and the cited source types. The shape hints at the page type; the cited sources go to `research/competitors.md`. Ongoing tracking: 60-measurement.md.

---

## Output format

`research/serp-intent.md`, one block per keyword:

```markdown
## <keyword>   (checked YYYY-MM-DD · source: built-in search, approximate | <API> | user screenshot)
- Intent: commercial (secondary: informational) · Stage: consideration · Local: no
- Dominant page type: comparison (6/9 content results, strong consensus)
- Platform results: Reddit ×2, G2 ×1 → people want peer opinions and review-site validation
- Features: ai-overview (cites G2, two vendor blogs; we are not cited), paa, video
- Answer format expected: table + short verdict; PAA: "<q1>", "<q2>", "<q3>"
- Depth norm: comprehensive; dated "2026" titles common
- Page to build/use: /compare/best-x-for-y (comparison) → feeds plan.csv
- User stories: 1) As a … (signals: PAA "…", ads "free plan") 2) …
```

Page diagnosis (in the audit):

```markdown
### Intent check: /blog/x  ·  keyword "<kw>"
Verdict: MISMATCH (article vs product/category consensus) · Priority: Critical
Evidence: 7/10 results are category pages; shopping grid present (approximate)
Personas: Budget buyer Partial/Fail/Partial/Fail · Technical evaluator Pass/Partial/Partial/Partial
Intent alignment: 41/100 (diagnostic)
Current → proposed first screen: "800-word intro" → "H1 + 2-line answer + product grid + filter"
Top actions: 1) … 2) … 3) …
Limits: built-in search, one location; ads not visible
```

## Fallbacks and "not measured"

| Missing ability | Do this |
|---|---|
| No web search | Ask the user for screenshots or copied top-10 results from their market; otherwise infer intent from keyword wording only and label it "intent inferred, SERP not checked" |
| Search but no features shown | Record organic results only; `serp_features` empty (= not checked), never `none` |
| No fetch of the target page | Ask for the page text or a screenshot; skip persona and gap ratings you can't see |
| No AI assistant access | Skip step 13; mark "AI answer shape: not measured" |
| No file access | Print the `serp-intent.md` blocks in chat |
