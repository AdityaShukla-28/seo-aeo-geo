# How it works

What happens, step by step, after you give the skill a website (or any SEO request).

```
You: "audit https://example.com"
   │
   0. Check own tools       can it browse? search? save files? run code? edit the site?
   1. Load memory           has this site been checked before?
   2. Ask the purpose  ◄─── YOU answer (or say "just go")
   3. Detect the site
      └ Site Profile card ◄─ YOU confirm or correct
   4. Build the run plan    modules to run, modules skipped and why
   5. Run the modules       order depends on the mode
   6. Prioritize            top 5–10 actions, findings by priority
   7. Fix  ◄─────────────── only with YOUR approval
   8. Save and schedule     profile, change log, re-check dates
```

You step in at only three points: **purpose (2)**, **profile confirmation (3)** and **approving fixes (7)**.

---

## Step 0: Check its own tools

The skill runs in many AIs, and they differ in what they can do. It checks quietly and adapts:

| Can it… | If yes | If no |
|---|---|---|
| Open web pages | Reads your site directly | Asks you to paste the page source, a URL list or screenshots |
| Search the web | Researches keywords, competitors and AI prompts | Asks you for competitors and topics; marks search data "not measured" |
| Save files | Keeps a folder per website | Prints every result in the chat and gives you a Site Profile block to save |
| Run code | Can use the two optional scripts | Uses the manual checklist each script step has |
| Edit your site | Can apply fixes (after approval) | Gives you a developer-ready fix list |

## Step 1: Load memory

It looks for `seo-workspace/<your-domain>/site-profile.md`, or asks you to paste a saved profile. If one exists it reads the profile and the change log, skips questions already answered, and re-checks only facts older than 90 days.

## Step 2: Ask the purpose

One short message you can answer in one line:

| Question | Options | Default |
|---|---|---|
| Focus | SEO · AEO · GEO · all three · one specific task | All three |
| Mode | Quick task · Full audit · Strategy · Content · Implement fixes · Monitor and report · Full program | Full audit |
| Goal | Sales, leads, calls, job offers, readers, sign-ups… | — |
| Access | URL only · CMS login · code repo · Search Console · GA4 · Bing Webmaster · paid SEO tool | URL only |
| Market | Country/region and language(s) | Inferred from the site |
| Limits | Who implements, time or budget, anything off-limits | — |

Saying **"just go"** uses all the defaults.

**Quick tasks skip most of this.** "Write meta titles for these 5 pages" gets only the missing questions, a quick site check and the one module needed.

## Step 3: Detect the site

It reads the home page, `robots.txt`, `sitemap.xml`, `llms.txt` and 3–5 key pages, then works out:

- **Type**: portfolio, local business, e-commerce, SaaS, blog/publisher, agency, docs, marketplace or landing page. Sites can have more than one type (e.g. SaaS + blog).
- **Goal**: what the site should achieve.
- **Platform**: WordPress, Shopify, Webflow, Wix, Squarespace, Framer, Next.js and others, detected from code fingerprints.
- **Size**: XS (≤20 pages) up to XL (100k+ pages), which decides how deep it can check.
- **Market**: country, language and main search engine.
- **Flags**: YMYL (health, money, legal), staging site, new site, JavaScript-only, login-gated, recent migration.

Then it shows a **Site Profile card** with its evidence:

```
SITE PROFILE: example.com            (detected — please confirm or correct)
Type:      Local business (primary) + blog (secondary)
           Evidence: address and map in footer, LocalBusiness schema, /blog/ with 34 posts
Platform:  WordPress + Yoast
Size:      S — 120 URLs
Market:    Pune, India · English
Will run:  technical, schema, AI readiness, local, content, links (light)
Skipping:  e-commerce, international (not relevant)
Not measurable yet: real traffic and rankings → connect Search Console to unlock
```

**It waits for your confirmation.** A wrong profile would make every later step wrong.

## Step 4: Build the run plan

Three things decide what runs:

1. **Site type**: each type's playbook marks modules as core, conditional or skipped (a portfolio skips e-commerce; a store skips local unless it has a shop).
2. **Focus**: SEO, AEO or GEO gives extra depth to different modules.
3. **Mode**: sets the order (below).

## Step 5: Run the modules

| Mode | Order |
|---|---|
| **Quick task** | The one module that matches |
| **Full audit** | Brand (light) → Technical → Schema → AI readiness → Content (light) → Images (light) → Local / E-commerce / International if relevant → Backlinks → Measurement (if data access) |
| **Strategy** | Brand and entity → Keywords and AI prompts → Search intent → Plan and roadmap |
| **Content** | Research (if needed) → Search intent → Write → Charts and images → Fact-check → Publish (if code access) |
| **Implement fixes** | Platform guide → Technical/schema/AI fixes (+ local/e-com/international) → Publish → Re-check |
| **Monitor and report** | Measurement: Search Console, GA4, AI visibility tracker, regression checks, monthly report |
| **Full program** | All of the above in order, then a refresh loop |

Each module file opens only when its turn comes, so the AI's memory isn't flooded.

## Step 6: Prioritize

Every finding must pass a **relevance check**. It has to fit the site's type, your goal, your platform and the people and time you have, or it's cut. You then get:

1. **Scores**: SEO Health and/or AI Search Readiness (0–100, grade A–F), with **coverage** (how much could actually be measured).
2. **Top 5–10 actions**: why each matters, how to do it on your platform, effort, and how you'll know it worked.
3. **All findings** grouped Critical (now) / High (1 week) / Medium (1 month) / Low (backlog).
4. **Not measured**: what couldn't be checked and what access would unlock it.
5. **Two versions** if needed: a plain summary for the owner and a technical list for the developer.

Every number shows its source (Search Console, PageSpeed, crawl, a named tool). Nothing is guessed.

## Step 7: Fix (only with approval)

With edit access:
1. Snapshot the current state.
2. Change on a branch or draft.
3. Log the change.
4. Preview it.
5. Get **your approval**.
6. Publish.
7. Verify.
8. Keep a rollback plan.

Without edit access you get ticket-style fixes for your developer: issue, evidence, fix, platform steps, acceptance test and priority.

## Step 8: Save and schedule

It updates the Site Profile and the change log and sets **re-check dates at 30, 60 and 90 days**, since SEO changes take weeks to show. Next time you open the site, it starts here.

### Where things are saved

```
seo-workspace/<domain>/
  site-profile.md       ← read first next time
  brand-dna.md
  research/   keywords.csv, prompts.csv, community.md, competitors.md, serp-intent.md
  plan/       plan.csv, roadmap.md, backlink-plan.md
  audits/     dated audit reports, fix lists, image and backlink audits
  content/    briefs/, drafts/, published/
  generated/  sitemap.xml, robots.txt, llms.txt, schema JSON (drafts)
  tracking/   change-log.md, ai-visibility-log.csv, baselines/
  reports/    monthly reports
```

Each website gets its own folder, so data from different brands is never mixed.
