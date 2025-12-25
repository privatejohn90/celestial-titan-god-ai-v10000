# ==========================================================
# 💎 Celestial Titan God AI v10,000.7
# Energy Pulse Orb + Major Split Edition
# ==========================================================
import streamlit as st
import random, time, json, os
from datetime import datetime
from titan_cloud_sync import titan_auto_background_sync

# 🪐 Start background auto sync every 30 minutes
titan_auto_background_sync(interval=1800)

# ==========================================================
# 🎨 TITAN THEME — Dual-Cosmos (Dark Violet + Glowing Cyan)
# ==========================================================
st.markdown("""
    <style>
        body {background-color:#0e0026 !important;}
        .stApp {background: radial-gradient(circle at 30% 30%, #14003d 0%, #000010 100%);}
        .titan-title {text-align:center; font-size:36px; color:#7df9ff; text-shadow:0 0 25px #7df9ff;}
        .titan-sub {text-align:center; font-size:18px; color:#a98cff; margin-top:-10px;}
        .orb {
            height:100px;width:100px;border-radius:50%;
            background:radial-gradient(circle, #7df9ff, #a98cff);
            box-shadow:0 0 30px #7df9ff; margin:auto;
            animation:pulse 2s infinite;
        }
        @keyframes pulse {
            0% {box-shadow:0 0 15px #7df9ff;}
            50% {box-shadow:0 0 35px #a98cff;}
            100% {box-shadow:0 0 15px #7df9ff;}
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='titan-title'>💠 CELESTIAL TITAN GOD AI v10,000.7</div>", unsafe_allow_html=True)
st.markdown("<div class='titan-sub'>Energy Pulse Orb + Major Split Console</div>", unsafe_allow_html=True)

# ==========================================================
# 🎯 DAILY & MAJOR GAME DEFINITIONS
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
    "TX Pick 3 Morning": 3, "TX Pick 3 Midday": 3, "TX Pick 3 Evening": 3, "TX Pick 3 Night": 3,
    "TX Pick 4 Morning": 4, "TX Pick 4 Midday": 4, "TX Pick 4 Evening": 4, "TX Pick 4 Night": 4
}

major_games = {
    "CA Fantasy 5": 5, "FL Fantasy 5": 5,
    "CA SuperLotto Plus": 5,
    "Powerball": 5, "Mega Millions": 5
}

# ==========================================================
# ⚙️ TITAN FUNCTIONS
# ==========================================================
def generate_forecast(game_type, n):
    if game_type in major_games:
        numbers = sorted(random.sample(range(1, 40), n)) if "Fantasy" in game_type else sorted(random.sample(range(1, 70), n))
        bonus = None
        if "SuperLotto" in game_type:
            bonus = random.randint(1, 27)
        elif "Powerball" in game_type:
            bonus = random.randint(1, 26)
        elif "Mega" in game_type:
            bonus = random.randint(1, 25)
        return numbers, bonus
    else:
        numbers = [random.randint(0, 9) for _ in range(n)]
        return numbers, None

def play_voice():
    if os.path.exists("titan_voice.mp3"):
        st.audio("titan_voice.mp3", format="audio/mp3", start_time=0)

# ==========================================================
# 🌌 TAB SETUP
# ==========================================================
tabs = st.tabs(["🎯 Daily Numbers Console", "💫 Major Games Console"])

# ----------------------------------------------------------
# TAB 1 — DAILY NUMBERS
# ----------------------------------------------------------
with tabs[0]:
    st.subheader("🎯 Daily Numbers Console")
    game = st.selectbox("Select Daily Game", list(daily_games.keys()))
    if st.button("Generate Forecast 🔮", key="daily_forecast"):
        nums, _ = generate_forecast(game, daily_games[game])
        confidence = round(random.uniform(85, 99.9), 1)
        st.write(f"**Titan Forecast:** {' - '.join(map(str, nums))}")
        st.progress(confidence / 100)
        st.write(f"**Confidence:** {confidence} %")

        if confidence >= 95:
            st.markdown("<div class='orb'></div>", unsafe_allow_html=True)
            play_voice()
            st.success("⚡ Strong harmonic resonance detected — triple pattern possible.")
        else:
            st.info("🪶 Normal harmonic state detected.")

# ----------------------------------------------------------
# TAB 2 — MAJOR GAMES
# ----------------------------------------------------------
with tabs[1]:
    st.subheader("💫 Major Games Console")
    game = st.selectbox("Select Major Game", list(major_games.keys()))
    if st.button("Generate Forecast 🎲", key="major_forecast"):
        nums, bonus = generate_forecast(game, major_games[game])
        confidence = round(random.uniform(88, 99.5), 1)

        if "Fantasy" in game:
            st.write(f"**Titan Forecast:** {' - '.join(map(str, nums))}")
        elif bonus:
            st.write(f"**Main:** {' - '.join(map(str, nums))} | **Bonus/Ball:** {bonus}")
        else:
            st.write(f"**Titan Forecast:** {' - '.join(map(str, nums))}")

        st.progress(confidence / 100)
        st.write(f"**Confidence:** {confidence} %")

        if confidence >= 95:
            st.markdown("<div class='orb'></div>", unsafe_allow_html=True)
            play_voice()
            st.success("💎 Jackpot window approaching — high orbital harmony detected.")
        else:
            st.info("🌙 Moderate alignment state.")

# ==========================================================
# ☁️ FOOTER
# ==========================================================
st.markdown("---")
st.markdown(f"<div style='text-align:center;color:#7df9ff;'>☁️ Titan Cloud Sync Active | {datetime.now().strftime('%b %d, %Y %I:%M %p')}<br>Version v10,000.7 • Cosmic Mode ON 🌌</div>", unsafe_allow_html=True)

