# 02 — Site-type playbooks and routing

Use the confirmed Site Profile. Read the **routing matrix**, then the playbook for the primary type, then add the core modules of any secondary types. Apply the YMYL overlay (§12) if flagged. Thresholds always come from 00-core-rules.md.

---

## 1. Routing matrix

● core (always run) · ◐ conditional or light (run if relevant or time allows) · – skip unless the user asks

| Module | Portfolio | Local | E-com | SaaS | Publisher | Agency | Docs | Marketplace | Landing |
|---|---|---|---|---|---|---|---|---|---|
| 10 Brand and entity | ● | ● | ● | ● | ● | ● | ◐ | ● | ◐ |
| 11 Demand research | ◐ | ● | ● | ● | ● | ● | ● | ● | ◐ |
| 12 Search intent | ◐ | ● | ● | ● | ● | ● | ◐ | ● | ● |
| 13 Strategy and plan | ◐ | ● | ● | ● | ● | ● | ● | ● | – |
| 20 Technical | ● | ● | ● | ● | ● | ● | ● | ● | ● (light) |
| 21 Schema | ● | ● | ● | ● | ● | ● | ◐ | ● | ● |
| 22 AI readiness | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| 30 Content | ● | ● | ● | ● | ● | ● | ● | ◐ | ● |
| 31 Visuals | ● | ◐ | ● | ◐ | ● | ◐ | ◐ | ◐ | ◐ |
| 32 Fact-check | ◐ | ● | ◐ | ● | ● | ● | ● | ◐ | ● |
| 33 Publishing in code | ◐ | ◐ | ◐ | ◐ | ◐ | ◐ | ● | ◐ | ◐ |
| 40 Links and mentions | ◐ | ● | ● | ● | ● | ● | ◐ | ● | ◐ |
| 50 Local | – (◐ local freelancer) | ● | ◐ (physical store) | – | – | ◐ | – | ◐ | ◐ |
| 51 E-commerce | – | ◐ (sells online) | ● | – | – | – | – | ◐ | – |
| 52 International | ◐ | ◐ | ◐ | ◐ | ◐ | ◐ | ◐ | ◐ | – |
| 60 Measurement | ● | ● | ● | ● | ● | ● | ● | ● | ◐ |

52 International runs only when the site has (or plans) more than one language or country.

---

## 2. Portfolio / personal brand

- **Goals**: job offers, freelance clients, speaking, personal reputation.
- **Top priorities**
  1. Rank #1 for the person's name (and name + profession). Home page title like "Asha Rao — Product Designer in Bengaluru".
  2. `Person` schema on the home/about page with `name`, `jobTitle`, `image`, `url`, `sameAs` (LinkedIn, GitHub, Behance, Dribbble, X, YouTube), `knowsAbout`, `alumniOf`/`worksFor` if public. `ProfilePage` on the about page.
  3. AI assistants should describe the person correctly: consistent one-line bio across the site and every profile (10-brand-and-entity.md).
  4. Each project as its **own indexable page** (not only a lightbox): problem → process → result with numbers, role, tools, client (if allowed). Coverage floor 400 words.
  5. Image weight and alt text (portfolios are image-heavy; LCP is usually the hero image).
  6. A clear contact/hire page; services page if freelancing.
- **Pages to have**: Home, About, Work index, one page per project, Services (freelancers), Contact, optional writing/blog.
- **AEO/GEO**: an "About" paragraph that states who, what, where, notable work in 40–60 words; FAQ for hiring questions (rates, availability, process) if freelancing.
- **KPIs**: name-query position, impressions for "name + role" queries, contact form submissions, AI assistant answers to "Who is <name>?".
- **Common mistakes**: everything on one page; projects only as images with no text; site title just "Portfolio"; no `sameAs`; heavy uncompressed images; Framer/Webflow default meta.
- **Skip**: e-commerce, programmatic pages, big content clusters (unless they want to write), heavy backlink campaigns.

## 3. Local business / service area

- **Goals**: calls, bookings, walk-ins, direction requests.
- **Top priorities**
  1. Google Business Profile complete and correct (primary category is the biggest local factor), plus Bing Places and Apple Business Connect (50-local.md).
  2. NAP (name, address, phone) identical on the site, profiles and directories.
  3. Reviews: steady flow, replies to all, no gating (00-core-rules §8).
  4. `LocalBusiness` subtype schema (e.g. `Dentist`, `Plumber`, `Restaurant`) with address, geo, hours, phone, `sameAs`, `areaServed`.
  5. One strong page per core service; location pages only where genuinely different (gates in core rules).
  6. Mobile speed and tap-to-call.
