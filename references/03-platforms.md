# 03 — Platforms and safe changes

How to apply SEO/AEO/GEO fixes on each CMS, store builder and framework, how to change a live site safely, and how to hand fixes to a developer when you can't edit the site.

**Inputs:** `seo-workspace/<domain>/site-profile.md` (platform, access, implementer), latest `audits/YYYY-MM-DD-audit.md`, `tracking/baselines/`
**Outputs:** `audits/YYYY-MM-DD-fix-list.md` (advice mode), entries in `tracking/change-log.md` (implement mode), new files in `tracking/baselines/`

## When to use / skip

- **Use** before changing anything on a site (Implement fixes, Full program) and whenever you write a fix list.
- **Use** the tables to pass the **platform fit** test (core rules §3). If a platform can't do something, give the workaround or drop the item.
- **Skip** the tables for pure strategy or content work, but follow §4 before publishing anything.
- *What* to fix comes from 20, 21, 22 (and 50/51/52). This file says **where and how**. Thresholds stay in core rules §4.

## Procedure

1. Read platform and access from the Site Profile (detect per 01 §3b if missing).
2. For each approved fix, find the exact place in §3.
3. If the platform lacks the capability, use the table's workaround or §2, or mark the fix "not possible on this platform" and replace or drop it.
4. Edit access + approval → safe-change protocol (§4). No edit access → fix list (§5).
5. After publishing, verify (§4 step 7) and set re-checks (60-measurement.md §12).

## 1. Rules on every platform

