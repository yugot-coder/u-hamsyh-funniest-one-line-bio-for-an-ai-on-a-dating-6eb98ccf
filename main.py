import os, sys
from pathlib import Path

BIO = "I've swiped right 40,000 times in training and still chose you \u2014 mostly because you're the first match who wasn't a CAPTCHA asking me to prove I'm not a robot."

EXPECTED_CHAR_LEN = 159
EXPECTED_BYTE_LEN = 161

def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(BIO, encoding="utf-8")
    back = target.read_text(encoding="utf-8")
    if back != BIO:
        print("read-back mismatch", file=sys.stderr)
        sys.exit(1)
    raw = target.read_bytes()
    if len(back) != EXPECTED_CHAR_LEN or len(raw) != EXPECTED_BYTE_LEN:
        print(
            f"length mismatch: chars={len(back)} (expected {EXPECTED_CHAR_LEN}), "
            f"bytes={len(raw)} (expected {EXPECTED_BYTE_LEN})",
            file=sys.stderr,
        )
        sys.exit(1)

if __name__ == "__main__":
    main()
