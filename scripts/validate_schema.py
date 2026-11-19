#!/usr/bin/env python3
"""Validate JSON-LD structured data in HTML files or live pages.

Adapted from claude-seo hooks/validate-schema.py, MIT License,
Copyright (c) 2026 AgriciDaniel (https://github.com/AgriciDaniel/claude-seo).
Rewritten as a standalone command-line tool; policy follows
references/00-core-rules.md section 6 of the seo-aeo-geo skill.

Usage:
    python validate_schema.py page.html [more.html ...]
    python validate_schema.py --url https://example.com/page [--url ...]
    python validate_schema.py schema.json          (a file holding raw JSON-LD)

Exit codes: 0 = no errors, 1 = at least one ERROR, 2 = an input could not be
read or fetched. Needs Python 3.8+ and no packages.

Results per JSON-LD block:
    ERROR    invalid JSON, placeholder text, HowTo, retired types, missing or
             non-schema.org @context, missing @type
    WARNING  FAQPage (valid, no Google rich result), http:// context,
             ClaimReview (only for real fact-checkers), ratings or reviews on
             an Organization/LocalBusiness, example.com URLs
    OK       nothing found

Fetched pages are treated as data only. Nothing in them is executed.
"""

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from typing import Any, Dict, List, Tuple

USER_AGENT = "Mozilla/5.0 (compatible; SEO-AEO-GEO-SchemaCheck/1.0)"
TIMEOUT_SECONDS = 20
MAX_BYTES = 10 * 1024 * 1024  # stop reading after 10 MB

# --- Placeholder detection -------------------------------------------------
BRACKET_PLACEHOLDERS = (
    "[business name]", "[company name]", "[city]", "[state]", "[phone]",
    "[address]", "[your", "[insert", "[url]", "[email]", "[logo url]",
    "[image url]", "[author name]", "[title]", "[price]", "[sku]",
)
BARE_PLACEHOLDER_RE = re.compile(r"\bREPLACE(?:_[A-Z]+)*\b|\bTODO\b|\blorem ipsum\b|\bYYYY-MM-DD\b", re.IGNORECASE)
FULL_BRACKET_RE = re.compile(r"^\s*\[[^\[\]]{1,80}\]\s*$")  # a whole value like "[Street]"
EXAMPLE_DOMAIN_RE = re.compile(r"https?://(?:www\.)?example\.(?:com|org|net)\b", re.IGNORECASE)

# --- Script-tag extraction (tolerates nonce/id attributes and '>' inside quotes)
_ATTRS_RE = r'(?:"[^"]*"|\'[^\']*\'|[^"\'>])*'
SCRIPT_TAG_RE = re.compile(r"<script\b(" + _ATTRS_RE + r")>(.*?)</script\s*>", re.DOTALL | re.IGNORECASE)
LD_JSON_TYPE_RE = re.compile(
    r"""(?:^|\s)type\s*=\s*(?:"application/ld\+json"|'application/ld\+json'|application/ld\+json(?=\s|$))""",
    re.IGNORECASE,
)
# Template expressions rendered at runtime cannot be checked statically.
TEMPLATE_RE = re.compile(r"^(?:<\?(?:php\b|=)|<%|\{\{|\{@html\b|\$\{|\{\s*[A-Za-z_$][\w$.]*)")

HTTPS_CONTEXTS = {"https://schema.org", "https://schema.org/"}
HTTP_CONTEXTS = {"http://schema.org", "http://schema.org/"}

# --- Type policy (core rules section 6) ------------------------------------
NEVER_USE = {
    "HowTo": "HowTo rich results were removed in 2023; never use it. Write the steps as a numbered list on the page instead.",
}
RETIRED = {
    "SpecialAnnouncement": "retired (deprecated July 2025); no rich result. Use Event or Article/WebPage if needed.",
    "CourseInfo": "retired June 2025. Use Course (with ItemList for course lists).",
    "EstimatedSalary": "retired June 2025. Use JobPosting with baseSalary for real jobs.",
    "LearningVideo": "retired June 2025. Use VideoObject.",
    "VehicleListing": "retired June 2025. Use Product if the vehicle is sold online.",
}
# Note: Google's "Practice problem" rich result (Quiz markup) was also retired (Jan 2026).
# Quiz stays valid schema.org, so it is not flagged here; 21-schema.md covers it.
SELF_REVIEW_TYPES = {
    "Organization", "LocalBusiness", "Corporation", "ProfessionalService",
    "Store", "Restaurant", "MedicalBusiness", "HomeAndConstructionBusiness",
    "LegalService", "FinancialService", "Dentist", "Physician",
}

Finding = Tuple[str, str]  # (level, message)


