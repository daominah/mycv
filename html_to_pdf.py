"""
Fix GitHub-rendered HTML for local use, then convert to PDF.

Steps:
1. Fix image src to use local path.
2. Remove SVG anchor icons from headings.
3. Convert to PDF using weasyprint.

Usage (Linux/macOS):
    python3 -m venv .venv
    .venv/bin/pip install -r requirements.txt
    .venv/bin/python html_to_pdf.py

Usage (Windows, Git Bash):
    weasyprint requires system libraries not available via pip.
    Use WSL with Ubuntu. In PowerShell:
        wsl --install -d Ubuntu-24.04
    Create a user, then in WSL:
        sudo apt update
        sudo apt install python3-pip python3-venv libpango-1.0-0
        sudo apt install -y ttf-mscorefonts-installer (for Arial font)
    Go to the project dir, then run (sudo needed for permissions on /mnt/c):
        cd /mnt/c/Users/tungd/go/src/github.com/daominah/mycv
        sudo python3 -m venv .venv
        sudo .venv/bin/pip install -r requirements.txt
    After the setup, in the future you can run from PowerShell:
        wsl --distribution Ubuntu-24.04
        cd /mnt/c/Users/tungd/go/src/github.com/daominah/mycv
        .venv/bin/python html_to_pdf.py
"""

import re
import sys


def fix_html(content):
    # Fix GitHub image paths to local
    content = re.sub(
        r'src="/daominah/mycv/raw/[^"]*portrait\.png"',
        'src="portrait.png"',
        content,
    )

    # Remove SVG anchor icons (multiline)
    content = re.sub(
        r'<a id="user-content-[^"]*" class="anchor".*?</a>',
        "",
        content,
        flags=re.DOTALL,
    )

    # Replace portrait img tag entirely for weasyprint compatibility.
    # GitHub adds align="right" and duplicate style attributes that
    # weasyprint cannot handle.
    content = re.sub(
        r'<img[^>]*portrait\.png[^>]*>',
        '<img src="portrait.png" alt="Tung photo"'
        ' style="float: right; width: 150px; height: 200px; margin: 0 0 16px 16px;">',
        content,
    )

    return content


def main():
    html_path = "readme.html"
    pdf_path = "readme.pdf"
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    content = fix_html(content)

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(content)

    print("Fixed: photo path and removed SVG anchors.")

    try:
        from weasyprint import HTML, CSS

        page_css = CSS(string="@page { margin-top: 8mm; margin-bottom: 8mm; }")
        HTML(filename=html_path).write_pdf(pdf_path, stylesheets=[page_css])
        print("Created: " + pdf_path)
    except ImportError:
        print("weasyprint not installed, skipping PDF generation.")
        print("Install with: pip install weasyprint")
        sys.exit(1)


if __name__ == "__main__":
    main()
