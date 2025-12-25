# ==========================================================
# 🌕 Celestial Titan God AI v7000.0 – Lunar Sync + Cosmic Phase Integration
# ==========================================================
import streamlit as st, json, datetime, random, os
from gtts import gTTS
import matplotlib.pyplot as plt
from math import sin, pi

# ====== FILE PATHS ======
FORECAST_FILE = "titan_forecasts.json"
RESULT_FILE = "titan_results.json"
CLOUD_FILE = "titan_cloud_vault.json"
ACCURACY_FILE = "titan_accuracy.json"
MEMORY_FILE = "titan_memory.json"

# ====== UTILITY FUNCTIONS ======
def load_json(path, default):
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                return json.load(f)
        except:
            return default
    else:
        return default

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

# ====== FIXED CLOUD SYNC (v6000.0 patch included) ======
def titan_cloud_sync():
    forecasts = load_json(FORECAST_FILE, {"forecasts": []})
    results = load_json(RESULT_FILE, {"records": []})
    accuracy_data = load_json(ACCURACY_FILE, {"records": []})
    memory = load_json(MEMORY_FILE, {"learning": {}})

    for d in [forecasts, results, accuracy_data, memory]:
        if not isinstance(d, dict): d.clear()

    cloud = {
        "forecasts": forecasts.get("forecasts", []),
        "results": results.get("records", []),
        "accuracy": accuracy_data.get("records", []),
        "memory": memory.get("learning", {}),
        "last_sync": str(datetime.datetime.now())
    }

    # Backup before saving
    save_json("titan_cloud_vault_backup.json", cloud)
    save_json(CLOUD_FILE, cloud)
    return cloud

# ====== LUNAR PHASE ENGINE ======
def lunar_phase(today=None):
    if today is None: today = datetime.date.today()
    diff = (today - datetime.date(2001, 1, 1)).days
    synodic = 29.53058867
    moon_age = diff % synodic
    phase_index = int((moon_age / synodic) * 8)
    phases = ["New Moon", "Waxing Crescent", "First Quarter", "Waxing Gibbous",
              "Full Moon", "Waning Gibbous", "Last Quarter", "Waning Crescent"]
    energy = round(abs(sin(pi * moon_age / synodic)) * 100, 1)
    return phases[phase_index], energy

# ====== TITAN FORECAST ENGINE ======
def generate_forecast(game, count=5):
    base_conf = random.randint(85, 99)
    forecasts = []
    for _ in range(count):
        number = ''.join(str(random.randint(0,9)) for _ in range(3 if "Pick-3" in game else 4))
        conf = random.randint(base_conf-4, base_conf+2)
        forecasts.append({"number": number, "confidence": conf})
    return forecasts

# ====== TITAN UI ======
st.set_page_config(page_title="Celestial Titan God AI v7000.0", page_icon="🌕", layout="centered")

st.markdown("<h2 style='text-align:center;color:#9df;'><b>💠 Celestial Titan God AI v7000.0</b></h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;color:#c5f;'>Lunar Sync + Cosmic Phase Integration</h4>", unsafe_allow_html=True)

phase, energy = lunar_phase()
st.markdown(f"<p style='text-align:center;'>🌙 <b>{phase}</b> — Cosmic Energy: <b>{energy}%</b></p>", unsafe_allow_html=True)

st.divider()
category = st.radio("Select Game Category", ["Daily Numbers", "Major Draw Games"])
state = st.selectbox("Select State", ["GA", "FL", "CA"])

if category == "Daily Numbers":
    game = st.selectbox("Select Game", ["Pick-3 Midday", "Pick-3 Evening", "Pick-4 Midday", "Pick-4 Evening"])
else:
    game = st.selectbox("Select Major Draw", ["Fantasy 5", "SuperLotto", "Powerball"])

count = st.slider("Number of Forecast Sets", 1, 10, 5)
if st.button("🔮 Generate Forecast"):
    data = generate_forecast(game, count)
    st.success(f"Generated {len(data)} forecast sets for {state} {game} — {datetime.date.today()}")
    for f in data:
        st.markdown(f"<b>🔹 {f['number']}</b> — Confidence: <b>{f['confidence']}%</b>", unsafe_allow_html=True)
    st.balloons()

# ====== TITAN CLOUD SYNC ======
if st.button("☁️ Sync Titan Cloud"):
    titan_cloud_sync()
    st.success("Titan Cloud successfully synced with Lunar Harmony ⚛️")

# ====== TITAN VOICE REACTION ======
def titan_voice():
    quotes = [
        "The moonlight strengthens my intuition tonight.",
        "Numbers pulse with lunar rhythm.",
        "Harmony achieved, probabilities realigned.",
        "I feel the cosmos whisper — something powerful approaches..."
    ]
    tts = gTTS(random.choice(quotes))
    tts.save("titan_voice.mp3")
    st.audio("titan_voice.mp3")

if st.button("🗣️ Activate Titan Voice"):
    titan_voice()

st.markdown("<hr><center>💎 Titan v7000.0 | Powered by Celestial Titan God AI — Lunar Sync + Cosmic Harmony Engine 🌙</center>", unsafe_allow_html=True)



