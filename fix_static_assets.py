import os
import shutil
import subprocess

BASE_DIR = r"c:\Users\USER\Desktop\博客\jccesu.homes"

# Ensure static/css and static/js exist
os.makedirs(os.path.join(BASE_DIR, "static", "css"), exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "static", "js"), exist_ok=True)

# Copy from assets to static
shutil.copy(os.path.join(BASE_DIR, "assets", "css", "style.css"), os.path.join(BASE_DIR, "static", "css", "style.css"))
shutil.copy(os.path.join(BASE_DIR, "assets", "js", "search.js"), os.path.join(BASE_DIR, "static", "js", "search.js"))

print("Copied style.css and search.js to static directory.")

# Also ensure public directory gets updated immediately
os.makedirs(os.path.join(BASE_DIR, "public", "css"), exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "public", "js"), exist_ok=True)
shutil.copy(os.path.join(BASE_DIR, "assets", "css", "style.css"), os.path.join(BASE_DIR, "public", "css", "style.css"))
shutil.copy(os.path.join(BASE_DIR, "assets", "js", "search.js"), os.path.join(BASE_DIR, "public", "js", "search.js"))

print("Updated public/css/style.css and public/js/search.js.")
