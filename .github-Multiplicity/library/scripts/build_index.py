#!/usr/bin/env python3
"""
Generate:
  - articles/index.md (master index)
  - tags/index.md
  - tags/<tag-slug>.md

Scans:
  - articles/**/*.md

Front matter (YAML) expected at top of file:
---
title: "..."
status: "draft|review|stable|deprecated"
tags: ["..."]
created: "YYYY-MM-DD"   # recommended
updated: "YYYY-MM-DD"   # recommended
stratum: "S0..S13|S+1"   # recommended per model
operator_class: "axiom|operator|functional|law|protocol|implementation|case-study"
xi_domain: "Lambda|Xi|H_lawful|delta_eth|drift|governance|proof|runtime|other"
csl_role: "glyph|scroll|monad|transformer|resonance-tensor|dictionary-entry|example|none"
---

This file is safe to run locally or in CI.
"""

from __future__ import annotations

import argparse

import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import json

try:
    import yaml
except ImportError:
    print("Missing dependency: pyyaml. Install with: pip install pyyaml", file=sys.stderr)
    sys.exit(1)


FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)

STATUS_ORDER = ["stable", "review", "draft", "deprecated"]
OPCLASS_ORDER = ["axiom", "operator", "functional", "law", "protocol", "implementation", "case-study"]

DEFAULT_EXCLUDE_PATTERNS = [
    r"/_",
    r"/index\.md$",
]


@dataclass
class Article:
    path: Path                 # absolute
    rel_path: Path             # relative to repo root
    title: str
    status: str
    tags: List[str]
    slug: str = ""
    version: str = ""
    created: str = ""
    updated: str = ""
    stratum: str = ""
    operator_class: str = ""
    xi_domain: str = ""
    csl_role: str = ""

    def sort_key(self) -> Tuple:
        # Status first, then operator_class, then stratum, then title
        s_idx = STATUS_ORDER.index(self.status) if self.status in STATUS_ORDER else len(STATUS_ORDER)
        o_idx = OPCLASS_ORDER.index(self.operator_class) if self.operator_class in OPCLASS_ORDER else len(OPCLASS_ORDER)
        # Parse created date if available
        created_dt = _parse_date(self.created) or datetime.min
        # Newer first within same buckets
        return (s_idx, o_idx, self.stratum or "ZZZ", -created_dt.timestamp() if created_dt != datetime.min else 0, self.title.lower())


def _parse_date(s: str) -> Optional[datetime]:
    if not s:
        return None
    try:
        return datetime.strptime(s, "%Y-%m-%d")
    except Exception:
        return None


def _extract_front_matter(text: str) -> Dict[str, Any]:
    m = FRONT_MATTER_RE.match(text)
    if not m:
        return {}
    raw = m.group(1)
    try:
        data = yaml.safe_load(raw) or {}
        if not isinstance(data, dict):
            return {}
        return data
    except Exception:
        return {}


def _slugify_tag(tag: str) -> str:
    # Keep stable filenames across unicode-heavy tags.
    # 1) normalize whitespace
    t = tag.strip().lower()
    # 2) replace common symbolic separators
    t = t.replace("–", "-").replace("—", "-").replace("_", "-")
    # 3) remove anything not alnum, dash, or space
    t = re.sub(r"[^a-z0-9\s\-]+", "", t)
    # 4) collapse whitespace to dash
    t = re.sub(r"\s+", "-", t)
    # 5) collapse multiple dashes
    t = re.sub(r"-{2,}", "-", t).strip("-")
    return t or "tag"


def _slugify(text: str) -> str:
    s = str(text or '').strip().lower()
    s = s.replace("–", "-").replace("—", "-").replace("_", "-")
    s = re.sub(r"[^a-z0-9\-\s]+", "", s)
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    # Ensure pattern: only a-z0-9 and single dashes
    s = re.sub(r"[^a-z0-9\-]", "", s)
    # Truncate to avoid 'File name too long' errors
    return s[:100].strip("-") or "slug"


