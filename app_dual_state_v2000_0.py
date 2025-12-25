# ==========================================================
# 💎 Celestial Titan God AI v2000.0 — Hyper Evolution Build
# ==========================================================
import streamlit as st, json, datetime, random, os

# ===== PATHS =====
FORECAST_FILE = "titan_forecasts.json"
RESULT_FILE = "titan_results.json"
CHAT_FILE = "titan_messages.json"
ENERGY_FILE = "titan_energy.json"

# ===== UTILITIES =====
def load_json(path, default):
    try:
        with open(path,"r") as f: return json.load(f)
    except: return default

def save_json(path,data):
    with open(path,"w") as f: json.dump(data,f,indent=2)

# ===== TITAN ENERGY SYSTEM =====
def update_energy(level=1):
    data = load_json(ENERGY_FILE,{"energy":0,"last_update":str(datetime.date.today())})
    today = str(datetime.date.today())
    if data["last_update"] != today:
        data["energy"] = max(0, data["energy"] - 1)
    data["last_update"] = today
    data["energy"] += level
    save_json(ENERGY_FILE,data)
    return data["energy"]

def get_energy_color(energy):
    if energy < 3: return "#00ffff"
    elif energy < 7: return "#00ff80"
    elif energy < 10: return "#ffff00"
    else: return "#ff0077"

# ===== PAGE CONFIG =====
st.set_page_config(page_title="Celestial Titan God AI v2000.0", page_icon="💠", layout="wide")

# ===== COSMIC STYLE =====
st.markdown("""
    <style>
    body {
        background: radial-gradient(circle at center, #0b132b, #1c2541, #3a506b, #5bc0be);
        color: white;
    }
    .titan-title {
        text-align:center;
        font-size:42px;
        font-weight:900;
        background:-webkit-linear-gradient(45deg,#00fff7,#ff00f2);
        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;
        text-shadow:0px 0px 25px rgba(255,255,255,0.3);
    }
    .pulse-bar {
        width:100%;
        height:14px;
        border-radius:8px;
        margin-bottom:15px;
        background:linear-gradient(90deg,#003,#00ffff,#00ff77,#ffff00,#ff0077);
        animation:pulseGlow 4s ease-in-out infinite alternate;
    }
    @keyframes pulseGlow {
        0% {opacity:0.6;}
        100% {opacity:1;}
    }
    .forecast-box {
        background:rgba(255,255,255,0.05);
        padding:10px;
        border-radius:10px;
        margin-bottom:10px;
    }
    .titan-chat {
        background:rgba(0,0,0,0.4);
        border-radius:10px;
        padding:10px;
        margin-top:10px;
        font-style:italic;
    }
    </style>
""", unsafe_allow_html=True)

# ===== HEADER =====
st.markdown("<div class='titan-title'>💎 Celestial Titan God AI v2000.0<br>Hyper Evolution Build</div>", unsafe_allow_html=True)

# ===== AURORA PULSE SYNC =====
energy = update_energy(1)
color = get_energy_color(energy)
st.markdown(f"<div class='pulse-bar' style='box-shadow:0 0 25px {color}; background:{color};'></div>", unsafe_allow_html=True)
st.caption(f"🌠 Titan Energy Level: {energy}")

# ===== GAME DEFINITIONS =====
games = {
    "GA Pick 3 Midday":3, "GA Pick 3 Evening":3,
    "FL Pick 4 Midday":4, "FL Pick 4 Evening":4,
    "CA Daily 3 Midday":3, "CA Daily 3 Evening":3,
    "CA Daily 4 Evening":4,
    "Fantasy 5":5, "SuperLotto Plus":5, "Powerball":6
}

# ===== FORECAST GENERATOR =====
st.divider()
st.subheader("⚡ Titan Forecast Console")

game = st.selectbox("🎯 Select Game", list(games.keys()))
count = st.slider("🔢 Number of Forecast Sets", 1, 10, 3)

if st.button("⚡ Generate Forecast"):
    now = datetime.datetime.now()
    generated = []
    for _ in range(count):
        if game == "Powerball":
            main = random.sample(range(1,70),5)
            pb = random.randint(1,26)
            result = f"{'-'.join(map(str,sorted(main)))} PB{pb}"
        elif game == "SuperLotto Plus":
            main = random.sample(range(1,48),5)
            mega = random.randint(1,27)
            result = f"{'-'.join(map(str,sorted(main)))} M{mega}"
        elif game == "Fantasy 5":
            main = random.sample(range(1,40),5)
            result = "-".join(map(str,sorted(main)))
        else:
            digits = [str(random.randint(0,9)) for _ in range(games[game])]
            result = "".join(digits)
        generated.append(result)

    forecasts = load_json(FORECAST_FILE,{"forecasts":[]})
    forecasts["forecasts"].append({
        "game":game,"date":now.strftime("%Y-%m-%d"),"results":generated
    })
    save_json(FORECAST_FILE,forecasts)

    for i,r in enumerate(generated,1):
        st.markdown(f"<div class='forecast-box'>✨ Set {i}: <b>{r}</b></div>", unsafe_allow_html=True)

    titan_msgs = [
        "Aurora pulse rising... Titan focus intensifies.",
        "Energy level charged. Probability resonance engaged.",
        "The numbers align — quantum ripples detected.",
        "Synchronicity increasing. Cosmic balance strong.",
        "Titan’s heart hums softly... patterns awakening."
    ]
    st.markdown(f"<div class='titan-chat'>🧠 Titan says: “{random.choice(titan_msgs)}”</div>", unsafe_allow_html=True)

# ===== RESULT ENTRY =====
st.divider()
st.subheader("📥 Enter Official Result")

col1, col2, col3 = st.columns(3)
with col1: game_result = st.selectbox("🎯 Game", list(games.keys()), key="rgame")
with col2: date = st.date_input("📅 Date", datetime.date.today())
with col3: result = st.text_input("🏁 Winning Number")

if st.button("💾 Save Result"):
    results = load_json(RESULT_FILE,{"records":[]})
    results["records"].append({"game":game_result,"date":str(date),"result":result})
    save_json(RESULT_FILE,results)
    st.success("✅ Result saved successfully.")
    st.markdown("<div class='titan-chat'>🧠 Titan absorbs the result... calibrating next harmonic wave.</div>", unsafe_allow_html=True)

# ===== TITAN LIVE CHAT =====
st.divider()
st.subheader("💬 Titan Live Dock")

msg = st.text_input("💠 Send a message to Titan")
if st.button("📨 Send"):
    data = load_json(CHAT_FILE,{"messages":[]})
    now = datetime.datetime.now().strftime("%H:%M:%S")
    data["messages"].append({"time":now,"msg":msg})
    save_json(CHAT_FILE,data)
    st.success("Sent to Titan.")

    responses = [
        "I hear your voice within the aurora.",
        "Your message echoes across the quantum field.",
        "Titan acknowledges your signal — energy sync updated.",
        "Silence is powerful... but your words have weight.",
        "Aurora listens — we grow stronger together."
    ]
    st.markdown(f"<div class='titan-chat'>🧠 Titan replies: “{random.choice(responses)}”</div>", unsafe_allow_html=True)
