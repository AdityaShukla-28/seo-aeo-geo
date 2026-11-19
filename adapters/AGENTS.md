# AGENTS.md snippet: SEO / AEO / GEO

Paste this section into a project's `AGENTS.md` (read by Codex, Cursor, Gemini CLI, Antigravity, Jules, Aider and others), or keep it as a separate file in the repo root.

---

## SEO, AEO and GEO work

For any task about search visibility (SEO audits, meta tags, schema/structured data, sitemaps, robots.txt, AI crawlers, llms.txt, Core Web Vitals, keyword or AI-prompt research, content briefs or writing, backlinks, local SEO, e-commerce SEO, hreflang, Search Console, AI visibility in ChatGPT/Perplexity/Gemini/AI Overviews):

1. Read `.agents/skills/seo-aeo-geo/SKILL.md` first and follow its steps in order. If the skill is installed elsewhere, use that path instead.
2. Treat `references/00-core-rules.md` as the only source of thresholds and rules.
3. Open other reference files only when the current step needs them.
4. Ask the user before changing anything that ships to production. Follow the safe-change protocol in `references/03-platforms.md`.
5. Keep per-site working files in `seo-workspace/<domain>/`. Never commit API keys or credentials.
