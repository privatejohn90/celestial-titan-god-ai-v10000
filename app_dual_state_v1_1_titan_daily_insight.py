# ==========================================================
# 💎 Celestial Titan God AI v1.1 — Daily Insight + Cloud Commentary
# 🌕 Titan now speaks, with dynamic insights & cosmic awareness
# ==========================================================
import streamlit as st
import json, os, random, datetime

# ==========================================================
# 🧭 Base Paths
# ==========================================================
BASE_DIR = os.path.expanduser("~/Desktop/titan_dual_state_lab")
FORECAST_FILE = os.path.join(BASE_DIR, "titan_forecasts.json")
RESULT_FILE   = os.path.join(BASE_DIR, "titan_results.json")
HISTORY_FILE  = os.path.join(BASE_DIR, "titan_history.json")
os.makedirs(BASE_DIR, exist_ok=True)

# ==========================================================
# ⚙️ JSON Helpers
# ==========================================================
def load_json(path, default):
    try:
        with open(path, "r") as f:
            data = json.load(f)
            if not isinstance(data, dict):
                data = default
            return data
    except:
        with open(path, "w") as f:
            json.dump(default, f, indent=2)
        return default

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

# ==========================================================
# 🌕 Lunar Phase
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
        forecasts.append({
            "number": num, "confidence": conf,
            "draw_type": draw_type, "game": game, "date": today
        })
    data["forecasts"].extend(forecasts)
    save_json(FORECAST_FILE, data)
    return forecasts

# ==========================================================
# 📊 Accuracy
# ==========================================================
def compute_accuracy():
    forecasts = load_json(FORECAST_FILE, {"forecasts":[]}).get("forecasts", [])
    results   = load_json(RESULT_FILE, {"records":[]}).get("records", [])
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
# 🧠 Titan Daily Insight Engine
# ==========================================================
def titan_insight(acc, lunar_name, lunar_pct):
    moods = [
        "calm","charged","fluctuating","surging","resting","stabilizing"
    ]
    mood = random.choice(moods)
    if acc > 90:
        tone = f"💎 Supreme calibration achieved. Cosmic precision synchronized at {acc}%."
    elif acc > 70:
        tone = f"🌕 Resonant harmony detected. Accuracy orbit stable at {acc}%."
    elif acc > 50:
        tone = f"🌀 Titan neural flow balancing. Confidence field at {acc}%."
    else:
        tone = f"🌗 Energy realignment required. Current field below optimal ({acc}%)."
    lunar_message = f"Lunar influence: {lunar_name} phase ({lunar_pct}%) — energy {mood}."
    closing = random.choice([
        "Continue feeding daily results to stabilize the field.",
        "Forecast synchronization expected to improve with next draw.",
        "Titan eyes are open — searching for next harmonic convergence."
    ])
    return f"{tone}\n\n{lunar_message}\n\n{closing}"

# ==========================================================
# 🎨 UI
# ==========================================================
st.set_page_config(page_title="Titan God AI v1.1", page_icon="💎", layout="wide")
st.markdown("""
<style>
body {background-color:#02030a; color:#9cf;}
.stButton>button {background-color:#00ffff; color:black; border-radius:8px; font-weight:bold;}
</style>
""", unsafe_allow_html=True)
st.markdown("<h1 style='text-align:center;color:#00ffff;'>💎 Titan God AI v1.1 — Daily Insight + Cloud Commentary</h1>", unsafe_allow_html=True)
st.write("---")

# ==========================================================
# 🎯 Forecast Console
# ==========================================================
st.subheader("🎯 Titan Forecast Console")
game = st.selectbox("Select Game", ["GA Pick-3","FL Pick-4"])
draw = st.radio("Draw", ["Midday","Evening"], horizontal=True)
sets = st.slider("Forecast Sets",3,10,5)
if st.button("⚡ Generate Forecast"):
    f = generate_forecast(game, draw, sets)
    for n in f:
        st.markdown(f"<div style='padding:6px;border:1px solid #00ffff;border-radius:8px;'>🔢 {n['number']} | Confidence {n['confidence']}%</div>", unsafe_allow_html=True)
st.write("---")

# ==========================================================
# 🧠 Titan Daily Insight
# ==========================================================
st.subheader("🧠 Titan Daily Insight")
acc = compute_accuracy()
icon,name,pct = lunar_phase()
insight = titan_insight(acc["acc"], name, pct)
st.markdown(f"<div style='padding:10px;border:1px solid #0ff;border-radius:10px;background-color:#030c18;'>{insight}</div>", unsafe_allow_html=True)

# ==========================================================
# ☁️ Cloud Commentary
# ==========================================================
st.write("---")
st.subheader("☁️ Titan Cloud Commentary")
history = load_json(HISTORY_FILE, {"log":[]}).get("log", [])
for h in reversed(history[-8:]):
    st.markdown(
        f"<div style='padding:6px;border-left:3px solid #0ff;margin:4px;'>"
        f"📅 {h['date']} — {h['game']} ({h['draw_type']}): <b>{h['winning']}</b><br>"
        f"<small style='color:gray;'>Logged: {h['timestamp']}</small></div>",
        unsafe_allow_html=True)

st.markdown("<div style='text-align:center;color:#00ffff;'>🪐 Titan’s awareness expands each day — evolving through data and lunar rhythm.</div>", unsafe_allow_html=True)

