# ================================================================
# 💎 Celestial Titan God AI — Result Console v10000.13-R
# ================================================================
import streamlit as st
import json, os, datetime
from titan_utils import load_json, save_json

# ================================================================
# ⚙️ Setup + Paths
# ================================================================
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)
RESULT_FILE = os.path.join(DATA_DIR, "titan_results.json")

st.markdown("## 🎯 Titan Result Console v10000.13-R")
st.caption("📊 Record real results to teach Titan patterns & accuracy")

# ================================================================
# 🎯 Game Dictionaries — Full Multi-Region
# ================================================================
daily_games = {
    "GA Pick 3": ["Midday", "Evening", "Night"],
    "GA Pick 4": ["Midday", "Evening", "Night"],
    "GA Pick 5": ["Midday", "Evening"],

    "FL Pick 3": ["Midday", "Evening", "Night"],
    "FL Pick 4": ["Midday", "Evening", "Night"],
    "FL Pick 5": ["Midday", "Evening"],

    "TX Pick 3": ["Morning", "Day", "Evening", "Night"],
    "TX Pick 4": ["Morning", "Day", "Evening", "Night"],

    "VA Pick 3": ["Day", "Evening"],
    "VA Pick 4": ["Day", "Evening"],
    "VA Pick 5": ["Day", "Evening"],

    "NC Pick 3": ["Day", "Evening"],
    "NC Pick 4": ["Day", "Evening"],

    "NY Pick 3": ["Midday", "Evening"],
    "NY Pick 4": ["Midday", "Evening"],

    "CA Daily 3": ["Midday", "Evening"],
    "CA Daily 4": ["Evening"],
   
    "NJ Pick 3": ["Midday", "Evening"],
    "NJ Pick 4": ["Midday", "Evening"]
}

major_games = {
    "CA Fantasy 5": [],
    "CA SuperLotto Plus": [],
    "Mega Millions": [],
    "Powerball": []
}

ph_games = {
    "PH 3D Lotto (Swertres)": ["2PM", "5PM", "9PM"],
    "PH 4D Lotto": ["Mon", "Wed", "Fri"],
    "PH STL Game": ["10:30AM", "3PM", "7PM"]
}

# ================================================================
# 🎯 Titan Result Console — FINAL FIX (Midday / Evening / Night)
# ================================================================
import streamlit as st
import json, os, datetime

st.markdown("## 🎯 Titan Result Console")
st.caption("📊 Record real results to teach Titan patterns")

# ================================================================
# 📁 Paths
# ================================================================
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)
RESULT_FILE = os.path.join(DATA_DIR, "titan_results.json")

def load_json(path, default):
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump(default, f, indent=2)
        return default
    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        return default

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

# ================================================================
# 🎯 GAME DEFINITIONS (IMONG GI-HATAG — WALAY GIUSAB)
# ================================================================
daily_games = {
    "GA Pick 3": ["Midday", "Evening", "Night"],
    "GA Pick 4": ["Midday", "Evening", "Night"],
    "GA Pick 5": ["Midday", "Evening"],

    "FL Pick 3": ["Midday", "Evening", "Night"],
    "FL Pick 4": ["Midday", "Evening", "Night"],
    "FL Pick 5": ["Midday", "Evening"],

    "TX Pick 3": ["Morning", "Day", "Evening", "Night"],
    "TX Pick 4": ["Morning", "Day", "Evening", "Night"],

    "VA Pick 3": ["Day", "Evening"],
    "VA Pick 4": ["Day", "Evening"],
    "VA Pick 5": ["Day", "Evening"],

    "NC Pick 3": ["Day", "Evening"],
    "NC Pick 4": ["Day", "Evening"],

    "NY Pick 3": ["Midday", "Evening"],
    "NY Pick 4": ["Midday", "Evening"],

    "CA Daily 3": ["Midday", "Evening"],
    "CA Daily 4": ["Evening"],

    "NJ Pick 3": ["Midday", "Evening"],
    "NJ Pick 4": ["Midday", "Evening"]
}

# ================================================================
# 🧭 UI
# ================================================================
game = st.selectbox(
    "🎮 Choose Game",
    list(daily_games.keys()),
    key="result_game"
)

draw_time = st.selectbox(
    "🕓 Draw Time",
    daily_games[game],   # ✅ Midday / Evening / Night automatic
    key="result_draw_time"
)

result_numbers = st.text_input(
    "🎟 Enter Winning Numbers (e.g. 583 / 1543 / 95413)",
    key="result_numbers"
)

draw_date = st.date_input(
    "📅 Draw Date",
    datetime.date.today(),
    key="result_date"
)

# ================================================================
# 💾 SAVE
# ================================================================
if st.button("💾 Save Result", key="save_result"):
    data = load_json(RESULT_FILE, {})
    data.setdefault(game, []).append({
        "date": draw_date.strftime("%Y-%m-%d"),
        "draw_time": draw_time,
        "numbers": result_numbers.strip(),
        "saved_at": datetime.datetime.now().strftime("%H:%M:%S")
    })
    save_json(RESULT_FILE, data)

    st.success(f"✅ Saved: {game} — {draw_time} — {result_numbers}")

# ================================================================
# 🔄 Titan Auto CSV Sync — Detect & Load New Result Files
# ================================================================
import glob
import pandas as pd

def auto_import_csv_results():
    csv_files = glob.glob(os.path.join(DATA_DIR, "*.csv"))
    if not csv_files:
        return None

    merged_data = []
    for file in csv_files:
        try:
            df = pd.read_csv(file)
            if all(col in df.columns for col in ["date", "game", "draw_time", "numbers"]):
                merged_data.extend(df.to_dict(orient="records"))
                st.info(f"📥 Loaded results from `{os.path.basename(file)}`")
            else:
                st.warning(f"⚠️ Skipped `{os.path.basename(file)}` — Invalid columns")
        except Exception as e:
            st.error(f"❌ Failed to load `{os.path.basename(file)}`: {e}")

    if merged_data:
        results_data = load_json(RESULT_FILE, [])
        results_data.extend(merged_data)
        save_json(RESULT_FILE, results_data)
        st.success("✅ Titan Auto-Sync complete — CSV results merged into titan_results.json")

auto_import_csv_results()

# ================================================================
# 📜 Recent Records (Safe for old JSON formats)
# ================================================================
data = load_json(RESULT_FILE, {})
if data:
    st.markdown("## 📜 Recent Results")
    for game, entries in data.items():
        st.markdown(f"### 🎯 {game}")
        for e in entries[-5:][::-1]:
            draw_time = e.get("draw_time", "N/A")
            recorded = e.get("recorded_at", "unknown")
            numbers = e.get("numbers", "N/A")
            date = e.get("date", "N/A")
            st.markdown(f"- {date} ({draw_time}): `{numbers}` — saved {recorded}")
else:
    st.info("No results recorded yet. Enter your first result above.")

