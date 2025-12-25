# ==========================================================
# 💎 Celestial Titan God AI — v500.1 Horizon Tier Patch
# Separate Fantasy 5 / SuperLotto / Powerball + Organized UI
# ==========================================================
import streamlit as st
import json, os, datetime, random

# ------------------------------
# CONFIG
# ------------------------------
st.set_page_config(page_title="Titan Horizon Core v500.1", page_icon="🌠", layout="wide")

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
# GENERATOR
# ------------------------------
def generate_numbers(game, sets=3):
    results = []
    if "Pick-3" in game: n, r = 3, range(10)
    elif "Pick-4" in game: n, r = 4, range(10)
    elif "Pick-5" in game: n, r = 5, range(10)
    elif "Fantasy" in game: n, r = 5, range(1, 40)
    elif "SuperLotto" in game: n, r = 5, range(1, 48)
    elif "Powerball" in game: n, r = 5, range(1, 70)
    else: n, r = 3, range(10)

    for _ in range(sets):
        combo = [str(random.choice(r)).zfill(2 if n > 3 else 1) for _ in range(n)]
        if "SuperLotto" in game: combo.append(str(random.randint(1,27)).zfill(2))
        if "Powerball" in game: combo.append(str(random.randint(1,26)).zfill(2))
        results.append(" ".join(combo))
    return results

def record_result(state, game, number, date):
    data = ensure_json(DATA_FILE, {"records":[]})
    data["records"].append({"state": state, "game": game, "number": number, "date": date})
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

# ------------------------------
# STYLE
# ------------------------------
st.markdown("""
<style>
    .main {background: linear-gradient(180deg, #001f3f 0%, #004d40 85%);}
    .stButton>button {
        background: linear-gradient(90deg, #00bcd4, #00ffcc);
        color: black; font-weight:bold; border-radius:10px;
    }
    .stMetric {background:rgba(255,255,255,0.1);border-radius:10px;padding:8px;}
</style>
""", unsafe_allow_html=True)

# ------------------------------
# DASHBOARD HEADER
# ------------------------------
st.title("🌠 Celestial Titan God AI — Horizon Tier v500.1")
st.caption("✨ Organized UI • Fantasy 5 & Major Draw Separation • Stable Aurora Core")
col1, col2, col3 = st.columns(3)
with col1: st.metric("📈 Accuracy", f"{compute_accuracy()}%")
with col2:
    lvl = random.randint(60,100)
    color = "#00ffcc" if lvl < 85 else "#ffd700"
    st.markdown(f"<div style='background:{color};width:{lvl}%;height:10px;border-radius:10px;'></div><small>⚡ Energy {lvl}%</small>", unsafe_allow_html=True)
with col3: st.info("Aurora Core Stable")

# ------------------------------
# GAME CHOICES
# ------------------------------
states = ["GA","FL","CA"]

daily_games = [
    "GA Pick-3 Midday","GA Pick-3 Evening",
    "FL Pick-4 Midday","FL Pick-4 Evening",
    "CA Daily 3 Midday","CA Daily 3 Evening","CA Daily 4 Evening"
]

major_draws = [
    "FL Fantasy 5","CA Fantasy 5",
    "SuperLotto","Powerball"
]

# ------------------------------
# FORECAST CONSOLE
# ------------------------------
st.subheader("🎯 Titan Forecast Console")

colA, colB = st.columns(2)
with colA:
    game_section = st.radio("Select Game Category", ["🎱 Daily Numbers","💰 Major Draw Games"])
with colB:
    sets = st.slider("Number of Forecast Sets", 1, 10, 3)

if game_section == "🎱 Daily Numbers":
    game = st.selectbox("Select Game", daily_games)
else:
    game = st.selectbox("Select Major Draw", major_draws)

state = st.selectbox("Select State", states)
date_today = datetime.date.today().strftime("%Y-%m-%d")

if st.button("⚡ Generate Forecast"):
    nums = generate_numbers(game, sets)
    fc = ensure_json(FORECAST_FILE, {"forecasts":[]})
    for n in nums:
        fc["forecasts"].append({"state":state,"game":game,"number":n,"date":date_today})
    save_json(FORECAST_FILE, fc)
    st.success(f"✨ Generated for {game} — {date_today}")
    for n in nums: st.markdown(f"**🎱 {n}**")

# ------------------------------
# RESULT ENTRY
# ------------------------------
st.subheader("📥 Enter Official Result")
colR1, colR2, colR3 = st.columns(3)
with colR1: state_r = st.selectbox("Result State", states)
with colR2: game_r = st.selectbox("Result Game", daily_games + major_draws)
with colR3: date_r = st.date_input("Draw Date", datetime.date.today())
number_r = st.text_input("Winning Number (Straight)")
if st.button("💾 Save Result"):
    record_result(state_r, game_r, number_r, str(date_r))
    st.success(f"Saved result for {game_r} ({date_r})")

# ------------------------------
# CHAT INSIGHT
# ------------------------------
st.subheader("💬 Titan Chat Insight")
if st.button("🧠 Ask Titan"):
    msg = random.choice([
        "Aurora flux within range — recalibration ongoing.",
        "Fantasy 5 pattern resonance increasing at mid digits.",
        "Powerball energy surge detected — expect anomalies near 30s.",
        "SuperLotto harmonic band stabilized at 20–40 zone."
    ])
    st.info(f"Titan says: {msg}")

st.caption("💠 Horizon Tier v500.1 — Fantasy & Major Games Organized, ready for next evolution.")


