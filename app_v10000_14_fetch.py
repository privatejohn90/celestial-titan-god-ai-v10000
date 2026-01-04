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

# ================================================================
# 🔹 Titan Auto-Fetch Chrono Bridge v14 — Part 4: Year History Downloader
# ================================================================
def download_yearly_history(game_name, base_url, year_range):
    """
    Generic downloader for historical draw results per year.
    Example: base_url='https://www.flalottery.com/pick3?year={}'
    """
    history_dir = os.path.join(DATA_DIR, "history")
    os.makedirs(history_dir, exist_ok=True)

    all_years = []
    for year in year_range:
        url = base_url.format(year)
        print(f"🕰 Fetching {game_name} {year} → {url}")

        try:
            resp = requests.get(url, timeout=12)
            resp.raise_for_status()

            soup = BeautifulSoup(resp.text, "html.parser")
            rows = soup.find_all("tr")

            year_records = []
            for r in rows:
                cols = [c.get_text(strip=True) for c in r.find_all("td")]
                if len(cols) >= 2:
                    year_records.append({
                        "game": game_name,
                        "year": year,
                        "date": cols[0],
                        "numbers": cols[1],
                    })

            all_years.extend(year_records)
            print(f"✅ {game_name} {year}: {len(year_records)} records")

        except Exception as e:
            print(f"⚠️ {game_name} {year} fetch failed → {e}")

    # Save combined CSV + JSON
    df = pd.DataFrame(all_years)
    csv_path = os.path.join(history_dir, f"{game_name}_history.csv")
    df.to_csv(csv_path, index=False)
    json_path = csv_path.replace(".csv", ".json")
    save_json(json_path, all_years)
    print(f"💾 Saved {len(df)} records for {game_name} → {csv_path}")


def titan_yearly_harvest():
    """Runs automatic yearly history downloads for configured games."""
    print("🌌 Launching Titan Chrono Harvest (2010 → 2024)…")
    year_range = range(2010, 2025)

    HISTORY_SOURCES = {
        "FL Pick 3": "https://www.flalottery.com/site/pick3?year={}",
        "GA Pick 4": "https://www.galottery.com/en-us/games/draw-games/cash-4/results?year={}",
        "PCSO 3D Lotto": "https://www.pcso.gov.ph/SearchLottoResult.aspx?Year={}",
    }

    for game, link in HISTORY_SOURCES.items():
        download_yearly_history(game, link, year_range)

    print("🌙 Titan Yearly Harvest Complete — Chrono Data Ready for Learning.")













