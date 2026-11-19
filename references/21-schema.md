# 21 — Schema (structured data)

Detect, validate and write JSON-LD that is true, visible on the page, eligible for the search features that still exist, and linked into one entity graph.

**Inputs:** `seo-workspace/<domain>/site-profile.md`, `seo-workspace/<domain>/brand-dna.md` (names, logo, sameAs list from 10-brand-and-entity.md), page HTML or URLs.
**Outputs:** Schema section in `seo-workspace/<domain>/audits/YYYY-MM-DD-audit.md`; ready-to-paste JSON-LD in `seo-workspace/<domain>/audits/YYYY-MM-DD-fix-list.md`.

Policy is fixed in core rules §6 and is not repeated here as opinion: JSON-LD, only visible and true facts, no placeholders, no self-serving reviews, `Organization` or `Person` with `sameAs` on every site. Local business extras are in 50-local.md; product, variant, shipping and return details in 51-ecommerce.md.

## When to use / skip

- Core for every type except Docs (◐) (02-site-types.md §1). Always run during a full audit and before publishing new page types.
- Skip types that don't fit the site (relevance check, core rules §3): no `Product` on a portfolio, no `LocalBusiness` without a real address or service area, no `JobPosting` without real openings.
- Don't promise rankings or AI citations from schema. It helps machines understand entities and unlocks some search features; Google says no special markup is needed for AI features (core rules §10).

## Procedure

1. **Detect**: in the raw HTML find every `<script type="application/ld+json">`, plus Microdata (`itemscope`, `itemprop`) and RDFa (`typeof`, `property`). Note if JSON-LD exists only in rendered HTML (JS-injected; see 20-technical-audit.md §5). List each block's types.
2. **Validate** each block (§6). Record ERROR / WARNING / OK per block.
3. **Check policy** against the status table (§1): flag never-use and retired types, FAQPage expectations, self-serving reviews, ClaimReview misuse.
4. **Check truth and visibility**: every name, price, rating, date, address and author in the markup appears on the page and is correct. Mismatch = High.
5. **Find gaps**: compare page types on the site with the "use on" column in §2. One recommendation per missing type, with the page it belongs on.
6. **Write the markup** from the templates (§4), linked with `@id` (§3). Fill every value from the page or brand-dna.md; if a value is unknown, ask the user or leave the property out. Never ship a placeholder.
7. **Re-validate** the generated JSON-LD (§6) before handing it over; implementation per platform in 03-platforms.md.

### 1. Type status *(perishable, verified 2026-11)*

| Status | Types | What to do |
|---|---|---|
| **Google rich result or feature** | Article/BlogPosting/NewsArticle, BreadcrumbList (desktop display only since 2025), Product + Offer, ProductGroup, Review/AggregateRating (genuine, not self-serving), LocalBusiness, Organization (logo/knowledge panel), Event (public, physical-location events), JobPosting, VideoObject (incl. Clip, BroadcastEvent), Course list (Course + ItemList), DiscussionForumPosting, QAPage, ProfilePage, Recipe, SoftwareApplication, Education Q&A, Book actions | Recommend where the page truly fits |
| **Valid, no rich result, still useful** | WebSite, WebPage, Person, Service, ItemList, ContactPage, SoftwareSourceCode, Dataset (used by Google Dataset Search), Speakable (beta) | Use for entity clarity and linking |
| **Valid, no rich result: optional** | FAQPage (FAQ rich results retired for all sites, May 2026) | Keep real FAQ sections on pages. Markup optional; never add it expecting a search feature; don't tell users to remove correct existing markup. Use QAPage only for real user-submitted Q&A (core rules §5) |
| **Never use** | HowTo (rich result removed 2023) | Write steps as a numbered list instead |
| **Retired** | SpecialAnnouncement, CourseInfo, EstimatedSalary, LearningVideo, VehicleListing, Practice Problem | Remove or replace: Event/Article, Course list, JobPosting `baseSalary`, VideoObject, Product (vehicles: `Car` + `Offer`) |
| **Only for real fact-checkers** | ClaimReview (no Search rich result; Fact Check Explorer still reads it) | Remove from ordinary business sites |

### 2. Required and recommended properties

"Required" = needed for the Google feature or for a meaningful entity. Use absolute URLs and ISO 8601 dates (`2026-11-20`, `2026-11-20T09:00:00+05:30`).

