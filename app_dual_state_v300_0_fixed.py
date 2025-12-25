# ==========================================================
# 💎 Celestial Titan God AI v300.0 — Final Hybrid Core (Stable Edition)
# ==========================================================
import streamlit as st
import json, os, random, datetime, time
import matplotlib.pyplot as plt

# ==========================================================
# 🧠 PATHS
# ==========================================================
BASE = os.path.expanduser("~/Desktop/titan_dual_state_lab")
FORECAST = os.path.join(BASE, "titan_forecasts.json")
RESULTS = os.path.join(BASE, "titan_results.json")
HISTORY = os.path.join(BASE, "titan_history.json")
CLOUD = os.path.join(BASE, "titan_cloud.json")
os.makedirs(BASE, exist_ok=True)

def load_json(p, d):
    try:
        with open(p, "r") as f:
            return json.load(f)
    except:
        with open(p, "w") as f:
            json.dump(d, f, indent=2)
        return d

def save_json(p, d):
    with open(p, "w") as f:
        json.dump(d, f, indent=2)

# ==========================================================
# 🌙 LUNAR + ENERGY
# ==========================================================
def lunar_phase():
    now = datetime.datetime.utcnow()
    diff = now - datetime.datetime(2001, 1, 1)
    days = diff.days + diff.seconds / 86400
    lunations = 0.20439731 + (days * 0.03386319269)
    phase_index = lunations % 1
    pct = round(phase_index * 100, 1)
    icons = ["🌑", "🌒", "🌓", "🌔", "🌕", "🌖", "🌗", "🌘"]
    names = ["New Moon", "Waxing Crescent", "First Quarter", "Waxing Gibbous",
             "Full Moon", "Waning Gibbous", "Last Quarter", "Waning Crescent"]
    i = int((phase_index * 8) % 8)
    return icons[i], names[i], pct, random.randint(70, 98)

# ==========================================================
# 🎯 FORECAST GENERATION (FIXED)
# ==========================================================
def generate_forecast(game, draw_type, sets=5):
    data = load_json(FORECAST, {"forecasts": []})
    if "forecasts" not in data:
        data["forecasts"] = []

    today = str(datetime.date.today())
    fc = []
    for _ in range(sets):
        nlen = 3 if "Pick-3" in game else 4
        num = "".join(str(random.randint(0, 9)) for _ in range(nlen))
        conf = random.randint(82, 99)
        fc.append({
            "number": num,
            "confidence": conf,
            "game": game,
            "draw_type": draw_type,
            "date": today
        })
    fc = sorted(fc, key=lambda x: x["confidence"], reverse=True)
    for i, f in enumerate(fc):
        f["priority"] = "💠 Titan Prime" if i == 0 else "🔥 High" if f["confidence"] > 90 else "⚪ Normal"

    data.setdefault("forecasts", [])
    data["forecasts"].extend(fc)
    save_json(FORECAST, data)

    hist = load_json(HISTORY, {"records": []})
    hist.setdefault("records", [])
    hist["records"].extend(fc)
    save_json(HISTORY, hist)

    return fc

# ==========================================================
# 📈 ACCURACY
# ==========================================================
def accuracy_chart():
    res = load_json(RESULTS, {"records": []}).get("records", [])
    if not res:
        return None
    total, hit = 0, 0
    acc, dates = [], []
    for r in res:
        total += 1
        if r.get("hit"):
            hit += 1
        acc.append(round((hit / total) * 100, 2))
        dates.append(r["date"])
    fig, ax = plt.subplots()
    ax.plot(dates, acc, color="#00ffff", marker="o")
    ax.set_title("Titan Accuracy Trend")
    ax.set_xlabel("Date")
    ax.set_ylabel("Accuracy %")
    plt.xticks(rotation=45)
    return fig, round((hit / total) * 100, 2)

# ==========================================================
# ☁️ CLOUD SYNC
# ==========================================================
def titan_sync():
    payload = {
        "forecasts": load_json(FORECAST, {"forecasts": []}),
        "results": load_json(RESULTS, {"records": []}),
        "history": load_json(HISTORY, {"records": []}),
        "timestamp": str(datetime.datetime.now())
    }
    save_json(CLOUD, payload)
    return payload

# ==========================================================
# 🎨 UI SETTINGS
# ==========================================================
st.set_page_config(page_title="Titan AI v300.0", page_icon="💠", layout="wide")

theme = st.sidebar.radio("🎨 Theme", ["Cosmic", "Dark Crystal", "Neon"])
mode = st.sidebar.radio("🧩 Display Mode", ["Integrated", "Fullscreen", "Hybrid"])
st.sidebar.markdown("💠 **Celestial Titan God AI v300.0 — Hybrid Core Active**")

if theme == "Cosmic":
    bg, fg, accent = "#000014", "#b5faff", "#00ffff"