- **Pages**: Home, one page per service, location/area pages (if justified), About with real team photos, Reviews/testimonials, Contact with map, FAQ.
- **AEO/GEO**: answer the money questions directly ("How much does X cost in <city>?", "Do you offer emergency service?"); AI assistants lean on review sites and directories, so citations and reviews double as GEO.
- **KPIs**: GBP calls, direction requests, website clicks; local pack visibility; calls/forms from organic; review count and rating trend.
- **Common mistakes**: city-swap doorway pages, wrong primary category, different phone numbers across listings, hiding the address for a storefront business, fake reviews.
- **Restaurants**: add `Menu`/`hasMenu`, `servesCuisine`, `acceptsReservations`, menu as HTML text (not only PDF/image), delivery platform listings.

## 4. E-commerce

- **Goals**: sales, average order value, product discovery.
- **Top priorities**
  1. Indexing control: faceted/filter URLs, sort and session parameters, out-of-stock and discontinued product handling, pagination (51-ecommerce.md).
  2. `Product` schema with `Offer` (price, currency, availability), shipping and return policy, `aggregateRating` only from genuine customer reviews.
  3. Unique product titles and descriptions (no manufacturer copy-paste), specs tables, real photos.
  4. Category pages as landing pages: intro copy, filters, FAQs, internal links.
  5. Google Merchant Center feed (free listings) and product images.
  6. Core Web Vitals on product and category templates.
- **AEO/GEO**: buying guides and comparison content answer "best X for Y" prompts; reviews on third-party sites and marketplaces feed AI shopping answers.
- **KPIs**: organic revenue and transactions, product page impressions, Merchant Center clicks, category rankings.
- **Common mistakes**: thousands of indexable filter combinations, duplicate product URLs across collections, missing canonical, thin categories, `AggregateOffer` where `Offer` is needed.

## 5. SaaS / software / app

- **Goals**: sign-ups, demos, trials.
- **Top priorities**
  1. Bottom-of-funnel pages: features, use cases, integrations, pricing, **"X vs Y" and "X alternatives" pages** (fair and dated, 30-content-creation.md).
  2. Presence on review platforms (G2, Capterra, product directories) and in "best tools" lists, which AI assistants cite heavily.
  3. AI prompt research ("best tool for…", "how to … without …") and entity consistency (GEO is often the highest-leverage focus for SaaS).
  4. `SoftwareApplication` (with `offers`, `applicationCategory`, `operatingSystem`) and `Organization` schema.
  5. Docs and help center indexable and well-linked (often the most-cited pages).
  6. JavaScript rendering of marketing pages (SPA risk).
- **KPIs**: sign-ups/demos from organic, BOFU page rankings, AI share of voice on category prompts, branded search growth.
- **Common mistakes**: marketing site rendered client-side only; pricing hidden; comparison pages that attack competitors without sources; blog content unrelated to the product.

## 6. Blog / publisher / news

- **Goals**: readers, subscribers, ad or affiliate revenue.
- **Top priorities**
  1. Content quality and E-E-A-T: named authors with bio pages, sources, first-hand experience, editorial policy.
  2. Topic clusters and internal linking; prune or merge thin and outdated posts.
  3. Refresh loop: update decaying posts (60-measurement.md).
  4. `Article`/`BlogPosting`/`NewsArticle` with author (`Person` with `url`), `datePublished`, `dateModified`, images.
  5. Google Discover readiness: large images (≥1200 px wide with `max-image-preview:large`), compelling but honest titles.
  6. News: news sitemap (last 2 days), publisher info, transparency pages.
- **AEO/GEO**: answer-first intros, definition boxes, data and original research (most citable content type), clear dates.
- **KPIs**: organic sessions, returning readers, Discover clicks, subscriber sign-ups, AI citations.
- **Common mistakes**: no authors, AI-generated filler, fake "updated" dates, affiliate pages without real testing evidence, ad-heavy layouts hurting CLS.

## 7. Agency / B2B services

- **Goals**: qualified leads.
- **Top priorities**: one page per service and per industry served (only where real experience exists); case studies with measurable results; team and credentials (E-E-A-T); `Organization`/`ProfessionalService` schema; directory and award listings (Clutch, GoodFirms, industry associations); local SEO if they serve a city.
- **AEO/GEO**: answer buyer questions (cost, timeline, process, "how to choose an agency"); third-party mentions and reviews drive AI recommendations.
- **KPIs**: organic leads, service page rankings, case study views, AI mentions for "best <service> agency in <city>".
- **Common mistakes**: generic service copy, no proof, dozens of thin industry pages.

