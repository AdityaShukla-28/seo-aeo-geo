# 10 — Brand and entity

Build the brand profile and competitor list, then make the brand (or person) one clear, consistent entity that search engines and AI assistants recognize and describe correctly.

**Inputs:** `seo-workspace/<domain>/site-profile.md`, the live site (or pasted pages), web search results, anything the user shares (pitch deck, sales FAQ, review exports).
**Outputs:** `seo-workspace/<domain>/brand-dna.md` (from `templates/brand-dna.md`), `seo-workspace/<domain>/research/competitors.md`, entity actions added to the run's `audits/YYYY-MM-DD-fix-list.md`.

---

## When to use / skip

| Situation | Run |
|---|---|
| Strategy, GEO focus, full program, new site / pre-launch | Full module (Parts A + B) |
| Full audit | **Light**: Part B steps 8–13 only (entity checks), plus a 5-line brand summary |
| Docs site, landing page (◐ in 02-site-types.md §1) | Light; skip competitor deep-dive unless asked |
| Portfolio / personal brand | Part B is the core of the work: the "entity" is the person |
| Local business | Part B, but the Google Business Profile itself is handled in 50-local.md |
| Quick task unrelated to brand | Skip |

## Why entity work matters (directional evidence)

- Third-party studies find that **brand mentions across the web track AI visibility more closely than backlinks do**. Ahrefs' study of ~75,000 brands found mentions correlated roughly 3× more strongly with AI visibility than backlink-based authority; YouTube mentions were the strongest single signal *(perishable, verified 2025-12)*. This is correlation, not proof that adding mentions causes citations (core rules §1.6).
- Analyses of AI answer citations show encyclopedic and community sources (Wikipedia, Reddit, review sites) are cited heavily by ChatGPT and Perplexity *(perishable, verified 2025-06)*. An AI assistant describes you from what **other** sites say about you, so those descriptions need to be accurate and consistent.
- Practical rule: when your site, your profiles and third-party pages all say the same thing about who you are, assistants repeat it. When they disagree, assistants guess, mix you up with a similarly named entity, or leave you out.

---

## Procedure

### Part A: Brand profile

1. **Read the site first.** Fetch: home, about, pricing, product/services, blog index, customers/case studies, contact. Skip 404s. Record in their own words: what they sell, tagline, features or services, pricing model, audience signals, proof (logos, numbers, awards), locations served.
2. **Search the web second.** Run these searches and note what third parties say:
   - `"<brand>"` and `"<brand>" what is` (independent descriptions)
   - `"<brand>" review`, `"<brand>" alternatives`, `"<brand>" vs` (sentiment and who you get compared to)
   - `"<brand>" site:linkedin.com`, `site:crunchbase.com`, the app stores, the main review platform for the type (table in step 11)
   - `"<founder name>"` (founder or author footprint)
   - `<category> tools <year>` / `best <service> in <city>` (landscape)
   Use region-specific sources for the market (01-intake-and-detection.md §3d).
3. **Prefer third-party language.** Record how customers and reviewers describe the brand next to how the brand describes itself. The gap is a finding (e.g. "site says 'revenue intelligence platform', reviewers say 'call recorder'").
4. **Build the competitor list** in two groups:
   - **Business competitors** (3–5): who customers choose instead. Sources: "vs"/"alternatives" searches, review-platform category pages, the user.
   - **Search competitors**: who actually ranks or gets cited for the brand's target queries. Often publishers, directories, marketplaces or review sites, not direct rivals. Fill this after 11-demand-research.md and 12-search-intent.md.
   For each business competitor: URL, one-line description, overlap, their edge, where they show up (review platforms, lists, AI answers). Save to `research/competitors.md` (format below).
