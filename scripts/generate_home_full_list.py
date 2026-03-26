#!/usr/bin/env python3

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"


FILE_CONFIGS = [
    {
        "path": "paradigms/README.md",
        "summary": "Paradigms",
        "summary_link": "paradigms/README.md",
        "skip_headings": {"Where the Evidence Lives"},
    },
    {
        "path": "methods/layer-1-intrinsic-cues.md",
        "summary": "Layer 1: Intrinsic Visual Cues",
        "summary_link": "methods/layer-1-intrinsic-cues.md",
        "skip_headings": {"Subcategory Guide"},
    },
    {
        "path": "methods/layer-2-spatiotemporal.md",
        "summary": "Layer 2: Spatiotemporal Consistency",
        "summary_link": "methods/layer-2-spatiotemporal.md",
        "skip_headings": {"Subcategory Guide"},
    },
    {
        "path": "methods/layer-3-cross-modal.md",
        "summary": "Layer 3: Cross-Modal Consistency",
        "summary_link": "methods/layer-3-cross-modal.md",
        "skip_headings": {"Subcategory Guide"},
    },
    {
        "path": "methods/layer-4-world-level-reasoning.md",
        "summary": "Layer 4: World-Level Reasoning",
        "summary_link": "methods/layer-4-world-level-reasoning.md",
        "skip_headings": {"Subcategory Guide"},
    },
    {
        "path": "benchmarks/local-manipulation-video.md",
        "summary": "Benchmarks: Local Manipulation Video",
        "summary_link": "benchmarks/local-manipulation-video.md",
        "skip_headings": set(),
    },
    {
        "path": "benchmarks/audio-visual-editing.md",
        "summary": "Benchmarks: Audio-Visual Editing",
        "summary_link": "benchmarks/audio-visual-editing.md",
        "skip_headings": set(),
    },
    {
        "path": "benchmarks/generative-video-synthesis.md",
        "summary": "Benchmarks: Generative Video Synthesis",
        "summary_link": "benchmarks/generative-video-synthesis.md",
        "skip_headings": set(),
    },
    {
        "path": "benchmarks/adjacent-diagnostics.md",
        "summary": "Benchmarks: Adjacent Diagnostics",
        "summary_link": "benchmarks/adjacent-diagnostics.md",
        "skip_headings": set(),
    },
]


FULL_LIST_START = "<!-- full-list:start -->"
FULL_LIST_END = "<!-- full-list:end -->"

HEADING_RE = re.compile(r"^## (.+)$")
TABLE_ROW_RE = re.compile(r"^\| ")
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


@dataclass
class Entry:
    date: str
    title: str
    url: str


@dataclass
class Subsection:
    title: str
    link: str
    entries: list[Entry] = field(default_factory=list)


@dataclass
class Section:
    summary: str
    summary_link: str
    subsections: list[Subsection] = field(default_factory=list)


def slugify(heading: str) -> str:
    slug = heading.strip().lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"\s+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    return slug


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("&nbsp;", " ")).strip()


def pair_links_and_dates(link_pairs: list[tuple[str, str]], date_cell: str) -> list[Entry]:
    date = normalize_text(date_cell)
    return [Entry(date=date, title=normalize_text(title), url=url.strip()) for title, url in link_pairs]


