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

# ================================================================
# ⚙️ Titan Smart Fetch Repair — Adaptive Parser + Anti-403 Bypass
# ================================================================
import requests
from bs4 import BeautifulSoup
import pandas as pd

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                  " AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/119.0 Safari/537.36"
}

def smart_fetch(url):
    """Fetches URL content safely with anti-403 headers and retries."""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        resp.raise_for_status()
        return resp.text
    except Exception as e:
        print(f"⚠️ Smart fetch failed for {url}: {e}")
        return None


def adaptive_parse(html_text, game_name):
    """Parse draw numbers even if layout differs."""
    if not html_text:
        return []

    soup = BeautifulSoup(html_text, "html.parser")
    rows = soup.find_all("tr")
    results = []

    for r in rows:
        cols = [c.get_text(strip=True) for c in r.find_all(["td", "th"])]
        if len(cols) >= 2:
            date_col, number_col = cols[0], cols[1]
            # Auto-detect number formatting (e.g., "1-2-3" or "123")
            clean_num = number_col.replace(" ", "").replace("-", "").replace(",", "")
            results.append({"date": date_col, "numbers": clean_num})
    return results


def repaired_download(game_name, url_template, year_range):
    print(f"🚀 Smart-fetching {game_name} with adaptive parser…")
    all_data = []
    for year in year_range:
        html = smart_fetch(url_template.format(year))
        parsed = adaptive_parse(html, game_name)
        print(f"✅ {game_name} {year}: {len(parsed)} records parsed")
        for p in parsed:
            p["year"] = year
            p["game"] = game_name
        all_data.extend(parsed)

    # Save combined data
    history_dir = os.path.join(DATA_DIR, "history")
    os.makedirs(history_dir, exist_ok=True)
    df = pd.DataFrame(all_data)
    csv_path = os.path.join(history_dir, f"{game_name}_smart_history.csv")
    df.to_csv(csv_path, index=False)
    print(f"💾 Smart history saved → {csv_path}")
    return all_data


def titan_smart_repair_harvest():
    """Run smart fetch with repaired access."""
    year_range = range(2010, 2025)
    smart_sources = {
        "FL Pick 3": "https://www.flalottery.com/pick3?year={}",
        "GA Pick 4": "https://www.galottery.com/en-us/games/draw-games/cash-4/results?year={}",
        "PCSO 3D Lotto": "https://www.pcso.gov.ph/SearchLottoResult.aspx?Year={}"
    }
    for game, link in smart_sources.items():
        repaired_download(game, link, year_range)

    print("🌈 Titan Smart Fetch Repair completed — adaptive parser active.")

# ================================================================
# ⚡ Titan Smart-HTML Fetch v14.1 — Full Bypass + Multi-Parser
# ================================================================
import time, random
from urllib.parse import urlparse

ADV_HEADERS = {
    "User-Agent": random.choice([
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 "
        "(KHTML, like Gecko) Version/17.1 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/121.0.0.0 Safari/537.36"
    ]),
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://google.com",
    "Connection": "keep-alive",
}

def smart_html_fetch(url, retries=3, delay=2):
    """Try several times with stronger headers."""
    for attempt in range(1, retries + 1):
        try:
            resp = requests.get(url, headers=ADV_HEADERS, timeout=20)
            if resp.status_code == 200:
                print(f"✅ Access success → {urlparse(url).netloc}")
                return resp.text
            else:
                print(f"⚠️ Attempt {attempt}: HTTP {resp.status_code}")
        except Exception as e:
            print(f"⚠️ Attempt {attempt} failed: {e}")
        time.sleep(delay + random.uniform(0.5, 2.5))
    print(f"❌ Smart-HTML fetch failed after {retries} attempts → {url}")
    return None


def titan_html_bypass_harvest():
    """Re-fetch critical sources using enhanced HTML bypass."""
    targets = {
        "FL Pick 3": "https://www.flalottery.com/pick3",
        "GA Pick 3": "https://www.galottery.com/en-us/games/draw-games/cash-3/results.html",
        "PCSO 3D Lotto": "https://www.pcso.gov.ph/SearchLottoResult.aspx",
    }

    for game, link in targets.items():
        html = smart_html_fetch(link)
        if not html:
            print(f"🚫 {game} still blocked.")
            continue

        parsed = adaptive_parse(html, game)
        print(f"🧩 {game}: {len(parsed)} records recovered.")

    print("🌌 Titan Smart-HTML Fetch v14.1 completed — resilience enabled.")

