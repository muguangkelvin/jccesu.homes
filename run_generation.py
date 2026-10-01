import subprocess
import sys

scripts = [
    "generate_data.py",
    "builder_part1.py",
    "builder_part2.py",
    "builder_part3.py",
    "builder_part4.py",
    "builder_part5.py",
    "builder_part6.py"
]

for s in scripts:
    print(f"Executing {s}...")
    res = subprocess.run([sys.executable, s], capture_output=True, text=True, cwd=r"c:\Users\USER\Desktop\博客\jccesu.homes")
    if res.returncode != 0:
        print(f"Error running {s}:", res.stderr)
        sys.exit(1)
    else:
        print(res.stdout)

print("All site generation scripts executed successfully!")
