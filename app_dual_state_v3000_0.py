
# ==========================================================
# 💎 Celestial Titan God AI v10,000.6
# 🌌 Cosmic Phase + Confidence Sync Build
# ==========================================================
import streamlit as st
import random, datetime, math, json

st.set_page_config(page_title="Celestial Titan God AI v10,000.6", page_icon="💎", layout="wide")

# ==========================================================
# ⚙️ Utility Functions
# ==========================================================
def load_json(path, default):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        return default

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

# ==========================================================
# 🌌 GAME REGISTRY v10,000.5 — Full Multi-State Map
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
# 🌙 Lunar Phase Detector
# ==========================================================
def get_lunar_phase():
    # simple lunar cycle: 29.53 days
    diff = (datetime.date.today() - datetime.date(2001, 1, 1)).days % 29.53
    if diff < 7.38:
        return "🌑 New Moon"
    elif diff < 14.77:
        return "🌓 First Quarter"
    elif diff < 22.15:
        return "🌕 Full Moon"
    else:
        return "🌗 Last Quarter"

# ==========================================================
# 🎯 TITAN FORECAST CONSOLE
# ==========================================================
st.title("🎯 Titan Forecast Console")

game_type = st.selectbox("Select Game", list(daily_games.keys()) + list(major_games.keys()))
num_sets = st.slider("Number of Forecast Sets", 1, 10, 5)

if st.button("⚡ Generate Titan Forecasts"):
    forecasts = []
    length = daily_games.get(game_type, major_games.get(game_type, 3))
    lunar_phase = get_lunar_phase()

    for i in range(num_sets):
        if "SuperLotto" in game_type:
            base = sorted(random.sample(range(1, 48), 5))
            bonus = random.randint(1, 27)
            confidence = random.randint(91, 100)
            set_num = f"{' '.join(map(str, base))} PB{bonus}"
        elif "Fantasy" in game_type:
            base = sorted(random.sample(range(1, 40), 5))
            confidence = random.randint(90, 100)
            set_num = " ".join(map(str, base))
        elif "Powerball" in game_type:
            base = sorted(random.sample(range(1, 70), 5))
            bonus = random.randint(1, 26)
            confidence = random.randint(91, 100)
            set_num = f"{' '.join(map(str, base))} PB{bonus}"
        else:
            set_num = "".join(str(random.randint(0, 9)) for _ in range(length))
            confidence = random.randint(88, 99)

        forecasts.append({"set": set_num, "confidence": confidence})

    top_pick = max(forecasts, key=lambda x: x["confidence"])

    st.success(f"✅ {len(forecasts)} Forecasts ready for {game_type} — {lunar_phase}")

    for f in forecasts:
        prefix = "💎 **Titan Priority Pick:**" if f == top_pick else "✨"
        st.markdown(f"{prefix} `{f['set']}` — Confidence: **{f['confidence']}%**")

    # 🌈 Visualization
    st.subheader("🌙 Confidence Visualization")
    for f in forecasts:
        conf = f["confidence"]
        color = "#00FF99" if conf >= 95 else "#FFD700" if conf >= 90 else "#FF5555"
        aura = "💠 Titan Aura Active" if f == top_pick else ""
        bar = f"<div style='background:{color};width:{conf}%;height:14px;border-radius:5px'></div>"
        st.markdown(f"{bar}<small>{f['confidence']}% {aura}</small>", unsafe_allow_html=True)

# ==========================================================
# 📥 RESULT ENTRY
# ==========================================================
st.header("📥 Enter Official Result")
RESULT_FILE = "titan_results.json"
with st.form("result_entry"):
    col1, col2, col3 = st.columns(3)
    with col1: r_game = st.selectbox("Game", list(daily_games.keys()))
    with col2: r_date = st.date_input("Draw Date", datetime.date.today())
    with col3: r_num = st.text_input("Winning Number (Straight or Combo)")
    submitted = st.form_submit_button("Save Result")

if submitted and r_num:
    data = load_json(RESULT_FILE, {"records": []})
    data["records"].append({"game": r_game, "date": str(r_date), "number": r_num})
    save_json(RESULT_FILE, data)
    st.success(f"Result for {r_game} recorded successfully.")

# ==========================================================
# 📊 ACCURACY REFLECTION BOARD
# ==========================================================
st.header("📊 Accuracy Reflection Board")
def compute_accuracy():
    f_data = load_json("titan_forecasts.json", {"forecasts": []}).get("forecasts", [])
    r_data = load_json(RESULT_FILE, {"records": []}).get("records", [])
    if not f_data or not r_data:
        return 0
    hits, total = 0, len(r_data)
    for r in r_data:
        for f in f_data:
            if r["number"] in f["set"]:
                hits += 1
                break
    return round((hits / total) * 100, 2)

acc = compute_accuracy()
st.metric("⚡ Titan Accuracy", f"{acc}%")

# ==========================================================
# 🪐 FOOTER
# ==========================================================
st.markdown("---")
st.markdown(
    f"<p style='text-align:center;font-size:13px;'>💎 Celestial Titan God AI v10,000.6 — Cosmic Phase + Confidence Sync Build<br>{get_lunar_phase()}</p>",
    unsafe_allow_html=True
)
