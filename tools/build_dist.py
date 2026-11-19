#!/usr/bin/env python3
"""Build shareable bundles of the seo-aeo-geo skill (stdlib only, any OS).

Usage:  python tools/build_dist.py [--out DIR]
Default output: a "dist" folder next to the skill folder.

Creates:
  seo-aeo-geo.zip        Agent Skills zip (claude.ai upload, any skills tool)
  chatgpt-gpt/           INSTRUCTIONS.txt + knowledge/ (<= 20 files) for a custom GPT
  seo-aeo-geo-ALL.md     the whole skill in one file for any chat AI
"""
import argparse
import shutil
import sys
import zipfile
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
NAME = SKILL.name

GPT_GROUPS = {
    "00-core-rules.md": ["00-core-rules.md"],
    "01-02-intake-and-site-types.md": ["01-intake-and-detection.md", "02-site-types.md"],
    "03-platforms.md": ["03-platforms.md"],
    "10-11-brand-and-demand-research.md": ["10-brand-and-entity.md", "11-demand-research.md"],
    "12-13-intent-and-strategy.md": ["12-search-intent.md", "13-strategy-and-plan.md"],
    "20-technical-audit.md": ["20-technical-audit.md"],
    "21-schema.md": ["21-schema.md"],
    "22-ai-search-readiness.md": ["22-ai-search-readiness.md"],
    "30-content-creation.md": ["30-content-creation.md"],
    "31-32-33-visuals-factcheck-publishing.md": ["31-visuals.md", "32-fact-check.md", "33-publishing-in-code.md"],
    "40-links-and-mentions.md": ["40-links-and-mentions.md"],
    "50-local.md": ["50-local.md"],
    "51-ecommerce.md": ["51-ecommerce.md"],
    "52-international.md": ["52-international.md"],
    "60-measurement.md": ["60-measurement.md"],
}
ROUTER_NOTE = (
    "NOTE FOR THIS GPT: reference files are merged. Module NN lives in the knowledge file whose "
    "name contains NN (e.g. 10 and 11 are in 10-11-brand-and-demand-research.md). Scripts that need "
    "internet are not available here; use the manual fallbacks.\n\n"
)


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def join(paths) -> str:
    parts = []
    for p in paths:
        if not p.exists():
            print("warning: missing", p, file=sys.stderr)
            continue
        rel = p.relative_to(SKILL).as_posix()
        parts.append(f"\n<!-- ===== FILE: {rel} ===== -->\n\n{read(p)}\n")
    return "".join(parts)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(SKILL.parent / "dist"))
    out = Path(ap.parse_args().out).resolve()
    if not (SKILL / "SKILL.md").exists():
        sys.exit("SKILL.md not found next to tools/")
    if out == SKILL or SKILL in out.parents:
        sys.exit("--out must be outside the skill folder")
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)

    # 1. Agent Skills zip: top folder = skill name, forward slashes.
    skip_dirs = {"__pycache__", ".git", ".github", "seo-workspace", "node_modules"}
    files = sorted(
        p for p in SKILL.rglob("*")
        if p.is_file()
        and not skip_dirs.intersection(p.relative_to(SKILL).parts)
        and not p.name.startswith(".")
    )
    with zipfile.ZipFile(out / f"{NAME}.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for p in files:
            z.write(p, f"{NAME}/{p.relative_to(SKILL).as_posix()}")

    # 2. ChatGPT custom GPT bundle.
    gpt = out / "chatgpt-gpt"
    kn = gpt / "knowledge"
    kn.mkdir(parents=True)
    shutil.copy(SKILL / "adapters" / "chatgpt-gpt-instructions.md", gpt / "INSTRUCTIONS.txt")
    (kn / f"{NAME}-ROUTER.md").write_text(ROUTER_NOTE + read(SKILL / "SKILL.md"), encoding="utf-8")
    refs = SKILL / "references"
    for name, members in GPT_GROUPS.items():
        (kn / name).write_text(join(refs / m for m in members), encoding="utf-8")
    templates = sorted((SKILL / "templates").iterdir())
    (kn / "templates-all.md").write_text("# All templates\n" + join(templates), encoding="utf-8")
    shutil.copy(SKILL / "scripts" / "validate_schema.py", kn / "validate_schema.py")
    count = len(list(kn.iterdir()))
    if count > 20:
        sys.exit(f"ChatGPT knowledge has {count} files (limit 20)")

    # 3. Single-file bundle.
    everything = [SKILL / "SKILL.md"] + sorted(refs.iterdir()) + templates
    (out / f"{NAME}-ALL.md").write_text(f"# {NAME}: complete skill in one file\n" + join(everything), encoding="utf-8")

    instr = len(read(gpt / "INSTRUCTIONS.txt"))
    for p in sorted(out.rglob("*")):
        if p.is_file():
            print(f"{p.relative_to(out).as_posix():60} {p.stat().st_size / 1024:8.0f} KB")
    print(f"GPT instructions: {instr} chars (limit 8000); knowledge files: {count} (limit 20)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
