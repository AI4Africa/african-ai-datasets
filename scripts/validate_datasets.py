import re
import requests
import sys
from pathlib import Path

README_PATH = Path("README.md")

REQUIRED_FIELDS = [
    "**Description**:",
    "**Languages",
    "**Size**:",
    "**Samples**:",
    "**Tasks**:",
    "**Source**:",
    "**Link**:",
    "**License**:",
    "**Last Updated**:",
    "**Best For**:"
]

BADGE_PATTERN = re.compile(r"!\[.*\]\(https:\/\/img\.shields\.io\/badge\/.*\)")

def fetch_wayback_link(url):
    wayback_api = f"http://archive.org/wayback/available?url={url}"
    try:
        resp = requests.get(wayback_api, timeout=8).json()
        if resp.get("archived_snapshots") and "closest" in resp["archived_snapshots"]:
            return resp["archived_snapshots"]["closest"]["url"]
    except requests.RequestException:
        pass
    return None

def check_required_fields(content):
    errors = []
    for dataset in [d for d in content.split("### ") if d.strip()]:
        dataset_name = dataset.splitlines()[0]
        for field in REQUIRED_FIELDS:
            if field not in dataset:
                suggestion = f"Add missing field:\n`- {field} <YOUR_VALUE>`"
                errors.append(f"❌ Missing '{field}' in dataset '{dataset_name}'.\n💡 Suggestion: {suggestion}")
    return errors

def check_badges(content):
    errors = []
    for dataset in [d for d in content.split("### ") if d.strip()]:
        dataset_name = dataset.splitlines()[0]
        badges = [line for line in dataset.splitlines() if "img.shields.io" in line]
        if not badges:
            suggestion = "Add a domain badge, e.g.: `![Domain](https://img.shields.io/badge/Domain-NLP-blue)`"
            errors.append(f"⚠️ No badges found in dataset '{dataset_name}'.\n💡 Suggestion: {suggestion}")
        else:
            for badge in badges:
                if not BADGE_PATTERN.search(badge):
                    suggestion = "Ensure badges follow Shields.io format: `![Label](https://img.shields.io/badge/Label-Value-Color)`"
                    errors.append(f"❌ Invalid badge format in dataset '{dataset_name}'.\n💡 Suggestion: {suggestion}")
    return errors

def check_links(content):
    errors = []
    urls = re.findall(r"\(https?://[^\)]+\)", content)
    urls = [u.strip("()") for u in urls]
    for url in urls:
        try:
            r = requests.head(url, allow_redirects=True, timeout=10)
            if r.status_code != 200:
                archive_url = fetch_wayback_link(url)
                if archive_url:
                    errors.append(f"❌ Broken link: {url} (status {r.status_code})\n💡 Archived version found: {archive_url}")
                else:
                    errors.append(f"❌ Broken link: {url} (status {r.status_code})\n💡 No archive found. Consider replacing or removing.")
        except requests.RequestException as e:
            errors.append(f"❌ Error checking link: {url} ({e})\n💡 Try updating to a current working link.")
    return errors

def main():
    if not README_PATH.exists():
        print("❌ README.md not found.")
        sys.exit(1)

    content = README_PATH.read_text(encoding="utf-8")

    errors = []
    errors += check_required_fields(content)
    errors += check_badges(content)
    errors += check_links(content)

    if errors:
        print("\n--- VALIDATION REPORT ---")
        for e in errors:
            print(e)
        print("\n❌ Validation failed. Please fix the above issues before merging.")
        sys.exit(1)
    else:
        print("✅ All dataset entries validated successfully.")

if __name__ == "__main__":
    main()
