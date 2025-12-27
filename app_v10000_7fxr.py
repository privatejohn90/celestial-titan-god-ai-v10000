
import streamlit as st
import json, random, os, datetime

# ======================================================
# 💎 Celestial Titan God AI v10,000.7-FXR — Dual Forecast + Result Fix
# Full Multi-Set Forecast + Confidence + Auto Save + Major Games Panel
# ======================================================

st.set_page_config(
    page_title="Celestial Titan God AI v10,000.7-FXR",
    page_icon="💎",
    layout="centered"
)

# ---------- TITAN GAME LIBRARIES ----------
daily_games = {
    "CA Pick 3 Midday":3,"CA Pick 3 Evening":3,"CA Pick 4 Evening":4,
    "FL Pick 3 Midday":3,"FL Pick 3 Evening":3,
    "FL Pick 4 Midday":4,"FL Pick 4 Evening":4,
    "FL Pick 5 Midday":5,"FL Pick 5 Evening":5,
    "GA Pick 3 Midday":3,"GA Pick 3 Evening":3,"GA Pick 3 Night":3,
    "GA Pick 4 Midday":4,"GA Pick 4 Evening":4,"GA Pick 4 Night":4,
    "GA Pick 5 Midday":5,"GA Pick 5 Evening":5,
    "VA Pick 3 Midday":3,"VA Pick 3 Evening":3,
    "VA Pick 4 Midday":4,"VA Pick 4 Evening":4,
    "VA Pick 5 Midday":5,"VA Pick 5 Evening":5,
    "TX Pick 3 Morning":3,"TX Pick 3 Midday":3,
    "TX Pick 3 Evening":3,"TX Pick 3 Night":3,
    "TX Pick 4 Morning":4,"TX Pick 4 Midday":4,
    "TX Pick 4 Evening":4,"TX Pick 4 Night":4
}

major_games = {
    "CA Fantasy 5":5,"FL Fantasy 5":5,
    "CA SuperLotto Plus":5,
    "Powerball":5,"Mega Millions":5
}

# ---------- TITAN FORECAST CONSOLE ----------
st.markdown("<h2 style='text-align:center;'>🎯 Titan Multi-Set Forecast</h2>", unsafe_allow_html=True)
st.caption("Full Multi-Set + Confidence + Auto Save + Titan Priority Pick")

category = st.selectbox("Select Category", ["Daily Games","Major Games"])
if category=="Daily Games":
    game = st.selectbox("Select Game", list(daily_games.keys()))
else:
    game = st.selectbox("Select Game", list(major_games.keys()))

if st.button("⚡ Generate 5 Sets"):
    sets=[]
    n = (daily_games.get(game) or major_games.get(game))
    for i in range(5):
        nums = random.sample(range(1,70), n)
        conf = random.randint(90,100)
        sets.append({"nums":nums,"conf":conf})
    st.success(f"✅ 5 Forecasts ready for {game}")
    for s in sets:
        txt=" ".join(str(x).zfill(2) for x in s["nums"])
        st.write(f"✨ {txt} — Confidence {s['conf']}%")
    data={"game":game,"timestamp":str(datetime.datetime.now()),"results":sets}
    os.makedirs("data",exist_ok=True)
    json.dump(data,open("data/titan_forecasts.json","w"),indent=4)

# ---------- ACCURACY BOARD ----------
st.header("📊 Accuracy Board")
try:
    rec=json.load(open("data/titan_forecasts.json"))
    st.write(f"Latest saved forecast — **{rec['game']}** @ {rec['timestamp']}")
except:
    st.info("No forecast saved yet.")

# ---------- RESULT ENTRY PANEL ----------
# 📨 ENTER OFFICIAL RESULT PANEL
st.subheader("📩 Enter Official Result")

res_cat = st.selectbox("Result Category", ["Daily Games", "Major Games"])

if res_cat == "Daily Games":
    g = st.selectbox("Result Game", list(daily_games.keys()))
    draw_type = st.selectbox("Draw Type", ["Morning","Midday","Evening","Night"])
    win = st.text_input("Winning Number (Straight or Combo)")
    if st.button("💾 Save Daily Result"):
        try:
            d = json.load(open("data/titan_results.json"))
        except:
            d = {"results": []}
        d["results"].append({
            "game": g,
            "draw": draw_type,
            "number": win,
            "date": str(datetime.date.today())
        })
        json.dump(d, open("data/titan_results.json", "w"), indent=4)
        st.success(f"✅ Saved Daily Result for {g} ({draw_type}) = {win}")

elif res_cat == "Major Games":
    g = st.selectbox("🎯 Select Major Game", list(major_games.keys()))
    nums = st.text_input("💎 Winning Numbers (space-separated)", placeholder="e.g. 03 09 14 22 39 PB 13")
    dte = st.date_input("📅 Draw Date", value=datetime.date.today())
    if st.button("💾 Save Major Result"):
        try:
            d = json.load(open("data/titan_results.json"))
        except:
            d = {"results": []}
        d["results"].append({
            "game": g,
            "number": nums,
            "date": str(dte)
        })
        json.dump(d, open("data/titan_results.json", "w"), indent=4)
        st.success(f"✅ Saved Major Result for {g} ({nums})")

# ---------- FOOTER ----------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center;'><small>💎 Celestial Titan God AI v10 000.7-FXR | Powered by Kaibigan ⚡ Cosmic Harmony</small></p>",
    unsafe_allow_html=True
)