def extract_table_entries(lines: list[str], path: str, default_title: str, skip_headings: set[str]) -> Section:
    section = Section(summary="", summary_link=path)
    current_heading = default_title
    current_subsection: Subsection | None = None
    idx = 0

    def ensure_subsection(title: str | None, link: str) -> Subsection:
        nonlocal current_subsection
        if current_subsection and current_subsection.title == title:
            return current_subsection
        current_subsection = Subsection(title=title or default_title, link=link)
        section.subsections.append(current_subsection)
        return current_subsection

    while idx < len(lines):
        line = lines[idx]

        heading_match = HEADING_RE.match(line)
        if heading_match:
            heading = heading_match.group(1).strip()
            if heading in skip_headings:
                current_heading = default_title
                current_subsection = None
            else:
                current_heading = heading
                current_subsection = None
            idx += 1
            continue

        if TABLE_ROW_RE.match(line):
            header_cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            idx += 1
            if idx >= len(lines) or not TABLE_ROW_RE.match(lines[idx]):
                continue
            separator = lines[idx]
            if "---" not in separator:
                continue
            idx += 1

            try:
                date_idx = header_cells.index("Date")
                paper_idx = header_cells.index("Paper")
            except ValueError:
                while idx < len(lines) and TABLE_ROW_RE.match(lines[idx]):
                    idx += 1
                continue

            subsection_title = current_heading
            subsection_link = f"{path}#{slugify(current_heading)}" if current_heading != default_title else path
            subsection = ensure_subsection(subsection_title, subsection_link)

            while idx < len(lines) and TABLE_ROW_RE.match(lines[idx]):
                row = lines[idx]
                idx += 1
                cells = [cell.strip() for cell in row.strip().strip("|").split("|")]
                if len(cells) <= max(date_idx, paper_idx):
                    continue
                link_pairs = LINK_RE.findall(cells[paper_idx])
                if not link_pairs:
                    continue
                subsection.entries.extend(pair_links_and_dates(link_pairs, cells[date_idx]))
            continue

        idx += 1

    return section


def build_section(config: dict[str, object]) -> Section:
    path = config["path"]
    file_path = ROOT / str(path)
    lines = file_path.read_text().splitlines()
    default_title = lines[0].removeprefix("# ").strip()
    section = extract_table_entries(
        lines=lines,
        path=str(path),
        default_title=default_title,
        skip_headings=set(config["skip_headings"]),
    )
    section.summary = str(config["summary"])
    section.summary_link = str(config["summary_link"])
    return section


def ensure_terminal_punctuation(title: str) -> str:
    if title.endswith((".", "?", "!")):
        return title
    return f"{title}."


def render_section(section: Section) -> str:
    lines = [f"### [{section.summary}]({section.summary_link})", ""]
    for subsection in section.subsections:
        if subsection.title != section.summary:
            lines.append(f"#### [{subsection.title}]({subsection.link})")
        for entry in subsection.entries:
            lines.append(
                f'- [{entry.date}] {ensure_terminal_punctuation(entry.title)} <a href="{entry.url}">[paper]</a>'
            )
        lines.append("")
    return "\n".join(lines).rstrip()


def render_full_list(sections: list[Section]) -> str:
    parts = [
        "## 📚 Paper List",
        "",
        "A flat, paper-first index in the same style as the reference list. Detailed notes and extra metadata stay on the linked section pages.",
        "",
        FULL_LIST_START,
    ]
    for section in sections:
        parts.append(render_section(section))
        parts.append("")
    parts.append(FULL_LIST_END)
    return "\n".join(parts).rstrip() + "\n"


def replace_full_list(readme_text: str, rendered: str) -> str:
    if FULL_LIST_START in readme_text and FULL_LIST_END in readme_text:
        first_start = readme_text.find(FULL_LIST_START)
        last_end = readme_text.rfind(FULL_LIST_END) + len(FULL_LIST_END)
        heading_start = readme_text.rfind("\n## ", 0, first_start)
        if heading_start == -1:
            heading_start = 0
        else:
            heading_start += 1
        while last_end < len(readme_text) and readme_text[last_end] == "\n":
            last_end += 1
        readme_text = readme_text[:heading_start] + readme_text[last_end:]

    return readme_text.rstrip() + "\n\n" + rendered


def main() -> None:
    sections = [build_section(config) for config in FILE_CONFIGS]
    rendered = render_full_list(sections)
    readme_text = README.read_text()
    README.write_text(replace_full_list(readme_text, rendered))


if __name__ == "__main__":
    main()
