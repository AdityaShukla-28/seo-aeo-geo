# Contributing

Thanks for improving the skill. Follow these rules so it stays consistent and works in every AI.

## Ground rules

1. **Numbers and rules live in one place.** Every threshold, score weight, schema rule, AI-crawler rule and guardrail lives in `references/00-core-rules.md`. Other files link to it (`core rules §4`) and never restate the number. If you change a rule, change it only there.
2. **One topic, one owner file.** Before adding content, check which reference file owns the topic (see `docs/modules.md`). Link to it instead of copying it.
3. **Tool-agnostic wording.** Write "fetch the page", "search the web", "if you can run code". Never use one AI product's tool names. Every script or API step needs a manual fallback.
4. **Free first.** Paid SEO tools are optional and named generically ("if a paid SEO data tool is available…").
5. **White-hat only.** Nothing that breaks core rules §8: no fake reviews, undisclosed promotion, self-serving schema, link schemes or cloaking.
6. **Date perishable facts.** Search rules change fast. Tag dated facts *(perishable, verified YYYY-MM)* and add important ones to the register in core rules §10.
7. **Size limits.** Keep each reference file under 20 KB (several are close) and `SKILL.md` under about 500 lines. Split a module before it gets bigger.

## Before you open a pull request

- [ ] No numbers restated outside core rules (search for the old number across the repo).
- [ ] Links point to files and sections that exist.
- [ ] Workspace file names match the layout in `SKILL.md`.
- [ ] CSV columns still match `templates/*.csv` and the modules that define them.
- [ ] Scripts still work:
  `node --check scripts/aeo-audit.mjs`
  `python scripts/validate_schema.py <some.html>`
- [ ] Bundles build: `python tools/build_dist.py` (the ChatGPT pack must stay at 20 files or fewer, and the instructions under 8,000 characters).
- [ ] `CHANGELOG.md` updated, with a version bump (see its header).

## Reporting problems

Open an issue with:
- the AI you used;
- the site type;
- what you asked;
- what the skill did;
- what you expected.

Never paste client data, API keys or Search Console exports with private data.
