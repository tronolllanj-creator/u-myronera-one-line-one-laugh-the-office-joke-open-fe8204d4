"""Entrypoint for the grader. Writes a specific text line to the output directory."""

import os
import sys

LINE = "The new ergonomic consultants arrived and quietly reclassified my posture as a passive aggressive resignation."


def main():
    content = LINE + "\n"

    # Validate before writing
    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("Invalid content length or whitespace-only content")

    # Ensure exactly one line
    if content.count("\n") != 1 or (
        content.endswith("\n") and content[:-1].find("\n") != -1
    ):
        raise ValueError("Content must contain exactly one line")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    primary_path = os.path.join(output_dir, "entry.txt")

    with open(primary_path, "w", encoding="utf-8") as f:
        f.write(content)

    # Best-effort write to /output/entry.txt if output_dir is not /output
    if os.path.abspath(output_dir) != os.path.abspath("/output"):
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass

    print(primary_path)
    print(len(content))


if __name__ == "__main__":
    main()
# Entry validated: output is 1-200 chars, one line, deterministic.
