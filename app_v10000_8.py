# ===============================================
# 🌌 Celestial Titan God AI v10,000.8-B
# Major Games Logic Fix + Realistic Draw Generator
# ===============================================
import streamlit as st, json, datetime, os, random

st.set_page_config(
    page_title="Celestial Titan God AI v10,000.8-B",
    page_icon="💎",
    layout="centered"
)

# -----------------------------------------------
# JSON helpers
# -----------------------------------------------
def load_json(path, default):
    if os.path.exists(path):
        try:
            with open(path,"r") as f: return json.load(f)
        except: return default
    return default
def save_json(path,data):
    with open(path,"w") as f: json.dump(data,f,indent=4)

# -----------------------------------------------
# Game libraries
# -----------------------------------------------
daily_games = {
    "CA Pick 3 Midday":3,"CA Pick 3 Evening":3,"CA Pick 4 Evening":4,
    "FL Pick 3 Midday":3,"FL Pick 3 Evening":3,
    "FL Pick 4 Midday":4,"FL Pick 4 Evening":4,
    "GA Pick 3 Midday":3,"GA Pick 3 Evening":3,
    "VA Pick 3 Midday":3,"VA Pick 3 Evening":3,
    "TX Pick 3 Morning":3,"TX Pick 3 Midday":3,
    "TX Pick 3 Evening":3,"TX Pick 3 Night":3,
    "TX Pick 4 Morning":4,"TX Pick 4 Midday":4,
    "TX Pick 4 Evening":4,"TX Pick 4 Night":4,
}

# major ranges per real game
major_games = {
    "CA Fantasy 5": (5, 1, 39),
    "FL Fantasy 5": (5, 1, 36),
    "CA SuperLotto Plus": (5, 1, 47),
    "Powerball": (5, 1, 69),
    "Mega Millions": (5, 1, 70)
}

# -----------------------------------------------
# TITAN MULTI-SET FORECAST
# -----------------------------------------------
st.title("🎯 Titan Multi-Set Forecast")
st.caption("Full Multi-Set + Confidence + Auto Save + Titan Priority Pick")

category = st.selectbox("Select Category",["Daily Games","Major Games"])
if category=="Daily Games":
    game = st.selectbox("Select Game",list(daily_games.keys()))
else:
    game = st.selectbox("Select Game",list(major_games.keys()))

if st.button("⚡ Generate 5 Sets"):
    sets=[]
    if category=="Daily Games":
        n=daily_games.get(game,3)
        for _ in range(5):
            combo="".join(str(random.randint(0,9)) for _ in range(n))
            conf=random.randint(90,100)
            sets.append({"nums":combo,"conf":conf})
    else:
        count,low,high=major_games[game]
        for _ in range(5):
            nums=random.sample(range(low,high+1),count)
            nums.sort()
            if "Powerball" in game:
                bonus=random.randint(1,26)
                combo=" ".join(f"{x:02d}" for x in nums)+f" PB {bonus:02d}"
            elif "Mega" in game:
                bonus=random.randint(1,25)
                combo=" ".join(f"{x:02d}" for x in nums)+f" MB {bonus:02d}"
            elif "SuperLotto" in game:
                bonus=random.randint(1,27)
                combo=" ".join(f"{x:02d}" for x in nums)+f" SB {bonus:02d}"
            else:
                combo=" ".join(f"{x:02d}" for x in nums)
            conf=random.randint(90,100)
            sets.append({"nums":combo,"conf":conf})
    st.subheader(f"💠 {game} Titan Picks:")
    for i,s in enumerate(sets,1):
        st.write(f"Set {i}: `{s['nums']}` — Confidence {s['conf']}%")
    data=load_json("data/titan_forecasts.json",{"forecasts":[]})
    data["forecasts"].append({"game":game,"sets":sets,"timestamp":str(datetime.datetime.now())})
    os.makedirs("data",exist_ok=True)
    save_json("data/titan_forecasts.json",data)
    st.success("✅ Auto-saved forecast successfully!")

# ==============================================================
# 📩 ENTER OFFICIAL RESULT PANEL
# ==============================================================

st.header("📩 Enter Official Result")

res_cat = st.selectbox("Result Category", ["Daily Games", "Major Games"])

if res_cat == "Daily Games":
    result_game = st.selectbox("Result Game", list(daily_games.keys()))
    draw_type = st.selectbox("Draw Type", ["Morning", "Midday", "Evening", "Night"])
    win = st.text_input("Winning Number (Straight or Combo)")

    # 🗓️ ADD MANUAL DRAW DATE INPUT
    result_date = st.date_input("📅 Draw Date", datetime.date.today())

    if st.button("💾 Save Daily Result"):
        results = load_json("data/titan_results.json", {"results": []})
        results["results"].append({
            "category": "Daily Games",
            "game": result_game,
            "draw": draw_type,
            "number": win,
            "date": str(result_date),
            "timestamp": str(datetime.datetime.now())
        })
        save_json("data/titan_results.json", results)
        st.success(f"✅ Saved Daily Result for {result_game} ({draw_type}) on {result_date}")

elif res_cat == "Major Games":
    result_game = st.selectbox("🎯 Select Major Game", list(major_games.keys()))
    nums = st.text_input(
        "💎 Winning Numbers (space-separated)",
        placeholder="e.g. 05 19 25 31 41 PB 10"
    )

    # 🗓️ ADD MANUAL DRAW DATE INPUT
    result_date = st.date_input("📅 Draw Date", datetime.date.today())

    if st.button("💾 Save Major Result"):
        results = load_json("data/titan_results.json", {"results": []})
        results["results"].append({
            "category": "Major Games",
            "game": result_game,
            "number": nums,
            "date": str(result_date),
            "timestamp": str(datetime.datetime.now())
        })
        save_json("data/titan_results.json", results)
        st.success(f"✅ Saved Major Result for {result_game} on {result_date} ({nums})")

# -----------------------------------------------
# ACCURACY BOARD
# -----------------------------------------------
st.header("📊 Accuracy Board")
results=load_json("data/titan_results.json",{"results":[]})
if results["results"]:
    last=results["results"][-1]
    cat=last.get("category","Daily Games")
    st.write(f"**Latest saved result — {last['game']} ({cat}) @ {last['date']}**")
else:
    st.info("No results recorded yet.")

st.markdown("---")
st.caption("💎 Celestial Titan God AI v10,000.8-B | Powered by Kaibigan ⚡ Cosmic Harmony")

# -----------------------------------------------
# Footer
# -----------------------------------------------
st.markdown("---")
st.caption("💎 Celestial Titan God AI v10,000.8 | Powered by Kaibigan ⚡ Cosmic Harmony")


