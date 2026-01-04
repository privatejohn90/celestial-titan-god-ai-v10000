# ================================================================
# 🧩 Titan Utilities — Shared JSON Functions
# ================================================================
import json, os

def load_json(path, default):
    """Safe loader — creates file if missing or corrupted."""
    if not os.path.exists(path):
        with open(path, "w") as f: json.dump(default, f, indent=2)
        return default
    try:
        with open(path, "r") as f:
            return json.load(f)
    except Exception:
        return default

def save_json(path, data):
    """Save dictionary as JSON safely."""
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