## 8. Docs / developer site

- **Goals**: adoption, fewer support tickets, developer trust.
- **Top priorities**: server-rendered docs; clean URL structure and versioning (canonical to the current version); in-page anchors; code examples as text; `llms.txt` and Markdown versions of pages (**Medium** priority here: developer AI tools actually use them, 22-ai-search-readiness.md); search-friendly titles ("How to authenticate with the X API"); `TechArticle`/`SoftwareSourceCode` where fitting.
- **AEO/GEO**: each page answers one task; copy-pasteable snippets; changelog with dates.
- **KPIs**: docs impressions, AI tool citations, support deflection.
- **Common mistakes**: duplicate pages across versions without canonicals, docs behind login, content in images.

## 9. Marketplace / directory / listings (jobs, real estate, events, vendors)

- **Goals**: listings found, both sides of the market growing.
- **Top priorities**: index-bloat control (facets, empty categories, expired listings → 404/410 or redirect with care); programmatic page gates (13-strategy-and-plan.md, core rules); unique value per listing page; schema per vertical (`JobPosting` with `validThrough`, `Event`, `RealEstateListing` is not a Google rich result: use `Offer`/`Place` sensibly); crawl budget on L/XL sites.
- **AEO/GEO**: market data pages (average salary, price trends) are highly citable.
- **KPIs**: indexed listing ratio, organic listing views, applications/inquiries.
- **Common mistakes**: millions of near-empty pages, expired listings still indexed, user-generated spam.

## 10. Landing page / one-page site

- **Goals**: one conversion.
- **Top priorities**: intent match for the one target query (12-search-intent.md); strong title and meta; one H1; fast load; `Organization` (or `Product`/`Event`/`SoftwareApplication`) schema; FAQ section answering objections; Open Graph image.
- **Honest limitation**: a single page can rank for a narrow set of queries only. If the user wants broad search traffic, recommend splitting into a few real pages (and say why).
- **Skip**: clusters, sitemaps beyond one URL, programmatic, international.

## 11. Other site kinds (map to the nearest type, then add)

| Kind | Map to | Add |
|---|---|---|
| Nonprofit | Agency/B2B (or Local) | `NGO`/`Organization` schema, donation page clarity, impact data pages, Google Ad Grants note |
| Education / courses | Publisher or SaaS | `Course` (list), instructor E-E-A-T, syllabus pages |
| Events / venue | Local or Landing | `Event` schema with dates, location, offers, `eventStatus`; past events handling |
| Community / forum | Publisher | `DiscussionForumPosting`/`QAPage`, moderation and spam control, thin-thread handling |
| Restaurant / hotel | Local | Menu, reservations, `LodgingBusiness`, booking platform listings |
| Mobile app site | SaaS | App store optimization links, `MobileApplication` schema, deep links |
| Personal blog | Publisher (light) | Author entity as in Portfolio |

## 12. YMYL overlay (health, finance, legal, safety, news)

Add to any type:

- Named expert authors and reviewers with credentials and bio pages; "Medically/legally/financially reviewed by" with date.
- Cite primary sources (studies, laws, official guidance) and link them.
- Clear disclaimers, contact details, editorial and correction policies.
- Stricter fact-check: every claim and number goes through 32-fact-check.md before publishing.
- Never write advice that needs a licensed professional as if it were personal advice.
- Raise the priority of E-E-A-T findings by one level.

## 13. Focus modifiers by type

| Type | If focus = SEO | If focus = AEO | If focus = GEO |
|---|---|---|---|
| Portfolio | Name rankings, project pages | About and FAQ answers | Entity consistency, profiles, "who is" answers |
| Local | GBP, local pack, service pages | Cost/availability answers, FAQ | Reviews and directories AI reads, Bing Places |
| E-com | Indexing, categories, product schema | Buying-guide answers, PAA | Third-party reviews, marketplaces, comparison content |
| SaaS | BOFU pages, docs | Definition and how-to answers | Review platforms, "best tools" lists, prompt research |
| Publisher | Clusters, refresh, Discover | Answer-first intros, featured snippets | Original data, author entities |
| Agency | Service + industry pages | Buyer-question answers | Directories, awards, mentions |
| Docs | Structure, versions | Task answers | llms.txt, Markdown, snippet clarity |
| Marketplace | Index control, programmatic gates | Data answers | Data pages, brand mentions |
| Landing | Intent match | Objection FAQ | Entity basics |