| Type | Use on | Required | Recommended |
|---|---|---|---|
| Organization (or subtype) | Home / About, site-wide via `@id` | name, url | logo, sameAs, description, contactPoint, address, foundingDate, legalName |
| Person | About, author pages, portfolio home | name | url, image, jobTitle, worksFor, sameAs, knowsAbout, alumniOf |
| WebSite | Home | name, url | publisher (`@id`), inLanguage. SearchAction gives no sitelinks search box any more |
| LocalBusiness subtype | Home or location page | name, address (PostalAddress) | telephone, geo, openingHoursSpecification, url, image, priceRange, areaServed, sameAs (more in 50-local.md) |
| Article / BlogPosting / NewsArticle | Articles | headline, image, datePublished | dateModified, author (Person with url), publisher (`@id`), mainEntityOfPage |
| Product + Offer | Product pages | name, image, offers.price, offers.priceCurrency, offers.availability | description, sku, gtin, brand, aggregateRating/review (genuine customers), shippingDetails, hasMerchantReturnPolicy (51-ecommerce.md) |
| SoftwareApplication | App / SaaS product page | name, offers (price, may be 0); Google's rich result also needs aggregateRating or review (from genuine users only) | applicationCategory, operatingSystem, screenshot |
| BreadcrumbList | Every page below home | itemListElement (position, name, item) | Last item may omit `item` |
| Event | Event pages | name, startDate, location | endDate, eventStatus, eventAttendanceMode, offers, organizer, image, description |
| JobPosting | Each open job | title, description, datePosted, hiringOrganization, jobLocation (or applicantLocationRequirements + jobLocationType TELECOMMUTE) | validThrough, employmentType, baseSalary, directApply |
| VideoObject | Pages with a main video | name, thumbnailUrl, uploadDate | description, duration, contentUrl or embedUrl, hasPart (Clip key moments) |
| ItemList | Hub pages, lists, course lists | itemListElement (position + url or item) | name, numberOfItems |
| ProfilePage | Author / creator / team-member pages | mainEntity (Person or Organization) | dateCreated, dateModified |
| Dataset | Pages publishing data (incl. charts, 31-visuals.md) | name, description | creator, license, url, distribution (DataDownload), temporalCoverage, spatialCoverage, variableMeasured |

### 3. One graph per page: `@graph` and `@id`

- Put all entities of a page in **one** JSON-LD block with `"@context"` once and a `"@graph"` array.
- Give every reusable entity a stable `@id` (a URL plus a fragment; it need not resolve):

| Entity | `@id` pattern |
|---|---|
| Organization | `https://example.com/#organization` |
| Person (site owner / author) | `https://example.com/about/#person` or `https://example.com/authors/jane/#person` |
| WebSite | `https://example.com/#website` |
| WebPage | `<page URL>#webpage` |
| Breadcrumb | `<page URL>#breadcrumb` |
| Main entity (article, product, event) | `<page URL>#article`, `#product`, `#event` |

- Link with references, not copies: `"publisher": {"@id": "https://example.com/#organization"}`. Define the Organization fully on the home page; on other pages a short node (name, url, `@id`) is enough.
- Use the same `@id`, name, logo and sameAs on every page and every platform (entity consistency, 10-brand-and-entity.md).

### 4. Templates

Replace every `[bracketed]` value and every `example.com` URL with real data from the page; delete properties you can't fill truthfully. `scripts/validate_schema.py` flags leftovers.

**Site base (Organization + WebSite + WebPage + BreadcrumbList), home page:**

```json
{"@context": "https://schema.org", "@graph": [
  {"@type": "Organization", "@id": "https://example.com/#organization",
   "name": "[Brand name]", "url": "https://example.com/",
   "logo": {"@type": "ImageObject", "url": "https://example.com/logo.png"},
   "description": "[One-sentence description used everywhere]",
   "sameAs": ["https://www.linkedin.com/company/[handle]", "https://www.wikidata.org/wiki/[Q-id]"],
   "contactPoint": {"@type": "ContactPoint", "telephone": "[+country number]", "contactType": "customer service"}},
  {"@type": "WebSite", "@id": "https://example.com/#website", "url": "https://example.com/",
   "name": "[Brand name]", "publisher": {"@id": "https://example.com/#organization"}, "inLanguage": "en"},
  {"@type": "WebPage", "@id": "https://example.com/#webpage", "url": "https://example.com/",
   "name": "[Page title]", "isPartOf": {"@id": "https://example.com/#website"},
   "about": {"@id": "https://example.com/#organization"}}
]}
```

Personal site: replace the Organization node with a Person node (`"@type": "Person"`, `@id` `#person`, name, url, image, jobTitle, sameAs, knowsAbout) and point `publisher`/`about` to it.

**Inner pages: add nodes to the page's `@graph`:**

