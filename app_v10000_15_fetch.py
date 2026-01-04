# ================================================================
# 🌌 Celestial Titan God AI — Auto-Fetch Expansion v15 (CA, TX, NJ, VA, NC, NY)
# ================================================================
import requests, json, os, datetime, re

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)
RESULT_FILE = os.path.join(DATA_DIR, "titan_results.json")

def load_json(path, default):
    if not os.path.exists(path):
        with open(path, "w") as f: json.dump(default, f, indent=2)
        return default
    try:
        with open(path, "r") as f: return json.load(f)
    except Exception: return default

def save_json(path, data):
    with open(path, "w") as f: json.dump(data, f, indent=2)

titan_data = load_json(RESULT_FILE, {})

# ================================================================
# ⚡ Auto-Fetch URLs (Backup & Mirror Sites)
# ================================================================
sources = {
    "CA": ["https://www.lotteryusa.com/california/daily-3/",
           "https://www.lotterycritic.com/ca/daily-3-results/"],
    "TX": ["https://www.lotteryusa.com/texas/pick-3/",
           "https://www.lotterycritic.com/tx/pick-3-results/"],
    "NJ": ["https://www.lotteryusa.com/new-jersey/pick-3/",
           "https://www.lotterycritic.com/nj/pick-3-results/"],
    "VA": ["https://www.lotteryusa.com/virginia/pick-3/",
           "https://www.lotterycritic.com/va/pick-3-results/"],
    "NC": ["https://www.lotteryusa.com/north-carolina/pick-3/",
           "https://www.lotterycritic.com/nc/pick-3-results/"],
    "NY": ["https://www.lotteryusa.com/new-york/pick-3/",
           "https://www.lotterycritic.com/ny/pick-3-results/"]
}

# ================================================================
# 🔍 Fetch Logic
# ================================================================
def fetch_results(url):
    try:
        r = requests.get(url, timeout=10)
        if r.status_code != 200: return None
        html = r.text
        # Simple regex to find number patterns (example: "1-2-3" or "123")
        found = re.findall(r"\b\d{3,4}\b", html)
        return found[:20] if found else None
    except Exception:
        return None

# ================================================================
# 🚀 Run Fetch for Each State
# ================================================================
today = datetime.date.today().isoformat()
print(f"\n🌀 Titan Auto-Fetch Expansion v15 — Running ({today})")

for state, urls in sources.items():
    success = False
    for link in urls:
        data = fetch_results(link)
        if data:
            titan_data[state] = titan_data.get(state, [])
            titan_data[state].append({"date": today, "numbers": data})
            print(f"✅ {state} data fetched successfully from {link}")
            success = True
            break
    if not success:
        print(f"⚠️ {state} fetch failed from all sources.")

save_json(RESULT_FILE, titan_data)
print("\n💾 Auto-Fetch complete — Results saved to titan_results.json")