5. **Write `brand-dna.md`** from the template. Every unknown fact is "Not found", never a guess. Pricing, funding and team details only from a public source, with the source noted.
6. **Content gaps (be opinionated).** List the 3–7 pages or assets the brand lacks that competitors or the SERP show are needed, and say why each matters for the goal. These feed 13-strategy-and-plan.md.
7. **Confirm with the user**: positioning, top competitors, anything sensitive (unannounced products, pricing they don't want public).

### Part B: Entity setup

8. **Write the canonical description, once.** Three lengths, used everywhere:

   | Version | Pattern | Example |
   |---|---|---|
   | One-liner (≤25 words) | `<Name> is a <category> that <does what> for <whom> [in <where>].` | "Brightdesk is a help-desk app that lets small e-commerce teams answer email, chat and WhatsApp from one inbox." |
   | Short bio (40–60 words, see core rules §4 "Direct answer block") | One-liner + founding year, HQ/market, one proof point | |
   | Long bio (100–150 words) | Short bio + founders, key products/services, notable customers or awards | |

   Use the same official name spelling, category words, founding year, location and founder names in all three. Decide the official name vs. alternate names (legal name, abbreviations, old names) and list them.

9. **Run the consistency check.** Compare the one-liner and core facts across every place the brand appears:

   | Place | Check |
   |---|---|
   | Home page, About page, footer | Name, one-liner, location, contact |
   | `Organization`/`Person` schema `description`, `name`, `alternateName` | Matches visible text (core rules §6) |
   | LinkedIn, X, Facebook, Instagram, YouTube, GitHub bios | Same one-liner (trim to fit), link to the site |
   | Google Business Profile, Bing Places, Apple Business Connect (local) | Name/address/phone identical (details in 50-local.md) |
   | Review platforms, app stores, marketplaces, directories | Category, description, website URL |
   | Crunchbase / company databases | Founding year, founders, HQ, website |
   | Author bios on guest posts, podcasts, conference pages | Same person bio |

   Log every mismatch as a finding (High if it's name, category or contact info; Medium for wording).

10. **Build the identity hub page.** One page is the official source of truth: the About page (organization) or the home/About page (person). It must show, as visible text:
    - Official name and any alternate names; logo (organization) or photo (person)
    - The one-liner and long bio
    - Founding date, location or service area (if public)
    - Founders / key people with links to their own bio pages
    - Contact details
    - **Visible links to every official profile** (same list as `sameAs`)
    - Proof with links: press coverage, awards, certifications, notable clients (with permission)

    Mark it up with `Organization` (or a subtype such as `LocalBusiness`, `ProfessionalService`) or `Person`, plus `ProfilePage`/`AboutPage` where it fits. Give the entity one stable `@id` (e.g. `https://example.com/#organization`, `https://example.com/#person`) and reuse it on every page (publisher, author, founder, brand). Templates and `@graph` linking: 21-schema.md.

11. **Choose the `sameAs` set.** Include only URLs that are (a) official profiles the brand controls, or (b) authoritative records about the brand (Wikidata, Wikipedia, a company register). Each must be live, show the same name, and ideally link back to the site.

    | Site type | Core `sameAs` set (use those that exist) |
    |---|---|
    | Portfolio / personal | LinkedIn, GitHub, Behance, Dribbble, X, YouTube, personal Wikidata item; ORCID or Google Scholar for researchers |
    | Local business | Google Maps place URL, Facebook, Instagram, Yelp or the market's main directory, Bing Places, industry association listing |
    | E-commerce | Instagram, Facebook, Pinterest, TikTok, YouTube, Trustpilot (or regional equivalent), Amazon/marketplace brand store |
    | SaaS / app | LinkedIn, X, GitHub, YouTube, G2, Capterra, Product Hunt, App Store / Google Play, Crunchbase, Wikidata |
    | Publisher | X, Facebook, YouTube, LinkedIn, Wikidata, Wikipedia (if it exists); authors: Muck Rack, LinkedIn |
    | Agency / B2B | LinkedIn, Clutch (or regional equivalent), Crunchbase, YouTube, industry association |
    | Docs / developer | GitHub org, package registry page (npm, PyPI…), Stack Overflow tag/collective, X |
    | Marketplace | LinkedIn, X, app stores, Crunchbase, Trustpilot |

    Never include: dead or abandoned accounts, profiles you don't control, competitor or aggregator pages, low-quality directory listings, or links added only "for SEO".

12. **Audit review-platform and profile presence.** For the type's main platforms (table above), record: exists? claimed by the owner? description matches the one-liner? correct website URL and contact? last activity date? rating and review count (label the source and date). Missing core profiles go to the fix list. Getting **new** listings, mentions and reviews is 40-links-and-mentions.md (local reviews: 50-local.md). Never write or buy reviews, review your own business, or ask only happy customers (core rules §8).

13. **Set up founder, author and expert entities.** For each person who represents the brand (founders, authors, reviewers, team leads):
    - A bio page on the site (`/about/<name>` or `/authors/<name>`): photo, role, credentials, experience, topics they cover, links to their profiles, list of their articles.
    - `Person` schema with `@id`, `jobTitle`, `worksFor` (pointing to the organization `@id`), `sameAs`, `knowsAbout` (see 21-schema.md).
    - Every byline links to the bio page; the organization's `founder`/`employee` and each article's `author` point to the person `@id`.
    - The same short bio on guest posts, podcast pages and conference profiles.
    - YMYL sites: credentials and "reviewed by" details (02-site-types.md §12).

14. **Check Wikidata and Wikipedia eligibility honestly.** Tell the user plainly which applies:

    | Item | Eligible when | Not eligible when | If eligible |
    |---|---|---|---|
    | **Wikidata item** | The entity is clearly identifiable and described by serious, publicly available, independent references (news coverage, government or company registers, books, academic sources), or it is needed to link other items | The only sources are the brand's own site and social profiles | Create or update the item with: instance of (P31), official website (P856), inception (P571), founded by (P112), headquarters (P159), country (P17), logo (P154), social IDs (e.g. X username P2002, LinkedIn company ID P4264, YouTube channel ID P2397, GitHub username P2037). Add a reference for each statement. |
    | **Wikipedia article** | Significant coverage in **multiple reliable, independent, secondary sources** (not press releases, sponsored posts, interviews, own content or trivial listings) | Coverage is mostly self-published, paid or passing mentions | Do not write it yourself. Anyone with a conflict of interest must disclose it, and paid editing must be declared. Use the draft/review process or suggest edits on the talk page with sources. |

    Items created without independent sources tend to be deleted, and a deleted article is worse than none. If the brand is not eligible, the honest path is to earn independent coverage first (40-links-and-mentions.md: digital PR, original data), then revisit.

15. **Knowledge panel.** Search the brand and person names (note it's approximate, core rules §1.4; ask the user for a screenshot from their market if possible).
    - **Panel exists**: the owner can claim it through the panel's "Claim this knowledge panel" option, verifying via an official profile they control; then suggest corrections through the panel's feedback. *(perishable: re-check Google's "Get verified on Google" help page before giving steps)*
    - **No panel**: it cannot be requested directly. It comes from consistent entity signals: steps 8–14, plus a Google Business Profile for local businesses (50-local.md).
    - Optional, if you can run code and the user supplies a Google API key in their environment: query the Knowledge Graph Search API for the brand name and record whether an entity and ID come back. Never write the key into files (core rules §9). Manual fallback: search and look for the panel.

16. **Baseline: how AI assistants describe the brand.** Ask at least two assistants: "What is <brand>?", "Who founded <brand>?", "What does <brand> cost?", "What are alternatives to <brand>?" (personal brand: "Who is <name>?"). Run each at least twice and log date and engine (core rules §1.5). Record wrong facts, mix-ups with similarly named entities, and which sources the answers cite. Each wrong fact traces back to a source to fix (an old profile, an outdated directory, a wrong database entry). Ongoing tracking: 60-measurement.md.

---

## Entity checklist (for audits)

| # | Check | Pass when | Priority if failing |
|---|---|---|---|
| E1 | One-liner consistent | Same category and core facts on site, schema and ≥80% of profiles | High |
| E2 | Identity hub page | About/home page shows all step-10 items as visible text | High |
| E3 | Organization/Person schema | Present, valid, stable `@id`, matches visible text | High |
| E4 | `sameAs` | Lists all live official profiles, nothing dead or unrelated | Medium |
| E5 | Profile presence | Core platforms for the type exist, claimed, accurate | Medium (High for local NAP) |
| E6 | People entities | Founders/authors have bio pages, bylines link to them | Medium (High for YMYL) |
| E7 | Wikidata | Item exists if eligible; not attempted if not eligible | Low |
| E8 | AI description | Assistants describe the brand correctly in ≥2 engines | High if wrong facts, Medium if absent |

---

## Output format

1. `brand-dna.md`: exactly the sections in `templates/brand-dna.md`.
2. `research/competitors.md`:

```markdown
# Competitors — <brand>   (updated YYYY-MM-DD)

## Business competitors
| Competitor | URL | One-liner | Overlap | Their edge | Where they show up |
|---|---|---|---|---|---|

## Search competitors (filled after 11 and 12)
| Domain | Type (publisher / directory / marketplace / rival / forum) | Ranks or is cited for | Source (SERP approximate / paid tool / AI answer) |
|---|---|---|---|

## Category evaluation criteria (from 11, prompt research)
| Criterion AI and reviewers use | What strong evidence looks like | Our evidence today |
|---|---|---|

## Sources AI answers cite for our category (from 11)
| Source | URL | Cited for | Are we present there? |
|---|---|---|---|
```

3. Entity status block (in the audit or chat):

```
ENTITY STATUS: <brand>                (checked YYYY-MM-DD)
One-liner:        "<text>"
Consistency:      9/12 places match (mismatches: Crunchbase category, X bio, Clutch founding year)
Identity hub:     /about — missing founder links, profile links not visible
Schema:           Organization present, no sameAs, no @id
Knowledge panel:  none found (approximate, built-in search)
Wikidata:         not eligible yet (no independent coverage found)
AI description:   ChatGPT correct (2/2 runs), Perplexity mixed up with <other brand> (2/2)
Top actions:      1) … 2) … 3) …
```

## Fallbacks and "not measured"

| Missing ability | Do this |
|---|---|
| No fetch | Ask the user to paste the About page and home page text and list their profile URLs |
| No web search | Ask the user for competitors, review platforms they're on, and press coverage; mark third-party language, knowledge panel and search competitors "not measured" |
| No AI assistant access | Give the user the step-16 prompts to run and paste back; mark AI description "not measured" |
| No code / no API key | Skip the Knowledge Graph lookup; use a manual search |
| No file access | Print `brand-dna.md` and `competitors.md` as fenced blocks for the user to save |
| Facts not public | Write "Not found"; never estimate funding, team size, ratings or review counts |
