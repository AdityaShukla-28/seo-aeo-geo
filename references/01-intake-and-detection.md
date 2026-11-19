# 01 — Intake and site detection

Goal: know **what this site is, what it's for, and what we can touch** before doing any work. Output: a confirmed Site Profile (`templates/site-profile.md`).

---

## 1. The intake message

Send one message (skip anything already known from the request or a saved profile):

```
Before I start, a few quick questions (reply in one line, or say "just go" for defaults):

1. Focus: SEO / AEO / GEO / all three (default) / one specific task?
2. Mode: quick task / full audit (default) / strategy / content / implement fixes / monitor & report / full program?
3. Goal: what should more visibility bring? (sales, leads, calls, job offers, readers, sign-ups…)
4. Access: URL only, CMS login, code repo, Search Console, GA4, Bing Webmaster, any paid SEO tool?
5. Market: which country/region and language(s)?
6. Limits: who implements (you, me, a developer), time/budget, anything off-limits?
```

Plain-language definitions to give a user who asks:
- **SEO**: ranking in Google and Bing results.
- **AEO**: being the direct answer (featured snippets, "People also ask", voice answers, the summary at the top of Google).
- **GEO**: being mentioned or cited by ChatGPT, Perplexity, Gemini, Claude and Google's AI Mode.

## 2. What to look at

Fetch (or ask the user to paste) the following. Stop early on small sites.

1. Home page HTML (raw source, and rendered if you can run a browser).
2. `/robots.txt`, `/sitemap.xml` (or the sitemap listed in robots.txt), `/llms.txt`.
3. 3–5 key pages linked from the main navigation (about, services/products, pricing, blog, contact).
4. A `site:domain.com` search, if you can search (rough idea of what is indexed; approximate).

## 3. Detection signals

### 3a. Site type (can be more than one)

| Type | Strong signals |
|---|---|
| **Portfolio / personal brand** | Person's name as brand; "work", "projects", "case studies", "about me", "resume/CV", "hire me"; `Person` schema; few pages; Behance/Dribbble/GitHub links |
| **Local business / service area** | Street address, map embed, local phone, opening hours, "near me", service-area list, `LocalBusiness` schema, booking or "call now" |
| **E-commerce** | Cart, "add to cart", product grids, prices, `Product`/`Offer` schema, `/products/`, `/collections/`, `/shop/`, checkout |
| **SaaS / software / app** | "Sign up", "free trial", "book a demo", pricing tiers, app subdomain or login, integrations page, `SoftwareApplication` schema, app store links |
| **Blog / publisher / news** | Many dated articles, authors, categories, `Article`/`BlogPosting`/`NewsArticle` schema, RSS feed, ads |
| **Agency / B2B services** | "Services", "our clients", case studies, "get a quote", team page, industries served |
| **Docs / developer** | `/docs/`, API reference, code blocks, versioned sidebar nav, search box, GitHub links |
| **Marketplace / directory / listings** | Many similar listing pages with filters (jobs, properties, vendors, events), user-generated listings, faceted URLs |
| **Landing page / one-page site** | One indexable URL, sections reached by `#anchors`, single call to action |
| **Other** (nonprofit, education, events, restaurant, community/forum) | Map to the nearest type and add the extras in 02-site-types.md §11 |

**Hybrids:** choose the **primary type** by the user's goal (where money or leads come from). Secondary types add their modules. Example: SaaS (primary) + blog (secondary) + merch store (secondary, small).

### 3b. Platform

| Platform | Signals |
|---|---|
| WordPress | `/wp-content/`, `/wp-json/`, `<meta name="generator" content="WordPress…">`; WooCommerce: `woocommerce` classes |
| Shopify | `cdn.shopify.com`, `Shopify.theme`, `/products/<handle>`, `myshopify.com` |
| Webflow | `data-wf-page`, `webflow.js`, `website-files.com` assets |
| Wix | `static.wixstatic.com`, `wix-` classes, `X-Wix-*` headers |
| Squarespace | `static1.squarespace.com`, `Squarespace` in source |
| Framer | `framerusercontent.com`, `framer` in source |
| Ghost | `ghost` generator meta, `/ghost/` admin path |
| HubSpot CMS | `hs-scripts`, `hubspot` assets |
| BigCommerce / Magento / PrestaShop | `bigcommerce`, `Magento`/`mage` scripts, `prestashop` |
| Next.js | `__NEXT_DATA__`, `/_next/` |
| Nuxt | `__NUXT__`, `/_nuxt/` |
| Astro / SvelteKit / Gatsby / Remix | `astro-island`, `__sveltekit`, `___gatsby`, `__remixContext` |
| Hugo / Jekyll / Eleventy / static | generator meta, plain HTML, GitHub Pages / Netlify / Vercel hosting |
| React/Vue single-page app | Almost empty `<body>` with `<div id="root">` or `id="app"` and big JS bundles → **JavaScript-rendering flag** |

