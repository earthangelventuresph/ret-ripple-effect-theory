"""
RET Freeze + Hash — §12.1
Usage: python freeze_and_hash.py predictions.json
Writes predictions.json.sha256. Hash recorded in OSF registration BEFORE any ripple trial.
Seed for randomisation = first 8 hex digits of hash, converted to int.
"""
import hashlib, sys, json

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "predictions.json"
    digest = sha256_file(path)
    with open(path + ".sha256", "w") as f:
        f.write(digest + "\n")
    seed = int(digest[:8], 16)
    print(f"SHA-256: {digest}")
    print(f"Randomisation seed (first 8 hex -> int): {seed}")
    print("Record hash in OSF registration BEFORE any ripple trial.")
