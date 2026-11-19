# Install: seo-aeo-geo

The skill is a plain folder that follows the open **Agent Skills** format (a `SKILL.md` plus `references/`, `templates/`, `scripts/`). Tools that support Agent Skills load the folder directly. Chat AIs without skill support use the ready-made bundles you build below.

## Build the bundles (once, or after editing the skill)

Needs Python 3.8+ (no packages). Run from inside the skill folder:

```
python tools/build_dist.py
```

This writes a `dist/` folder **next to** the skill folder:
- `seo-aeo-geo.zip`: the skill folder, for upload-based tools
- `chatgpt-gpt/`: instructions plus up to 20 knowledge files for a custom GPT
- `seo-aeo-geo-ALL.md`: the whole skill in one file, for any other chat AI

Use `--out <folder>` to write somewhere else.

---

## Tools with skill support (copy the folder)

`~` means your home folder (`C:\Users\<you>` on Windows).

| Tool | For all projects (global) | For one project only |
|---|---|---|
| **Claude Code** | `~/.claude/skills/seo-aeo-geo/` | `<project>/.claude/skills/seo-aeo-geo/` |
| **Claude apps** (claude.ai, desktop) | Settings → Capabilities/Skills → upload `dist/seo-aeo-geo.zip` | — |
| **OpenAI Codex** | `~/.agents/skills/seo-aeo-geo/` | `<repo>/.agents/skills/seo-aeo-geo/` |
| **Google Antigravity** | `~/.gemini/config/skills/seo-aeo-geo/` | `<workspace>/.agents/skills/seo-aeo-geo/` |
| **Gemini CLI** | `~/.gemini/skills/seo-aeo-geo/` *(check your version's docs)* | `<repo>/.agents/skills/seo-aeo-geo/` |
| **Cursor, Windsurf, Aider, Jules, other agents** | — | Copy to `<repo>/.agents/skills/seo-aeo-geo/`, add `adapters/AGENTS.md` to the repo's `AGENTS.md`; in Cursor also copy `adapters/cursor-rule.mdc` to `.cursor/rules/` |

One copy in `<repo>/.agents/skills/` serves both Codex and Antigravity.

Copy commands (Claude Code, global). Run them from the folder that contains `seo-aeo-geo`:

Windows PowerShell:
```powershell
Copy-Item -Recurse .\seo-aeo-geo "$env:USERPROFILE\.claude\skills\seo-aeo-geo"
```

macOS / Linux:
```bash
mkdir -p ~/.claude/skills && cp -R ./seo-aeo-geo ~/.claude/skills/
```

For other tools, change the destination path to one from the table. Install paths change between tool versions *(perishable, verified 2026-11)*; if a tool doesn't pick the skill up, check its current docs.

## ChatGPT (custom GPT)

1. ChatGPT → **Explore GPTs → Create → Configure**.
2. **Instructions**: paste everything from `dist/chatgpt-gpt/INSTRUCTIONS.txt` (about 5,000 characters).
3. **Knowledge**: upload every file in `dist/chatgpt-gpt/knowledge/` (18 files; the limit is 20).
4. **Capabilities**: turn on **Web Search** and **Code Interpreter & Data Analysis**.
5. Name it (e.g. "SEO + AEO + GEO") and save it as private.

ChatGPT doesn't keep files between chats, so the GPT prints your Site Profile at the end of each session. Save it and paste it at the start of the next one.

## Other chat AIs (Gemini Gems, Claude Projects, Perplexity Spaces, Copilot Notebooks, etc.)

1. Upload `dist/seo-aeo-geo-ALL.md` as a knowledge/project file.
2. Paste this as the custom instruction:

```
Follow the attached seo-aeo-geo-ALL.md exactly. Start at "Step 0" of SKILL.md:
ask my purpose (SEO / AEO / GEO / all three / one task) and mode, detect the
site profile and get my confirmation before auditing. 00-core-rules is the only
source of thresholds and rules.
```

## Optional scripts (any tool that can run code)

| Script | Needs | Run |
|---|---|---|
| `scripts/aeo-audit.mjs` | Node.js 18+ | `node scripts/aeo-audit.mjs example.com --max-pages=15 --out=aeo-audit.json` (default 10 pages, max 30; polite crawl rate) |
| `scripts/validate_schema.py` | Python 3.8+ (no packages) | `python scripts/validate_schema.py page.html` or `python scripts/validate_schema.py --url https://example.com` |

Nothing else needs installing. The skill uses free Google tools (PageSpeed Insights, Search Console, Rich Results Test) through their websites or public APIs, plus any paid SEO tool you already have (optional).