```json
{"@type": "BreadcrumbList", "@id": "https://example.com/blog/post/#breadcrumb", "itemListElement": [
  {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://example.com/"},
  {"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://example.com/blog/"},
  {"@type": "ListItem", "position": 3, "name": "[Post title]"}]}
```

```json
{"@type": "BlogPosting", "@id": "https://example.com/blog/post/#article",
 "headline": "[Visible H1]", "image": ["https://example.com/img/post-1200x675.webp"],
 "datePublished": "[ISO date]", "dateModified": "[ISO date of last real update]",
 "author": {"@type": "Person", "@id": "https://example.com/authors/jane/#person", "name": "[Author]", "url": "https://example.com/authors/jane/"},
 "publisher": {"@id": "https://example.com/#organization"},
 "mainEntityOfPage": {"@id": "https://example.com/blog/post/#webpage"}}
```

```json
{"@type": "ProfilePage", "@id": "https://example.com/authors/jane/#webpage",
 "mainEntity": {"@type": "Person", "@id": "https://example.com/authors/jane/#person",
   "name": "[Full name]", "jobTitle": "[Role]", "image": "https://example.com/img/jane.jpg",
   "worksFor": {"@id": "https://example.com/#organization"},
   "sameAs": ["https://www.linkedin.com/in/[handle]"], "knowsAbout": ["[Topic]"]}}
```

```json
{"@type": "Dentist", "@id": "https://example.com/#organization", "name": "[Business name]",
 "url": "https://example.com/", "telephone": "[+country number]", "image": "https://example.com/photo.jpg",
 "address": {"@type": "PostalAddress", "streetAddress": "[Street]", "addressLocality": "[City]",
   "addressRegion": "[Region]", "postalCode": "[Postcode]", "addressCountry": "[ISO country, e.g. IN]"},
 "geo": {"@type": "GeoCoordinates", "latitude": 0.0, "longitude": 0.0},
 "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
   "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "09:00", "closes": "18:00"}],
 "sameAs": ["https://maps.google.com/?cid=[id]"]}
```

(Use the most specific LocalBusiness subtype; set real coordinates. No `aggregateRating` on your own business.)

```json
{"@type": "Product", "@id": "https://example.com/p/widget/#product", "name": "[Product name]",
 "image": ["https://example.com/img/widget.webp"], "description": "[Unique description]",
 "sku": "[SKU]", "brand": {"@type": "Brand", "name": "[Brand]"},
 "offers": {"@type": "Offer", "url": "https://example.com/p/widget/", "price": "[29.99]",
   "priceCurrency": "[ISO currency, e.g. INR]", "availability": "https://schema.org/InStock",
   "itemCondition": "https://schema.org/NewCondition"}}
```

```json
{"@type": "SoftwareApplication", "name": "[App name]", "applicationCategory": "BusinessApplication",
 "operatingSystem": "Web, iOS, Android", "url": "https://example.com/",
 "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
 "publisher": {"@id": "https://example.com/#organization"}}
```

```json
{"@type": "Event", "name": "[Event name]", "startDate": "[ISO date-time with offset]", "endDate": "[ISO date-time]",
 "eventStatus": "https://schema.org/EventScheduled",
 "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
 "location": {"@type": "Place", "name": "[Venue]", "address": {"@type": "PostalAddress",
   "streetAddress": "[Street]", "addressLocality": "[City]", "addressCountry": "[ISO country]"}},
 "organizer": {"@id": "https://example.com/#organization"},
 "offers": {"@type": "Offer", "url": "https://example.com/tickets/", "price": "[0]", "priceCurrency": "[ISO]",
   "availability": "https://schema.org/InStock", "validFrom": "[ISO date]"}}
```

```json
{"@type": "JobPosting", "title": "[Job title]", "description": "<p>[Full job description as HTML]</p>",
 "datePosted": "[ISO date]", "validThrough": "[ISO date-time]", "employmentType": "FULL_TIME",
 "hiringOrganization": {"@id": "https://example.com/#organization"},
 "jobLocation": {"@type": "Place", "address": {"@type": "PostalAddress", "addressLocality": "[City]", "addressCountry": "[ISO]"}},
 "baseSalary": {"@type": "MonetaryAmount", "currency": "[ISO]",
   "value": {"@type": "QuantitativeValue", "minValue": 0, "maxValue": 0, "unitText": "YEAR"}}}
```

```json
{"@type": "VideoObject", "name": "[Video title]", "description": "[What the video shows]",
 "thumbnailUrl": "https://example.com/img/video-thumb.jpg", "uploadDate": "[ISO date]",
 "duration": "PT4M30S", "embedUrl": "https://www.youtube.com/embed/[id]",
 "hasPart": [{"@type": "Clip", "name": "[Chapter]", "startOffset": 0, "endOffset": 75,
   "url": "https://example.com/video-page/?t=0"}]}
```

