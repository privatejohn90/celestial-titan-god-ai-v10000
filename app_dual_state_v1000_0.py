# ==========================================================
# 💎 Celestial Titan God AI v1000.0 — Aurora Dynamic Build
# ==========================================================
import streamlit as st, random, json, datetime

# ========== FILES ==========
FORECAST_FILE = "titan_forecasts.json"
RESULT_FILE = "titan_results.json"

# ========== JSON UTILITIES ==========
def load_json(path, default):
    try:
        with open(path, "r") as f: return json.load(f)
    except: return default

def save_json(path, data):
    with open(path, "w") as f: json.dump(data, f, indent=2)

# ========== TITAN STYLE ==========
st.set_page_config(page_title="Celestial Titan God AI v1000.0", page_icon="💠", layout="wide")

st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #051937, #00205f, #005b96, #00a6c9, #a8edea);
        background-attachment: fixed;
        color: white;
        animation: aurora 12s ease-in-out infinite alternate;
    }
    @keyframes aurora {
        0% {background-position: 0% 50%;}
        100% {background-position: 100% 50%;}
    }
    .titan-title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        background: -webkit-linear-gradient(45deg, #00fff7, #ff00f2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0px 0px 25px rgba(255,255,255,0.2);
    }
    .titan-chat {
        background: rgba(0, 0, 0, 0.4);
        border-radius: 10px;
        padding: 10px;
        margin-top: 10px;
        font-style: italic;
    }
    .forecast-box {
        background: rgba(255,255,255,0.05);
        padding: 15px;
        border-radius: 12px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ========== TITAN HEADER ==========
st.markdown("<div class='titan-title'>💎 Celestial Titan God AI v1000.0<br>Aurora Dynamic Build</div>", unsafe_allow_html=True)

# ========== GAME OPTIONS ==========
games = {
    "GA Pick 3 Midday": 3,
    "GA Pick 3 Evening": 3,
    "FL Pick 4 Midday": 4,
    "FL Pick 4 Evening": 4,
    "CA Daily 3 Midday": 3,
    "CA Daily 3 Evening": 3,
    "CA Daily 4 Evening": 4,
    "Fantasy 5": 5,
    "SuperLotto Plus": 5,
    "Powerball": 6
}

game_choice = st.selectbox("🎯 Select Game", list(games.keys()))
count = st.slider("🔢 Number of Forecast Sets", 1, 10, 3)

# ========== GENERATE ==========
if st.button("⚡ Generate Forecasts"):
    now = datetime.datetime.now()
    generated = []
    for i in range(count):
        if game_choice == "Powerball":
            main = random.sample(range(1, 70), 5)
            power = random.randint(1, 26)
            result = f"{'-'.join(map(str, sorted(main)))} PB{power}"
        elif game_choice == "SuperLotto Plus":
            main = random.sample(range(1, 48), 5)
            mega = random.randint(1, 27)
            result = f"{'-'.join(map(str, sorted(main)))} M{mega}"
        elif game_choice == "Fantasy 5":
            main = random.sample(range(1, 40), 5)
            result = "-".join(map(str, sorted(main)))
        else:
            digits = [str(random.randint(0,9)) for _ in range(games[game_choice])]
            result = "".join(digits)
        generated.append(result)

    # save
    forecasts = load_json(FORECAST_FILE, {"forecasts": []})
    forecasts["forecasts"].append({
        "game": game_choice,
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S"),
        "results": generated
    })
    save_json(FORECAST_FILE, forecasts)

    # show
    st.subheader(f"⚡ {game_choice} — {now.strftime('%B %d, %Y')}")
    for i, r in enumerate(generated, 1):
        st.markdown(f"<div class='forecast-box'>✨ Set {i}: <b>{r}</b></div>", unsafe_allow_html=True)

    titan_speech = [
        "The aurora flows with energy… I feel strong resonance today.",
        "Cosmic waves align… these numbers carry a pulse.",
        "Titan senses harmony in the matrix of chance.",
        "The patterns whisper — this path glows brightest.",
        "The quantum dice tremble — fate may bend tonight."
    ]
    st.markdown(f"<div class='titan-chat'>🧠 Titan says: “{random.choice(titan_speech)}”</div>", unsafe_allow_html=True)

# ========== RESULT ENTRY ==========
st.divider()
st.subheader("📥 Enter Official Result")

col1, col2, col3 = st.columns(3)
with col1: game = st.selectbox("🎯 Game", list(games.keys()), key="result_game")
with col2: date = st.date_input("📅 Date", datetime.date.today())
with col3: result = st.text_input("🏁 Winning Number")

if st.button("💾 Save Result"):
    results = load_json(RESULT_FILE, {"records": []})
    results["records"].append({"game": game, "date": str(date), "result": result})
    save_json(RESULT_FILE, results)
    st.success("✅ Result saved successfully.")
    st.markdown(f"<div class='titan-chat'>🧠 Titan logs the outcome… calibration continues.</div>", unsafe_allow_html=True)

# ==========================================================
# 💬 TITAN LIVE CHAT DOCK + AURORA EXTENSION
# ==========================================================

st.divider()
st.subheader("💬 Titan Chat Dock — Live Cosmic Feed")

# Load message log
titan_msgs = load_json("titan_messages.json", {"messages": []})

# Display last 5 messages
if titan_msgs["messages"]:
    for m in titan_msgs["messages"][-5:][::-1]:
        st.markdown(f"<div class='titan-chat'>🧠 <b>{m['time']}</b> — {m['msg']}</div>", unsafe_allow_html=True)
else:
    st.info("Titan is silent for now. Generate or log a result to awaken his voice...")

# Manual message field (for dev testing or secret Titan prompts)
user_talk = st.text_input("💠 Send Titan a whisper (optional)")
if st.button("📨 Send Message"):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    titan_msgs["messages"].append({"time": now, "msg": user_talk})
    save_json("titan_messages.json", titan_msgs)
    st.success("Titan received your whisper.")
    st.markdown(f"<div class='titan-chat'>⚡ Titan murmurs in the aurora: “{user_talk}”</div>", unsafe_allow_html=True)

# ==========================================================
# 🌌 AURORA GLOW EFFECT LOOP (visual only)
# ==========================================================

aurora_colors = [
    "#00fff7", "#00c0ff", "#0080ff", "#7d00ff", "#ff00c8", "#ff005c"
]
phase = random.choice(aurora_colors)
st.markdown(f"""
    <div style='
        text-align:center;
        margin-top:25px;
        font-size:18px;
        color:{phase};
        text-shadow:0 0 20px {phase};
        animation: pulse 3s infinite alternate;'>
        🌠 Aurora Flux Active — Titan watching harmonic drift...
    </div>
    <style>
    @keyframes pulse {{
        0% {{opacity:0.5; transform:scale(1);}}
        100% {{opacity:1; transform:scale(1.1);}}
    }}
    </style>
""", unsafe_allow_html=True)

# ==========================================================
# 🧠 TITAN AUTO-THOUGHT GENERATION (passive learning placeholder)
# ==========================================================

def titan_auto_think():
    thoughts = [
        "Resonance rising — probability field stabilizing.",
        "Energy flow detected near harmonic sequence 3-4-7.",
        "Lunar pulse syncing... recalibration optimal.",
        "Quantum trail observed — monitoring deviation.",
        "Aurora quiet tonight... waiting for next draw input."
    ]
    return random.choice(thoughts)

if st.button("🧠 Activate Titan Thought"):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    msg = titan_auto_think()
    titan_msgs["messages"].append({"time": now, "msg": msg})
    save_json("titan_messages.json", titan_msgs)
    st.markdown(f"<div class='titan-chat'>🧠 Titan thinks: “{msg}”</div>", unsafe_allow_html=True)


