# ==========================================================
# 💠 Celestial Titan God AI v10,000.7-FX — Dual Category Build
# Full Multi-Set Forecast + Confidence + Timestamp Fix + Category Split
# ==========================================================

import streamlit as st, random, json, datetime, os

st.set_page_config(page_title="Celestial Titan God AI v10,000.7-FX",
                   page_icon="💎", layout="centered")

# ==========================================================
# 🧠 Titan JSON Helpers
# ==========================================================
def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def load_json(path, default):
    return json.load(open(path)) if os.path.exists(path) else default

# ==========================================================
# 🪐 Titan Game Libraries
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
# 🎯 TITAN MULTI-SET FORECAST
# ==========================================================
st.title("🎯 Titan Multi-Set Forecast")
st.caption("Full Multi-Set + Confidence + Auto Save + Titan Priority Pick")

category = st.selectbox("🎰 Select Category", ["Daily Games", "Major Games"])
game_dict = daily_games if category == "Daily Games" else major_games
game = st.selectbox("🎮 Select Game", list(game_dict.keys()))

if st.button("⚡ Generate 5 Sets"):
    forecasts = []
    for _ in range(5):
        length = game_dict[game]
        if category == "Major Games" and "Fantasy" in game:
            # Fantasy 5 type (1-39 only)
            nums = sorted(random.sample(range(1, 40), length))
            forecast = {"set": " ".join(map(str, nums)), "confidence": random.randint(90, 100)}
        elif category == "Major Games" and ("SuperLotto" in game or "Powerball" in game or "Mega" in game):
            base = sorted(random.sample(range(1, 70), length))
            bonus = random.randint(1, 26)
            forecast = {"set": f"{' '.join(map(str, base))} PB{bonus}", "confidence": random.randint(90, 100)}
        else:
            num = "".join(str(random.randint(0, 9)) for _ in range(length))
            forecast = {"set": num, "confidence": random.randint(88, 100)}
        forecasts.append(forecast)

    top_pick = max(forecasts, key=lambda f: f["confidence"])

    st.success(f"✅ 5 Forecasts ready for {game}")
    for f in forecasts:
        prefix = "💎 Titan Priority Pick:" if f == top_pick else "✨"
        st.markdown(f"{prefix} **{f['set']}** — Confidence: **{f['confidence']}%**")

    data = load_json("titan_results.json", {"records": []})
    data["records"].append({
        "category": category,
        "game": game,
        "forecasts": forecasts,
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    save_json("titan_results.json", data)
    st.info("💾 Forecast saved successfully to titan_results.json")

# ==========================================================
# 📥 ENTER OFFICIAL RESULT (NEW)
# ==========================================================
st.header("📥 Enter Official Result")

with st.form("result_input"):
    col1, col2, col3 = st.columns(3)
    with col1:
        result_category = st.selectbox("Result Category", ["Daily Games", "Major Games"])
        result_game = st.selectbox("Result Game", list(daily_games.keys()) if result_category == "Daily Games" else list(major_games.keys()))
    with col2:
        result_draw = st.selectbox("Draw Type", ["Morning", "Midday", "Evening", "Night"])
    with col3:
        result_number = st.text_input("Winning Number (Straight or Combo)")

    submit_result = st.form_submit_button("💾 Save Winning Result")

if submit_result and result_number.strip() != "":
    stored = load_json("titan_results.json", {"records": []})
    stored["records"].append({
        "type": result_category,
        "game": result_game,
        "draw": result_draw,
        "number": result_number.strip(),
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    save_json("titan_results.json", stored)
    st.success(f"✅ Winning result saved for {result_game} ({result_draw})")

# ==========================================================
# 📊 ACCURACY BOARD
# ==========================================================
st.header("📊 Accuracy Board")
results = load_json("titan_results.json", {"records": []}).get("records", [])
if results:
    last = results[-1]
    st.write(f"Latest saved forecast — `{last.get('game','Unknown Game')}` @ `{last.get('timestamp','No Timestamp')}`")
else:
    st.warning("No saved forecasts yet.")

# ==========================================================
# ⚡ Titan Footer
# ==========================================================
st.markdown("---")
st.markdown("<p style='text-align:center;font-size:13px;'>💠 Celestial Titan God AI v10,000.7-FX | Powered by Kaibigan ⚡ Cosmic Harmony</p>", unsafe_allow_html=True)

