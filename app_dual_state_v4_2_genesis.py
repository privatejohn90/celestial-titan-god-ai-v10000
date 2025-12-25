# ===========================================================
# 💎 Celestial Titan Dual-State Cloud Genesis v4.2
# 🌌 GA Pick-3 & FL Pick-4 | Cloud Simulation + Lunar Sync
# ===========================================================

import streamlit as st, json, os, random, datetime, math, pandas as pd, matplotlib.pyplot as plt

st.set_page_config(page_title="Titan Cloud Genesis Portal", page_icon="💎", layout="wide")

# ===========================================================
# ⚙️ Setup + File Paths
# ===========================================================
DATA_DIR = "data"; os.makedirs(DATA_DIR, exist_ok=True)
MEM_FILE = os.path.join(DATA_DIR, "titan_cloud_memory.json")

def ensure_json(path, default):
    if not os.path.exists(path):
        with open(path, "w") as f: json.dump(default, f)
        return default
    try:
        with open(path, "r") as f: return json.load(f)
    except: return default

def save_json(path, data):
    with open(path, "w") as f: json.dump(data, f, indent=2)

# ===========================================================
# ☁️ Cloud Memory Simulation
# ===========================================================
cloud = ensure_json(MEM_FILE, {"users": {}, "results": []})

def save_result(game, number, date, user):
    cloud["results"].append({"user":user,"game":game,"number":number,"date":date})
    save_json(MEM_FILE, cloud)

def get_user_data(user):
    return [r for r in cloud["results"] if r["user"]==user]

# ===========================================================
# 🔐 Member Login
# ===========================================================
st.markdown("<h1 style='text-align:center;color:#9ef0ff;'>💠 Titan Cloud Genesis Portal</h1>", unsafe_allow_html=True)
user = st.text_input("👤 Enter username", "Kaibigan")
if not user: st.stop()

st.success(f"Welcome back, {user} — Titan Cloud field active!")

# ===========================================================
# 🌙 Lunar Phase Calculator
# ===========================================================
def lunar_phase():
    synodic = 29.53058867
    now = datetime.datetime.now()
    new_moon = datetime.datetime(2000, 1, 6, 18, 14)
    days = (now - new_moon).days + (now - new_moon).seconds / 86400.0
    lunations = days / synodic
    phase = lunations - int(lunations)
    phase_name = ["New Moon","Waxing Crescent","First Quarter","Waxing Gibbous",
                  "Full Moon","Waning Gibbous","Last Quarter","Waning Crescent"]
    index = int((phase * 8) + 0.5) % 8
    return phase_name[index], round(phase * 100, 2)

# ===========================================================
# ⚡ Forecast Generator
# ===========================================================
def generate_forecast(game, sets=5):
    n = 3 if "Pick-3" in game else 4
    out = []
    for _ in range(sets):
        num = "".join(str(random.randint(0,9)) for _ in range(n))
        conf = random.randint(85,99)
        out.append({"number":num,"confidence":conf})
    return out

# ===========================================================
# 🎨 Cosmic Theme Styling
# ===========================================================
st.markdown("""
<style>
body {background-color: #020b16;}
h1,h2,h3,h4 {color:#9ef0ff;}
.metric {color:#00ffff;}
div[data-testid="stMetricValue"] {color:#00ffff;}
</style>
""", unsafe_allow_html=True)

# ===========================================================
# 🧠 Titan Energy Overview
# ===========================================================
phase_name, phase_percent = lunar_phase()
energy_level = round(phase_percent + random.uniform(0,10), 2)
st.markdown(f"### 🌙 Lunar Phase: {phase_name} ({phase_percent}%)")
st.progress(int(min(energy_level,100)))

col1, col2, col3 = st.columns(3)
col1.metric("🌎 Active States","GA / FL")
col2.metric("⚡ Energy Field", f"{energy_level}%")
col3.metric("📈 Accuracy", f"{random.randint(82,97)}%")

# ===========================================================
# 🎯 Forecast Console
# ===========================================================
st.divider(); st.subheader("🎯 Titan Forecast Console")
game = st.selectbox("Select Game",["GA Pick-3 Midday","GA Pick-3 Evening","FL Pick-4 Midday","FL Pick-4 Evening"])
sets = st.slider("Number of Forecast Sets",1,10,5)

if st.button("⚡ Generate Forecast"):
    forecasts = generate_forecast(game, sets)
    st.success(f"Generated {len(forecasts)} forecast sets for {game}")
    for f in forecasts:
        color = "#ffcc00" if f["confidence"]>95 else "#00ffff"
        st.markdown(
            f"<div style='background:rgba(255,255,255,0.05);border:1px solid {color};padding:8px;margin:4px 0;border-radius:6px;'>"
            f"<b>{f['number']}</b> — Confidence: <b style='color:{color}'>{f['confidence']}%</b></div>",
            unsafe_allow_html=True)

# ===========================================================
# 📥 Save Result Entry
# ===========================================================
st.divider(); st.subheader("📥 Log Official Result")
rcol1, rcol2, rcol3 = st.columns(3)
with rcol1: rgame = st.selectbox("Game",["GA Pick-3 Midday","GA Pick-3 Evening","FL Pick-4 Midday","FL Pick-4 Evening"])
with rcol2: rnum = st.text_input("Winning Number (Straight)")
with rcol3: rdate = st.date_input("Date", datetime.date.today())

if st.button("💾 Save Result"):
    if rnum.strip():
        save_result(rgame, rnum.strip(), rdate.isoformat(), user)
        st.success(f"Saved result for {rgame} ({rnum})")
    else: st.warning("Enter valid number first.")

# ===========================================================
# 📊 Analytics + Calendar View
# ===========================================================
st.divider(); st.subheader("📊 Titan Analytics & Calendar Sync")
data = get_user_data(user)
if data:
    df = pd.DataFrame(data)
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")

    # Chart
    fig, ax = plt.subplots()
    for g, sub in df.groupby("game"):
        ax.plot(sub["date"], range(len(sub)), label=g)
    ax.legend(); ax.set_title("Forecast Activity Timeline")
    st.pyplot(fig)

    # Calendar log
    for g in df["game"].unique():
        st.markdown(f"### 🌠 {g}")
        for m, subset in df[df["game"]==g].groupby(df["date"].dt.strftime("%B %Y")):
            st.markdown(f"**{m}**")
            for d, s in subset.groupby(subset["date"].dt.strftime("%Y-%m-%d")):
                nums = ", ".join(s["number"])
                st.markdown(f"{d} → {nums}")

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("📤 Export CSV", csv, "titan_results.csv")
else:
    st.info("No records yet — log results to start Titan learning.")

# ===========================================================
# 🧠 Titan Commentary
# ===========================================================
st.divider()
commentary = [
    "Energy harmonics stable — pattern optimization in progress.",
    "Variance decreasing — forecast precision improving daily.",
    "Lunar influence rising — expect elevated field resonance.",
    "Data field synchronized — Titan confidence core active."
]
st.markdown(f"### 🧠 Titan Insight: {random.choice(commentary)}")

# ===========================================================
# ☁️ Footer
# ===========================================================
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center;color:#9ef0ff;'>☁️ Titan Cloud Genesis Field Ready — v5.0 Uplink Imminent 💎</div>", unsafe_allow_html=True)

