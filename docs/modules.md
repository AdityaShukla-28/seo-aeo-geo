# Modules

Every module is one file in `references/`. Each topic has exactly one owner file; other files link to it instead of repeating it. All numbers and rules come from `00-core-rules.md`.

## Foundation (always used)

| File | What it does | Used in |
|---|---|---|
| `00-core-rules.md` | The single source of truth: thresholds, the two scores and how they're assembled, grades, priority levels, the relevance check, resolved conflicts, schema policy, the AI crawler table, guardrails, safety rules and the dated-facts register | Everything |
| `01-intake-and-detection.md` | The purpose questions, signals for detecting site type, platform, size, market and flags, the Site Profile card, and what to do when detection fails | Steps 2–3 |
| `02-site-types.md` | Playbooks for 9 site types plus other kinds, the routing matrix (type → modules), the YMYL overlay, and focus modifiers per type | Step 4 |
| `03-platforms.md` | How to apply fixes on WordPress, Shopify, Webflow, Wix, Squarespace, Framer, Ghost, HubSpot, Next.js, Nuxt, Astro, SvelteKit, static sites and SPAs; the safe-change protocol; the developer fix-list format | Fixes, fix lists |

## Research and strategy

| File | What it does | Produces |
|---|---|---|
| `10-brand-and-entity.md` | Brand profile, competitors, and entity setup: consistent description everywhere, Organization/Person identity, `sameAs` profiles, Wikidata, knowledge panel, review platforms | `brand-dna.md` |
| `11-demand-research.md` | Keyword research, AI prompt research (the questions people ask ChatGPT and others), community language from Reddit, forums and reviews, keyword clustering | `keywords.csv`, `prompts.csv`, `community.md` |
| `12-search-intent.md` | What Google rewards for a query (page type, format, SERP features, AI Overview), page-type mismatch, user stories and personas | `serp-intent.md` |
| `13-strategy-and-plan.md` | Page plan, hub-and-spoke topic clusters, internal-link plan, roadmap and KPIs, programmatic (at-scale) page planning | `plan.csv`, `roadmap.md` |

## Audit and fixes

| File | What it does |
|---|---|
| `20-technical-audit.md` | Crawling, indexing, canonicals, redirects, HTTPS, URLs, mobile, Core Web Vitals diagnosis, JavaScript rendering, sitemaps, robots.txt, pagination, single-page and on-page checks, crawl strategy by site size |
| `21-schema.md` | Structured data: which types are active or retired, required properties, JSON-LD templates (Organization, Person, LocalBusiness, Article, Product, SoftwareApplication, Event, JobPosting and others), validation |
| `22-ai-search-readiness.md` | The AEO/GEO audit and AI Search Readiness score: AI bot access, firewall checks, llms.txt, how quotable the content is, content visible without JavaScript, snippet controls, agent readiness, notes per AI engine |

## Content

| File | What it does | Produces |
|---|---|---|
| `30-content-creation.md` | Content briefs with competitor gaps, outlines for 11 page types, writing standards (answer-first, E-E-A-T, quotable blocks), fair comparison pages, content quality score, refreshing old pages | Briefs, drafts |
| `31-visuals.md` | Image SEO audit and optimization, charts AI can read (summary + table + CSV + Dataset schema), social/Open Graph images | Image audit, charts |
| `32-fact-check.md` | Checks every link, statistic, quote, study and brand claim before publishing; spots AI-invented facts | Fact-check report |
| `33-publishing-in-code.md` | Builds content pages in a codebase from Markdown and frontmatter, with a mandatory preview and approval before deploying | Code changes |

## Off-site and special cases

| File | Used for | What it does |
|---|---|---|
| `40-links-and-mentions.md` | Most sites | Backlink profile analysis, link and mention opportunities, ethical community participation, outreach, digital PR, brand mention monitoring |
| `50-local.md` | Local businesses | Google Business Profile, Bing Places, Apple Business Connect, NAP consistency, region-specific directories, reviews, location pages, map rank tracking |
| `51-ecommerce.md` | Online stores | Product and category pages, filter URLs, variants, out-of-stock items, product schema details, Merchant Center, marketplaces |
| `52-international.md` | Multi-language or multi-country sites | hreflang, language and region targeting, content parity, locale formats, machine-translation quality checks |

## Measurement

| File | What it does |
|---|---|
| `60-measurement.md` | Search Console, GA4, PageSpeed/CrUX, Bing Webmaster, AI referral traffic, a free AI visibility tracker, indexing (URL Inspection, IndexNow), regression checks after site changes, content decay detection, monthly report, 30/60/90-day re-checks |

## Which modules run for which site

● always · ◐ if relevant · – skipped

| Module | Portfolio | Local | E-com | SaaS | Publisher | Agency | Docs | Marketplace | Landing |
|---|---|---|---|---|---|---|---|---|---|
| 10 Brand | ● | ● | ● | ● | ● | ● | ◐ | ● | ◐ |
| 11 Research | ◐ | ● | ● | ● | ● | ● | ● | ● | ◐ |
| 12 Intent | ◐ | ● | ● | ● | ● | ● | ◐ | ● | ● |
| 13 Plan | ◐ | ● | ● | ● | ● | ● | ● | ● | – |
| 20 Technical | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| 21 Schema | ● | ● | ● | ● | ● | ● | ◐ | ● | ● |
| 22 AI readiness | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| 30 Content | ● | ● | ● | ● | ● | ● | ● | ◐ | ● |
| 40 Links | ◐ | ● | ● | ● | ● | ● | ◐ | ● | ◐ |
| 50 Local | – | ● | ◐ | – | – | ◐ | – | ◐ | ◐ |
| 51 E-commerce | – | ◐ | ● | – | – | – | – | ◐ | – |
| 60 Measurement | ● | ● | ● | ● | ● | ● | ● | ● | ◐ |

The full matrix, including modules 31–33 and 52, is in `references/02-site-types.md`.

## Templates

`templates/` holds one template for every file the workflow produces:
- site profile, brand DNA;
- keywords / prompts / plan CSVs, community notes, roadmap;
- content brief, article frontmatter, fact-check report;
- audit report, fix list, change log, monthly report;
- backlink plan, outreach templates, AI visibility log;
- `robots.txt` and `llms.txt` examples.

## Scripts (optional)

| Script | Does |
|---|---|
| `scripts/aeo-audit.mjs` | Crawls up to 30 pages politely and runs 16 technical AEO/SEO checks, saving a JSON result (Node 18+) |
| `scripts/validate_schema.py` | Checks JSON-LD in HTML files or a URL: broken JSON, placeholders, retired types, self-serving review stars (Python 3.8+, no packages) |
