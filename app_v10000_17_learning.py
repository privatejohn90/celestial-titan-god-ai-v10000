# ================================================================
# 🧠 Celestial Titan God AI v17 — Confidence-Weighted Learning Core
# ================================================================
import json, os, datetime
from collections import Counter

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

RESULT_FILE = os.path.join(DATA_DIR, "titan_results.json")
LEARN_FILE = os.path.join(DATA_DIR, "titan_learning_v17.json")

def load_json(path, default):
    if not os.path.exists(path):
        with open(path, "w") as f: json.dump(default, f, indent=2)
        return default
    try:
        with open(path, "r") as f: return json.load(f)
    except: return default

def save_json(path, data):
    with open(path, "w") as f: json.dump(data, f, indent=2)

results = load_json(RESULT_FILE, {})
learning = {
    "updated": datetime.datetime.now().isoformat(),
    "state_analysis": {}
}

def analyze_state(state, entries):
    digits = []
    for e in entries[-20:]:
        nums = e.get("numbers", [])
        for n in nums:
            digits.extend(list(str(n)))
    freq = Counter(digits)
    total = sum(freq.values())
    confidence = {k: round((v/total)*100,2) for k,v in freq.items()}
    return confidence

for state, entries in results.items():
    if isinstance(entries, list) and len(entries) >= 10:
        learning["state_analysis"][state] = {
            "confidence_map": analyze_state(state, entries),
            "status": "READY" if len(entries) >= 20 else "WARMING"
        }

save_json(LEARN_FILE, learning)
print("🧠 Titan v17 Learning Core updated.")


