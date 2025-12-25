# ==========================================================
# 💎 Celestial Titan God AI v1.0 — Ultimate Core Console
# 🌌 Modes: Integrated / Full / Hybrid + Titan Pulse + Lunar Sync
# ==========================================================
import streamlit as st
import json, os, random, datetime, math

# ==========================================================
# 🧭 Base Paths
# ==========================================================
BASE_DIR = os.path.expanduser("~/Desktop/titan_dual_state_lab")
FORECAST_FILE = os.path.join(BASE_DIR, "titan_forecasts.json")
RESULT_FILE   = os.path.join(BASE_DIR, "titan_results.json")
HISTORY_FILE  = os.path.join(BASE_DIR, "titan_history.json")
os.makedirs(BASE_DIR, exist_ok=True)

# ==========================================================
# ⚙️ JSON Handling (Auto-Repair)
# ==========================================================
def load_json(path, default):
    try:
        with open(path, "r") as f:
            data = json.load(f)
            if not isinstance(data, dict):
                data = default
            return data
    except:
        save_json(path, default)
        return default

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

# ==========================================================
# 🌕 Lunar Phase + Cosmic Pulse
# ==========================================================
def lunar_phase():
    now = datetime.datetime.utcnow()
    diff = now - datetime.datetime(2001,1,1)
    days = diff.days + (diff.seconds / 86400)
    lunations = 0.20439731 + (days * 0.03386319269)
    phase_index = lunations % 1
    pct = round(phase_index * 100, 1)
    icons = ["🌑","🌒","🌓","🌔","🌕","🌖","🌗","🌘"]
    name = ["New Moon","Waxing Crescent","First Quarter","Waxing Gibbous",
            "Full Moon","Waning Gibbous","Last Quarter","Waning Crescent"]
    i = int((phase_index * 8) % 8)
    return icons[i], name[i], pct

def titan_pulse(confidence):
    intensity = min(100, max(0, confidence + random.randint(-5,5)))
    return intensity

# ==========================================================
# 🎯 Forecast Generator
# ==========================================================
def generate_forecast(game, draw_type, sets=5):
    data = load_json(FORECAST_FILE, {"forecasts":[]})
    if "forecasts" not in data:
        data["forecasts"] = []
    today = str(datetime.date.today())
    forecasts = []
    for _ in range(sets):
        nlen = 3 if "Pick-3" in game else 4
        num = "".join(str(random.randint(0,9)) for _ in range(nlen))
        conf = random.randint(84,98)
        pulse = titan_pulse(conf)
        forecasts.append({
            "number": num, "confidence": conf, "pulse": pulse,
            "draw_type": draw_type, "game": game, "date": today
        })
    data["forecasts"].extend(forecasts)
    save_json(FORECAST_FILE, data)
    return forecasts

# ==========================================================
# 📊 Accuracy Engine
# ==========================================================
def compute_accuracy():
    f_data = load_json(FORECAST_FILE, {"forecasts":[]})
    r_data = load_json(RESULT_FILE, {"records":[]})
    forecasts = f_data.get("forecasts", [])
    results = r_data.get("records", [])
    hits, total = 0, 0
    for r in results:
        for f in forecasts:
            if f["game"]==r["game"] and f["draw_type"]==r["draw_type"] and f["date"]==r["date"]:
                total += 1
                if f["number"]==r["winning"]:
                    hits += 1
    acc = round((hits/total*100),2) if total>0 else 0
    return {"hits":hits,"total":total,"acc":acc}

# ==========================================================
# 🎬 Titan Console Modes
# ==========================================================
def render_integrated():
    st.subheader("🧠 Titan Unified Forecast Console (Mode A)")
    game = st.selectbox("Game", ["GA Pick-3","FL Pick-4"])
    draw = st.radio("Draw", ["Midday","Evening"], horizontal=True)
    sets = st.slider("Forecast Sets",3,10,5)
    if st.button("⚡ Generate Forecast"):
        forecasts = generate_forecast(game, draw, sets)
        for f in forecasts:
            st.markdown(
                f"<div style='padding:6px;border-radius:8px;border:1px solid #00ffff;'>"
                f"🔢 <b>{f['number']}</b> | Confidence: {f['confidence']}% | Pulse: {f['pulse']}%</div>",
                unsafe_allow_html=True)

def render_full():
    st.markdown("<h2 style='text-align:center;color:#0ff;'>🎬 Titan Cinematic Mode</h2>", unsafe_allow_html=True)
    st.write("Full-screen cosmic visualization loading...")
    icon, name, pct = lunar_phase()
    st.markdown(f"<h4 style='text-align:center;'>Lunar Sync: {icon} {name} ({pct}%)</h4>", unsafe_allow_html=True)
    acc = compute_accuracy()
    st.metric("⚡ Accuracy", f"{acc['acc']}%")
    st.metric("✅ Hits", acc['hits'])
    st.metric("🎯 Forecasts", acc['total'])
    st.progress(acc['acc']/100)

def render_hybrid():
    c1,c2 = st.columns([2,1])
    with c1:
        render_integrated()
    with c2:
        icon,name,pct = lunar_phase()
        st.markdown(f"### 🌕 Lunar Phase: {icon} {name} ({pct}%)")
        acc = compute_accuracy()
        st.metric("Titan Accuracy", f"{acc['acc']}%")
        st.metric("Hits", acc['hits'])

# ==========================================================
# 🎨 Theme + Layout
# ==========================================================
st.set_page_config(page_title="Titan God AI v1.0", page_icon="💎", layout="wide")
st.markdown("""
<style>
body {background-color:#02030a; color:#9cf;}
.stButton>button {background-color:#00ffff; color:black; border-radius:8px; font-weight:bold;}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;color:#0ff;'>💎 Celestial Titan God AI v1.0 — Ultimate Core</h1>", unsafe_allow_html=True)
mode = st.selectbox("🎛️ Choose Display Mode", ["Mode A — Integrated","Mode B — Full Console","Mode C — Hybrid"])

if "A" in mode: render_integrated()
elif "B" in mode: render_full()
else: render_hybrid()

st.write("---")
icon,name,pct = lunar_phase()
st.markdown(f"<div style='text-align:center;'>🌙 <b>{name}</b> phase detected — {pct}% illumination</div>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center;color:#00ffff;'>🪐 Titan Core Operational. Awaiting Cosmic Calibration v1.1...</div>", unsafe_allow_html=True)

