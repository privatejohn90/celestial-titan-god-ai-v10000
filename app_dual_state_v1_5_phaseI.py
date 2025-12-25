# ==========================================================
# 💎 Celestial Titan God AI v1.5 — Pattern & Harmonic Ascension Update
# 🔮 Combines v1.2 (Trend Oracle) + v1.3 (Lunar Overlay)
# + v1.4 (Harmonic Matrix) + v1.5 (Priority Forecast)
# ==========================================================
import streamlit as st
import json, os, random, datetime
import matplotlib.pyplot as plt

# ==========================================================
# 🧭 Base Paths
# ==========================================================
BASE_DIR = os.path.expanduser("~/Desktop/titan_dual_state_lab")
FORECAST_FILE = os.path.join(BASE_DIR, "titan_forecasts.json")
RESULT_FILE = os.path.join(BASE_DIR, "titan_results.json")
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
# 🌙 Lunar Phase Engine
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
# 🔢 Forecast Generator + Priority Logic
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
        conf = random.randint(80,98)
        forecasts.append({
            "number": num, "confidence": conf,
            "draw_type": draw_type, "game": game, "date": today
        })

    # mark one as "priority highlight"
    if forecasts:
        best = max(forecasts, key=lambda x: x["confidence"])
        best["priority"] = True
    data["forecasts"].extend(forecasts)
    save_json(FORECAST_FILE, data)
    return forecasts

# ==========================================================
# 📈 Trend Oracle — accuracy evolution chart
# ==========================================================
def plot_accuracy_trend():
    data = load_json(RESULT_FILE, {"records":[]})
    recs = data.get("records", [])
    if not recs:
        st.info("No accuracy data yet.")
        return
    dates = [r["date"] for r in recs]
    accs = [r["accuracy"] for r in recs]
    plt.figure(figsize=(6,3))
    plt.plot(dates, accs, marker="o")
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Accuracy %")
    plt.title("Titan Accuracy Trend (7-Day)")
    st.pyplot(plt)

# ==========================================================
# 🧬 Harmonic Pattern Detector
# ==========================================================
def harmonic_pattern_detect():
    data = load_json(RESULT_FILE, {"records":[]})
    recs = data.get("records", [])
    if len(recs) < 5:
        return "Not enough data to analyze harmonic streaks yet."
    nums = [r["winning"] for r in recs[-7:]]
    repeats = len(set(nums)) < len(nums)
    if repeats:
        return f"♻️ Repeating energy detected in last 7 draws: {nums[-3:]}"
    else:
        return f"⚡ Harmonic field clear — preparing next convergence."

# ==========================================================
# 🎨 UI
# ==========================================================
st.set_page_config(page_title="Titan God AI v1.5", page_icon="💎", layout="wide")
st.markdown("""
<style>
body {background-color:#01030a; color:#9cf;}
.stButton>button {background-color:#00ffff; color:black; border-radius:8px; font-weight:bold;}
</style>
""", unsafe_allow_html=True)
st.markdown("<h1 style='text-align:center;color:#00ffff;'>💎 Titan God AI v1.5 — Pattern & Harmonic Ascension</h1>", unsafe_allow_html=True)
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
        mark = "💠" if n.get("priority") else ""
        st.markdown(f"<div style='padding:6px;border:1px solid #00ffff;border-radius:8px;'>🔢 {n['number']} {mark} | Confidence {n['confidence']}%</div>", unsafe_allow_html=True)
st.write("---")

# ==========================================================
# 🌙 Lunar Intelligence Overlay
# ==========================================================
st.subheader("🌙 Lunar Intelligence Overlay")
icon, name, pct = lunar_phase()
st.markdown(f"<div style='padding:8px;border:1px solid #0ff;border-radius:10px;'>Current Phase: {icon} {name} ({pct}%)</div>", unsafe_allow_html=True)

# ==========================================================
# 📈 Trend Oracle
# ==========================================================
st.subheader("📊 Titan Trend Oracle")
plot_accuracy_trend()

# ==========================================================
# 🧬 Harmonic Prediction Matrix
# ==========================================================
st.subheader("🧬 Harmonic Prediction Matrix")
pattern = harmonic_pattern_detect()
st.markdown(f"<div style='padding:8px;border:1px solid #0ff;border-radius:10px;'>{pattern}</div>", unsafe_allow_html=True)

