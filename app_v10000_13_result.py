# ================================================================
# 💎 Celestial Titan God AI — Result Console v10000.13-R
# ================================================================
import streamlit as st
import json
import os
import datetime
import glob

from titan_utils import load_json, save_json

# ================================================================
# ⚙️ Setup + Paths
# ================================================================
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)
RESULT_FILE = os.path.join(DATA_DIR, "titan_results.json")

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
    "NJ Pick 4": ["Midday", "Evening"],
}

major_games = {
    "CA Fantasy 5": [],
    "CA SuperLotto Plus": [],
    "Mega Millions": [],
    "Powerball": [],
}

ph_games = {
    "PH 3D Lotto (Swertres)": ["2PM", "5PM", "9PM"],
    "PH 4D Lotto": ["Mon", "Wed", "Fri"],
    "PH STL Game": ["10:30AM", "3PM", "7PM"],
}

# ================================================================
# 🎯 UI Header
# ================================================================
st.markdown("## 🎯 Titan Result Console v10000.13-R")
st.caption("📊 Record real results to teach Titan patterns & accuracy")

# -------------------------------
# 🌍 REGION SELECT
# -------------------------------
result_region = st.radio(
    "🌍 Select Region",
    ["US Daily Games", "Major Games", "PH Games"],
    key="result_region_select",
)

# -------------------------------
# 🎮 GAME + DRAW TIME
# -------------------------------
if result_region == "US Daily Games":
    result_game = st.selectbox(
        "🎮 Select US Game",
        list(daily_games.keys()),
        key="result_us_game",
    )
    result_draw_time = st.selectbox(
        "🕓 Draw Time",
        daily_games[result_game],
        key="result_us_draw_time",
    )

elif result_region == "Major Games":
    result_game = st.selectbox(
        "🎮 Select Major Game",
        list(major_games.keys()),
        key="result_major_game",
    )
    result_draw_time = "Main Draw"

else:  # PH Games
    result_game = st.selectbox(
        "🎮 Select PH Game",
        list(ph_games.keys()),
        key="result_ph_game",
    )
    result_draw_time = st.selectbox(
        "🕓 Draw Time",
        ph_games[result_game],
        key="result_ph_draw_time",
    )

# -------------------------
# 📅 DRAW DATE (FIXED)
# -------------------------
st.markdown("### 📅 Draw Date")
result_date = st.date_input(
    "📅 Select Draw Date",
    value=datetime.date.today(),
    key="result_draw_date",
)

# -------------------------------
# 🔢 RESULT INPUT
# -------------------------------
result_number = st.text_input(
    "🔢 Enter Winning Number",
    key="result_number_input",
    help="Example: Pick3=080, Pick4=1172, Fantasy5=1 2 3 4 5, etc.",
)

# -------------------------------
# 💾 SAVE RESULT
# -------------------------------
if st.button("💾 Save Result", key="result_save_btn"):
    if result_number.strip() == "":
        st.warning("⚠️ Please enter a valid winning number.")
    else:
        data = load_json(RESULT_FILE, {})
        if not isinstance(data, dict):
            # safety fallback if old format became list
            data = {}

        entry = {
            "date": result_date.strftime("%Y-%m-%d"),  # ✅ uses selected date
            "draw_time": result_draw_time,
            "number": result_number.strip(),
            "numbers": result_number.strip(),          # ✅ backward/forward safe
            "region": result_region,
            "recorded_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        data.setdefault(result_game, []).append(entry)
        save_json(RESULT_FILE, data)

        st.success(
            f"✅ Result saved for **{result_game} — {result_draw_time}** "
            f"({entry['date']})"
        )

# ================================================================
# 🔄 Titan Auto CSV Sync — Detect & Load New Result Files
# ================================================================
def auto_import_csv_results():
    """
    Looks for CSV files in /data. Accepts columns:
    required: date, game, draw_time, number
    optional: region
    """
    try:
        import pandas as pd
    except Exception:
        st.info("ℹ️ CSV Auto-Sync needs `pandas` installed. Skipping CSV import.")
        return

    csv_files = glob.glob(os.path.join(DATA_DIR, "*.csv"))
    if not csv_files:
        return

    data = load_json(RESULT_FILE, {})
    if not isinstance(data, dict):
        data = {}

    imported_count = 0
    for file in csv_files:
        try:
            df = pd.read_csv(file)

            required = {"date", "game", "draw_time", "number"}
            if not required.issubset(set(df.columns)):
                st.warning(
                    f"⚠️ Skipped `{os.path.basename(file)}` — Missing required columns: "
                    f"{', '.join(sorted(list(required)))}"
                )
                continue

            for _, row in df.iterrows():
                game = str(row.get("game", "")).strip()
                if not game:
                    continue

                entry = {
                    "date": str(row.get("date", "")).strip(),
                    "draw_time": str(row.get("draw_time", "")).strip(),
                    "number": str(row.get("number", "")).strip(),
                    "numbers": str(row.get("number", "")).strip(),
                    "region": str(row.get("region", result_region)).strip() if "region" in df.columns else result_region,
                    "recorded_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "source": f"csv:{os.path.basename(file)}",
                }
                data.setdefault(game, []).append(entry)
                imported_count += 1

            st.info(f"📥 Loaded results from `{os.path.basename(file)}`")

        except Exception as e:
            st.error(f"❌ Failed to load `{os.path.basename(file)}`: {e}")

    if imported_count > 0:
        save_json(RESULT_FILE, data)
        st.success(f"✅ Titan Auto-Sync complete — {imported_count} CSV rows merged into results.")

auto_import_csv_results()

# ================================================================
# 📜 Recent Records (Safe for old JSON formats)
# ================================================================
data = load_json(RESULT_FILE, {})
if isinstance(data, dict) and data:
    st.markdown("## 📜 Recent Results")

    for game, entries in data.items():
        if not isinstance(entries, list) or len(entries) == 0:
            continue

        st.markdown(f"### 🎯 {game}")
        for e in entries[-5:][::-1]:
            date_val = e.get("date", "N/A")
            draw_time = e.get("draw_time", "N/A")
            recorded = e.get("recorded_at", "unknown")
            numbers = e.get("number", e.get("numbers", "N/A"))
            region = e.get("region", "N/A")

            st.markdown(f"- {date_val} ({draw_time}) — `{numbers}` | {region} | saved {recorded}")
else:
    st.info("No results recorded yet. Enter your first result above.")

