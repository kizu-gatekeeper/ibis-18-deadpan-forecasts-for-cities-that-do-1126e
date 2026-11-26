"""Write one deadpan weather forecast to the make.fun output directory."""

import os

LINE = "Good evening, Plinth: expect light drizzle, a 40 percent chance of fog, and a 100 percent chance the fog is lying about something."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/tmp/out")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