### 3c. Size tier (from sitemap URL count, or `site:` estimate)

| Tier | Indexable URLs | How to audit |
|---|---|---|
| XS | ≤20 | Check every page |
| S | 21–200 | Check every page type; all key pages |
| M | 201–5,000 | Sample 3–5 pages per template plus top pages |
| L | 5,001–100,000 | Template sampling; lean on Search Console data; crawl by section |
| XL | >100,000 | Template sampling only; index-coverage and crawl-budget focus; say clearly that a full crawl is out of scope |

### 3d. Market and language

- `<html lang>`, hreflang tags, currency, phone country codes, address, domain ending (`.in`, `.co.uk`, `.de`).
- Main search engine for the market: Google almost everywhere; **Naver** (South Korea), **Baidu** (China), **Yandex** (Russia), **Seznam** (Czechia) are significant. Bing matters more for desktop and Copilot users.
- Region-specific listing sites, e.g. India: Google Business Profile, Justdial, Sulekha, IndiaMART; US: Yelp, BBB; UK: Yell, Trustpilot. Don't assume US sources.

### 3e. Special flags

| Flag | Signals | Effect |
|---|---|---|
| **YMYL** (health, money, legal, safety, news) | Medical/financial/legal advice, calculators, insurance, investing, pharmacies | Load the YMYL overlay in 02-site-types.md; stricter E-E-A-T |
| **Staging / dev** | `staging.`, `dev.`, `test.`, `localhost`, password prompt, site-wide `noindex` | Don't flag noindex or blocks as errors; produce a pre-launch checklist |
| **New site** | Under ~10 pages, almost nothing indexed, new domain | Focus on foundations, entity setup and the first content plan; few data-based checks possible |
| **JavaScript-only** | Empty HTML until JS runs | Compare raw vs rendered HTML; rendering is a likely Critical issue |
| **Login-gated** | Most content behind login | Only public pages are in scope; say so |
| **Recent migration or redesign** | New platform, changed URLs, traffic drop | Prioritize redirects, lost pages and indexing checks |

## 4. The Site Profile card (show it, then wait for confirmation)

```
SITE PROFILE: example.com            (detected — please confirm or correct)
Focus:      All three (SEO + AEO + GEO)
Mode:       Full audit
Type:       Local business (primary) + blog (secondary)
            Evidence: address and map in footer, LocalBusiness schema, /blog/ with 34 posts
Goal:       Phone calls and bookings
Platform:   WordPress + Yoast   Evidence: /wp-content/, generator meta
Access:     URL only (no Search Console yet)
Size:       S — 120 URLs in sitemap
Market:     Pune, India · English (Marathi not present)
Flags:      none
Will run:   technical, schema, AI readiness, local, content, links (light)
Skipping:   e-commerce, international (not relevant)
Not measurable yet: real traffic, rankings, Core Web Vitals field data → connect Search Console to unlock
```

If the user corrects anything, update and re-show only the changed lines.

## 5. When detection fails

- **Can't fetch the site** (blocked, offline, firewall): ask for page source, screenshots or a URL list; or switch to advice mode based on the user's description.
- **Truly ambiguous type**: ask one question: "What is the main thing visitors should do on this site?"
- **Nothing published yet**: run the pre-launch path: brand and entity (10), demand research (11), plan (13), and a technical launch checklist (20).

## 6. Save the profile

Write `seo-workspace/<domain>/site-profile.md` from `templates/site-profile.md`. Without file access, print the filled profile in a fenced block and tell the user to keep it and paste it next time.
