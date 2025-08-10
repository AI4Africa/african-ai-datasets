# scripts/build_index.py
import sys, re
from pathlib import Path

readme = Path("README.md")
docs_dir = Path("docs")
index = docs_dir / "index.md"

if not readme.exists():
    print("❌ README.md not found in repository root.")
    sys.exit(2)

docs_dir.mkdir(parents=True, exist_ok=True)
content = readme.read_text(encoding="utf-8")

# For project sites, make asset links baseurl-aware.
# Handle common patterns: href/src/markdown image/link to assets/
content = re.sub(r'href="assets/', 'href="{{ site.baseurl }}/assets/', content)
content = re.sub(r"src=\"assets/", 'src="{{ site.baseurl }}/assets/', content)
content = re.sub(r"\]\(assets/", "]({{ site.baseurl }}/assets/", content)

# Front matter (required so Jekyll treats it as a page)
front_matter = (
    "---\n"
    "title: Awesome African AI Datasets\n"
    "layout: default\n"
    "---\n\n"
)

index.write_text(front_matter + content, encoding="utf-8")

# Sanity checks + preview
stat = index.stat()
print(f"✅ Wrote {index} ({stat.st_size} bytes)")
print("🔎 First 15 lines of docs/index.md:\n")
with index.open(encoding="utf-8") as f:
    for i, line in zip(range(15), f):
        print(line.rstrip())
