import os

# Entry point: emit the answer (247) with no trailing newline.
ENTRY = "247"
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as out:
    out.write(ENTRY)
