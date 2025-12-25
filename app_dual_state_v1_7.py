# ==========================================================
# 💎 Celestial Titan Dual-State Forecast Lab v1.7.1
# 📜 Titan History + Calendar Safe Fix
# ==========================================================
import streamlit as st, json, random, datetime, os, math, pandas as pd
from calendar import monthcalendar

st.set_page_config(page_title="Titan Dual-State Forecast Lab v1.7.1", page_icon="💎", layout="wide")
BASE = os.path.dirname(os.path.abspath(__file__))

# ==========================================================
# 🎨 COSMIC DESIGN
# ==========================================================
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
  background: radial-gradient(circle at 20% 20%, #090B1A 0%, #14183F 100%);
  color: #E0E0E0 !important;
  font-family: 'Orbitron', sans-serif;
}
h1,h2,h3,h4,h5,h6 {
  color: #9EE6FF !important;
  text-shadow: 0 0 8px #00C6FF;
}
.stButton>button {
  background: linear-gradient(90deg,#0070FF,#9B00FF);
  border:none;border-radius:12px;
  color:white;font-weight:bold;
  padding:0.6em 1.2em;box-shadow:0 0 15px #0078FF;
  transition:all .3s ease-in-out;
}
.stButton>button:hover {transform:scale(1.05);box-shadow:0 0 30px #9B00FF;}
.glow-box {
  background:rgba(255,255,255,0.05);
  border:1px solid rgba(0,150,255,0.3);
  border-radius:12px;
  padding:15px;margin-top:10px;
  box-shadow:0 0 15px rgba(0,150,255,0.25);
}
.hit-row {background-color:rgba(0,255,140,0.1);}
.miss-row{background-color:rgba(255,80,80,0.1);}
</style>
""", unsafe_allow_html=True)

# ==========================================================
# 🧠 JSON HELPERS
# ==========================================================
def ensure_json(path, default):
    if not os.path.exists(path):
        with open(path, "w") as f: json.dump(default, f, indent=2)
    with open(path) as f:
        try: return json.load(f)
        except: return default

def save_json(path, data):
    with open(path, "w") as f: json.dump(data, f, indent=2)

# ==========================================================
# 📂 FILES INIT
# ==========================================================
CAL_FILE = os.path.join(BASE, "titan_calendar.json")
ensure_json(CAL_FILE, {"days": []})

# ==========================================================
# 🌕 LUNAR PHASE
# ==========================================================
def lunar_phase():
    now = datetime.datetime.now(datetime.timezone.utc)
    ref = datetime.datetime(2001, 1, 1, tzinfo=datetime.timezone.utc)
    diff = (now - ref).total_seconds() / 86400.0
    cycle = 29.53
    frac = (diff % cycle) / cycle
    illum = int((1 - math.cos(2 * math.pi * frac)) / 2 * 100)
    if illum < 10: phase = "🌑 New"
    elif illum < 40: phase = "🌓 First"
    elif illum < 60: phase = "🌕 Full"
    elif illum < 90: phase = "🌗 Last"
    else: phase = "🌘 Waning"
    return phase, illum

# ==========================================================
# ⚙️ CORE
# ==========================================================
def generate_forecast(game, sets):
    forecasts = []
    for i in range(sets):
        n = int(game.split()[-1])
        nums = [random.randint(0, 9) for _ in range(n)]
        conf = random.randint(75, 98)
        forecasts.append((nums, conf))
    return forecasts

def load_results():
    return ensure_json(CAL_FILE, {"days": []}).get("days", [])

def save_result(date, draw, number, status):
    data = ensure_json(CAL_FILE, {"days": []})
    data["days"].append({"date": str(date), "draw": draw, "number": number, "status": status})
    save_json(CAL_FILE, data)

# ==========================================================
# 🧭 NAVIGATION
# ==========================================================
st.sidebar.title("💠 Titan Dual-State Forecast Lab")
menu = st.sidebar.radio("Select Module", [
    "🎯 Forecast Console",
    "📜 History Panel",
    "📅 Calendar View"
])

st.markdown("<h1 style='text-align:center;'>💎 Celestial Titan Dual-State Forecast Lab v1.7.1</h1>", unsafe_allow_html=True)

# ==========================================================
# 🎯 FORECAST CONSOLE
# ==========================================================
if menu == "🎯 Forecast Console":
    st.subheader("🎯 Forecast Console")

    game = st.selectbox("Select Game", [
        "GA Pick 3 Midday",
        "GA Pick 3 Evening",
        "FL Pick 4 Midday",
        "FL Pick 4 Evening"
    ])
    sets = st.slider("Number of Forecast Sets", 3, 10, 3)

    if st.button("🌠 Generate Forecast"):
        fc = generate_forecast(game, sets)
        st.markdown("<div class='glow-box'>", unsafe_allow_html=True)
        for i, (nums, conf) in enumerate(fc, 1):
            digits = ''.join(map(str, nums))
            st.markdown(f"<b>Set {i}</b> → <span style='color:#00E6FF;'>{digits}</span> | Confidence <b>{conf}%</b>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        st.info("🧠 Titan: Forecasts stored in harmonic memory core.")

    st.markdown("---")
    st.subheader("📥 Enter Official Result")
    date = st.date_input("Date", datetime.date.today())
    result = st.text_input("Winning Number (Straight)")
    state_sel = "hit" if st.checkbox("Hit") else "miss"

    if st.button("💾 Save Result & Sync"):
        save_result(date, game, result, state_sel)
        st.success(f"✅ Saved {game} result on {date}")
        st.rerun()

# ==========================================================
# 📜 HISTORY PANEL
# ==========================================================
elif menu == "📜 History Panel":
    st.subheader("📜 Titan Result History")
    data = pd.DataFrame(load_results())
    if data.empty:
        st.warning("No results recorded yet.")
    else:
        data["date"] = pd.to_datetime(data["date"])
        data = data.sort_values(by="date", ascending=False)
        selected_game = st.selectbox("Filter by Game", ["All"] + sorted(data["draw"].unique().tolist()))
        if selected_game != "All":
            data = data[data["draw"] == selected_game]
        st.markdown(f"### Showing {len(data)} result(s)")
        for _, row in data.iterrows():
            color = "hit-row" if row["status"] == "hit" else "miss-row"
            st.markdown(f"<div class='{color}'><b>{row['date'].strftime('%Y-%m-%d')}</b> | {row['draw']} | 🎯 {row['number']} | Status: <b>{row['status'].upper()}</b></div>", unsafe_allow_html=True)

# ==========================================================
# 📅 CALENDAR VIEW (SAFE FIX)
# ==========================================================
else:
    st.subheader("📅 Titan Calendar View")
    data = pd.DataFrame(load_results())

    if not data.empty and "date" in data.columns:
        today = datetime.date.today()
        year, month = today.year, today.month
        cal = monthcalendar(year, month)

        for week in cal:
            cols = st.columns(7)
            for i, day in enumerate(week):
                if day == 0:
                    cols[i].markdown(" ")
                else:
                    key = f"{year}-{month:02d}-{day:02d}"
                    match = data[data["date"].astype(str) == key]
                    if not match.empty:
                        status = match.iloc[-1]["status"]
                        color = "🟢" if status == "hit" else "🔴"
                    else:
                        color = "⚪"
                    cols[i].markdown(f"{color} **{day}**")
    else:
        st.warning("📭 No recorded results yet. Please add entries from Forecast Console.")

    phase, illum = lunar_phase()
    st.metric("🌙 Lunar Phase", f"{phase} ({illum}%)")

st.markdown("<hr><center><small>💎 Celestial Titan v1.7.1 — Calendar Safe Edition</small></center>", unsafe_allow_html=True)

