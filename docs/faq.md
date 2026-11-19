# FAQ

**What's the difference between SEO, AEO and GEO?**
- **SEO** is ranking in Google and Bing results.
- **AEO** (Answer Engine Optimization) is being the direct answer: featured snippets, "People also ask", voice assistants, and the summary at the top of Google.
- **GEO** (Generative Engine Optimization) is being mentioned and cited by AI assistants such as ChatGPT, Perplexity, Gemini, Claude and Google's AI Mode.

The skill can focus on one or all three.

**Which AI works best with it?**
Tools that can browse, run code and save files get the most out of it: Claude Code, Codex, Antigravity, Gemini CLI. ChatGPT with web search and code interpreter works well but can't remember between chats, so you save the Site Profile it prints. Chat-only AIs still work, using the manual fallbacks.

**Do I need paid SEO tools?**
No. It uses free sources: your site itself, Google Search Console, PageSpeed Insights, Bing Webmaster Tools and web search. If you have DataForSEO, Ahrefs, Semrush, SE Ranking or Moz, it uses them too and labels their numbers.

**Will it change my website on its own?**
No. It always asks first, takes a snapshot, logs every change and checks the result. Without edit access it gives you a fix list instead.

**Why does it say "not measured"?**
It never guesses numbers like search volume, traffic or rankings. If it has no real source, it says so and tells you what access would unlock it (usually Search Console).

**Why does it ask about AI "training bots"?**
AI companies run two kinds of bots. **Search bots** fetch your pages to answer users and cite you, so the skill always recommends allowing them. **Training bots** copy content to train future models. Allowing or blocking those is your business decision, so the skill asks you.

**Does it use llms.txt and FAQ schema?**
- **llms.txt:** low priority, and placed at the site root. Google says it doesn't use it, but some AI tools do; it's more useful for documentation sites.
- **FAQ sections:** recommended, because answer engines like them.
- **FAQPage schema:** optional. Google retired FAQ rich results in 2026.

**How current is the SEO advice?**
Search rules change fast. Dated facts are tagged with when they were verified (see the register in `references/00-core-rules.md` §10). If a fact is older than 6 months and the AI can browse, the skill re-checks it against official documentation before calling it current.

**Is my data private?**
Working files stay in `seo-workspace/<domain>/` on your machine, which is excluded from git by `.gitignore`. Never commit that folder or any API keys. The skill never writes credentials into files.

**Can I use it for client sites?**
Yes. Each site gets its own workspace folder, so client data is never mixed. Check the site owner's permission before running crawls, and only run security-related checks on sites you own or manage.

**What are its limits?**
- Built-in web search isn't a real Google results page, so rankings it observes are labelled approximate.
- AI answers vary by person, place and day, so the AI tracker shows trends rather than exact facts.
- Very large sites (100k+ pages) are sampled, not fully crawled.
- It can't log into your accounts for you.
