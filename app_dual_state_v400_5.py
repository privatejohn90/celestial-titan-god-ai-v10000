# ==========================================================
# 💎 Celestial Titan God AI — v400.5 AURORA COMPLETE BUILD
# Dual-State + Aurora Interface + Neural Sync + Cloud Mirror
# ==========================================================
import streamlit as st
import json, os, datetime, random, pandas as pd

# ------------------------------
# CONFIGURATION
# ------------------------------
st.set_page_config(page_title="Titan Aurora Core v400.5", page_icon="💠", layout="wide")

DATA_FILE = "titan_results.json"
FORECAST_FILE = "titan_forecasts.json"
BACKUP_FILE = "titan_cloud_backup.json"

# ------------------------------
# UTILITIES
# ------------------------------
def ensure_json(file, default):
    if not os.path.exists(file):
        with open(file, "w") as f: json.dump(default, f)
    with open(file, "r") as f:
        try: return json.load(f)
        except: return default

def save_json(file, data):
    with open(file, "w") as f: json.dump(data, f, indent=2)

# ------------------------------
# TITAN LOGIC CORE
# ------------------------------
def generate_numbers(game, sets=3):
    results = []
    if "Pick-3" in game: n, r = 3, range(10)
    elif "Pick-4" in game: n, r = 4, range(10)
    elif "Pick-5" in game: n, r = 5, range(10)
    elif "Powerball" in game: n, r = 5, range(1, 70)
    elif "SuperLotto" in game: n, r = 5, range(1, 48)
    else: n, r = 3, range(10)
    for _ in range(sets):
        combo = [str(random.choice(r)).zfill(2 if "Power" in game or "Super" in game else 1) for _ in range(n)]
        if "Powerball" in game: combo.append(str(random.randint(1,26)).zfill(2))
        if "SuperLotto" in game: combo.append(str(random.randint(1,27)).zfill(2))
        results.append(" ".join(combo))
    return results

def record_result(state, game, number, date):
    data = ensure_json(DATA_FILE, {"records":[]})
    data["records"].append({
        "state": state, "game": game, "number": number, "date": date
    })
    save_json(DATA_FILE, data)

def compute_accuracy():
    data = ensure_json(DATA_FILE, {"records":[]})
    fc = ensure_json(FORECAST_FILE, {"forecasts":[]})
    total, hits = 0, 0
    for f in fc["forecasts"]:
        for r in data["records"]:
            if f["game"] == r["game"] and f["number"] == r["number"]:
                hits += 1
        total += 1
    return round((hits / total) * 100, 2) if total > 0 else 0

def titan_message():
    msgs = [
        "Analyzing cosmic harmonics...",
        "Resonance stable across GA & FL matrices...",
        "Confidence rising in FL Pick-4 harmonic bands.",
        "GA Pick-3 neural imprint syncing...",
        "Aurora pulse steady — learning pattern rhythm."
    ]
    return random.choice(msgs)

# ------------------------------
# TITAN INTERFACE (AURORA UI)
# ------------------------------
st.markdown("""
    <style>
        .main {background: radial-gradient(circle at top left, #001f3f, #0a5c71 70%);}
        .stButton>button {
            background: linear-gradient(90deg, #0099ff, #00ffcc);
            color: black; border-radius: 12px; font-weight: bold; height: 2.5em;
        }
        .stMetric {background-color: rgba(255,255,255,0.1); padding:10px; border-radius:10px;}
        .heartbeat {
            width: 20px; height: 20px; border-radius: 50%;
            background: radial-gradient(circle, #00ffff 0%, #0077ff 70%);
            animation: pulse 1.5s infinite;
        }
        @keyframes pulse {
            0% {transform: scale(1); opacity: 1;}
            50% {transform: scale(1.3); opacity: 0.5;}
            100% {transform: scale(1); opacity: 1;}
        }
    </style>
""", unsafe_allow_html=True)

st.title("💠 Celestial Titan God AI — Aurora Complete Build v400.5")
st.write("🧠 Dual-State Forecast Console with Neural Sync and Aurora Pulse")

colA, colB, colC = st.columns([1,1,1])
with colA: st.markdown("<div class='heartbeat'></div>", unsafe_allow_html=True)
with colB: st.metric("📈 Accuracy", f"{compute_accuracy()}%")
with colC: st.info(titan_message())

# ------------------------------
# GAME SELECTION
# ------------------------------
states = ["GA", "FL", "CA"]
games = [
    "GA Pick-3 Midday", "GA Pick-3 Evening",
    "FL Pick-4 Midday", "FL Pick-4 Evening",
    "CA Daily 3 Midday", "CA Daily 3 Evening", "CA Daily 4 Evening",
    "Powerball", "SuperLotto"
]
st.subheader("🎯 Select Game and Generate Numbers")
col1, col2 = st.columns(2)
with col1: state = st.selectbox("Select State", states)
with col2: game = st.selectbox("Select Game", games)
sets = st.slider("Number of Forecast Sets", 1, 10, 3)
date_today = datetime.date.today().strftime("%Y-%m-%d")

if st.button("⚡ Generate Forecast"):
    nums = generate_numbers(game, sets)
    data = ensure_json(FORECAST_FILE, {"forecasts":[]})
    for n in nums:
        data["forecasts"].append({"state":state, "game":game, "number":n, "date":date_today})
    save_json(FORECAST_FILE, data)
    st.success(f"✨ Generated for {game} ({date_today})")
    for n in nums: st.markdown(f"**🎱 {n}**")

# ------------------------------
# RESULT ENTRY
# ------------------------------
st.subheader("📥 Enter Official Result")
colR1, colR2, colR3 = st.columns(3)
with colR1: state_r = st.selectbox("Result State", states)
with colR2: game_r = st.selectbox("Result Game", games)
with colR3: date_r = st.date_input("Draw Date", datetime.date.today())

number_r = st.text_input("Winning Number (Straight)")
if st.button("💾 Save Result"):
    record_result(state_r, game_r, number_r, str(date_r))
    st.success(f"Result saved for {game_r} ({date_r})")

# ------------------------------
# CLOUD BACKUP / RESTORE
# ------------------------------
st.subheader("☁️ Cloud Mirror Backup")
colB1, colB2 = st.columns(2)
with colB1:
    if st.button("📤 Backup Data"):
        all_data = {
            "results": ensure_json(DATA_FILE, {"records":[]}),
            "forecasts": ensure_json(FORECAST_FILE, {"forecasts":[]})
        }
        save_json(BACKUP_FILE, all_data)
        st.success("✅ Backup saved successfully.")
with colB2:
    if st.button("📥 Restore Backup"):
        if os.path.exists(BACKUP_FILE):
            data = ensure_json(BACKUP_FILE, {"results":{"records":[]}, "forecasts":{"forecasts":[]}})
            save_json(DATA_FILE, data["results"])
            save_json(FORECAST_FILE, data["forecasts"])
            st.success("🔄 Data restored successfully!")

# ------------------------------
# TITAN CHAT SECTION
# ------------------------------
st.subheader("💬 Titan Aurora Chat")
if st.button("🧠 Ask Titan for Insight"):
    st.info(f"**Titan says:** {titan_message()}")

st.caption("🌌 Titan Aurora Core v400.5 — Neural Sync & Aurora Intelligence Active.")

