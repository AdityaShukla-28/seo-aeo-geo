# 51 — E-commerce SEO

Get a store's products and categories crawled, indexed once, shown with prices in search and shopping results, and recommended in AI shopping answers.

**Inputs:** `seo-workspace/<domain>/site-profile.md`, `research/keywords.csv`, `research/competitors.md`, sitemap and crawl data from 20-technical-audit.md, Search Console / Merchant Center access if given.
**Outputs:** e-commerce section of `seo-workspace/<domain>/audits/YYYY-MM-DD-audit.md`, items in `audits/YYYY-MM-DD-fix-list.md`, category/buying-guide pages in `plan/plan.csv`.

## When to use / skip

Core for **e-commerce**; light for local businesses or marketplaces that sell online (02-site-types.md §1). Skip for sites without a cart or product catalog. Generic crawl, canonical, redirect, sitemap and pagination mechanics live in 20-technical-audit.md; base Product/Offer template in 21-schema.md; product images in 31-visuals.md; thresholds in core rules §4.

---

## Procedure

### 1. Map the templates

List the URL patterns and count them (sitemap or crawl): home, category, subcategory, product, variant, brand, filtered/faceted, sorted, paginated, search, cart/checkout/account, blog/buying guides. Sample 3–5 URLs per template (core size tiers in 01 §3c). Note the platform (Shopify, WooCommerce, Magento, BigCommerce, headless).

### 2. Product pages

| Check | Pass when |
|---|---|
| Title | Product name + key attribute + brand, within core rules §4 lengths; unique across variants |
| Meta description | Benefit plus a concrete detail (price "from", free delivery, warranty); within core rules §4 |
| H1 | One, the product name |
| Description | Unique, not the manufacturer's copy; who it's for, use cases, what's in the box; coverage floor in core rules §4 |
| Specs | HTML table (dimensions, materials, compatibility, model numbers) |
| Images | 3+ (hero, detail, in-use), descriptive alt and filenames, real photos; size rules in core rules §4; LCP image not lazy-loaded |
| Price, availability, delivery, returns | Visible as text near the buy button; same as schema and feed |
| Reviews | Genuine customer reviews on the page; no review gating; incentives only as core rules §8 allows (none on platforms that prohibit them) |
| Q&A / FAQ | Real buyer questions (sizing, compatibility, care) |
| Internal links | Breadcrumbs (Home › Category › Subcategory › Product), link to parent category, related products per core rules §4 |
| Rendering | Price, title, description and JSON-LD in the server HTML, not injected only by JavaScript |

Score each product template (module sub-score): Schema completeness 25 · Title and meta 15 · Images 20 · Content 20 · Internal links 10 · Technical (speed, mobile, canonical) 10.

### 3. Category pages (usually the biggest organic opportunity)

- Treat each category as a landing page for a head term from `keywords.csv`: unique title and H1, a short intro above the grid (what's here, how to choose), a longer guide or FAQ below the grid, links to subcategories and related buying guides. Coverage floor in core rules §4.
- Products listed as real `<a href>` links, server-rendered.
- Empty or near-empty categories: merge, or `noindex` until stocked. Don't leave dozens of thin categories indexed.
- Schema: `BreadcrumbList`; `ItemList` or `CollectionPage` optional. No `Product` markup for the category itself.
- Create category or collection pages for real demand found in research ("waterproof hiking boots women"), not for every tag.

### 4. Faceted navigation and parameters

Filters (size, colour, price, brand) can create millions of URLs. Decide per facet:

| Facet URL | Treatment |
|---|---|
| Has real search demand, a distinct product set, and stable content (e.g. `/boots/waterproof/`) | Indexable: clean static URL, self-canonical, unique title/H1/intro, in sitemap, linked internally |
| Useful to shoppers only (most filters, multi-select combinations, price ranges) | Not indexable: keep out of crawl paths. Preferred: `robots.txt` disallow for the parameter pattern, or filters as URL fragments / form controls that don't create crawlable links. Alternatives: `rel="canonical"` to the unfiltered category (a hint only), or `noindex, follow` |
| Sort, view, page-size, session, tracking parameters (`?sort=`, `?view=`, `?utm_`) | Never indexable; canonical to the clean URL; don't link to them internally |
| On-site search results (`/search?q=`) | Disallow in robots.txt; never in sitemaps |

Rules: don't combine `robots.txt` disallow with `noindex` on the same URLs (blocked pages can't show their `noindex`); keep one parameter order; filtered URLs that return no products should return 404, not an empty 200 page; never put non-indexable facet URLs in the sitemap.

### 5. Pagination

Mechanics (own URL per page, crawlable links, self-canonical, "load more"/infinite scroll): 20-technical-audit.md §12. Catalog note: don't `noindex` paginated pages that are the only path to products, and make every product reachable through categories, sitemaps and related links within the click depth in core rules §4.

### 6. Variants

