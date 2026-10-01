import subprocess
import sys

scripts = [
    "generate_bespoke_articles.py",
    "generate_bespoke_articles_part2.py",
    "generate_bespoke_articles_part3.py",
    "generate_bespoke_articles_part4.py",
    "generate_bespoke_articles_part5.py",
    "generate_bespoke_articles_part6.py",
    "generate_bespoke_articles_part7.py",
    "generate_bespoke_tutorials.py",
    "generate_bespoke_speedtests.py",
    "generate_bespoke_knowledge.py"
]

for s in scripts:
    print(f"Executing {s}...")
    res = subprocess.run([sys.executable, s], capture_output=True, text=True, cwd=r"c:\Users\USER\Desktop\博客\jccesu.homes")
    if res.returncode != 0:
        print(f"Error executing {s}:", res.stderr)
        sys.exit(1)
    else:
        print(res.stdout)

print("Rebuilding Hugo site with Hugo --gc --minify...")
res_hugo = subprocess.run(["hugo", "--gc", "--minify"], capture_output=True, text=True, cwd=r"c:\Users\USER\Desktop\博客\jccesu.homes")
print(res_hugo.stdout)
if res_hugo.returncode != 0:
    print("Hugo build error:", res_hugo.stderr)
    sys.exit(1)

print("All bespoke articles generated & site rebuilt successfully!")