def _should_exclude(rel_posix: str, extra_patterns: Optional[List[str]] = None) -> bool:
    pats = DEFAULT_EXCLUDE_PATTERNS + (extra_patterns or [])
    return any(re.search(p, rel_posix) for p in pats)


def _rel_link(from_dir: Path, target: Path) -> str:
    # from_dir and target are absolute
    rp = os.path.relpath(target, start=from_dir)
    return rp.replace(os.sep, "/")


def _coerce_list(x: Any) -> List[str]:
    if x is None:
        return []
    if isinstance(x, list):
        return [str(i).strip() for i in x if str(i).strip()]
    if isinstance(x, str):
        # allow comma-separated
        return [s.strip() for s in x.split(",") if s.strip()]
    return [str(x).strip()] if str(x).strip() else []


def load_articles(root: Path, articles_dir: Path, only_files: Optional[List[Path]] = None) -> List[Article]:
    if not articles_dir.exists():
        print(f"Articles directory not found: {articles_dir}", file=sys.stderr)
        return []

    articles: List[Article] = []

    for md in articles_dir.rglob("*.md"):
        rel_path = md.relative_to(root)
        rel_posix = "/" + rel_path.as_posix()

        if _should_exclude(rel_posix):
            continue

        if only_files:
            # only consider files that match the only_files list
            resolved = md.resolve()
            if not any(resolved == of.resolve() for of in only_files):
                continue
        text = md.read_text(encoding="utf-8", errors="ignore")
        fm = _extract_front_matter(text)

        title = str(fm.get("title", "")).strip() or md.stem
        status = str(fm.get("status", "draft")).strip().lower() or "draft"
        tags = _coerce_list(fm.get("tags"))
        created = str(fm.get("created", "")).strip()
        updated = str(fm.get("updated", "")).strip()
        stratum = str(fm.get("stratum", "")).strip()
        operator_class = str(fm.get("operator_class", "")).strip().lower()
        xi_domain = str(fm.get("xi_domain", "")).strip()
        csl_role = str(fm.get("csl_role", "")).strip().lower()
        
        # Truncate slug to avoid 'File name too long' errors
        slug = str(fm.get("slug", "")).strip()
        if not slug:
            slug = _slugify(title or md.stem)
        else:
            # Re-slugify to ensure it's clean and truncated
            slug = _slugify(slug)
            
        version = str(fm.get("version", "")).strip()

        # Minimal normalization
        if status not in STATUS_ORDER:
            status = "draft"
        if operator_class and operator_class not in OPCLASS_ORDER:
            operator_class = ""

        article = Article(
            path=md.resolve(),
            rel_path=rel_path,
            title=title,
            status=status,
            tags=tags,
            slug=slug,
            version=version,
            created=created,
            updated=updated,
            stratum=stratum,
            operator_class=operator_class,
            xi_domain=xi_domain,
            csl_role=csl_role,
        )
        articles.append(article)

    articles.sort(key=lambda a: a.sort_key())
    return articles


