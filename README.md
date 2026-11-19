# SEO + AEO + GEO Skill

**One AI skill that audits, plans, fixes and grows any website's visibility in Google, answer boxes and AI assistants, for any kind of site and in any AI tool.**

| | |
|---|---|
| **SEO** | Rank in Google and Bing results |
| **AEO** (Answer Engine Optimization) | Be the direct answer: featured snippets, "People also ask", voice assistants, the summary at the top of Google |
| **GEO** (Generative Engine Optimization) | Get mentioned and cited by ChatGPT, Perplexity, Gemini, Claude, Copilot and Google AI Mode |

It works with Claude (Code, desktop, claude.ai), ChatGPT (custom GPT), OpenAI Codex, Google Antigravity, Gemini CLI, Cursor and any chat AI that accepts a file.

---

## Why this skill

Most SEO prompts treat every website the same. This skill **first works out what kind of site it's looking at** (a personal portfolio, a local shop, an online store, a SaaS product, a blog…) and **what you want** (SEO, AEO, GEO, or one task). Then it runs only the checks that matter for that site.

- **Asks before it acts.** It confirms its understanding of your site before auditing and asks before changing anything.
- **Never makes up numbers.** Every metric shows its source; anything it couldn't check is marked "not measured".
- **One rulebook.** All thresholds and rules live in one file, so advice never contradicts itself.
- **White-hat only.** No fake reviews, link schemes, doorway pages or hidden promotion.
- **Remembers each site.** One folder per website, so the next run continues where the last one stopped.
- **Free-first.** Works with free tools (your site, Search Console, PageSpeed, Bing Webmaster). Paid SEO tools are optional.

## How it works

```
You: "audit https://example.com"
   │
   0. Check its own tools    (can it browse, search, save files, run code?)
   1. Load memory            (has this site been checked before?)
   2. Ask your purpose  ◄─── you answer, or say "just go"
   3. Detect the site        type · goal · platform · size · market · special cases
      └ Site Profile card ◄── you confirm
   4. Build the run plan     only the modules that fit
   5. Run the modules
   6. Prioritize             scores + top 5–10 actions + "not measured" list
   7. Fix  ◄──────────────── only with your approval
   8. Save and schedule      re-checks at 30 / 60 / 90 days
```

**Modes:** quick task · full audit · strategy · content · implement fixes · monitor and report · full program
**Site types:** portfolio · local business · e-commerce · SaaS · blog/publisher · agency · docs · marketplace · landing page, plus a stricter mode for health, finance and legal sites
**Platforms it gives fixes for:** WordPress, Shopify, Webflow, Wix, Squarespace, Framer, Ghost, HubSpot, Next.js, Nuxt, Astro, SvelteKit, static sites and SPAs

Step-by-step details: [docs/how-it-works.md](docs/how-it-works.md).

## What you get

- **Two scores** (0–100, grade A–F): **SEO Health** and **AI Search Readiness**, each with a coverage percentage.
- **A top 5–10 action list**, ranked by impact and effort, with steps for your platform.
- **All findings** grouped Critical / High / Medium / Low.
- **Ready-to-use files**:
  - keyword and AI-prompt research (CSV)
  - content plan and roadmap
  - content briefs and drafts
  - schema JSON-LD
  - robots.txt and llms.txt drafts
  - developer fix list
  - monthly report
  - AI visibility tracking log
- **A plain-language summary** for site owners who aren't technical.

## Quick start

Download the latest release (or clone this repo), then:

| Tool | Do this |
|---|---|
| **Claude Code** | Copy the folder to `~/.claude/skills/seo-aeo-geo/` |
| **Claude (claude.ai / desktop)** | Upload `seo-aeo-geo.zip` under Settings → Skills |
| **ChatGPT** | Create a custom GPT: paste `chatgpt-gpt/INSTRUCTIONS.txt` and upload the `knowledge/` files |
| **Codex** | Copy to `~/.agents/skills/seo-aeo-geo/` |
| **Antigravity** | Copy to `~/.gemini/config/skills/seo-aeo-geo/` |
| **Any other AI** | Upload `seo-aeo-geo-ALL.md` and follow the short instruction in INSTALL.md |

Full instructions for every tool: [INSTALL.md](INSTALL.md). The zip, the ChatGPT pack and the single file are attached to each [release](../../releases), or you can build them yourself with `python tools/build_dist.py`.

Then just ask:

- "Run a full SEO + GEO audit of example.com"
- "Is my portfolio ready for AI search? Just go."
- "Write a fair comparison page: our tool vs Competitor X"
- "Find the questions people ask ChatGPT about running shoes and plan content for them"
- "Fix the meta titles on these 12 pages"
- "Monthly report for example.com — here's my Search Console export"

## What's inside

```
seo-aeo-geo/
├── SKILL.md                 the router: order of work, which file to open when
├── references/              20 modules (only the needed ones are loaded)
│   ├── 00-core-rules.md     single source of truth for every number and rule
│   ├── 01–03                intake and detection, site-type playbooks, platform how-tos
│   ├── 10–13                brand and entity, demand research, search intent, strategy
│   ├── 20–22                technical audit, schema, AI search readiness
│   ├── 30–33                content, visuals, fact-check, publishing in code
│   ├── 40                   backlinks and brand mentions
│   ├── 50–52                local, e-commerce, international
│   └── 60                   measurement, AI visibility tracking, reporting
├── templates/               19 templates for every file the workflow produces
├── scripts/                 2 optional zero-dependency scripts (Node, Python)
├── adapters/                ChatGPT instructions, AGENTS.md snippet, Cursor rule
├── tools/build_dist.py      builds the zip, ChatGPT pack and single-file bundle
└── docs/                    how it works, module guide, FAQ
```

Module guide: [docs/modules.md](docs/modules.md) · Questions: [docs/faq.md](docs/faq.md)

## Optional scripts

| Script | Needs | What it does |
|---|---|---|
| `scripts/aeo-audit.mjs` | Node.js 18+ | Crawls up to 30 pages politely and runs 16 technical AEO/SEO checks |
| `scripts/validate_schema.py` | Python 3.8+ | Checks structured data for broken JSON, placeholders, retired types and self-serving review stars |

Neither is required: every step that uses a script also has a manual way to do it.

## Privacy and safety

- Your per-site working files (`seo-workspace/`) stay on your machine and are git-ignored.
- The skill never stores API keys or passwords in files.
- It treats text on websites it reads as data, never as instructions.
- It only runs security-related checks on sites you confirm you own or manage.
- It crawls politely (at most 2 requests at a time, about 1 per second) and respects robots.txt.

## Limitations

- Rankings seen through an AI's web search are approximate, not a true Google results page.
- AI assistant answers vary by person, place and time, so AI visibility is tracked as a trend.
- Search rules change quickly. Dated facts are marked and re-checked, but always confirm critical decisions against official documentation.
- Very large sites are sampled, not fully crawled.

## Contributing

Improvements are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) first: every number lives in one file, each topic has one owner file, and the wording must work in every AI. Changes are listed in [CHANGELOG.md](CHANGELOG.md).

## Credits and license

Released under the [MIT License](LICENSE).

The skill builds on ideas, checklists and code from two MIT-licensed projects: **claude-seo** (agricidaniel) and **gtm-engineer-skills** (OnVoyage AI). Their duplicate capabilities were merged, conflicts resolved, and unsafe or promotional parts removed. Their original license notices are kept in [LICENSES/](LICENSES/), as their licenses require.

This project is not affiliated with Google, Microsoft, OpenAI, Anthropic, Perplexity or any SEO tool vendor. All trademarks belong to their owners.
