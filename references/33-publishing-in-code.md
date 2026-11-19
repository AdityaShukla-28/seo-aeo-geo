# 33 — Publishing content in a codebase

Turn approved Markdown files (frontmatter + body from 30) into real pages in the site's own code: article pages, section listings, hubs and cross-links, using the site's framework and design system, with a mandatory review before anything goes live.

**Inputs:** approved files in `content/published/<slug>.md` (frontmatter per `templates/article-frontmatter.md`), `plan/plan.csv` (sections and URLs), `site-profile.md` (framework), access to the code repository
**Outputs:** code changes on a branch, a preview build, the review checklist below filled in, an entry in `tracking/change-log.md`, and, only after the owner's approval, the deployed pages

## When to use / skip

- **Use** when the site is built from code (Next.js, Nuxt, Astro, SvelteKit, Remix, Hugo, Jekyll, Eleventy, Gatsby, Docusaurus…) and content should live in the repo as Markdown/MDX. Core for docs sites (02-site-types §1).
- Covers **any content section**: blog, guides, comparisons, alternatives, use cases, glossary/definitions, case studies, services, locations, FAQ/trust pages, a resource hub.
- **Skip** for CMS sites (WordPress, Shopify, Webflow, Wix…): publish through the CMS using 03-platforms.md. Skip if you have no repo access: hand the developer the mapping table and checklist below as a fix list (03 advice-mode format).
- Generic platform steps (branches, snapshots, rollback) live in 03; JSON-LD templates live in 21; sitemap, canonical and pagination rules in 20.

## The frontmatter contract

The build reads **exactly these 13 fields**, written by 30. Don't rename them in content files; if a generator expects other names, map them in config or templates.