| Situation | Treatment |
|---|---|
| Variants differ only by size/colour and share one description | One product URL; variant selectors may add `?variant=`; all variant URLs canonical to the main product URL |
| A variant has its own search demand (e.g. "iPhone case red leather") and distinct content | Separate indexable URL with self-canonical, unique title and images |
| Schema | `ProductGroup` with `productGroupID`, `variesBy` (e.g. `https://schema.org/color`) and `hasVariant` listing each `Product` with its own `sku`, `gtin`, image and `Offer` |

Variant titles must differ; each variant's price and availability must be correct in schema and feed.

### 7. Out of stock and discontinued

| Case | Do |
|---|---|
| Temporarily out of stock | Keep the page live (200); `availability` `OutOfStock`, `BackOrder` or `PreOrder`; show the restock date if known, a back-in-stock alert, and alternatives |
| Seasonal product | Keep the same URL year-round; update content and availability |
| Discontinued, direct replacement exists | 301 to the replacement |
| Discontinued, no replacement, page has links or traffic | Keep it (200) with "discontinued" notice, specs, and links to alternatives and the category; or 301 to the closest category |
| Discontinued, no links, no traffic, no value | 404 or 410 |

Never mass-redirect old products to the home page (treated as soft 404). Remove dead URLs from sitemaps.

### 8. Duplicate URLs

| Source | Fix |
|---|---|
| Shopify collection paths: `/collections/x/products/y` alongside `/products/y` | One URL per product: `/products/<handle>` as canonical and in theme links (how: 03-platforms.md §3, Shopify) |
| Shopify tag-filter pages `/collections/x/<tag>`, `/collections/vendors?q=`, `/collections/types?q=`, `/collections/all` | `noindex` or disallow unless curated with unique content |
| Same product in several category paths (WooCommerce, Magento) | Category-free product URLs, or one canonical path |
| Upper/lowercase, trailing slash, `http`/`https`, `www` | One version; 301 the rest (20-technical-audit.md) |
| Tracking/affiliate parameters, quick-view, print pages | Canonical to the clean URL; don't link internally |
| Manufacturer copy shared with other retailers | Rewrite the top sellers first |

### 9. Shopify notes (where most stores run)

- URL structure is fixed (`/products/`, `/collections/`, `/pages/`, `/blogs/<blog>/`); don't promise custom paths.
- `sitemap.xml` is generated automatically (nested child sitemaps); `robots.txt` is customizable (how: 03-platforms.md §3, Shopify). The default rules already block cart, checkout, search and sort parameters; review before changing.
- Check the theme's Product JSON-LD: many themes omit `gtin`, `brand`, shipping and returns, or output `AggregateOffer`; fix in the theme or with one schema app, never both (duplicate blocks).
- Apps often inject heavy JavaScript and duplicate schema; audit installed apps for speed and markup.
- Shopify rate-limits storefront crawling: use the polite crawl rate (core rules §8), start from the sitemap, and sample templates on large stores. The owner can authorize a crawler in the Shopify admin if a full crawl is truly needed; that setup is out of scope here.
- Multi-market stores (Shopify Markets): hreflang and currency checks in 52-international.md.

### 10. Product schema specifics (beyond 21-schema.md)

| Property | Rule |
|---|---|
| `offers` | `Offer` per seller/variant for merchant listings; `AggregateOffer` only for product snippets of multi-seller pages |
| `price` | Number as text (`"49.00"`, no symbol), greater than zero for merchant listings; `priceCurrency` ISO 4217 |
| `availability` | Full URL enum (`https://schema.org/InStock`, `OutOfStock`, `PreOrder`, `BackOrder`, `Discontinued`…) |
| Sale prices | `priceValidUntil`, or `validFrom` + `validThrough`, ISO 8601 with time zone when known |
| Identifiers | `sku`, `gtin8/12/13/14` (or `gtin`), `mpn`, `brand` with a real `name` (not "N/A") |
| Shipping | `shippingDetails` → `OfferShippingDetails` (rate, destination, handling and transit times); or set store-wide shipping in Merchant Center / Search Console |
| Returns | `hasMerchantReturnPolicy` → `MerchantReturnPolicy` (country, category, days, fees), or store-wide via `Organization` / Search Console |
| Reviews | `aggregateRating` (`ratingValue` + `reviewCount`) and `review` only from genuine customer reviews shown on the page; editorial product reviews can add `positiveNotes`/`negativeNotes` |
| Other | `hasCertification` (energy, safety, organic); `category` as text or Google product-category `CategoryCode`; `hasAdultConsideration` required for adult products *(perishable, verified 2026-05)* |
| Consistency | Price, availability and currency must match the visible page and the Merchant Center feed |

Completeness ladder for reporting: required fields only (name, image, offers with price, currency, availability) 50 · + genuine `aggregateRating` 65 · + identifiers 75 · + shipping 85 · + returns 90 · + individual reviews 100.

### 11. Merchant Center and free listings

1. Create or check a Google Merchant Center account; verify and claim the domain; set shipping and return policies.
2. Choose a data source: a product feed (file, spreadsheet or platform app) or automatic product data from the site's structured data. Free listings ("surfaces across Google") are on by default in most markets.
3. Feed quality checklist:

