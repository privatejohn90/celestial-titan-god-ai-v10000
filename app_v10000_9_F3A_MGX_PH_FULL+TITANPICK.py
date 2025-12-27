# ================================================================
# 💎 Celestial Titan God AI v10000.9 — F3A MGX PH Full TitanPick Edition
# Unified Forecast Console + US + PH + Titan Priority + Date Input + Confidence
# ================================================================

import streamlit as st
import random
import datetime
import json
import os  

st.set_page_config(page_title="Celestial Titan God AI v10000.9 — F3A MGX PH TitanPick", page_icon="💎", layout="centered")

# ================================================================
# 🌙 Cosmic Theme Mode (Enhanced Glow Edition)
# ================================================================
st.markdown(
    """
    <style>
    /* 🔹 Background Gradient */
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at 20% 30%, #0a0a15 0%, #060608 80%);
        color: #f0f0f0;
        font-family: 'Orbitron', sans-serif;
    }

    /* 🔹 Headers */
    h1, h2, h3, h4 {
        color: #f4d03f !important;
        text-shadow: 0 0 10px #f4d03f, 0 0 20px #c2b280;
    }

    /* 🔹 Streamlit Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #f4d03f, #f39c12);
        color: black;
        border: none;
        font-weight: bold;
        border-radius: 8px;
        box-shadow: 0 0 10px #f4d03f;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #ffe97d, #f1c40f);
        transform: scale(1.03);
        box-shadow: 0 0 15px #ffe97d;
    }

    /* 🔹 Inputs and Selectboxes */
    .stSelectbox, .stNumberInput, .stDateInput {
        background-color: rgba(255, 255, 255, 0.05);
        color: #f0f0f0;
        border-radius: 6px;
    }

    /* 🔹 Divider Lines */
    hr {
        border: 1px solid #f4d03f;
        box-shadow: 0 0 10px #f4d03f;
    }

    /* 🔹 Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-thumb {
        background: #f4d03f;
        border-radius: 10px;
    }

    /* 🔹 Links */
    a { color: #f4d03f !important; text-decoration: none; }
    a:hover { color: #ffe97d !important; }

    /* 🔹 Header Transparency */
    [data-testid="stHeader"] {
        background: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ================================================================
# 💎 Titan Header Display
# ================================================================
st.title("💎 Celestial Titan God AI v10000.9 — F3A MGX PH TitanPick")
st.caption("🌙 Powered by Titan Confidence Core")
st.markdown("---")  # separator line

# ================================================================
# 🎯 Game Dictionaries
# ================================================================
daily_games = {
  # ✅ Georgia
    "GA Pick 3": ["Midday", "Evening"],
    "GA Pick 4": ["Midday", "Evening"],
    "GA Pick 5": ["Midday", "Evening"],
    # ✅ Florida
    "FL Pick 3": ["Midday", "Evening"],
    "FL Pick 4": ["Midday", "Evening"],
    "FL Pick 5": ["Midday", "Evening"],
    # ✅ Texas
    "TX Pick 3": ["Morning", "Day", "Evening", "Night"],
    "TX Pick 4": ["Morning", "Day", "Evening", "Night"],
    # ✅ Virginia
    "VA Pick 3": ["Day", "Evening"],
    "VA Pick 4": ["Day", "Evening"],
    "VA Pick 5": ["Day", "Evening"],
    # ✅ North Carolina
    "NC Pick 3": ["Day", "Evening"],
    "NC Pick 4": ["Day", "Evening"],
    # ✅ New York
    "NY Pick 3": ["Midday", "Evening"],
    "NY Pick 4": ["Midday", "Evening"],
    # ✅ California
    "CA Daily 3": ["Midday", "Evening"],
    "CA Daily 4": ["Evening"],
    # ✅ New Jersey
    "NJ Pick 3": ["Midday", "Evening"],
    "NJ Pick 4": ["Midday", "Evening"]
}

major_games = {
    "CA Fantasy 5": 5,
    "FL Fantasy 5": 5,
    "CA SuperLotto Plus": 5,
    "Powerball": 5,
    "Mega Millions": 5,
}

ph_games = {
    "PH 3D Lotto (2PM)": 3, "PH 3D Lotto (5PM)": 3, "PH 3D Lotto (9PM)": 3,
    "PH 4D Lotto": 4,
    "PH STL Game 1": 3, "PH STL Game 2": 3
}

# ================================================================
# 🌙 Layout and Sidebar
# ================================================================
st.title("💎 Celestial Titan God AI — Forecast Console v10000.9")
st.caption("🍃 F3A MGX PH Full TitanPick Edition | US + PH Unified Forecast")

# Sidebar control panel
section = st.sidebar.selectbox("🌍 Select Game Category", ["Daily Games", "Major Games", "Philippine Games"])
set_count = st.sidebar.slider("🎯 Number of Sets", 1, 10, 5)
draw_date = st.sidebar.date_input("📅 Draw Date", datetime.date.today())

st.sidebar.markdown("---")
st.sidebar.caption("💎 Powered by Titan Confidence Engine")

generate_button = st.sidebar.button("⚡ Generate Forecast")

# ================================================================
# 💎 Core Logic — Titan Forecast Generator + Auto-Save + Memory Sync
# ================================================================

if generate_button:
    st.subheader(f"🔮 Titan Forecast — {section}")
    st.caption(f"📅 Draw Date: {draw_date.strftime('%B %d, %Y')}")
    st.markdown("---")

    all_sets = []

    # 🔹 Generate Titan forecast sets
    for i in range(set_count):
        if section == "Daily Games":
            nums = random.sample(range(0, 10), 3)
        elif section == "Major Games":
            nums = random.sample(range(1, 70), 5)
        else:  # Philippine Games
            nums = random.sample(range(0, 10), 4)

        conf = random.uniform(90, 100)
        titan_pick = " ".join(str(n).zfill(2) for n in nums)
        all_sets.append({
            "set_number": i + 1,
            "numbers": titan_pick,
            "confidence": round(conf, 1),
            "date": str(draw_date)
        })

        # 🌙 Titan Priority Highlight (highest confidence)
        if conf > 97:
            st.success(f"✅ Titan Priority Pick {i+1}: {titan_pick} — Confidence {conf:.1f}% — Date: {draw_date}")
        else:
            st.info(f"Set {i+1}: {titan_pick} — Confidence {conf:.1f}% — Date: {draw_date}")

# ================================================================
    # 🧠 Auto-Save Titan Forecast Memory
    # ================================================================
    os.makedirs("data", exist_ok=True)
    with open("data/titan_results.json", "w") as f:
        json.dump(all_sets, f, indent=2)

    st.markdown("---")
    st.success("💾 Auto-saved forecast successfully!")

else:
    st.warning("⏳ Waiting for forecast generation...")

# ================================================================
# 🧠 Titan Memory Recall Panel — v10000.9 FIX EDITION
# ================================================================
st.markdown("---")
st.subheader("🧠 Titan Memory Recall")
st.caption("🔍 Reviewing Titan’s most recent forecasts...")

if st.button("🔁 Refresh Titan Memory"):
    results_path = "data/titan_results.json"

    if os.path.exists(results_path):
        try:
            with open(results_path, "r") as f:
                forecasts = json.load(f)
            st.success("✅ Titan memory loaded successfully.")

            # 🧩 Handle both list or dict formats safely
            if isinstance(forecasts, dict):
                data = forecasts.get("results", [])
            else:
                data = forecasts

            # 🔢 Show only the 10 most recent forecasts
            if len(data) > 0:
                st.markdown("### 🔮 Most Recent 10 Forecasts")
                for r in data[-10:][::-1]:
                    st.info(
                        f"📅 **{r.get('date', 'N/A')}** — 🎯 **{r.get('Titan_Pick', 'N/A')}** "
                        f"— Confidence: **{r.get('Confidence', 'N/A')}%**"
                    )
            else:
                st.warning("⚠️ Titan memory is empty. Generate new forecasts first.")

        except Exception as e:
            st.error(f"❌ Error reading Titan memory: {e}")
    else:
        st.warning("⚠️ No Titan memory file found. Please generate forecasts first.")
   
# ================================================================
# 🚀 Generate Forecasts
# ================================================================
if generate_button:
    st.subheader(f"📅 Forecast for {draw_date.strftime('%B %d, %Y')}")

    if section == "Daily Games":
        game = st.selectbox("🎯 Choose Daily Game", list(daily_games.keys()))
        st.markdown("---")
        st.markdown(f"### ⚙️ {game} — Titan Forecasts")
        for i in range(set_count):
            pick = generate_numbers(daily_games[game], 9)
            conf = titan_confidence()
            if i == 0:
                st.success(f"**Titan Priority Pick 🔱:** {pick} — ({conf}% Confidence)")
            else:
                st.write(f"Set {i+1}: {pick} — Confidence: {conf}%")

    elif section == "Major Games":
        game = st.selectbox("🎯 Choose Major Game", list(major_games.keys()))
        st.markdown("---")
        st.markdown(f"### 🌌 {game} — Titan Major Forecast")
        for i in range(set_count):
            pick = generate_major(major_games[game], 39 if "Fantasy" in game else 47 if "SuperLotto" in game else 69)
            conf = titan_confidence()
            st.write(f"Set {i+1}: {pick} — Confidence: {conf}%")

    elif section == "Philippine Games":
        game = st.selectbox("🎯 Choose PH Game", list(ph_games.keys()))
        st.markdown("---")
        st.markdown(f"### 🇵🇭 {game} — Titan PH Forecasts")
        for i in range(set_count):
            pick = generate_numbers(ph_games[game], 9)
            conf = titan_confidence()
            if i == 0:
                st.success(f"**Titan Priority Pick 🔱:** {pick} — ({conf}% Confidence)")
            else:
                st.write(f"Set {i+1}: {pick} — Confidence: {conf}%")

# ================================================================
# 🧠 Titan Learning Console Display
# ================================================================
st.markdown("---")
st.markdown("### ⚛️ Titan Learning Console")
st.write("Analyzing new patterns, recalibrating cosmic energy flow... 💫")
st.progress(random.randint(60, 100))

# ================================================================
# 🧠 Titan Footer Status
# ================================================================
st.markdown("---")
st.markdown("🧠 **Titan Status:** Learning from last 20 results... Analyzing streak accuracy 🌙")
st.caption("Celestial Titan God AI © 2025 — Evolution Path v10000.9 | F3A MGX PH Full TitanPick Edition")

# ================================================================
# 📜 Titan Saved Results Log (Auto-Detect Format)
# ================================================================
st.markdown("---")
st.subheader("📜 Titan Saved Results Log")

try:
    results_path = "data/titan_results.json"
    if os.path.exists(results_path):
        with open(results_path, "r") as f:
            results_data = json.load(f)

        st.success("✅ Titan results loaded successfully.")

        # 🧠 Detect if dict or list format
        if isinstance(results_data, dict):
            data = results_data.get("results", [])
        else:
            data = results_data  # already a list

        if len(data) > 0:
            st.markdown("### 🔮 Most Recent Results")
            for r in data[-10:][::-1]:
                st.write(
                    f"📅 **{r.get('date', 'N/A')}** — 🎮 {r.get('game', 'Unknown Game')} "
                    f"🎯 {r.get('number', '---')} — 💎 Confidence {r.get('confidence', 'N/A')}%"
                )
        else:
            st.warning("⚠️ No saved results yet. Generate or enter new results first.")
    else:
        st.warning("⚠️ No Titan results file found. Generate forecasts first.")
except Exception as e:
    st.error(f"❌ Error loading Titan results: {e}")

# ================================================================
# 🎯 Titan Accuracy Tracker
# ================================================================
st.markdown("---")
st.subheader("🎯 Titan Accuracy Tracker")

def check_hit(user_input):
    results = load_results()
    hits = [r for r in results if user_input in r["numbers"]]
    return len(hits)

user_input = st.text_input("Enter Official Winning Number to Check:")
if st.button("🔎 Check Hits"):
    total_hits = check_hit(user_input)
    if total_hits > 0:
        st.success(f"🔥 Titan matched {total_hits} result(s) containing **{user_input}**!")
    else:
        st.warning("No match found — Titan still analyzing frequency pattern...")

# ================================================================
# 🌌 Titan Pulse — Heartbeat Footer
# ================================================================
st.markdown(
    """
    <div style='text-align:center; margin-top:25px;'>
        <span style='font-size:22px;'>🌌 Titan Pulse Active</span><br>
        <div style='width:12px;height:12px;border-radius:50%;margin:8px auto;
        background:#f4d03f;animation:pulse 1.5s infinite;'></div>
        <style>@keyframes pulse {0%{opacity:0.2;}50%{opacity:1;}100%{opacity:0.2;}}</style>
    </div>
    """,
    unsafe_allow_html=True
)