# ================================================================
# ⚙️ Titan Auto-Fetch Chrono Bridge v14.2 — WebDriver Mode
# ================================================================
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def titan_webdriver_fetch(url):
    """Use headless Chrome to fully render JS-heavy pages."""
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--window-size=1920,1080")
    opts.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=opts)
    driver.get(url)
    time.sleep(3)  # wait for JS content to render
    html = driver.page_source
    driver.quit()
    return html


def titan_webdriver_bridge():
    """Fetch key lottery sources with WebDriver fallback."""
    targets = {
        "FL Pick 3": "https://www.flalottery.com/pick3",
        "GA Pick 3": "https://www.galottery.com/en-us/games/draw-games/cash-3/results.html",
        "PCSO 3D Lotto": "https://www.pcso.gov.ph/SearchLottoResult.aspx",
    }

    for game, link in targets.items():
        try:
            html = titan_webdriver_fetch(link)
            if html:
                print(f"✅ WebDriver success — {game}")
                parsed = adaptive_parse(html, game)
                print(f"🧩 {game}: {len(parsed)} records parsed.")
            else:
                print(f"⚠️ Empty page for {game}")
        except Exception as e:
            print(f"🚫 {game} WebDriver failed: {e}")

print("🌌 Titan WebDriver Bridge v14.2 complete — full JS rendering enabled.")

# ================================================================
# 🌌 Part 8 — Smart Finder + Stealth Bridge Mode v14.3
# ================================================================
import random, time

def smart_find_text(soup, keywords):
    """Tries to find text from multiple possible tags or classes."""
    for key in keywords:
        el = soup.find(lambda tag: tag.name in ["td","div","span","p"] and key.lower() in tag.get_text(strip=True).lower())
        if el:
            return el.get_text(strip=True)
    return None

def titan_auto_fetch_smart():
    print("🧠 Activating Smart Finder + Stealth Bridge...")
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://google.com"
    }

    sites = {
        "Florida": "https://www.flalottery.com/pick3",
        "Georgia": "https://www.galottery.com/en-us/games/draw-games/cash-3.html",
        "PCSO": "https://www.pcso.gov.ph/SearchLottoResult.aspx"
    }

    for state, url in sites.items():
        try:
            print(f"🌍 Fetching {state} data...")
            r = requests.get(url, headers=headers, timeout=10)
            if r.status_code != 200:
                print(f"⚠️ {state} fetch failed: HTTP {r.status_code}")
                continue

            soup = BeautifulSoup(r.text, "html.parser")
            text = smart_find_text(soup, ["Pick 3", "3D", "Results", "Draw", "Winning"])
            if text:
                print(f"✅ {state} found: {text[:80]}...")
            else:
                print(f"⚠️ {state} no recognizable draw data found")

            time.sleep(random.uniform(2.5, 4.5))
        except Exception as e:
            print(f"⚠️ {state} fetch error: {e}")

    print("🌙 Smart Finder Mode complete — stealth fetch finished.")

titan_auto_fetch_smart()

# ================================================================
# 🎯 Part 9 — Titan Result Extractor Engine v14.4
# ================================================================
import re, json

def extract_numbers_from_text(text):
    """Find 3D, 4D, or 5D numbers within mixed website text."""
    patterns = [
        r"\b\d{3}\b",     # 3-digit
        r"\b\d{4}\b",     # 4-digit
        r"\b\d{2}\s\d{2}\s\d{2}\b"  # 6-digit with spaces
    ]
    found = []
    for p in patterns:
        found += re.findall(p, text)
    return list(set(found))

def titan_result_extractor():
    print("🧩 Running Titan Result Extractor Engine v14.4...")
    raw_file = "titan_auto_fetch_raw.json"
    result_file = "titan_results.json"
    extracted_data = {}

    try:
        with open(raw_file, "r") as f:
            raw_data = json.load(f)
    except:
        print("⚠️ No raw auto-fetch data found.")
        return

    for region, text in raw_data.items():
        nums = extract_numbers_from_text(text)
        if nums:
            extracted_data[region] = nums
            print(f"✅ {region}: Extracted {len(nums)} numbers → {nums[:5]}")
        else:
            print(f"⚠️ {region}: No numeric patterns detected.")

    with open(result_file, "w") as f:
        json.dump(extracted_data, f, indent=2)

    print("💾 Extraction complete — results saved to titan_results.json")

titan_result_extractor()





