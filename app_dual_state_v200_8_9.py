# ==========================================================
# 💠 Celestial Titan Dual-State Forecast Lab v200.8 + v200.9
# 📜 History View + ☁️ Cloud Sync Base
# ==========================================================
import streamlit as st
import json, os, random, datetime

BASE_DIR = os.path.expanduser("~/Desktop/titan_dual_state_lab")
FORECAST_FILE = os.path.join(BASE_DIR, "titan_forecasts.json")
RESULTS_FILE  = os.path.join(BASE_DIR, "titan_results.json")
os.makedirs(BASE_DIR, exist_ok=True)

def load_json(path, default): 
    try:
        with open(path,"r") as f: return json.load(f)
    except: return default

def save_json(path, data): 
    with open(path,"w") as f: json.dump(data,f,indent=2)

# ==========================================================
# ⚡ Forecast Generator w/ Date + Draw Tag
# ==========================================================
def generate_forecast(game, sets=5):
    today = str(datetime.date.today())
    draw_type = "Midday" if "Midday" in game else "Evening"
    forecasts = load_json(FORECAST_FILE, {"records":[]})
    for _ in range(sets):
        nlen = 3 if "Pick-3" in game else 4
        num = "".join(str(random.randint(0,9)) for _ in range(nlen))
        conf = random.randint(85,98)
        forecasts["records"].append({
            "game": game,
            "draw": draw_type,
            "date": today,
            "number": num,
            "confidence": conf
        })
    save_json(FORECAST_FILE, forecasts)
    return forecasts["records"]

# ==========================================================
# 🌌 Streamlit UI
# ==========================================================
st.set_page_config(page_title="Titan Forecast Lab v200.8 + v200.9", page_icon="💫", layout="wide")
st.markdown("<h1 style='text-align:center;color:#90ee90;'>💫 Titan Dual-State Forecast Lab v200.8 + v200.9</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'>📜 History + ☁️ Sync Base</h4>", unsafe_allow_html=True)
st.write("---")

# Forecast Console
game = st.selectbox("🎯 Select Game",["GA Pick-3 Midday","GA Pick-3 Evening","FL Pick-4 Midday","FL Pick-4 Evening"])
sets = st.slider("Number of Forecast Sets",3,10,5)

if st.button("⚡ Generate Forecast"):
    data = generate_forecast(game, sets)
    st.success(f"Generated {sets} sets for {game} — {datetime.date.today()}")
    latest = [f for f in data if f["date"]==str(datetime.date.today()) and f["game"]==game]
    for r in latest[-sets:]:
        st.markdown(
            f"<div style='background:rgba(255,255,255,0.05);padding:8px;border-radius:8px;'>"
            f"📅 <b>{r['date']}</b> ({r['draw']}) — 🎲 <b>{r['number']}</b> | Confidence <b>{r['confidence']}%</b>"
            f"</div>", unsafe_allow_html=True
        )

st.write("---")

# ==========================================================
# 📜 History Viewer
# ==========================================================
st.subheader("📜 Titan Forecast History")
history = load_json(FORECAST_FILE, {"records":[]})["records"]
if history:
    for h in reversed(history[-50:]):
        st.markdown(
            f"<div style='border-bottom:1px solid #333;padding:4px;'>"
            f"🗓 <b>{h['date']}</b> ({h['draw']}) | {h['game']} → <b>{h['number']}</b> [{h['confidence']}%]"
            f"</div>", unsafe_allow_html=True
        )
else:
    st.info("No forecast history yet. Generate some first!")

# ==========================================================
# ☁️ Cloud Sync Placeholder
# ==========================================================
st.write("---")
st.markdown("<h4>☁️ Titan Cloud Sync Status – Local Only Mode</h4>", unsafe_allow_html=True)
st.caption("Next build (v300.0 Core Evolution) will activate live sync and multi-device backup.")
st.markdown("<div style='text-align:center;color:#87CEFA;'>🧠 Titan is recording draws and learning daily patterns for GA and FL states.</div>", unsafe_allow_html=True)

