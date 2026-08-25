#!/usr/bin/env python3
"""
Build the downloadable PDFs from source.

  python3 scripts/build-pdf.py

Outputs:
  public/downloads/bc-owners-handbook.pdf   <- src/content/guides/bc-owners-handbook.md
  public/downloads/erskine-referral-kit.pdf <- docs/referral-kit.md

Requires: pandoc, and `pip install weasyprint`.
The handbook PDF is generated from the markdown source — edit the markdown and
rebuild rather than editing the PDF.
"""

import re
import subprocess
import sys
from pathlib import Path

from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

ROOT = Path(__file__).resolve().parent.parent
FONTS = ROOT / "public" / "fonts"
OUT = ROOT / "public" / "downloads"

PAPER = "#f7f5f1"
INK = "#16181a"
MID = "#6e6e6e"
RULE = "#cfcac2"
ACCENT = "#1f4e46"

FONT_FACES = f"""
@font-face {{
  font-family: 'Inter';
  src: url('file://{FONTS}/inter-var.woff2') format('woff2');
  font-weight: 100 900;
}}
@font-face {{
  font-family: 'Inter Tight';
  src: url('file://{FONTS}/inter-tight-var.woff2') format('woff2');
  font-weight: 100 900;
}}
@font-face {{
  font-family: 'JetBrains Mono';
  src: url('file://{FONTS}/jetbrains-mono-var.woff2') format('woff2');
  font-weight: 100 800;
}}
"""

BASE_CSS = f"""
{FONT_FACES}

@page {{
  size: A4;
  margin: 22mm 20mm 20mm 20mm;
  @bottom-left {{
    content: "Erskine Advisory";
    font-family: 'JetBrains Mono', monospace;
    font-size: 7pt;
    letter-spacing: 0.06em;
    color: {MID};
  }}
  @bottom-center {{
    content: "Not legal advice — consult a BC construction lawyer on your project";
    font-family: 'JetBrains Mono', monospace;
    font-size: 7pt;
    color: {MID};
  }}
  @bottom-right {{
    content: counter(page);
    font-family: 'JetBrains Mono', monospace;
    font-size: 7pt;
    color: {MID};
  }}
}}
@page cover {{
  margin: 0;
  background: {PAPER};
  @bottom-left {{ content: none; }}
  @bottom-center {{ content: none; }}
  @bottom-right {{ content: none; }}
}}

html {{ font-size: 10.5pt; }}
body {{
  font-family: 'Inter', sans-serif;
  color: {INK};
  line-height: 1.55;
}}

.cover {{
  page: cover;
  break-after: page;
  padding: 46mm 20mm 20mm 20mm;
  height: 100%;
  box-sizing: border-box;
}}
.cover .kicker {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 8pt;
  text-transform: uppercase;
  letter-spacing: 0.18em;
  color: {ACCENT};
}}
.cover h1 {{
  font-family: 'Inter Tight', sans-serif;
  font-size: 32pt;
  font-weight: 600;
  line-height: 1.08;
  letter-spacing: -0.02em;
  margin: 9mm 0 0 0;
  max-width: 130mm;
  border: 0;
  padding: 0;
  break-before: auto;
}}
.cover .sub {{
  font-size: 12pt;
  color: {MID};
  margin-top: 7mm;
  max-width: 118mm;
  line-height: 1.5;
}}
.cover .rule {{
  border-top: 1.5pt solid {ACCENT};
  width: 34mm;
  margin: 12mm 0;
}}
.cover .meta {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 8pt;
  color: {MID};
  line-height: 1.9;
  margin-top: 10mm;
}}
.cover .foot {{
  position: absolute;
  bottom: 20mm;
  left: 20mm;
  right: 20mm;
  font-size: 8.5pt;
  color: {MID};
  border-top: 0.5pt solid {RULE};
  padding-top: 4mm;
  max-width: 130mm;
}}

nav#TOC {{ break-after: page; }}
nav#TOC h1, nav#TOC h2 {{
  font-family: 'Inter Tight', sans-serif;
  font-size: 16pt;
  margin: 0 0 6mm 0;
  padding: 0;
  border: 0;
  break-before: auto;
}}
nav#TOC ul {{ list-style: none; padding: 0; margin: 0; }}
nav#TOC li {{ margin: 0; }}
nav#TOC ul ul {{ display: none; }}
nav#TOC > ul > li > a {{
  display: block;
  border-top: 0.5pt solid {RULE};
  padding: 2.6mm 0;
  font-size: 10.5pt;
  color: {INK};
  text-decoration: none;
}}

/* Chapters are level-2 headings in the markdown source. */
h2 {{
  font-family: 'Inter Tight', sans-serif;
  font-size: 18pt;
  font-weight: 600;
  letter-spacing: -0.015em;
  line-height: 1.15;
  margin: 0 0 6mm 0;
  padding-top: 4mm;
  border-top: 1.5pt solid {ACCENT};
  break-before: page;
  break-after: avoid;
}}
h3 {{
  font-family: 'Inter Tight', sans-serif;
  font-size: 12pt;
  font-weight: 600;
  margin: 7mm 0 2.5mm 0;
  break-after: avoid;
}}
h4 {{
  font-family: 'Inter Tight', sans-serif;
  font-size: 10.5pt;
  font-weight: 600;
  margin: 5mm 0 1.5mm 0;
  break-after: avoid;
}}
p {{ margin: 0 0 3.2mm 0; }}
p, li {{ orphans: 2; widows: 2; }}
strong {{ font-weight: 600; }}
em {{ font-style: italic; color: {INK}; }}
a {{ color: {ACCENT}; text-decoration: none; }}

ul, ol {{ margin: 0 0 3.5mm 0; padding-left: 5mm; }}
li {{ margin-bottom: 1.4mm; }}

blockquote {{
  margin: 4mm 0;
  padding-left: 5mm;
  border-left: 1.5pt solid {ACCENT};
  color: {MID};
  font-style: italic;
}}

hr {{
  border: 0;
  border-top: 0.5pt solid {RULE};
  margin: 7mm 0;
}}

table {{
  width: 100%;
  border-collapse: collapse;
  font-size: 9pt;
  margin: 4mm 0 5mm 0;
  break-inside: avoid;
}}
th {{
  text-align: left;
  font-family: 'JetBrains Mono', monospace;
  font-size: 7.5pt;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: {MID};
  font-weight: 500;
  border-bottom: 1pt solid {ACCENT};
  padding: 2mm 3mm 2mm 0;
}}
td {{
  border-bottom: 0.5pt solid {RULE};
  padding: 2.2mm 3mm 2.2mm 0;
  vertical-align: top;
}}

code {{ font-family: 'JetBrains Mono', monospace; font-size: 9pt; }}
"""


