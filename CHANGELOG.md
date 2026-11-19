# Changelog

Format: [Keep a Changelog](https://keepachangelog.com/). Versioning: [Semantic Versioning](https://semver.org/).

- **MAJOR**: workflow changes that break saved workspaces or file formats.
- **MINOR**: new modules, site types or checks.
- **PATCH**: fixes, wording, refreshed facts.

## [1.1.0] — 2026-11-20

### Added
- `seo-aeo-geo-plugin.zip`, for Claude's "Upload a plugin" page. It contains `.claude-plugin/plugin.json` plus `skills/seo-aeo-geo/`. This fixes the "Zip must contain a .claude-plugin/plugin.json file" validation error.
- `seo-aeo-geo-chatgpt-gpt.zip`: the ChatGPT pack as a single download.

### Changed
- README quick start now lists which release file goes to which upload page, and warns against GitHub's "Download ZIP".
- INSTALL.md covers both the Skills and Plugins upload pages.

## [1.0.0] — 2026-11-20

### Added
- Router `SKILL.md`. It asks the purpose (SEO / AEO / GEO / all three / one task) and the mode, detects the site profile, gets confirmation, then runs only the modules that fit.
- `references/00-core-rules.md`: the single source of truth for thresholds, scoring, resolved conflicts, schema policy, AI-crawler policy and guardrails.
- 9 site-type playbooks (portfolio, local, e-commerce, SaaS, publisher, agency, docs, marketplace, landing page), a YMYL overlay and a routing matrix.
- 20 modules covering platforms, brand and entity, demand research, search intent, strategy, technical, schema, AI search readiness, content, visuals, fact-check, publishing in code, links and mentions, local, e-commerce, international, and measurement.
- 19 templates for every workspace file.
- Optional zero-dependency scripts: `aeo-audit.mjs` (crawl politely and run 16 checks) and `validate_schema.py` (JSON-LD checks).
- Adapters for ChatGPT (custom GPT), AGENTS.md tools and Cursor, plus `tools/build_dist.py` for bundles.

### Changed versus the source projects
- Merged duplicate capabilities across the two source repos and resolved about 50 conflicting rules in favour of the core rules.
- Removed self-serving schema, stealth community promotion, allowing AI training bots by default, vendor promotion and OS-specific commands.
- The audit script now crawls politely (at most 2 concurrent requests, about 1 request per second). It parses robots.txt groups correctly and does not penalize sites for blocking training-only bots.