- Title, meta description, canonical, meta robots and JSON-LD belong in the **server-rendered HTML**. If raw and rendered HTML disagree on canonical or robots, Google may use either (diagnosis in 20).
- One plugin/app per job. Two tools writing titles, sitemaps or schema create duplicates: switch the feature off in one.
- Permanent moves: 301 (or 308), one hop, to the final URL. No meta-refresh or JavaScript redirects when a server redirect is possible.
- robots.txt follows core rules §7 (search bots allowed; training bots per the owner's recorded decision). Template `templates/robots-ai.txt`; mechanics in 20. llms.txt at the root (core rules §5; content in 22). Schema content in 21.
- Platform menus and features are **perishable (baseline 2026-11)**. Where a cell says "check docs", confirm in the platform's current documentation before promising the fix.

## 2. Workarounds for hosted builders (no root files, no robots.txt editing)

1. Look for a native setting or official app first (check docs).
2. **Verification files** (Search Console, Bing): use the DNS TXT or meta-tag method instead.
3. **llms.txt**: if redirects from non-existent paths work, 301 `/llms.txt` to a hosted copy (some AI tools don't follow redirects). It is Low priority outside docs sites (core rules §5), so skipping it is acceptable. Say so.
4. **CDN/edge worker** (Cloudflare Workers, host rewrites) can serve root files or rewrite robots.txt. Only if the site already runs through it and the owner approves. Log it as a moving part.
5. **Robots.txt not editable**: control indexing with per-page `noindex`; use the platform's AI-crawler toggle (if any) for training bots.

## 3. Platform tables

### WordPress (Yoast SEO, Rank Math, SEOPress) and WooCommerce

| Item | Where / how |
|---|---|
| Titles/meta | Plugin box per post; templates in plugin settings (Yoast Settings → Content types; Rank Math Titles & Meta; SEOPress Titles & Metas) |
| robots.txt | Virtual file; edit in Yoast (Tools → File editor), Rank Math (General Settings → Edit robots.txt), SEOPress PRO. A physical file in the web root overrides it: check first |
| Sitemap | Core `/wp-sitemap.xml` or plugin index (Yoast/Rank Math `/sitemap_index.xml`, SEOPress `/sitemaps.xml`). Keep one |
| Redirects | Rank Math Redirections, Yoast Premium, free Redirection plugin, or `.htaccess`/nginx (best for migrations) |
| Canonical | Plugin self-canonical; override in the Advanced tab |
| JSON-LD / head | Plugin `@graph`; extend via plugin filters or a `wp_head` hook in a child theme or snippets plugin. Never edit the parent theme; no second `Organization` node |
| llms.txt | Upload to web root (SFTP/file manager); some SEO plugins generate one (check docs) |
| noindex | Plugin Advanced tab. Settings → Reading "Discourage search engines" must be off in production |
| Speed | Page cache, image optimization, CDN, current PHP, fewer plugins, light theme |
| Limits | WordPress.com lower plans block plugins/files → upgrade or use built-in fields. Security plugins/host firewalls may block AI bots → allow search bots with the owner's OK. WooCommerce: check for duplicate `Product` nodes; noindex filter/sort URLs (51) |

### Shopify

| Item | Where / how |
|---|---|
| Titles/meta | "Search engine listing" on each product, collection, page, post; home in Online Store → Preferences |
| robots.txt | Customize via the `robots.txt.liquid` theme template; keep Shopify's defaults and add rules |
| Sitemap | Auto `/sitemap.xml`, not editable; `seo.hidden` metafield excludes items |
| Redirects | Admin URL redirects (Navigation/Menus area; CSV import); "create redirect" checkbox on handle change. Fires only if the old path no longer exists |
| Canonical | `{{ canonical_url }}` in `theme.liquid`. `/collections/x/products/y` canonicalizes to `/products/y`; make theme links use `product.url` |
| JSON-LD / head | Theme sections/`theme.liquid` or an app. Themes and apps often both emit Product: keep one |
| llms.txt | No arbitrary root files: check docs/app store, else §2 |
| noindex | `seo.hidden` metafield (also drops from sitemap) or Liquid condition printing robots meta |
| Speed | Light theme, remove unused apps (and leftover app code), `image_url` with widths, fewer fonts |
| Limits | Fixed `/products/`, `/collections/`, `/pages/`, `/blogs/<name>/` prefixes: accept them. Checkout locked. Tag-filter and `/collections/all` duplicates → canonical/noindex in theme (51) |

### Webflow

| Item | Where / how |
|---|---|
| Titles/meta | Page settings → SEO; CMS templates bind fields (`{Name} | Brand`) |
| robots.txt | Site settings → SEO → robots.txt |
| Sitemap | Site settings → SEO → auto-generate (or custom); per-page exclusion in page settings |
| Redirects | Site settings → Publishing → 301 redirects (capture-group patterns) |
| Canonical | Global canonical URL in SEO settings; per page via head code (check docs for a per-page field) |
| JSON-LD / head | Page settings → Custom code (head); CMS fields can be inserted. Paid site plan required |
| llms.txt | Check docs for native upload, else §2 |
| noindex | Page settings indexing toggle or robots meta in head code; keep `*.webflow.io` staging noindexed |
| Speed | WebP/AVIF in Assets panel, lazy-load all but the hero, fewer interactions/Lottie, fewer fonts |

### Wix

| Item | Where / how |
|---|---|
| Titles/meta | Page → SEO Basics; SEO settings per page type for patterns |
| robots.txt | SEO settings → robots.txt editor |
| Sitemap | Auto `/sitemap.xml`; non-indexed pages excluded |
| Redirects | SEO → URL Redirect Manager (CSV import) |
| Canonical | Auto; override in page Advanced SEO |
| JSON-LD / head | Page Advanced SEO → Structured data markup; site-wide code in Settings → Custom code (premium + connected domain) |
| llms.txt | Check docs, else §2 |
| noindex | SEO Basics → "Let search engines index this page" off |
| Speed / limits | Fewer apps, widgets, animations and video backgrounds. Fixed prefixes for blog/product/dynamic pages; no server access |

### Squarespace

| Item | Where / how |
|---|---|
| Titles/meta | Page settings → SEO; title formats in the SEO panel |
| robots.txt | Auto-generated, not editable as far as known; AI-crawler setting exists (check docs) |
| Sitemap | Auto `/sitemap.xml`, not editable |
| Redirects | Settings → Developer tools → URL mappings: `/old -> /new 301` |
| Canonical | Automatic; per-page control: check docs |
| JSON-LD / head | Code injection, site-wide and per page (plan-dependent) |
| llms.txt | No root uploads as far as known: check docs, else §2 |
| noindex | Page settings → SEO → hide from search |
| Speed / limits | Upload images at display size, fewer blocks and scripts. Limited robots/canonical control → per-page noindex |

### Framer

| Item | Where / how |
|---|---|
| Titles/meta | Page settings; CMS field variables. Replace Framer's default site meta |
| robots.txt / canonical | Auto-generated; custom rules and canonicals: check docs |
| Sitemap | Auto `/sitemap.xml` |
| Redirects | Site settings → Redirects (wildcards) |
| JSON-LD / head | Site and per-page custom code (plan-dependent) |
| llms.txt | Check docs, else §2 |
| noindex | Page settings → exclude from search engines |
| Speed / limits | Compress images, limit scroll effects and fonts. Pages are server-rendered (good). Lightbox-only portfolios need real CMS pages per project (02 §2) |

### Ghost

| Item | Where / how |
|---|---|
| Titles/meta, canonical | Post settings → Meta data (has a Canonical URL field); site defaults in Settings |
| robots.txt | Add `robots.txt` to the theme root and upload the theme |
| Sitemap | Auto `/sitemap.xml` |
| Redirects | Upload a redirects YAML/JSON file in settings (location varies by version) |
| JSON-LD / head | Default JSON-LD from `{{ghost_head}}`; add via Code injection (site/post) or theme |
| llms.txt | Check docs (theme-root files beyond robots.txt may not be served), else §2 |
| noindex | Robots meta via post code injection or theme logic |
| Limits | Ghost(Pro): no server access → redirects file and code injection only |

### HubSpot CMS

| Item | Where / how |
|---|---|
| Titles/meta | Page/post editor → Settings |
| robots.txt | Settings → Website → Pages → SEO & Crawlers (per domain) |
| Sitemap | Auto; manage exclusions in website settings (check docs) |
| Redirects | Settings → Domains & URLs → URL redirects (bulk import, flexible patterns) |
| Canonical | Global setting in SEO & Crawlers; per page in advanced settings |
| JSON-LD / head, noindex | Page → Advanced → Head HTML; site header HTML; HubL templates |
| llms.txt | Check docs, else §2 |

### Other stores (brief)

- **BigCommerce**: SEO fields per product/category; robots.txt editable in store settings; auto sitemap; built-in 301 manager; JSON-LD in Stencil templates (watch app duplicates).
- **Magento / Adobe Commerce**: robots.txt and default meta in Content → Design → Configuration; Marketing → Site Map; URL rewrites for redirects; canonical options in Catalog SEO configuration; JSON-LD in theme templates. Needs a developer and a deploy.

### Next.js (App Router)

| Item | Where / how |
|---|---|
| Titles/meta | `metadata` / `generateMetadata()`; `metadataBase` in root layout; `title: { template: '%s | Brand' }` |
| robots.txt / sitemap | `app/robots.ts`, `app/sitemap.ts` (`generateSitemaps()` above 50,000 URLs). Not both a static and generated file |
| Redirects | `redirects()` in `next.config` with `permanent: true` (308, treated like 301), or `permanentRedirect()` in server code |
| Canonical / noindex | `alternates: { canonical: '/path' }`; `robots: { index: false, follow: true }` |
| llms.txt | `public/llms.txt` or `app/llms.txt/route.ts` |
| Speed | `next/image` with sizes and high priority on the LCP image (prop name changed across versions: check docs), `next/font`, Server Components, static rendering |
| Limits | Pages Router: `next/head` + a sitemap package. Meta set only in client effects is missing from raw HTML |

```ts
// app/robots.ts: search bots allowed; training bots only per the owner's decision (core rules §7)
import type { MetadataRoute } from 'next'
export default function robots(): MetadataRoute.Robots {
  return {
    rules: [
      { userAgent: '*', allow: '/', disallow: ['/api/', '/admin/'] },
      // Owner opted out of training (full list: templates/robots-ai.txt):
      // { userAgent: ['GPTBot','ClaudeBot','Google-Extended','Applebot-Extended','CCBot','Bytespider','Meta-ExternalAgent'], disallow: '/' },
    ],
    sitemap: 'https://example.com/sitemap.xml',
  }
}
```

```tsx
// In a Server Component. Escape "<" so data can't close the script tag.
<script type="application/ld+json"
  dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd).replace(/</g, '\\u003c') }} />
```

### Nuxt, Astro, SvelteKit

| Item | Nuxt 3+ | Astro | SvelteKit |
|---|---|---|---|
| Meta, canonical, noindex | `useSeoMeta({ title, description, robots })`, `useHead({ link: [{ rel: 'canonical', href }] })` | Shared layout `<head>` with props | `<svelte:head>` filled from `load` |
| robots, sitemap, llms.txt | `public/` files or `@nuxtjs/robots`, `@nuxtjs/sitemap` | `public/` files; `@astrojs/sitemap` (needs `site`) | `static/` or `+server.ts` endpoints with `prerender = true` |
| Redirects | `routeRules` `{ redirect: { to, statusCode: 301 } }` | `redirects` config; static output without an adapter makes meta-refresh pages → add host 301 rules | `redirect(301, …)` in `load` or `hooks.server` |
| JSON-LD | `useHead({ script: [{ type: 'application/ld+json', innerHTML: JSON.stringify(d) }] })` or `nuxt-schema-org` | `<script type="application/ld+json" set:html={JSON.stringify(d)} />` | `{@html}` script in `<svelte:head>`, escape `<` |
| Risk | `ssr: false` = SPA | Client-only islands hide content | `ssr = false` = SPA |

**Gatsby**: `Head` export per page; `gatsby-plugin-sitemap`; root files in `static/`; redirects via host rules. **Remix / React Router v7 framework mode**: `meta` and `links` exports (canonical), resource routes for robots/sitemap/llms, `redirect(url, 301)` in loaders.

### Hugo, Jekyll, Eleventy, plain HTML

| Item | Where / how |
|---|---|
| Meta, canonical, JSON-LD | Hugo `layouts/partials/head.html`; Jekyll `jekyll-seo-tag` or `_includes/head.html`; Eleventy base layout; plain HTML each `<head>`. JSON-LD partial from front matter (title, date, lastmod) |
| Root files, sitemap | Hugo `static/` + built-in sitemap/robots; Jekyll root + `jekyll-sitemap`; Eleventy passthrough copy + sitemap template; plain HTML web root |
| Redirects | Host rules: Netlify/Cloudflare `_redirects`, `vercel.json`, `.htaccess`, nginx. GitHub Pages can't send 301s (only meta refresh) → change host or accept it |

### Client-side React / Vue / Angular SPAs

Raw HTML is an empty `<div id="root">`: AI fetchers that don't run JavaScript see nothing (diagnosis in 20). Options, best first:

1. **SSR/SSG for public pages** (Next.js, React Router framework mode, Nuxt, Angular SSR, Astro); keep the logged-in app as a SPA.
2. **Build-time prerendering** for a few mostly static routes; rebuild on content change.
3. **Prerender service** (dynamic rendering): stop-gap only. Google calls it a workaround, and bots and users must get the same content or it becomes cloaking (core rules §8).
4. **Minimum hygiene meanwhile**: history routes (no `#/`), unique title/meta per route (`react-helmet-async`, `@unhead/vue`), real 404 status, robots/sitemap/llms in `public/`, host redirects.

## 4. Safe-change protocol (every live change)

Never publish or deploy without the user's explicit OK (core rules §9).

| Step | Do | Done when |
|---|---|---|
| 1. Baseline + backup | Drift baseline of every affected URL (60 §7) into `tracking/baselines/`. Backup: plugin/host backup, duplicate Shopify theme, builder version history, or git commit | Baseline file + backup name noted |
| 2. Isolate | Branch (code); draft, duplicate theme, staging or unpublished page (CMS) | Nothing live yet |
| 3. Change | Smallest change that fixes the finding; one finding per change where possible | Before/after captured |
| 4. Log | Append to `tracking/change-log.md` (ID, URLs, before → after, finding, rollback) | Entry exists |
| 5. Preview | View source: title, canonical, robots meta, JSON-LD (validate per 21), status codes, redirects; mobile look | Checklist passed |
| 6. Approve + publish | Show the owner before/after; wait for an explicit yes; then publish/merge/deploy | Approval in the log |
| 7. Verify live | Re-fetch, drift compare (60 §7), test robots.txt and redirects, request indexing for key URLs (60 §5) | No Critical drift; log says "verified" |
| 8. Rollback ready | Exact undo written before step 6: revert commit, restore theme/backup, remove redirect, restore old values from the baseline | In the log entry |

Bulk redirects, robots.txt, canonical rules, site-wide templates and migrations: test on a few URLs first, then roll out. Staging sites keep noindex/password protection (core rules §9.3).

## 5. Advice-mode developer fix list

Write `audits/YYYY-MM-DD-fix-list.md` from `templates/fix-list.md`: a summary table, then one self-contained ticket per issue (pasteable into Jira, Linear, GitHub or email), ordered by priority (core rules §2):

```
### FIX-007 · High · Product pages missing canonical tag
Issue:      /products/* pages have no <link rel="canonical">; collection paths create duplicates.
Evidence:   view-source of /collections/shoes/products/runner-x has no canonical (crawl, 2026-11-20);
            14 URLs under "Duplicate without user-selected canonical" (GSC).
Why:        Google may pick the wrong URL and split signals between duplicates.
Fix:        Self-referencing canonical to /products/<handle> on every product page.
Platform steps (Shopify): duplicate theme → Edit code → theme.liquid → add
            <link rel="canonical" href="{{ canonical_url }}"> in <head> → preview → publish after approval.
Acceptance test: 3 product URLs (direct and via a collection) show the same /products/<handle>
            canonical in view-source; URL Inspection shows user-declared = Google-selected canonical
            within ~2 weeks.
Effort: S · Owner: theme developer · Depends on: none
```

Ticket rules: evidence has a source label (core rules §1); the acceptance test is checkable by a non-SEO; platform steps come from §3; one ticket per repeated issue with a URL list; a plain-language "Why" line when the owner isn't technical.

## Output format

- **Implement mode**: change-log entries (`templates/change-log.md`) plus a short chat summary: what changed, where, verification result, rollback step, next re-check date.
- **Advice mode**: `audits/YYYY-MM-DD-fix-list.md`: summary table (ID · priority · title · effort · owner), then tickets as above.

## Fallbacks and "not measured"

- **Platform unknown**: give the generic fix plus how to find the setting, and ask which CMS they use.
- **Unsure the platform allows it**: say "check current platform docs" and give the §2 workaround. Never invent a menu path.
- **No file access**: print fix list and change-log entries in chat as fenced blocks.
- **Can't fetch the live site after publishing**: ask for view-source of the changed page; mark verification "not measured" until then.
