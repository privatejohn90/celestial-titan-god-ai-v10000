
# ==========================================================
# 💎 Celestial Titan God AI v8000.0 — Cosmic TrueDraw + Voice Core
# ==========================================================
# Features:
# - TrueDraw format for Powerball, SuperLotto, Fantasy 5
# - Titan Prediction Commentary
# - Aurora Pulse Orb animation
# - Always-on Titan Voice (“Forecast ready — harmonic alignment complete”)
# ==========================================================

import streamlit as st
import random, datetime, json, time
from gtts import gTTS
import os

st.set_page_config(page_title="Celestial Titan God AI v8000.0", page_icon="💎", layout="centered")

# ==========================================================
# 🌌 Aurora UI Design
# ==========================================================
st.markdown("""
    <style>
    body {background: radial-gradient(circle at 20% 20%, #001f3f, #000000);}
    .stButton>button {
        background: linear-gradient(90deg, #00ccff, #66ff99);
        color: black; border-radius: 10px; font-weight: bold;
        box-shadow: 0 0 20px #00ccff;
    }
    .aurora-pulse {
        width: 25px; height: 25px; border-radius: 50%;
        margin: auto; background: radial-gradient(circle, #00ffff 0%, #0066ff 80%);
        animation: pulse 1.5s infinite alternate;
    }
    @keyframes pulse {
        from { box-shadow: 0 0 10px #00ffff; }
        to { box-shadow: 0 0 25px #00ffcc; }
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;color:#66ffff;'>💎 Celestial Titan God AI v8000.0</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;color:#aaa;'>Cosmic TrueDraw Forecast Console + Voice Core</h4>", unsafe_allow_html=True)
st.markdown("<div class='aurora-pulse'></div>", unsafe_allow_html=True)
st.write("")

# ==========================================================
# 🎯 Select Game Type
# ==========================================================
game_type = st.radio("Select Game Category", ["Daily Numbers", "Major Draw Games"])
state = st.selectbox("Select State", ["GA", "FL", "CA"])

# ==========================================================
# 🎰 Game Logic
# ==========================================================
def generate_major_draw(draw_name):
    if draw_name == "Powerball":
        nums = sorted(random.sample(range(1, 70), 5))
        pb = random.randint(1, 26)
        formatted = "-".join([f"{n:02d}" for n in nums]) + f" PB-{pb:02d}"
    elif draw_name == "SuperLotto":
        nums = sorted(random.sample(range(1, 48), 5))
        mega = random.randint(1, 27)
        formatted = "-".join([f"{n:02d}" for n in nums]) + f" + MEGA {mega:02d}"
    elif draw_name == "Fantasy 5":
        nums = sorted(random.sample(range(1, 40), 5))
        formatted = "-".join([f"{n:02d}" for n in nums])
    else:
        formatted = "Invalid Draw"
    return formatted

def titan_commentary(draw_name):
    comments = {
        "Powerball": "Energy synchronized. Strong harmonic resonance detected across high bands.",
        "SuperLotto": "Patterns aligned within the aurora spectrum. Expect radiant outcomes.",
        "Fantasy 5": "Core stability balanced. Short-cycle frequency high today.",
    }
    return comments.get(draw_name, "Cosmic field stable — proceed with focus.")

# ==========================================================
# 🧠 Generate Section
# ==========================================================
if game_type == "Major Draw Games":
    draw = st.selectbox("Select Major Draw", ["Fantasy 5", "SuperLotto", "Powerball"])
    sets = st.slider("Number of Forecast Sets", 1, 5, 3)
    if st.button("🌠 Generate Forecast"):
        st.write(f"✨ **Generated {sets} forecast sets for {state} {draw} — {datetime.date.today()}**")
        for i in range(sets):
            result = generate_major_draw(draw)
            confidence = random.randint(90, 101)
            st.success(f"{result} — Confidence: {confidence}%")
        st.info(f"🎙️ Titan Commentary: {titan_commentary(draw)}")

        # 🔊 Titan Voice (always-on)
        tts = gTTS("Forecast ready — harmonic alignment complete.")
        tts.save("titan_voice.mp3")
        audio_file = open("titan_voice.mp3", "rb")
        st.audio(audio_file.read(), format="audio/mp3")
        audio_file.close()

# ==========================================================
# 🔢 Daily Numbers Mode
# ==========================================================
else:
    state = st.selectbox("Select State for Daily Numbers", ["GA", "FL"])
    draw_type = st.radio("Select Draw Type", ["Midday", "Evening"])
    if st.button("⚡ Generate Daily Forecast"):
        generated = [random.randint(0, 9) for _ in range(3)]
        number = "".join(map(str, generated))
        conf = random.randint(90, 99)
        st.success(f"{state} {draw_type} Pick-3 Forecast: {number} — Confidence {conf}%")
        st.info("🎙️ Titan Commentary: Harmonic stream aligned with short-wave pattern flow.")
        tts = gTTS("Forecast ready — harmonic alignment complete.")
        tts.save("titan_voice.mp3")
        audio_file = open("titan_voice.mp3", "rb")
        st.audio(audio_file.read(), format="audio/mp3")
        audio_file.close()
