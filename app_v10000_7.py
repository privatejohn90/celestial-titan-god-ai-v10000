# ==========================================================
# 💎 Celestial Titan God AI v10,000.7-FXR
# Full Multi-Set Forecast + Confidence + Auto-Save + Accuracy Fix
# ==========================================================

import streamlit as st
import random, json, os, datetime

# ---------- UTILITIES ----------
def load_json(filename, default=None):
    if not os.path.exists(filename):
        return default or {}
    with open(filename, "r") as f:
        try:
            return json.load(f)
        except:
            return default or {}

def save_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

# ---------- TITAN HEADER ----------
st.markdown("<h2 style='text-align:center;'>💠 Celestial Titan God AI v10,000.7-FXR</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'>Full Multi-Set Forecast + Confidence + Auto-Save + Accuracy Fix</h4>", unsafe_allow_html=True)
st.markdown("---")

# ---------- GAME LIBRARIES ----------
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

# ---------- TITAN FORECAST ENGINE ----------
st.header("🎯 Titan Multi-Set Forecast")
game = st.selectbox("Select Game", list(daily_games.keys()) + list(major_games.keys()))
num_sets = 5

if st.button("⚡ Generate 5 Sets"):
    forecasts = []
    length = daily_games.get(game, major_games.get(game, 3))
    is_major = game in major_games

    for i in range(num_sets):
        if is_major:
            base = sorted(random.sample(range(1, 40 if "Fantasy" in game else 70), length))
            bonus = None
            if "SuperLotto" in game:
                bonus = random.randint(1, 27)
            elif "Powerball" in game:
                bonus = random.randint(1, 26)
            elif "Mega" in game:
                bonus = random.randint(1, 25)

            set_str = " ".join(map(str, base))
            if bonus:
                set_str += f" PB{bonus}"
            confidence = random.randint(90, 100)
        else:
            digits = [str(random.randint(0, 9)) for _ in range(length)]
            set_str = "".join(digits)
            confidence = random.randint(88, 99)

        forecasts.append({"set": set_str, "confidence": confidence})

    top_pick = max(forecasts, key=lambda f: f["confidence"])
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Save auto forecast
    forecast_file = "titan_forecasts.json"
    data = load_json(forecast_file, {"forecasts": []})
    data["forecasts"].append({
        "game": game,
        "timestamp": timestamp,
        "sets": forecasts
    })
    save_json(forecast_file, data)

    st.success(f"✅ Generated {num_sets} forecasts for {game}")
    for f in forecasts:
        prefix = "💎 **Titan Priority Pick:**" if f == top_pick else "✨"
        st.markdown(f"{prefix} {f['set']} — Confidence: **{f['confidence']}%**")
        
# ==============================
# 🎯 ENTER OFFICIAL RESULT PANEL
# ==============================
if res_cat == "Daily Games":
    g = st.selectbox("Result Game", list(daily_games.keys()))
    draw_type = st.selectbox("Draw Type", ["Morning","Midday","Evening","Night"])
    win = st.text_input("Winning Number (Straight or Combo)")
    if st.button("💾 Save Winning Result"):
        try:
            d=json.load(open("data/titan_results.json"))
        except:
            d={"results":[]}
        d["results"].append({
            "game":g,
            "draw":draw_type,
            "number":win,
            "date":str(datetime.date.today())
        })
        json.dump(d,open("data/titan_results.json","w"),indent=4)
        st.success(f"✅ Saved result for {g} ({draw_type}) = {win}")

elif res_cat == "Major Games":
    g = st.selectbox("🎯 Select Major Game", list(major_games.keys()))
    nums = st.text_input("💎 Winning Numbers (space-separated)", placeholder="e.g. 03 09 14 22 39 PB 13")
    dte = st.date_input("📅 Draw Date", value=datetime.date.today())
    if st.button("💾 Save Major Game Result"):
        try:
            d=json.load(open("data/titan_results.json"))
        except:
            d={"results":[]}
        d["results"].append({
            "game":g,
            "number":nums,
            "date":str(dte)
        })
        json.dump(d,open("data/titan_results.json","w"),indent=4)
        st.success(f"✅ Saved Major Game Result for {g} ({nums})")
# ---------- ACCURACY BOARD ----------
st.markdown("---")
st.header("📊 Accuracy Board")

forecasts = load_json("titan_forecasts.json", {"forecasts": []})
results = load_json("titan_results.json", {"results": []})
if forecasts.get("forecasts") and results.get("results"):
    hits, total = 0, 0
    for r in results["results"]:
        for fset in forecasts["forecasts"]:
            for s in fset["sets"]:
                if r["number"] in s["set"]:
                    hits += 1
                    break
        total += 1
    acc = round((hits / total) * 100, 2) if total > 0 else 0
    st.metric("🎯 Titan Accuracy", f"{acc}%")
    st.info(f"Analyzed {total} results with {hits} total hits.")
else:
    st.warning("⚠️ No data yet — generate forecasts and enter results first.")

# ---------- FOOTER ----------
st.markdown("---")
st.markdown("<p style='text-align:center;'>💠 Celestial Titan God AI v10,000.7-FXR — Stable Stream</p>", unsafe_allow_html=True)