```json
{"@type": "ItemList", "name": "[Hub title]", "itemListElement": [
  {"@type": "ListItem", "position": 1, "url": "https://example.com/guide/a/", "name": "[Page A]"},
  {"@type": "ListItem", "position": 2, "url": "https://example.com/guide/b/", "name": "[Page B]"}]}
```

```json
{"@type": "Dataset", "name": "[Dataset name]", "description": "[What it measures, 50+ characters]",
 "creator": {"@id": "https://example.com/#organization"}, "license": "[License URL: ask the owner, never default]",
 "temporalCoverage": "2025-01/2026-06", "variableMeasured": ["[Variable]"],
 "distribution": [{"@type": "DataDownload", "encodingFormat": "text/csv", "contentUrl": "https://example.com/data/file.csv"}]}
```

### 5. Policy checks (fail = finding)

| Check | Priority |
|---|---|
| HowTo or a retired type present | Medium (remove/replace; no penalty, but no benefit and it signals stale setup) |
| Markup describes content not visible on the page, or false data (prices, ratings, dates) | High (can lead to a manual action) |
| `aggregateRating`/`review` on your own Organization/LocalBusiness, or reviews written by the business | High (self-serving; remove) |
| Product ratings not from genuine customers, or reviews collected with incentives that core rules §8 forbids (any incentive on platforms that prohibit them; undisclosed or rating-conditional elsewhere) | High |
| ClaimReview on a site that is not a fact-checking organization | Medium (remove) |
| Existing correct FAQPage | Info only: mention "no rich result since 2026", don't push removal |
| `dateModified` changed without a real update | Medium (core rules §4 freshness) |
| Product/Offer injected only by JavaScript | Medium (move to server HTML; 20-technical-audit.md §5) |
| Same entity in Microdata and JSON-LD with conflicting values | Medium (keep JSON-LD) |
| No Organization/Person with sameAs anywhere | High for GEO focus, Medium otherwise |

### 6. Validation procedure

1. **Static check** (if you can run Python, no packages): `python scripts/validate_schema.py page.html` or `python scripts/validate_schema.py --url https://example.com/page`. ERROR lines must be fixed (invalid JSON, placeholders, HowTo, retired types, missing `@context`/`@type`); WARNING lines need a judgment (FAQPage, `http://` context, ClaimReview, ratings on your own business, example.com URLs). Exit code 1 = errors present.
2. **Manual fallback** (no code), per block: valid JSON (no trailing commas, straight quotes) · `"@context": "https://schema.org"` · every node has `@type` (a `@graph` container doesn't need one) · no `[brackets]`, "TODO" or example URLs · absolute URLs · ISO dates · every value visible on the page.
3. **Google Rich Results Test** (`https://search.google.com/test/rich-results`): confirms eligibility for Google features and shows the rendered HTML. It no longer lists retired types; "no items detected" for FAQPage or Dataset is expected.
4. **Schema Markup Validator** (`https://validator.schema.org/`): checks any schema.org type and nesting, including types Google ignores.
5. **Compare with the visible page** (step 4 of the procedure).
6. **After deploy**: Search Console enhancement reports and URL Inspection (60-measurement.md); re-test 1–3 on the live URL.

## Output format

```markdown
## Schema — <domain> — YYYY-MM-DD
Schema score: XX/100 (coverage XX%) · pages checked: N (crawl)

| Page | Types found | Status | Issues (ERROR/WARNING) | Source |
|---|---|---|---|---|
| / | Organization, WebSite | OK | — | validate_schema.py |
| /blog/x/ | BlogPosting, FAQPage | WARNING | FAQPage: no rich result (info) | Rich Results Test |

### Missing opportunities
| Page/template | Add type | Why (feature or entity clarity) | Priority |

### Ready-to-paste JSON-LD
<one fenced json block per page/template, already validated>
```

## Fallbacks and "not measured"

| Situation | Do this |
|---|---|
| Can't fetch pages | Ask for view-source HTML (raw) of key templates; mark JS-injected schema "not measured" |
| Can't run code | Manual checklist (§6 step 2) plus the two online validators via the user (they paste the URL and send a screenshot) |
| Can't reach online validators | Static/manual checks only; mark "Google eligibility not measured" |
| Facts unknown (address, prices, founding date) | Ask the user; omit the property rather than guess |
| JSON-LD built by JS | Validate the rendered HTML (Rich Results Test shows it); recommend server-side output |