# One-pager: no chapter breaks, no legal-advice footer, tighter measure.
KIT_CSS = f"""
{FONT_FACES}

@page {{
  size: A4;
  margin: 14mm 15mm 12mm 15mm;
  background: {PAPER};
}}

html {{ font-size: 8.4pt; }}
body {{
  font-family: 'Inter', sans-serif;
  color: {INK};
  line-height: 1.45;
}}

h1 {{
  font-family: 'Inter Tight', sans-serif;
  font-size: 20pt;
  font-weight: 600;
  letter-spacing: -0.02em;
  margin: 0 0 2mm 0;
}}
h1 + p {{
  font-size: 11pt;
  color: {ACCENT};
  margin: 0 0 4mm 0;
}}
h2 {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 7.5pt;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: {ACCENT};
  margin: 4mm 0 1.5mm 0;
  break-after: avoid;
}}
p {{ margin: 0 0 1.9mm 0; }}
strong {{ font-weight: 600; }}
em {{ font-style: italic; }}
a {{ color: {ACCENT}; text-decoration: none; }}
ul {{ margin: 0 0 2.2mm 0; padding-left: 4mm; }}
li {{ margin-bottom: 1mm; }}
hr {{
  border: 0;
  border-top: 0.75pt solid {ACCENT};
  margin: 3mm 0;
}}
"""


def md_to_html(md_path: Path, toc: bool) -> str:
    cmd = ["pandoc", str(md_path), "-f", "markdown+pipe_tables", "-t", "html5"]
    tpl_path = None
    if toc:
        tpl_path = md_path.parent / ".pandoc-tpl.html"
        tpl_path.write_text(
            '<nav id="TOC"><h2 class="toc-title">Contents</h2>\n'
            "$table-of-contents$\n</nav>\n$body$\n"
        )
        cmd += ["--toc", "--toc-depth=2", "--standalone", "--template", str(tpl_path)]
    try:
        return subprocess.run(cmd, capture_output=True, text=True, check=True).stdout
    finally:
        if tpl_path is not None:
            tpl_path.unlink(missing_ok=True)


def strip_frontmatter(text: str) -> str:
    return re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)


def build(md_path: Path, out_path: Path, cover: str, toc: bool, css: str = None) -> None:
    src = strip_frontmatter(md_path.read_text())
    tmp = md_path.parent / f".{md_path.stem}.tmp.md"
    tmp.write_text(src)
    try:
        body = md_to_html(tmp, toc=toc)
    finally:
        tmp.unlink(missing_ok=True)

    html = f"<!doctype html><html lang='en-CA'><head><meta charset='utf-8'></head><body>{cover}{body}</body></html>"

    font_config = FontConfiguration()
    HTML(string=html, base_url=str(ROOT)).write_pdf(
        out_path,
        stylesheets=[CSS(string=css or BASE_CSS, font_config=font_config)],
        font_config=font_config,
    )
    print(f"wrote {out_path.relative_to(ROOT)} ({out_path.stat().st_size // 1024} KB)")


HANDBOOK_COVER = f"""
<section class="cover">
  <p class="kicker">Erskine Advisory · A guide for owners</p>
  <h1>Building in British Columbia: what the owner is responsible for</h1>
  <div class="rule"></div>
  <p class="sub">Licensing, warranty, the statutory 10% holdback, payment, change
  orders, liens and completion — in plain language, with the section references.</p>
  <p class="meta">
    Independent owner's representation<br>
    Statutory references verified August 2026<br>
    erskineadvisory.com
  </p>
  <p class="foot">This guide explains what the legislation requires. It is not legal
  advice. Consult a BC construction lawyer on your specific project.</p>
</section>
"""

REFERRAL_COVER = ""


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    build(
        ROOT / "src" / "content" / "guides" / "bc-owners-handbook.md",
        OUT / "bc-owners-handbook.pdf",
        HANDBOOK_COVER,
        toc=True,
    )
    kit = ROOT / "docs" / "referral-kit.md"
    if kit.exists():
        build(kit, OUT / "erskine-referral-kit.pdf", REFERRAL_COVER, toc=False, css=KIT_CSS)
    return 0


if __name__ == "__main__":
    sys.exit(main())
