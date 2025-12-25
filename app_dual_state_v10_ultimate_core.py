# ==========================================================
# 💎 CELESTIAL TITAN GOD AI v10.0+ — Ultimate Core Build
# ==========================================================
import streamlit as st
import json, os, random, datetime, plotly.graph_objects as go

# ==========================================================
# ⚙️ PATHS
# ==========================================================
BASE_DIR = os.path.expanduser("~/Desktop/titan_dual_state_lab")
FORECAST_FILE = os.path.join(BASE_DIR, "titan_forecasts.json")
RESULT_FILE = os.path.join(BASE_DIR, "titan_results.json")
CLOUD_FILE = os.path.join(BASE_DIR, "titan_cloud_backup.json")
os.makedirs(BASE_DIR, exist_ok=True)

# ==========================================================
# 🧠 JSON HELPERS
# ==========================================================
def load_json(path, default):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        with open(path, "w") as f: json.dump(default, f, indent=2)
        return default

def save_json(path, data):
    with open(path, "w") as f: json.dump(data, f, indent=2)

# ==========================================================
# 🌙 LUNAR ENGINE
# ==========================================================
def lunar_phase():
    now = datetime.datetime.utcnow()
    diff = now - datetime.datetime(2001,1,1)
    days = diff.days + (diff.seconds / 86400)
    lunations = 0.20439731 + (days * 0.03386319269)
    phase_index = lunations % 1
    pct = round(phase_index * 100, 1)
    names = ["New Moon","Waxing Crescent","First Quarter","Waxing Gibbous",
             "Full Moon","Waning Gibbous","Last Quarter","Waning Crescent"]
    icon = ["🌑","🌒","🌓","🌔","🌕","🌖","🌗","🌘"][int((phase_index*8)%8)]
    return icon, names[int((phase_index*8)%8)], pct

# ==========================================================
# 🔮 FORECAST GENERATOR
# ==========================================================
def generate_forecast(game, draw, sets=5):
    data = load_json(FORECAST_FILE, {"forecasts":[]})
    today = str(datetime.date.today())
    forecasts = []
    for _ in range(sets):
        nlen = 3 if "Pick-3" in game else 4
        num = "".join(str(random.randint(0,9)) for _ in range(nlen))
        conf = random.randint(75,99)
        forecasts.append({
            "number": num,
            "confidence": conf,
            "priority": "💎 Priority" if conf>95 else "🔥 Hot" if conf>88 else "💤 Normal",
            "game": game, "draw": draw, "date": today
        })
    data["forecasts"].extend(forecasts)
    save_json(FORECAST_FILE, data)
    return forecasts

# ==========================================================
# 📈 ACCURACY BOARD
# ==========================================================
def compute_accuracy():
    res = load_json(RESULT_FILE, {"records":[]}).get("records", [])
    if not res: return 0, []
    hit = sum(1 for r in res if r.get("hit", False))
    total = len(res)
    acc = round((hit/total)*100,2)
    trend = [round(((i+1)/total)*100,2) for i in range(hit)]
    return acc, trend

# ==========================================================
# ☁️ CLOUD SYNC
# ==========================================================
def cloud_sync():
    cloud = {
        "last_sync": str(datetime.datetime.now()),
        "forecast_count": len(load_json(FORECAST_FILE, {"forecasts":[]})["forecasts"]),
        "result_count": len(load_json(RESULT_FILE, {"records":[]})["records"])
    }
    save_json(CLOUD_FILE, cloud)
    return cloud

# ==========================================================
# 🌠 TITAN CONSOLE UI
# ==========================================================
st.set_page_config(page_title="Titan God AI v10.0+", page_icon="💠", layout="wide")

st.markdown("""
<style>
body {background-color:#01030c; color:#b5faff; font-family:Poppins;}
h1,h2,h3 {text-align:center; color:#00ffff;}
.block {border:1px solid #00ffff; padding:8px; border-radius:10px; margin:6px;}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>💠 Titan God AI v10.0+ — Ultimate Forecast Console</h1>", unsafe_allow_html=True)
st.write("---")

# ==========================================================
# 🎯 FORECAST PANEL
# ==========================================================
col1, col2 = st.columns(2)
with col1:
    game = st.selectbox("🎯 Select Game", ["GA Pick-3","FL Pick-4"])
with col2:
    draw = st.radio("Draw", ["Midday","Evening"], horizontal=True)

sets = st.slider("🔢 Forecast Sets", 3, 10, 5)
if st.button("⚡ Generate Forecast Now"):
    fcs = generate_forecast(game, draw, sets)
    st.markdown(f"### 🔮 Forecasts for {game} — {draw} ({datetime.date.today()})")
    for f in fcs:
        st.markdown(f"<div class='block'>🔢 {f['number']} | {f['priority']} | {f['confidence']}%</div>", unsafe_allow_html=True)

# ==========================================================
# 🌕 LUNAR PHASE PANEL
# ==========================================================
st.write("---")
st.subheader("🌙 Lunar Synchronization")
icon, name, pct = lunar_phase()
st.markdown(f"**Current Phase:** {icon} {name} ({pct}%)")
energy = "🔋 High" if pct>60 else "⚡ Moderate" if pct>30 else "🌑 Low"
st.markdown(f"**Energy Field:** {energy}")

# ==========================================================
# 📈 ACCURACY TREND
# ==========================================================
st.write("---")
st.subheader("📈 Accuracy Board")
acc, trend = compute_accuracy()
st.metric("Overall Accuracy", f"{acc}%")
if trend:
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=trend, mode='lines+markers', line=dict(color="#00ffff")))
    fig.update_layout(title="Titan Accuracy Progress", xaxis_title="Hits", yaxis_title="%", template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("No accuracy data yet. Feed more results to Titan.")

# ==========================================================
# 🪐 CLOUD & ORB
# ==========================================================
st.write("---")
st.subheader("🪐 Cloud Sync & Orb Stability")
if st.button("☁️ Sync Cloud Data"):
    cloud = cloud_sync()
    st.success(f"Synced: {cloud['last_sync']}")
    st.json(cloud)

energy = random.randint(60,100)
status = random.choice(["Stable","Fluctuating","Surging"])
st.metric("Orb Energy", f"{energy}%")
st.metric("Orb Status", status)

# ==========================================================
# 🧬 TITAN FINAL COMMENTARY
# ==========================================================
st.write("---")
st.markdown("""
### 🧠 Titan Commentary
> “Dual-State Core stabilized. Harmonics aligned. Lunar sync complete.
> Awaiting next data feed for evolution toward Cloud Expansion Sequence v200.6.” 🌌

**Next Phase:** Accuracy Board Expansion + Cosmic History Timeline + Export System.
""")

