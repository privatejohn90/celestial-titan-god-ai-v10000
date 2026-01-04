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
    "FL Pick 3": ["Midday", "Evening"],
    "FL Pick 4": ["Midday", "Evening"],
    "TX Pick 3": ["Morning", "Day", "Evening", "Night"],
    "TX Pick 4": ["Morning", "Day", "Evening", "Night"],
    "VA Pick 3": ["Day", "Evening"],
    "VA Pick 4": ["Day", "Evening"],
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
# 🎯 Titan Result Console — Fixed with Unique Keys + 8-State Support
# ================================================================
st.markdown("## 🎯 Titan Result Console v10000.13-R")
st.caption("📊 Record real results to teach Titan patterns & accuracy")

# --- Select Region / State ---
region = st.radio("🌎 Select Region", ["US Daily Games", "Major Games", "PH Games"], key="result_region")

if region == "US Daily Games":
    selected_state = st.selectbox(
        "🏛 Select State",
        ["California", "Georgia", "Florida", "Texas", "New York", "North Carolina", "New Jersey", "Virginia"],
        key="result_state"
    )
    game = st.selectbox("🎮 Choose US Game", list(daily_games.keys()), key="result_us_game")
    draw_time = st.selectbox("🕓 Draw Time", daily_games[game], key="result_us_draw")

elif region == "Major Games":
    game = st.selectbox("💰 Choose Major Game", list(major_games.keys()), key="result_major_game")
    draw_time = "Main Draw"
    selected_state = "N/A"

else:
    game = st.selectbox("🇵🇭 Choose PH Game", list(ph_games.keys()), key="result_ph_game")
    draw_time = st.selectbox("🕓 Draw Time", ph_games[game], key="result_ph_draw")
    selected_state = "PH"

# --- Input Result Numbers ---
result_numbers = st.text_input("🎟 Enter Winning Numbers (e.g. 583, 1543, 9541)", key="result_numbers")
draw_date = st.date_input("📅 Draw Date", datetime.date.today(), key="result_date")

# --- Save Button ---
if st.button("💾 Save Result", key="save_result_btn"):
    data = load_json(RESULT_FILE, {})
    game_data = data.get(game, [])

    entry = {
        "state": selected_state,
        "region": region,
        "date": draw_date.strftime("%B %d, %Y"),
        "draw_time": draw_time,
        "numbers": result_numbers.strip(),
        "recorded_at": datetime.datetime.now().strftime("%I:%M %p"),
    }

    game_data.append(entry)
    data[game] = game_data
    save_json(RESULT_FILE, data)

    st.success(f"✅ Result saved for {game} ({selected_state}) — {draw_time}: {result_numbers}")


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