| Attribute | Good |
|---|---|
| `title` | Brand + product type + key attributes (size, colour, material); front-load what shoppers search; no promo text or ALL CAPS |
| `description` | Accurate, specific, no links or promotions |
| `link`, `image_link` | Canonical product URL; clean product image without watermarks, logos or overlay text; additional images |
| `price`, `availability` | Identical to the landing page at crawl time |
| `gtin`, `brand`, `mpn` | Real identifiers; `identifier_exists` = no only for genuinely custom products |
| `google_product_category`, `product_type` | Most specific category; own category path |
| Variants | `item_group_id` plus `color`, `size`, etc. |
4. Check the Diagnostics/Needs attention page monthly: disapprovals, price mismatches, missing identifiers, policy issues.
5. AI-generated product images need the IPTC `DigitalSourceType` = `TrainedAlgorithmicMedia` label *(perishable, verified 2026-09)*.
6. API integrations: the Merchant API replaces the Content API for Shopping (sunset 2026-08-18) *(perishable)*.
7. Also submit to Microsoft Merchant Center (Bing Shopping and Copilot shopping) where available.

**Gap check** (with Search Console + Merchant Center performance, or a paid tool): products ranking organically but absent from Shopping → fix feed coverage; products visible in Shopping but weak organically → improve the product/category page and add a buying guide.

### 12. Marketplaces

- Amazon, Flipkart (India), eBay, Etsy, Walmart and vertical marketplaces often outrank the brand's own product pages and feed AI shopping answers with their reviews.
- Listing basics: keyword-led title in the marketplace's format, benefit bullets, complete attributes and backend search terms, real images, genuine reviews only, brand registry where available.
- Use **different, richer copy on the own site** than on marketplaces (identical copy lets the marketplace win), keep prices and product names consistent across channels, and link marketplace brand stores to the official site where allowed.
- For GEO, consistent product entity data across the site, marketplaces and Merchant Center helps assistants recognize the same product.

### 13. Buying guides and comparison content

Category-level "how to choose", "best X for Y" and "X vs Y" pages answer AI shopping prompts and PAA questions. Plan them in 13-strategy-and-plan.md, write them with 30-content-creation.md (fairness rules for comparisons), and link them to categories and products.

### 14. Agentic commerce (brief, highly perishable)

*(perishable, verified 2026-09; re-check before advising)* AI assistants are starting to complete purchases. Google's **Universal Commerce Protocol (UCP)** lets agents discover and check out with merchants, starting with conversational buying in Google AI Mode; merchants declare capabilities in a JSON profile at `/.well-known/ucp`, versions are dates (e.g. `2026-08-25`, never `"1.0"`), and access currently goes through a Merchant Center waitlist (developers.google.com/merchant/ucp, ucp.dev). Other assistants run their own checkout protocols (e.g. OpenAI's Agentic Commerce Protocol). Prerequisites are the same as everything above: clean Merchant Center feed, correct Product schema, accurate price and availability. Report a missing profile as an opportunity, never as an error.

---

## E-commerce KPIs

| KPI | Source |
|---|---|
| Organic revenue, transactions, conversion rate | GA4 (organic search, AI-assistant channel) |
| Product and category impressions, clicks, CTR | GSC (filter by `/products/`, `/collections/` or equivalent) |
| Merchant listing / product snippet coverage and errors | GSC enhancements reports |
| Free listing clicks and impressions, disapproved items | Merchant Center |
| Indexed vs submitted product URLs | GSC page indexing |
| Category head-term positions | GSC or a paid tool (label it) |
| AI shopping answer mentions for "best X for Y" prompts | 60-measurement.md tracker |

## Output format

```
## E-commerce — <domain> (YYYY-MM-DD)
Platform: <x>   Products: <n> (source)   Categories: <n>   Indexable facet URLs: <n>
Template scores (sub-scores): Product NN/100 · Category NN/100   (source: crawl sample of n pages)
Schema completeness ladder: NN (template) | errors: <list>
Merchant Center: connected / not connected / not measured; disapprovals: <n>

| Issue | Template / URL pattern | Evidence | Fix (platform-specific) | Priority |
|---|---|---|---|---|

Faceted navigation decision table (facet → index / block / canonical)
Out-of-stock and discontinued policy
Top actions (Critical → Low)
Not measured: <item → access needed>
```

## Fallbacks and "not measured"

| Missing | Do instead |
|---|---|
| Can't crawl (rate-limited, blocked) | Use the sitemap plus 3–5 sample URLs per template from the user; say "sampled" |
| No fetch at all | Ask for page source of one product, one category and one filtered URL |
| No Merchant Center access | Check schema only; mark feed quality "not measured"; ask for a Diagnostics screenshot |
| No Search Console | Skip indexing ratios; use `site:` checks (approximate) |
| No search | Skip marketplace and Shopping comparisons; mark "not measured" |
| Can't run code | Manual checks per template using the tables above |