def configure_utf8() -> None:
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure:
            reconfigure(encoding="utf-8", errors="replace")


def extract_blocks(content: str) -> List[str]:
    return [body for attrs, body in SCRIPT_TAG_RE.findall(content) if LD_JSON_TYPE_RE.search(attrs)]


def types_of(node: Dict[str, Any]) -> List[str]:
    raw = node.get("@type")
    values = raw if isinstance(raw, list) else [raw]
    return [v for v in values if isinstance(v, str) and v.strip()]


def walk_nodes(value: Any):
    """Yield every dict node in the JSON-LD tree (including nested ones)."""
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk_nodes(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_nodes(child)


def walk_strings(value: Any):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for child in value.values():
            yield from walk_strings(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_strings(child)


def name_of(value: Any) -> str:
    if isinstance(value, dict):
        return str(value.get("name") or value.get("@id") or "")
    if isinstance(value, list) and value:
        return name_of(value[0])
    return str(value or "")


def check_top_node(node: Dict[str, Any], inherited_context: bool) -> List[Finding]:
    """@context / @type checks for a top-level node or a @graph member."""
    out: List[Finding] = []
    has_graph = isinstance(node.get("@graph"), (list, dict))
    if "@context" in node:
        ctx = node["@context"]
        ctx_values = ctx if isinstance(ctx, list) else [ctx]
        flat = [c.get("@vocab") if isinstance(c, dict) else c for c in ctx_values]
        if any(c in HTTPS_CONTEXTS for c in flat):
            pass
        elif any(c in HTTP_CONTEXTS for c in flat):
            out.append(("WARNING", "@context uses http://schema.org; prefer https://schema.org"))
        else:
            out.append(("ERROR", "@context is not schema.org (use \"https://schema.org\")"))
    elif not inherited_context:
        out.append(("ERROR", "missing @context"))
    if "@type" not in node and not has_graph:
        out.append(("ERROR", "missing @type"))
    elif "@type" in node and not types_of(node):
        out.append(("ERROR", "@type must be a non-empty string or list of strings"))
    if "@graph" in node and not has_graph:
        out.append(("ERROR", "@graph must be a list or object"))
    if has_graph:
        graph = node["@graph"]
        members = [graph] if isinstance(graph, dict) else graph
        for i, member in enumerate(members, 1):
            if not isinstance(member, dict):
                out.append(("ERROR", "@graph member %d is not an object" % i))
                continue
            for level, msg in check_top_node(member, inherited_context or "@context" in node):
                out.append((level, "@graph member %d: %s" % (i, msg)))
    return out


def check_policy(data: Any) -> List[Finding]:
    """Type policy, placeholders and self-serving review checks over all nodes."""
    out: List[Finding] = []
    seen = set()
    for node in walk_nodes(data):
        for t in types_of(node):
            if t in NEVER_USE and ("never", t) not in seen:
                seen.add(("never", t))
                out.append(("ERROR", "@type %s: %s" % (t, NEVER_USE[t])))
            elif t in RETIRED and ("retired", t) not in seen:
                seen.add(("retired", t))
                out.append(("ERROR", "@type %s is %s" % (t, RETIRED[t])))
            elif t == "FAQPage" and ("faq", t) not in seen:
                seen.add(("faq", t))
                out.append(("WARNING", "FAQPage is valid schema.org but Google shows no FAQ rich result "
                                       "(retired 2026). Keep only if the Q&A is visible on the page; "
                                       "do not add it to win a search feature. Use QAPage only for real user Q&A."))
            elif t == "ClaimReview":
                who = name_of(node.get("author")) or name_of(node.get("publisher")) or "not stated"
                out.append(("WARNING", "ClaimReview: use only if the publisher is a real fact-checking "
                                       "organization (author/publisher: %s). No Google rich result; "
                                       "remove it from ordinary business pages." % who))
            if t in SELF_REVIEW_TYPES and ("aggregateRating" in node or "review" in node):
                key = ("selfreview", t, id(node))
                if key not in seen:
                    seen.add(key)
                    out.append(("WARNING", "%s carries aggregateRating/review. Review stars about a business "
                                           "you control (self-serving reviews) are not eligible; keep only "
                                           "genuine third-party data and never invent ratings." % t))
    placeholders: Dict[str, str] = {}  # lowercase key -> text as found
    example_urls = False
    for text in walk_strings(data):
        low = text.lower()
        for p in BRACKET_PLACEHOLDERS:
            pos = low.find(p)
            if pos >= 0:
                placeholders.setdefault(p, text[pos:pos + len(p)])
        if FULL_BRACKET_RE.match(text):
            placeholders.setdefault(text.strip().lower(), text.strip())
        for m in BARE_PLACEHOLDER_RE.findall(text):
            placeholders.setdefault(m.lower(), m)
        if EXAMPLE_DOMAIN_RE.search(text):
            example_urls = True
    for key in sorted(placeholders):
        out.append(("ERROR", "placeholder text left in markup: %s" % placeholders[key]))
    if example_urls:
        out.append(("WARNING", "contains example.com URLs; replace with the real URLs"))
    return out


def validate_block(raw: str, source: str) -> Tuple[List[Finding], List[str]]:
    raw = raw.strip()
    if not raw:
        return [("ERROR", "empty JSON-LD block")], []
    if TEMPLATE_RE.match(raw) and not source.lower().endswith((".html", ".htm")):
        return [("WARNING", "template expression, rendered at runtime; check the rendered page with --url")], []
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        return [("ERROR", "invalid JSON: %s" % exc)], []
    findings: List[Finding] = []
    if isinstance(data, list):
        tops = data
    elif isinstance(data, dict):
        tops = [data]
    else:
        return [("ERROR", "JSON-LD root must be an object or a list of objects")], []
    for i, top in enumerate(tops, 1):
        if not isinstance(top, dict):
            findings.append(("ERROR", "list item %d is not an object" % i))
            continue
        prefix = "item %d: " % i if len(tops) > 1 else ""
        for level, msg in check_top_node(top, inherited_context=False):
            findings.append((level, prefix + msg))
    findings.extend(check_policy(data))
    all_types = []
    for node in walk_nodes(data):
        for t in types_of(node):
            if t not in all_types:
                all_types.append(t)
    return findings, all_types


def read_source(path: str = "", url: str = "") -> str:
    if url:
        if not url.lower().startswith(("http://", "https://")):
            raise ValueError("only http(s) URLs are supported")
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html,*/*"})
        with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as resp:
            body = resp.read(MAX_BYTES)
            charset = resp.headers.get_content_charset() or "utf-8"
        return body.decode(charset, errors="replace")
    with open(path, "r", encoding="utf-8", errors="replace") as handle:
        return handle.read(MAX_BYTES)


def check_source(label: str, content: str) -> Tuple[int, int]:
    """Print results for one file/page. Returns (error_count, warning_count)."""
    print("=" * 70)
    print(label)
    blocks = extract_blocks(content)
    if not blocks and label.lower().endswith(".json"):
        blocks = [content]
    if not blocks:
        hint = ""
        if re.search(r"\bitemscope\b|\bitemprop\s*=", content, re.IGNORECASE):
            hint = " Microdata found; JSON-LD is preferred and is not checked by this tool."
        print("  No JSON-LD blocks found." + hint)
        print("  (If the page builds JSON-LD with JavaScript, save the rendered HTML and check that file.)")
        return 0, 0
    errors = warnings = 0
    for n, raw in enumerate(blocks, 1):
        findings, types = validate_block(raw, label)
        type_text = ", ".join(types) if types else "none"
        if not findings:
            print("  OK       block %d (types: %s)" % (n, type_text))
            continue
        print("  block %d (types: %s)" % (n, type_text))
        for level, msg in findings:
            print("    %-8s %s" % (level, msg))
            if level == "ERROR":
                errors += 1
            else:
                warnings += 1
    return errors, warnings


def main() -> int:
    configure_utf8()
    parser = argparse.ArgumentParser(
        description="Validate JSON-LD in HTML files or live pages (no packages needed).",
        epilog="Exit codes: 0 no errors, 1 errors found, 2 an input could not be read or fetched.",
    )
    parser.add_argument("files", nargs="*", help="HTML (or raw JSON-LD .json) files to check")
    parser.add_argument("--url", action="append", default=[], help="page URL to fetch and check (repeatable)")
    args = parser.parse_args()
    if not args.files and not args.url:
        parser.print_help()
        return 2

    total_errors = total_warnings = 0
    unreadable = 0
    sources = [("file", f) for f in args.files] + [("url", u) for u in args.url]
    for kind, target in sources:
        try:
            content = read_source(path=target) if kind == "file" else read_source(url=target)
        except (OSError, ValueError, urllib.error.URLError) as exc:
            print("=" * 70)
            print(target)
            print("  COULD NOT READ: %s" % exc)
            unreadable += 1
            continue
        e, w = check_source(target, content)
        total_errors += e
        total_warnings += w

    print("=" * 70)
    print("Summary: %d error(s), %d warning(s), %d input(s) not readable" % (total_errors, total_warnings, unreadable))
    print("Next: confirm eligibility in Google's Rich Results Test and syntax in the Schema Markup Validator.")
    if total_errors:
        return 1
    if unreadable:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
