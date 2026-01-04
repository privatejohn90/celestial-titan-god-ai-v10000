# ================================================================
# 🌌 Celestial Titan God AI — Stealth Mirror Mode v16
# ================================================================
import requests, json, os, re, random, datetime, time

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
# 🛰 Universal Browser Headers (Anti-block)
# ================================================================
headers = {
    "User-Agent": random.choice([
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    ]),
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
}

# ================================================================
# 🌐 Titan Mirror Sources (Extended)
# ================================================================
sources = {
    "CA": ["https://www.lotteryusa.com/california/daily-3/",
           "https://www.lotterypost.com/ca",
           "https://www.lotterycritic.com/ca/daily-3-results/"],
    "TX": ["https://www.lotteryusa.com/texas/pick-3/",
           "https://www.lotterypost.com/tx",
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
# 🧠 Smart HTML Scraper
# ================================================================
def extract_numbers(html):
    patterns = [
        r"\b\d{3}\b",        # 3-digit
        r"\b\d{4}\b",        # 4-digit
        r"\b\d{1}\s?\d{1}\s?\d{1}\b"  # spaced digits
    ]
    found = []
    for pat in patterns:
        found.extend(re.findall(pat, html))
    return list(set(found))[:25] if found else None

# ================================================================
# ⚙️ Fetch Routine
# ================================================================
today = datetime.date.today().isoformat()
print(f"\n🛰 Titan Stealth Mirror Mode v16 — Running ({today})")

for state, urls in sources.items():
    success = False
    for url in urls:
        try:
            r = requests.get(url, headers=headers, timeout=10)
            if r.status_code == 200:
                numbers = extract_numbers(r.text)
                if numbers:
                    titan_data[state] = titan_data.get(state, [])
                    titan_data[state].append({
                        "date": today,
                        "numbers": numbers,
                        "source": url
                    })
                    print(f"✅ {state}: {len(numbers)} numbers fetched from {url}")
                    success = True
                    break
                else:
                    print(f"⚠️ {state}: No numbers found in {url}")
            else:
                print(f"⚠️ {state}: HTTP {r.status_code}")
        except Exception as e:
            print(f"❌ {state} mirror error: {e}")
        time.sleep(random.uniform(1.5, 3.0))
    if not success:
        print(f"🚫 {state}: All mirrors failed.")

save_json(RESULT_FILE, titan_data)
print("\n💾 Stealth Fetch Complete — Results saved to titan_results.json")