| Field | Type | Used for | Rendered as |
|---|---|---|---|
| `title` | string | Page heading, cards, breadcrumb label, `og:title`, Article `headline` | `<h1>` (body H1 must equal it) |
| `title_tag` | string | Browser/search title | `<title>` exactly as written (don't let a layout template append the brand twice) |
| `meta_description` | string | Search snippet, social description | `<meta name="description">`, `og:description`, `twitter:description`, Article `description` |
| `slug` | string | Route parameter, file name | Last URL segment; build fails if `url` does not end with it |
| `url` | string, root-relative path | Route, canonical, breadcrumbs, sitemap, internal link resolution | Canonical = site origin + `url`; `og:url` |
| `primary_keyword` | string | Related-content matching only | **Not rendered** (no meta keywords tag) |
| `secondary_keywords` | list | Related-content matching only | **Not rendered** |
| `target_prompts` | list | AI visibility tracking (60) | **Not rendered** |
| `page_type` | enum (13) | Layout choice, schema type, card label, TOC on/off | Label on cards; layout variant |
| `author` | string (name) | Byline, author page link, Article `author` | Visible byline linking to the author's page; `Person` in JSON-LD |
| `date_published` | ISO date `YYYY-MM-DD` (or datetime with timezone) | Sorting, visible date, `datePublished`, `article:published_time` | Visible "Published" date |
| `date_modified` | ISO date | Visible "Last updated", `dateModified`, `article:modified_time`, sitemap `lastmod` | Visible "Last updated" date |
| `summary` | string, 1–2 sentences | Listing card excerpt, RSS item description, related-content cards, `llms.txt` entry (22) | Card text (not in `<head>`) |

**Derived, not stored:** section = the path of `url` without the slug (e.g. `/resources/guides`); canonical = origin + `url`; `og:image` = the page's first content image if it meets 31's social size, else the site default; TOC = H2/H3 headings of the body; author page URL = from the site's existing author data (create an author record if missing, with bio and `sameAs` per 10).

**Validate at build time:** every field present and non-empty, `page_type` is any page_type from 13-strategy-and-plan.md, dates valid ISO and `date_modified ≥ date_published`, `url` unique across all files and ending in `slug`, `url` matches URL rules in core rules §4. A failure stops the build with the file name and field; never silently skip or invent a value.

## Procedure

1. **Discover the stack** (read before writing code): framework and version, router (file-based or config), how Markdown/MDX is already loaded (content collections, content module, `fs` + parser, CMS), styling system (tokens, Tailwind config, component library), existing components (layout shell, cards, buttons, CTA, breadcrumbs), how existing pages set `<head>`, canonical, Open Graph and JSON-LD, and whether pages are statically generated. **Report the findings and the plan to the user**, including any new dependency, before changing anything.
2. **Set up safely** per 03-platforms.md: new branch, no direct commits to the main branch, note the starting commit for rollback.
3. **Copy content in.** Copy approved files from `content/published/` into the repo's content folder, one folder per section (e.g. `content/guides/<slug>.md`). Only approved files; drafts never enter the repo.
4. **Content loading.** Use the framework's native method (framework notes below). Parse frontmatter into a typed object with the validation above. Render Markdown with full support: tables (GFM), blockquotes, code blocks, nested lists, links, images, heading IDs for anchors. Pass through any JSON-LD or chart HTML (31) in the body untouched; never strip the data tables.
5. **Layouts** (reuse the site's design system; never introduce a competing one):
   - *Shell:* site header/footer, max-width matching the site, breadcrumbs (Home → Section → Title).
   - *Article layout:* H1, byline with author link, published and "Last updated" dates, optional TOC (on for `guide`, `definition`, `comparison`, `alternatives` and long pages), the rendered body, related content (3 cards), one CTA at the end using the site's CTA component.
   - Style the **first direct answer** (lead paragraph or blockquote after the H1 or first question H2) with the site's callout pattern; tables with header row, padding and horizontal scroll on mobile; FAQ as H3 question + answer groups; readable body (16–18 px, line height 1.6–1.8, 65–75 characters per line).
6. **Article routes.** One dynamic route per section, or a catch-all route matched on `url`. Statically generate every page. Set `<head>` from the contract table. Internal links in the body render through the framework's link component (client-side navigation, still plain `<a href>` in the HTML).
7. **Structured data.** Per page, JSON-LD built from frontmatter (templates and rules: 21-schema.md; policy: core rules §6): `Article`/`BlogPosting` for editorial types (`headline`=title, `description`=meta_description, `datePublished`, `dateModified`, `author` Person with `url`, `publisher` = site Organization `@id`, `image`), plus `BreadcrumbList`. Other `page_type`s use the type 21 assigns (e.g. `Service`, `LocalBusiness` subtype via 50, `Product` via 51; `SoftwareApplication` via 21). `FAQPage` optional only (core rules §5); never `HowTo`. Server-render it into the HTML; head and JSON-LD code per framework, including escaping: 03-platforms.md §3.
8. **Listing pages.** One hub (e.g. `/resources`) and one listing per section: section title and intro, cards (title, `summary`, date, `page_type` label), newest `date_published` first, pagination with real crawlable links (20). The hub links to every section and a few featured items. Every published page must be linked from its listing (core rules §4 internal link rules).
9. **Cross-links.** Related content: 3 pages, same section first, ranked by shared `primary_keyword`/`secondary_keywords`; cross-section links where the body references another section. At build, check every internal link in the body resolves to a known `url`; fail on broken ones.
10. **Feeds and discovery.** Add new URLs to the sitemap with `lastmod` = `date_modified` (20 owns sitemap rules); RSS/Atom with `summary`; update `llms.txt` if the site has one (22).
11. **Preview build and checks** (mandatory review below).
12. **Owner approval, then deploy** via the site's normal deploy (03), merge only with the owner's OK.
13. **Verify live:** fetch each new URL; view source shows title, meta, canonical, Open Graph, JSON-LD, the body text and tables without JavaScript; validate JSON-LD (21); confirm sitemap entries; submit or request indexing (60). Log everything in `tracking/change-log.md` with the commit and rollback point.

## Mandatory review before deploy

Nothing ships straight to production. Build a preview (local production build such as `npm run build` then `npm run preview`/`start`, or the host's preview deployment) and complete this checklist. Send the owner the preview link (or screenshots) and the filled checklist, and **wait for explicit written approval**. No answer = no deploy.

**Automated / developer checks**
- [ ] Production build passes with zero frontmatter validation errors
- [ ] Every approved file renders; listing pages show all items of their section; no draft or unapproved files built
- [ ] `<title>`, meta description, canonical, `og:*`, `article:*` correct from frontmatter; keywords and prompts not rendered anywhere
- [ ] One H1 equal to `title`; no skipped heading levels (core rules §4)
- [ ] JSON-LD valid and matching visible content (21); no FAQPage-for-rich-results claims, no HowTo
- [ ] Main text, tables and FAQ present in the raw HTML (no JS needed; 22)
- [ ] No broken internal links; external links open the right pages (32 already checked claims)
- [ ] Images: dimensions set, LCP image not lazy-loaded, sizes per core rules §4 (31)
- [ ] Mobile: tables scroll, cards reflow, tap targets per core rules §4; keyboard focus visible, contrast adequate
- [ ] No debug panels, raw frontmatter, developer notes or placeholder text visible
- [ ] Sitemap and feed include the new URLs; canonical URLs and trailing-slash style match the rest of the site (20)

**Owner checks**
- [ ] Pages look like the rest of the site
- [ ] Content, author, dates and CTA are right
- [ ] Approved to deploy: name, date

## Framework notes

| Framework | Load content | Routes and static generation |
|---|---|---|
| **Next.js (App Router)** | `fs` + `gray-matter`, render with `remark`/`rehype` (`remark-gfm`, `rehype-slug`), or MDX (`@next/mdx` or a remote-MDX loader) | `app/<section>/[slug]/page.tsx` with `generateStaticParams` listing the files. Pages Router: `getStaticPaths`/`getStaticProps` |
| **Nuxt 3** | Nuxt Content module (v3: collections in `content.config.ts` with a schema for the 13 fields, `queryCollection`; v2: `queryContent`; check the installed version) | `pages/<section>/[slug].vue`; prerender via `nitro.prerender` or `nuxi generate` |
| **Astro** | Content collections with a schema for the 13 fields (`src/content.config.ts` in Astro 5, `src/content/config.ts` before), `getCollection` | `src/pages/<section>/[slug].astro` with `getStaticPaths`; rendering returns `headings` for the TOC |
| **SvelteKit** | `import.meta.glob` over the content folder (raw) + a frontmatter parser, or mdsvex | `src/routes/<section>/[slug]/+page.server.ts` with `load`, `export const prerender = true`, `entries()` listing slugs |
| **Remix / React Router** | Loader reads files server-side | Route module per section; pre-render if the adapter supports it |
| **Hugo** | Native: Markdown in `content/<section>/`; `title`, `slug`, `url` are native keys. In config `[frontmatter] date = ["date_published", ":default"]`, `lastmod = ["date_modified", ":default"]`; templates read `.Params.title_tag`, `.Params.meta_description`, `.Params.summary` | Built-in |
| **Jekyll / Eleventy / Gatsby / Docusaurus** | Native Markdown collections. SEO plugins expect `description`/`date`/`last_modified_at`: feed them from `meta_description`/`date_published`/`date_modified` in the layout rather than editing the content files | Map `url` to the generator's `permalink` in a layout default, data file or computed data; sort by `date_published` explicitly |
| **Plain React SPA** | — | Client-only rendering hides content from many crawlers and AI bots: add pre-rendering or static generation first (20, 22) |

Head tags (title, meta, canonical, Open Graph) and JSON-LD code per framework: 03-platforms.md §3. Fill them from the contract table; use the absolute form for `title_tag` (e.g. Next.js `title: { absolute: fm.title_tag }`) so a layout template doesn't append the brand twice.

## Output format

```
PUBLISHING PLAN — <domain>
Stack: <framework + version>, styling <x>, content loader <x>, static generation yes/no
New dependencies (need OK): <list or none>
Files to add/change: <paths>
Pages: <n> articles in <sections>; hub <url>; listings <urls>
Frontmatter validation: <n> files OK / <n> errors (file → field)

REVIEW REQUEST
Preview: <link or "screenshots attached">
Checklist: <filled checklist above>
Waiting for owner approval to deploy.

DEPLOY LOG (after approval): log it in tracking/change-log.md using templates/change-log.md
```

## Fallbacks and "not measured"

- **No repo access:** deliver the frontmatter contract, the framework row for their stack, and the review checklist as a developer fix list (03).
- **Can't run a build:** write the code changes, then ask the user or developer to run the build and preview and report errors; mark "preview not verified".
- **Can't fetch the live site after deploy:** ask the user to open view-source on one page and paste the `<head>`; mark live verification "not measured" until then.
- **Missing field in a file:** stop and send the file back to 30 with the missing field named; never fill in a date, author or description yourself.
- **Owner unavailable for approval:** leave the branch and preview ready, do not deploy, and note it in the change log as pending.
