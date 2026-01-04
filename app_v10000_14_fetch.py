# ================================================================
# ⚡ CELESTIAL TITAN GOD AI v10000.14 — AUTO-FETCH CHRONO BRIDGE CORE
# ================================================================
import streamlit as st
import json, os, datetime, requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="Titan Auto-Fetch Core", page_icon="🌐")

# ================================================================
# 📁 Setup Paths
# ================================================================
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)
FETCH_LOG = os.path.join(DATA_DIR, "titan_fetch_log.json")
RESULT_FILE = os.path.join(DATA_DIR, "titan_results.json")

def load_json(path, default):
    if not os.path.exists(path):
        with open(path, "w") as f: json.dump(default, f, indent=2)
        return default
    try:
        with open(path) as f: return json.load(f)
    except: return default

def save_json(path, data):
    with open(path, "w") as f: json.dump(data, f, indent=2)

# ================================================================
# 🌍 FETCH MAP — All Game Sources (Base URLs)
# ================================================================
FETCH_SOURCES = {
    "Powerball": "https://www.powerball.net/archive/{year}",
    "Mega Millions": "https://www.megamillions.com/winning-numbers/previous-drawings.aspx",
    "Florida Lottery": "https://www.flalottery.com/winningNumbers",
    "Georgia Lottery": "https://www.galottery.com/en-us/winning-numbers.html",
    "Texas Lottery": "https://www.txlottery.org/export/sites/lottery/Games/List",
    "Virginia Lottery": "https://www.valottery.com/results",
    "North Carolina Lottery": "https://www.nclottery.com/results",
    "New York Lottery": "https://nylottery.ny.gov/winning-numbers/history",
    "New Jersey Lottery": "https://www.njlottery.com/en-us/results.html",
    "California Lottery": "https://www.calottery.com/play/daily-games/winning-numbers",
    "PCSO 3D/4D/STL": "https://www.pcso.gov.ph/SearchLottoResult.aspx"
}

# ================================================================
# 🧠 Titan Fetch Console
# ================================================================
st.title("🌐 Titan Auto-Fetch Chrono Bridge v14")
st.caption("Fetching 2010–2024 historical draws — USA + PH unified bridge")

selected_game = st.selectbox("🎯 Choose Game Source", list(FETCH_SOURCES.keys()))
selected_year = st.selectbox("📅 Choose Year", list(range(2010, 2025)))

if st.button("⚡ Fetch Results"):
    url = FETCH_SOURCES[selected_game].format(year=selected_year)
    st.info(f"🔗 Connecting to: {url}")
    # Placeholder: Titan will parse next step

# ================================================================
# 🔹 Titan Auto-Fetch Chrono Bridge v14 — Part 2: Parser Framework
# ================================================================
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime, os, json

FETCH_DATA_FILE = os.path.join(DATA_DIR, "titan_auto_fetch_log.json")

def fetch_lottery_results(source_name, url, selectors):
    """
    Base fetcher for a given state or country.
    selectors = {
        'draw_date': 'css_selector_here',
        'numbers': 'css_selector_here'
    }
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        draw_date = soup.select_one(selectors["draw_date"]).get_text(strip=True)
        numbers = soup.select_one(selectors["numbers"]).get_text(strip=True)

        entry = {
            "source": source_name,
            "draw_date": draw_date,
            "numbers": numbers,
            "fetched_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        data = load_json(FETCH_DATA_FILE, [])
        data.append(entry)
        save_json(FETCH_DATA_FILE, data)

        print(f"✅ {source_name}: {numbers} ({draw_date})")
        return entry

    except Exception as e:
        print(f"⚠️ {source_name} fetch failed: {e}")
        return None


# Example state sources (expandable later)
LOTTERY_SOURCES = {
    "Florida": {
        "url": "https://www.flalottery.com/pick3",
        "selectors": {"draw_date": ".gamePageNumbers > h2", "numbers": ".numbers"}
    },
    "Georgia": {
        "url": "https://www.galottery.com/en-us/games/draw-games/cash-3.html",
        "selectors": {"draw_date": ".drawDate", "numbers": ".drawNumbers"}
    },
    "PCSO": {
        "url": "https://www.pcso.gov.ph/SearchLottoResult.aspx",
        "selectors": {"draw_date": "#date", "numbers": ".results"}
    }
}

def run_auto_fetch():
    print("🔄 Running Titan Auto-Fetch Chrono Bridge…")
    for name, src in LOTTERY_SOURCES.items():
        fetch_lottery_results(name, src["url"], src["selectors"])
    print("💾 Auto-fetch complete — data saved.")

if __name__ == "__main__":
    run_auto_fetch()

# ================================================================
# 🔹 Titan Auto-Fetch Chrono Bridge v14 — Part 3: CSV + Sync System
# ================================================================
def sync_fetched_results_to_csv():
    print("🧩 Syncing fetched results to Titan Data CSV...")
    try:
        data = load_json(FETCH_DATA_FILE, [])
        if not data:
            print("⚠️ No fetched data yet to sync.")
            return

        df = pd.DataFrame(data)
        csv_path = os.path.join(DATA_DIR, "titan_auto_results.csv")

        # Merge if CSV exists
        if os.path.exists(csv_path):
            old_df = pd.read_csv(csv_path)
            merged_df = pd.concat([old_df, df], ignore_index=True).drop_duplicates(
                subset=["source", "draw_date", "numbers"], keep="last"
            )
        else:
            merged_df = df

        merged_df.to_csv(csv_path, index=False)
        print(f"✅ Synced {len(merged_df)} records to {csv_path}")

        # Also backup to JSON mirror
        save_json(FETCH_DATA_FILE, merged_df.to_dict(orient="records"))

    except Exception as e:
        print(f"⚠️ Sync error: {e}")


# 🔁 Combined run (fetch + sync)
def titan_auto_sync_bridge():
    print("🚀 Starting Titan Chrono Fetch + Sync Bridge...")
    run_auto_fetch()
    sync_fetched_results_to_csv()
    print("🌙 Titan Chrono Sync Complete — All data aligned.")















