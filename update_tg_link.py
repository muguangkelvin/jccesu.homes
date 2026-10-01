import os

BASE_DIR = r"c:\Users\USER\Desktop\博客\jccesu.homes"

old_tg = "https://t.me/+HVHzlzUXk4YyOWM9"
new_tg = "https://t.me/+HVHzlzUXk4YyOWM9"

count = 0
for root, dirs, files in os.walk(BASE_DIR):
    # Skip public and .git
    if "public" in root or ".git" in root:
        continue
    for file in files:
        if file.endswith((".html", ".json", ".toml", ".md", ".py", ".txt")):
            fp = os.path.join(root, file)
            with open(fp, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            if old_tg in content:
                new_content = content.replace(old_tg, new_tg)
                with open(fp, "w", encoding="utf-8") as f:
                    f.write(new_content)
                count += 1
                print(f"Updated TG link in: {file}")

print(f"Finished updating TG link in {count} files.")