def write_master_index(root: Path, articles: List[Article], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    index_dir = out_path.parent.resolve()

    lines: List[str] = []
    lines.append("# Master Index")
    lines.append("")
    lines.append("_Auto-generated. Do not edit by hand._")
    lines.append("")
    lines.append(f"Generated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    total = len(articles)
    by_status = {s: 0 for s in STATUS_ORDER}
    for a in articles:
        by_status[a.status] = by_status.get(a.status, 0) + 1
    lines.append(f"- Total articles: **{total}**")
    for s in STATUS_ORDER:
        lines.append(f"- {s.title()}: **{by_status.get(s, 0)}**")
    lines.append("")

    # Group: status -> operator_class -> stratum
    grouped: Dict[str, Dict[str, Dict[str, List[Article]]]] = {}
    for a in articles:
        oc = a.operator_class or "unspecified"
        st = a.stratum or "unspecified"
        grouped.setdefault(a.status, {}).setdefault(oc, {}).setdefault(st, []).append(a)

    for status in STATUS_ORDER:
        if status not in grouped:
            continue
        lines.append(f"## {status.title()}")
        lines.append("")

        oc_map = grouped[status]
        # Order operator_class buckets
        oc_keys = sorted(
            oc_map.keys(),
            key=lambda k: OPCLASS_ORDER.index(k) if k in OPCLASS_ORDER else 999
        )

        for oc in oc_keys:
            # Make headings unique per status to avoid duplicate heading lint (MD024)
            lines.append(f"### Operator class: {oc} — {status.title()}")
            lines.append("")

            st_map = oc_map[oc]
            st_keys = sorted(st_map.keys())

            for st in st_keys:
                lines.append(f"#### Stratum: {st}")
                lines.append("")
                for a in st_map[st]:
                    link = _rel_link(index_dir, a.path)
                    meta_bits = []
                    if a.created:
                        meta_bits.append(f"created {a.created}")
                    if a.xi_domain:
                        meta_bits.append(f"Ξ-domain {a.xi_domain}")
                    if a.csl_role and a.csl_role != "none":
                        meta_bits.append(f"CSL {a.csl_role}")
                    meta = f" — _{', '.join(meta_bits)}_" if meta_bits else ""
                    lines.append(f"- [{a.title}]({link}){meta}")
                lines.append("")

    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_tag_pages(root: Path, articles: List[Article], tags_dir: Path) -> None:
    tags_dir.mkdir(parents=True, exist_ok=True)

    # Build tag -> articles
    tag_map: Dict[str, List[Article]] = {}
    display_name: Dict[str, str] = {}

    for a in articles:
        for t in a.tags:
            if not t:
                continue
            slug = _slugify_tag(t)
            tag_map.setdefault(slug, []).append(a)
            # Keep first observed display name (stable)
            display_name.setdefault(slug, t.strip())

    # tag index
    tag_index_lines: List[str] = []
    tag_index_lines.append("# Tags")
    tag_index_lines.append("")
    tag_index_lines.append("_Auto-generated. Do not edit by hand._")
    tag_index_lines.append("")
    tag_index_lines.append(f"Generated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}")
    tag_index_lines.append("")

    # Sort tags by display name
    items = sorted(tag_map.items(), key=lambda kv: display_name.get(kv[0], kv[0]).lower())

    for slug, arts in items:
        name = display_name.get(slug, slug)
        tag_page = tags_dir / f"{slug}.md"
        link = f"./{tag_page.name}"
        tag_index_lines.append(f"- [{name}]({link}) — **{len(arts)}**")

    (tags_dir / "index.md").write_text("\n".join(tag_index_lines).rstrip() + "\n", encoding="utf-8")

    # individual tag pages
    for slug, arts in items:
        name = display_name.get(slug, slug)
        tag_page = tags_dir / f"{slug}.md"
        page_dir = tag_page.parent.resolve()

        lines: List[str] = []
        lines.append(f"# Tag: {name}")
        lines.append("")
        lines.append("_Auto-generated. Do not edit by hand._")
        lines.append("")
        lines.append(f"Articles: **{len(arts)}**")
        lines.append("")

        # Sort within tag by status + date
        sorted_arts = sorted(arts, key=lambda a: a.sort_key())

        # Group by status for readability
        s_bucket: Dict[str, List[Article]] = {s: [] for s in STATUS_ORDER}
        for a in sorted_arts:
            s_bucket.setdefault(a.status, []).append(a)

        for status in STATUS_ORDER:
            bucket = s_bucket.get(status, [])
            if not bucket:
                continue
            lines.append(f"## {status.title()}")
            lines.append("")
            for a in bucket:
                link = _rel_link(page_dir, a.path)
                bits = []
                if a.stratum:
                    bits.append(f"stratum {a.stratum}")
                if a.operator_class:
                    bits.append(a.operator_class)
                if a.created:
                    bits.append(a.created)
                meta = f" — _{', '.join(bits)}_" if bits else ""
                lines.append(f"- [{a.title}]({link}){meta}")
            lines.append("")

        tag_page.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_tag_pages_json(root: Path, articles: List[Article], tags_dir: Path, minify: bool = False) -> None:
    import json
    tags_dir.mkdir(parents=True, exist_ok=True)
    # Build tag -> articles
    tag_map: Dict[str, List[Article]] = {}
    display_name: Dict[str, str] = {}
    for a in articles:
        for t in a.tags:
            if not t:
                continue
            slug = _slugify_tag(t)
            tag_map.setdefault(slug, []).append(a)
            display_name.setdefault(slug, t.strip())

    # Write tags/index.json
    index_data = {
        "generated": datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC'),
        "tags": [ {"slug": slug, "name": display_name.get(slug, slug), "count": len(arts)} for slug, arts in sorted(tag_map.items(), key=lambda kv: display_name.get(kv[0], kv[0]).lower()) ],
    }
    (tags_dir / 'index.json').write_text(json.dumps(index_data, ensure_ascii=False, indent=2) + "\n", encoding='utf-8')
    if minify:
        (tags_dir / 'index.min.json').write_text(json.dumps(index_data, ensure_ascii=False, separators=(",", ":")) + "\n", encoding='utf-8')

    # Individual tag JSON
    for slug, arts in tag_map.items():
        name = display_name.get(slug, slug)
        data = {
            "generated": datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC'),
            "slug": slug,
            "name": name,
            "articles": [ _article_to_dict(a) for a in sorted(arts, key=lambda a: a.sort_key()) ],
        }
        (tags_dir / f"{slug}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding='utf-8')
        if minify:
            (tags_dir / f"{slug}.min.json").write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n", encoding='utf-8')


def _article_to_dict(a: Article) -> Dict[str, Any]:
    return {
        "slug": a.slug,
        "path": a.rel_path.as_posix(),
        "title": a.title,
        "status": a.status,
        "version": a.version,
        "tags": a.tags,
        "created": a.created,
        "updated": a.updated,
        "stratum": a.stratum,
        "operator_class": a.operator_class,
        "xi_domain": a.xi_domain,
        "csl_role": a.csl_role,
    }


def write_master_index_json(root: Path, articles: List[Article], out_path: Path, minify: bool = False) -> None:
    import json
    out_path.parent.mkdir(parents=True, exist_ok=True)
    data = {
        "generated": datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC'),
        "total": len(articles),
        "articles": [ _article_to_dict(a) for a in articles ],
    }
    out_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if minify:
        out_path_min = out_path.with_name(out_path.stem + ".min.json")
        out_path_min.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")


def write_repo_index_json(root: Path, articles: List[Article], out_path: Path, version: str = "1", minify: bool = False) -> None:
    import json
    out_path.parent.mkdir(parents=True, exist_ok=True)
    data = {
        "generated_utc": datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
        "version": str(version),
        "articles": [ _article_to_dict(a) for a in articles ],
    }
    out_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if minify:
        out_path_min = out_path.with_name(out_path.stem + ".min.json")
        out_path_min.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    # nothing else: function finishes here


def main() -> int:
    p = argparse.ArgumentParser(description='Build master index and tags')
    p.add_argument('--paths-file', help='Write list of processed markdown files (newline separated)')
    p.add_argument('--only', help='Comma-separated list of files to process (overrides scanning)')
    p.add_argument('--no-json', action='store_true', help='Do not write JSON outputs (articles/index.json, tags/index.json, index.json)')
    p.add_argument('--minify', action='store_true', help='Also write minified index.min.json files')
    args = p.parse_args()

    root = Path(__file__).resolve().parents[1]
    articles_dir = root / "articles"
    tags_dir = root / "tags"
    master_index = root / "articles" / "index.md"

    only_files = None
    if args.only:
        only_files = [Path(str(root / f.strip())) if not Path(f.strip()).is_absolute() else Path(f.strip()) for f in args.only.split(',') if f.strip()]
    articles = load_articles(root, articles_dir, only_files)
    if not articles:
        # Still create empty scaffolds to keep MkDocs nav stable
        tags_dir.mkdir(parents=True, exist_ok=True)
        (tags_dir / "index.md").write_text("# Tags\n\n_No articles found._\n", encoding="utf-8")
        master_index.parent.mkdir(parents=True, exist_ok=True)
        master_index.write_text("# Master Index\n\n_No articles found._\n", encoding="utf-8")
        # Also write machine-readable empty JSON
        write_master_index_json(root, [], root / 'articles' / 'index.json')
        (tags_dir / 'index.json').write_text('{"generated":"" , "tags": []}\n', encoding='utf-8')
        return 0

    write_master_index(root, articles, master_index)
    # Also write machine readable article index
    write_master_index_json(root, articles, root / 'articles' / 'index.json', minify=args.minify)
    write_tag_pages(root, articles, tags_dir)
    # Also write tag JSON: tags/index.json and individual tag JSON files
    write_tag_pages_json(root, articles, tags_dir, minify=args.minify)

    # Write repository root index.json
    if not args.no_json:
        write_repo_index_json(root, articles, root / 'index.json', version="1", minify=args.minify)
        # Also write docs/index.json (create docs dir if needed)
        docs_dir = root / 'docs'
        docs_dir.mkdir(parents=True, exist_ok=True)
        write_repo_index_json(root, articles, docs_dir / 'index.json', version="1", minify=args.minify)
        if args.minify:
            # also ensure minified root index.json written
            pass
        # Write per-article JSON files to articles/<slug>.json
        articles_dir = root / 'articles'
        for a in articles:
            # Use slug if present, otherwise derive
            fname = a.slug or _slugify(a.title or Path(a.path).stem)
            per_file = articles_dir / f"{fname}.json"
            per_file.write_text(json.dumps(_article_to_dict(a), ensure_ascii=False, indent=2) + "\n", encoding='utf-8')
            if args.minify:
                per_file.with_name(per_file.stem + ".min.json").write_text(json.dumps(_article_to_dict(a), ensure_ascii=False, separators=(",", ":")) + "\n", encoding='utf-8')
        # Write docs index wrapper (human-friendly) summarizing repo index and link
        docs_md = docs_dir / 'index.md'
        # Render a Markdown table with relevant metadata for human readers
        lines = [
            "# Library Index (Machine-Readable)",
            "",
            "This file is auto-generated and linked to the full machine-readable `index.json`.",
            "",
            f"Generated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}",
            "",
            "## Summary",
            "",
            f"- Total articles: **{len(articles)}**",
            "",
            "## Articles",
            "",
            "| Title | Status | Tags | Stratum | Operator class | Ξ-domain | CSL role | Version | Created | Updated | Path |",
            "|---|---|---|---|---|---|---|---|---|---|---|",
        ]
        for a in articles:
            safe_title = a.title.replace('|', '\\|')
            safe_tags = ', '.join([t.replace('|', '\\|') for t in a.tags])
            row = [
                safe_title,
                a.status,
                safe_tags,
                a.stratum or '',
                a.operator_class or '',
                a.xi_domain or '',
                a.csl_role or '',
                a.version or '',
                a.created or '',
                a.updated or '',
                a.rel_path.as_posix(),
            ]
            lines.append("| " + " | ".join(row) + " |")
        docs_md.write_text("\n".join(lines).rstrip() + "\n", encoding='utf-8')

    if args.paths_file:
        pf = Path(args.paths_file)
        pf.parent.mkdir(parents=True, exist_ok=True)
        with pf.open('w', encoding='utf-8') as out:
            for a in articles:
                out.write(a.rel_path.as_posix() + "\n")

    print(f"Wrote master index: {master_index.relative_to(root)}")
    print(f"Wrote tags index:   {(tags_dir / 'index.md').relative_to(root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
