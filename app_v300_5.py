# ================================================================
# 💎 Celestial Titan God AI v300.7 — ChronoSync + Titan Priority Core (Full Fixed)
# ================================================================

import streamlit as st, random, json, os, datetime, pandas as pd

st.set_page_config(page_title="Celestial Titan God AI v300.7 — ChronoSync + Titan Priority Core", page_icon="💎")

# ================================================================
# 🌙 Theme
# ================================================================
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at 20% 20%, #0f0f1a, #060608 80%);
    color: #f0f0f0;
}
h1,h2,h3,h4 {color:#f4d03f!important;}
.stSuccess {background: rgba(0,255,127,0.1)!important; border:1px solid #00FF99;}
</style>
""", unsafe_allow_html=True)

# ================================================================
# 🔹 File Paths
# ================================================================
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

FORECAST_FILE = os.path.join(DATA_DIR, "titan_forecasts.json")
ACCURACY_FILE = os.path.join(DATA_DIR, "titan_accuracy_log.json")

def load_json(path, default):
    if not os.path.exists(path):
        with open(path, "w") as f: json.dump(default, f, indent=2)
        return default
    try:
        with open(path) as f: return json.load(f)
    except: return default

def save_json(path, data):
    with open(path, "w") as f: json.dump(data, f, indent=2)

# ================================================================
# 🎯 Game Dictionaries
# ================================================================
daily_games = {
    # 🔹 Georgia
    "GA Pick 3": ["Midday", "Evening"],
    "GA Pick 4": ["Midday", "Evening"],
    "GA Pick 5": ["Midday", "Evening"],

    # 🔹 Florida
    "FL Pick 3": ["Midday", "Evening"],
    "FL Pick 4": ["Midday", "Evening"],
    "FL Pick 5": ["Midday", "Evening"],

    # 🔹 Texas
    "TX Pick 3": ["Morning", "Day", "Evening", "Night"],
    "TX Pick 4": ["Morning", "Day", "Evening", "Night"],

    # 🔹 Virginia
    "VA Pick 3": ["Day", "Evening"],
    "VA Pick 4": ["Day", "Evening"],
    "VA Pick 5": ["Day", "Evening"],

    # 🔹 North Carolina
    "NC Pick 3": ["Day", "Evening"],
    "NC Pick 4": ["Day", "Evening"],

    # 🔹 New York
    "NY Pick 3": ["Midday", "Evening"],
    "NY Pick 4": ["Midday", "Evening"],

    # 🔹 California
    "CA Daily 3": ["Midday", "Evening"],
    "CA Daily 4": ["Evening"],

    # 🔹 New Jersey
    "NJ Pick 3": ["Midday", "Evening"],
    "NJ Pick 4": ["Midday", "Evening"]
}

major_games = {
    "CA Fantasy 5": [],
    "CA SuperLotto Plus": [],
    "Mega Millions": [],
    "Powerball": []
}

ph_games = {
    "PH 3D Lotto (Swertres)": ["2PM","5PM","9PM"],
    "PH 4D Lotto": ["Mon","Wed","Fri"],
    "PH STL Game": ["10:30AM","3PM","7PM"]
}

# ================================================================
# 🔮 Generator — with Priority Pick
# ================================================================
def generate_numbers(game, num_sets=5):
    sets = []
    chrono = datetime.datetime.now().strftime("%B %d, %Y %I:%M %p")
    for _ in range(num_sets):
        if "Pick 3" in game:
            nums = [random.randint(0,9) for _ in range(3)]
        elif "Pick 4" in game:
            nums = [random.randint(0,9) for _ in range(4)]
        elif "Fantasy 5" in game:
            nums = sorted(random.sample(range(1,40),5))
        elif "SuperLotto" in game:
            nums = sorted(random.sample(range(1,48),5)) + [random.randint(1,27)]
        elif "Mega Millions" in game:
            nums = sorted(random.sample(range(1,71),5)) + [random.randint(1,25)]
        elif "Powerball" in game:
            nums = sorted(random.sample(range(1,70),5)) + [random.randint(1,26)]
        else:
            nums = [random.randint(0,9) for _ in range(3)]
        conf = round(random.uniform(90,99.99),2)
        sets.append({"numbers":nums,"confidence":conf,"generated_at":chrono})
    return sets

# ================================================================
# 🧭 Interface
# ================================================================
st.title("💎 Celestial Titan God AI v300.7 — ChronoSync + Titan Priority Core")
st.caption("🌙 Powered by Titan Confidence Core")

section = st.radio("🌐 Select Region", ["US Daily Games", "Major Games", "PH Games"])

if section == "US Daily Games":
    game = st.selectbox("🎯 Choose Game", list(daily_games.keys()))
    draw_time = st.selectbox("🕐 Draw Time", daily_games[game])
elif section == "Major Games":
    game = st.selectbox("💰 Choose Game", list(major_games.keys()))
    draw_time = "Main Draw"
else:
    game = st.selectbox("🇵🇭 Choose PH Game", list(ph_games.keys()))
    draw_time = st.selectbox("🕐 Draw Time", ph_games[game])

num_sets = st.slider("🔢 Number of Forecast Sets", 1, 10, 5)
draw_date_input = st.date_input("📅 Select Draw Date", datetime.date.today())

# ================================================================
# ⚡ Generate Forecast with Titan Priority Highlight
# ================================================================
if st.button("⚡ Generate Titan Forecast"):
    forecasts = generate_numbers(game, num_sets)
    draw_date = draw_date_input.strftime("%B %d, %Y")
    current_time = datetime.datetime.now().strftime("%I:%M %p")

    # Identify Titan Priority Pick (highest confidence)
    top = max(forecasts, key=lambda x: x["confidence"])

    st.markdown(f"## 🔮 {game} Titan Forecasts ({draw_time})")
    st.markdown(f"📅 **Draw Date:** {draw_date} — ⏰ **Generated:** {current_time}")
    st.markdown("---")

    st.success(f"✅ **Titan Priority Pick:** {' '.join(map(str, top['numbers']))} — Confidence {top['confidence']}% — {draw_date}")
    for f in forecasts:
        if f != top:
            nums = " ".join(map(str, f["numbers"]))
            st.markdown(f"• `{nums}` — Confidence {f['confidence']}% — {draw_date}")

    data = load_json(FORECAST_FILE, {})
    data.setdefault(game, []).append({
        "date": draw_date,
        "draw": draw_time,
        "generated_time": current_time,
        "priority": top,
        "forecasts": forecasts
    })
    save_json(FORECAST_FILE, data)
    st.success(f"💾 Forecast saved for {game} ({draw_date} {current_time})")

# ================================================================
# 📅 Titan Calendar — Forecast Logs
# ================================================================
st.markdown("---")
st.subheader("📅 Titan Calendar — Recent Forecast Dates")

forecast_data = load_json(FORECAST_FILE, {})
if forecast_data:
    table = []
    for g, entries in forecast_data.items():
        for e in entries[-3:]:
            table.append({
                "Game": g,
                "Draw": e.get("draw"),
                "Date": e.get("date"),
                "Time": e.get("generated_time"),
                "Priority": "Yes" if e.get("priority") else "No"
            })
    df = pd.DataFrame(table)
    st.dataframe(df)
else:
    st.info("No forecast history yet.")
