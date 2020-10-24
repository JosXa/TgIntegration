from pathlib import Path
from typing import Callable

root_path = Path(__file__).parent.parent
docs_folder = root_path / "docs"

METADATA_HEADER = (
    """<!-- Autogenerated from README.md in the repository root. -->\n\n"""
)

readme_source = root_path / "README.md"

doc = readme_source.read_text(encoding="utf-8")


def copy_readme_sections_to_docs():
    copy_section(
        "Quick Start Guide\n---",
        "Integrating with Test Frameworks\n---",
        new_header="# Getting Started",
        out_file=docs_folder / "getting-started.md",
    )
    copy_section(
        "Prerequisites\n---",
        "Installation\n---",
        new_header="## Prerequisites",
        out_file=docs_folder / "prerequisites.md",
    )
    copy_section(
        "Installation\n---",
        "Quick Start Guide\n---",
        new_header="## Installation",
        out_file=docs_folder / "installation.md",
        formatter=lambda doc: doc.replace("<br />", "").replace(
            "$ `pip install git+https://github.com/JosXa/tgintegration.git`",
            "<pre>pip install git+https://github.com/JosXa/tgintegration.git</pre>",
        ),
    )


def copy_section(
    section_part: str,
    end: str,
    new_header: str,
    out_file: Path,
    formatter: Callable = None,
) -> None:
    content = _get_md_doc_section(section_part, end, new_header)

    if formatter:
        content = formatter(content)

    out_file.write_text(content, encoding="utf-8")


def _get_md_doc_section(section_part: str, end: str, new_header: str) -> str:
    _, after = doc.split(section_part)
    result, _ = after.split(end)
    result = result.lstrip("-\n").rstrip("-\n")
    return f"{METADATA_HEADER}{new_header}\n\n{result}"


if __name__ == "__main__":
    copy_readme_sections_to_docs()
