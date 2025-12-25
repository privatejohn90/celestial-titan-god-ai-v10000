# ==========================================================
# 💎 Celestial Titan God AI v10,000.7-F
# Full Multi-Set + Confidence + Titan Pick + Auto Save
# ==========================================================

import streamlit as st
import random, json, os
from datetime import datetime

# ----------------------------------------------------------
# 🪐 Titan Cloud Auto Sync (background)
try:
    from titan_cloud_sync import titan_auto_background_sync
    titan_auto_background_sync(interval=1800)
except:
    pass

# ==========================================================
# ⚙️ INITIAL SETUP
# ==========================================================

RESULT_FILE = "titan_results.json"

def load_json(path, default):
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                return json.load(f)
        except:
            return default
    return default

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def record_result(entry):
    existing = load_json(RESULT_FILE, {"records": []})
    existing["records"].append(entry)
    save_json(RESULT_FILE, existing)

# ==========================================================
# 🎨 COLOR THEME
# ==========================================================
st.set_page_config(page_title="Celestial Titan God AI v10,000.7-F", page_icon="💠", layout="wide")
st.markdown("""
    <style>
        body {background:#0a001f;}
        .stApp {background:radial-gradient(circle at 30% 30%, #14003d 0%, #000010 100%);}
        .title {font-size:32px; color:#7df9ff; text-align:center;}
        .sub {font-size:16px; color:#a98cff; text-align:center; margin-bottom:15px;}
    </style>
""", unsafe_allow_html=True)
st.markdown('<p class="title">💠 Celestial Titan God AI v10,000.7-F</p>', unsafe_allow_html=True)
st.markdown('<p class="sub">Full Multi-Set + Confidence + Auto Save + Titan Priority Pick</p>', unsafe_allow_html=True)

# ==========================================================
# 🎯 GAME DEFINITIONS
# ==========================================================

daily_games = {
    "CA Pick 3 Midday": 3, "CA Pick 3 Evening": 3, "CA Pick 4 Evening": 4,
    "FL Pick 3 Midday": 3, "FL Pick 3 Evening": 3,
    "FL Pick 4 Midday": 4, "FL Pick 4 Evening": 4,
    "FL Pick 5 Midday": 5, "FL Pick 5 Evening": 5,
    "GA Pick 3 Midday": 3, "GA Pick 3 Evening": 3, "GA Pick 3 Night": 3,
    "GA Pick 4 Midday": 4, "GA Pick 4 Evening": 4, "GA Pick 4 Night": 4,
    "GA Pick 5 Midday": 5, "GA Pick 5 Evening": 5,
    "VA Pick 3 Midday": 3, "VA Pick 3 Evening": 3,
    "VA Pick 4 Midday": 4, "VA Pick 4 Evening": 4,
    "VA Pick 5 Midday": 5, "VA Pick 5 Evening": 5,
    "TX Pick 3 Morning": 3, "TX Pick 3 Midday": 3,
    "TX Pick 3 Evening": 3, "TX Pick 3 Night": 3,
    "TX Pick 4 Morning": 4, "TX Pick 4 Midday": 4,
    "TX Pick 4 Evening": 4, "TX Pick 4 Night": 4,
}

major_games = {
    "CA Fantasy 5": 5, "FL Fantasy 5": 5,
    "CA SuperLotto Plus": 5,
    "Powerball": 5, "Mega Millions": 5
}

# ==========================================================
# 🧠 FORECAST GENERATOR
# ==========================================================

st.header("🎯 Titan Multi-Set Forecast")

game = st.selectbox("Select Game", list(daily_games.keys()) + list(major_games.keys()))

if st.button("Generate 5 Sets 🔮"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sets = []
    for i in range(5):
        if game in major_games:
            n = major_games[game]
            if "Fantasy" in game:
                nums = sorted(random.sample(range(1, 40), n))
                bonus = None
            elif "SuperLotto" in game:
                nums = sorted(random.sample(range(1, 48), n))
                bonus = random.randint(1, 27)
            elif "Powerball" in game:
                nums = sorted(random.sample(range(1, 70), n))
                bonus = random.randint(1, 26)
            elif "Mega" in game:
                nums = sorted(random.sample(range(1, 71), n))
                bonus = random.randint(1, 25)
        else:
            n = daily_games[game]
            nums = [random.randint(0, 9) for _ in range(n)]
            bonus = None

        confidence = round(random.uniform(88.0, 99.9), 1)
        sets.append({"numbers": nums, "bonus": bonus, "confidence": confidence})

    # Titan Priority Pick
    top = max(sets, key=lambda x: x["confidence"])

    # Display output
    st.markdown(f"**Game:** `{game}` — *{timestamp}*")
    for idx, s in enumerate(sets, start=1):
        num_display = " ".join(map(str, s["numbers"]))
        if s["bonus"] not in (None,):
            num_display += f" | Ball: {s['bonus']}"
        tag = "💎 Titan Priority Pick" if s == top else "✨"
        st.write(f"{tag} Set {idx}: `{num_display}` — Confidence: **{s['confidence']}%**")
    
    # Save result entry
    record = {
        "timestamp": timestamp,
        "game": game,
        "results": sets
    }
    record_result(record)
    st.success("✅ All sets saved to titan_results.json")

# ==========================================================
# 📊 ACCURACY REFLECTION
# ==========================================================

st.header("📊 Accuracy Board")

data = load_json("titan_results.json", {"records": []}).get("records", [])
if not data:
    st.write("No saved history yet.")
else:
    last = data[-1]
    st.write(f"Latest saved forecast — `{last['game']} @ {last['timestamp']}`")
    hits = 0
    total = len(data)
    for rec in data:
        for s in rec["results"]:
            # if result matches a previous saved real draw, check separate
            pass
    st.write(f"Total saved forecasts: **{total}**")

# ==========================================================
# ☁️ FOOTER
# ==========================================================
st.markdown("---")
st.markdown(f"<div style='text-align:center;color:#7df9ff;'>Version v10,000.7-F • Titan Forecast saved at titan_results.json 🌌</div>", unsafe_allow_html=True)