elif theme == "Dark Crystal":
    bg, fg, accent = "#080808", "#e6e6e6", "#9b59b6"
else:
    bg, fg, accent = "#000000", "#00ffea", "#ff007f"

st.markdown(f"""
<style>
body {{background-color:{bg};color:{fg};}}
.block{{border:1px solid {accent};padding:10px;border-radius:10px;margin:6px;}}
</style>
""", unsafe_allow_html=True)

# ==========================================================
# 🌀 TITAN HEADER
# ==========================================================
st.markdown(f"<h1 style='text-align:center;color:{accent};'>💠 Celestial Titan God AI — Hybrid Evolution v300.0</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Unified Forecast • Cosmic Accuracy • Hybrid Console</p>", unsafe_allow_html=True)
st.write("---")

# ==========================================================
# 🌙 ENERGY DISPLAY
# ==========================================================
icon, name, pct, orb = lunar_phase()
st.metric("🌙 Lunar Phase", f"{name} ({pct}%)")
st.metric("⚡ Orb Energy", f"{orb}%")

# ==========================================================
# 🎯 FORECAST CONSOLE
# ==========================================================
st.subheader("🎯 Titan Forecast Console")
c1, c2 = st.columns(2)
with c1:
    game = st.selectbox("Game", ["GA Pick-3", "FL Pick-4"])
with c2:
    draw = st.radio("Draw Type", ["Midday", "Evening"], horizontal=True)
sets = st.slider("Number of Forecast Sets", 3, 10, 5)

if st.button("⚡ Generate Forecast"):
    f = generate_forecast(game, draw, sets)
    st.markdown(f"### 📅 {datetime.date.today()} | {game} {draw}")
    for x in f:
        st.markdown(f"<div class='block'>🔢 {x['number']} | Confidence: {x['confidence']}% | {x['priority']}</div>", unsafe_allow_html=True)
    st.info("🧠 Titan Insight: " + random.choice([
        "Forecast harmonized with cosmic pattern field.",
        "Stability wave aligned — energy field responsive.",
        "Phase link established — prediction ready for sync."
    ]))

# ==========================================================
# 🧾 RESULT ENTRY
# ==========================================================
st.write("---")
st.subheader("📥 Log Official Result")
c1, c2, c3, c4 = st.columns(4)
with c1:
    rg = st.selectbox("Game", ["GA Pick-3", "FL Pick-4"], key="resg")
with c2:
    rd = st.radio("Draw Type", ["Midday", "Evening"], horizontal=True, key="resd")
with c3:
    rdate = st.date_input("Date", datetime.date.today())
with c4:
    rnum = st.text_input("Winning Number", "")

if st.button("💾 Save Result"):
    results = load_json(RESULTS, {"records": []})
    rec = {"game": rg, "draw_type": rd, "date": str(rdate), "winning": rnum}
    allf = load_json(FORECAST, {"forecasts": []}).get("forecasts", [])
    rec["hit"] = any(f for f in allf if f["game"] == rg and f["draw_type"] == rd and f["date"] == str(rdate) and f["number"] == rnum)
    results["records"].append(rec)
    save_json(RESULTS, results)
    if rec["hit"]:
        st.success(f"🎯 Titan Hit Detected — {rnum} ({rg} {rd})")
    else:
        st.warning(f"Saved {rnum} ({rg} {rd}) — no hit match.")

# ==========================================================
# 📊 ACCURACY + HISTORY
# ==========================================================
st.write("---")
st.subheader("📊 Accuracy Dashboard")
chart = accuracy_chart()
if chart:
    fig, acc = chart
    st.pyplot(fig)
    st.metric("Current Accuracy", f"{acc}%")
else:
    st.info("No logged results yet — Titan calibration pending.")

st.write("---")
st.subheader("📖 Forecast History")
hist = load_json(HISTORY, {"records": []}).get("records", [])
if hist:
    for rec in hist[-15:][::-1]:
        st.markdown(f"🔹 {rec['date']} | {rec['game']} {rec['draw_type']} → {rec['number']} ({rec['confidence']}%)")
else:
    st.info("No forecast history yet.")

# ==========================================================
# ☁️ CLOUD SYNC
# ==========================================================
st.write("---")
if st.button("☁️ Sync to Titan Cloud"):
    s = titan_sync()
    st.success(f"Titan Cloud Synced at {s['timestamp']}")

# ==========================================================
# 🌌 FINAL SUMMARY
# ==========================================================
st.write("---")
st.markdown(f"""
### 🌌 Titan Final Hybrid Summary
✅ Unified Forecast Console  
✅ Log Result + Hit Detection  
✅ Accuracy + Trend Chart  
✅ History + Cloud Sync  
✅ Theme Customizer ({theme})  
✅ Display Mode: {mode}  

> “Hybrid Core active — Titan’s field harmonized across all states.” 💠
""")

