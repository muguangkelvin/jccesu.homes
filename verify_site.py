import os
import json
import re
import sys

PUBLIC_DIR = r"c:\Users\USER\Desktop\博客\jccesu.homes\public"
BASE_DIR = r"c:\Users\USER\Desktop\博客\jccesu.homes"

errors = []

print("Running site verification audit...")

# 1. Verify index.html exists
index_html_path = os.path.join(PUBLIC_DIR, "index.html")
if not os.path.exists(index_html_path):
    errors.append("public/index.html is missing!")
else:
    with open(index_html_path, "r", encoding="utf-8") as f:
        html = f.read()
        if "灵动云" not in html or "暮光网络" not in html or "飞猫云" not in html or "微风网络" not in html:
            errors.append("Top 4 providers missing from index.html!")
        if "https://t.me/+HVHzlzUXk4YyOWM9" not in html:
            errors.append("Telegram channel link missing from header/index.html!")
        if "search-input" not in html:
            errors.append("Search input box missing from header!")

# 2. Verify search index (index.json)
index_json_path = os.path.join(PUBLIC_DIR, "index.json")
if not os.path.exists(index_json_path):
    errors.append("public/index.json is missing!")
else:
    with open(index_json_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            if len(data) < 150:
                errors.append(f"public/index.json has only {len(data)} items, expected >150.")
            print(f"Verified public/index.json with {len(data)} indexed pages.")
        except Exception as e:
            errors.append(f"Invalid JSON in public/index.json: {e}")

# 3. Verify all 28 providers and rel="sponsored nofollow noopener"
all_airports_path = os.path.join(PUBLIC_DIR, "all-airports", "index.html")
if not os.path.exists(all_airports_path):
    errors.append("public/all-airports/index.html is missing!")
else:
    with open(all_airports_path, "r", encoding="utf-8") as f:
        html = f.read()
        if 'rel="sponsored nofollow noopener"' not in html:
            errors.append("rel='sponsored nofollow noopener' missing in all-airports page!")

        # Verify all 28 provider names present
        with open(os.path.join(BASE_DIR, "data", "providers.json"), "r", encoding="utf-8") as pf:
            providers = json.load(pf)
            for p in providers:
                if p["name"] not in html:
                    errors.append(f"Provider {p['name']} missing from all-airports page!")

# 4. Verify word counts of generated markdown files
content_dir = os.path.join(BASE_DIR, "content")
sample_md = os.path.join(content_dir, "speed-test", "speed-test-1.md")
if os.path.exists(sample_md):
    with open(sample_md, "r", encoding="utf-8") as f:
        text = f.read()
        chinese_char_count = len(re.findall(r'[\u4e00-\u9fa5]', text))
        print(f"Sample article Chinese character count: {chinese_char_count} chars.")
        if chinese_char_count < 1000:
            errors.append(f"Article word count too low: {chinese_char_count} chars.")

# 5. Check docs directory
docs_files = [
    "site-seo-profile.json", "content-plan.md", "keyword-map.md", "keyword-coverage.csv",
    "faq-keywords-100.csv", "faq-content-matrix.md", "navigation-content-matrix.md",
    "provider-review-matrix.md", "reference-publisher-blocklist.md",
    "seo-profile-replacement-contract.md", "launch-checklist.md"
]

for df in docs_files:
    if not os.path.exists(os.path.join(BASE_DIR, "docs", df)):
        errors.append(f"Missing doc file: docs/{df}")

if errors:
    print("VERIFICATION FAILED WITH ERRORS:")
    for e in errors:
        print(f" - {e}")
    sys.exit(1)
else:
    print("ALL VERIFICATION CHECKS PASSED PERFECTLY!")
