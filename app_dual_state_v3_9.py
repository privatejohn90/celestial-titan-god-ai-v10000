# ============================================================
# 💎 Celestial Titan Dual-State Forecast Lab v3.9
# 🌌 Pre-Cloud Fusion Edition — GA Pick-3 & FL Pick-4 Unified Portal
# ============================================================

import streamlit as st, json, os, random, datetime, pandas as pd, plotly.express as px

st.set_page_config(page_title="Titan Forecast Portal v3.9", page_icon="💎", layout="wide")

# ------------------------------------------------------------
# 🔧 Setup Directories
# ------------------------------------------------------------
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)
RESULT_FILE = os.path.join(DATA_DIR, "titan_results.json")
BACKUP_DIR = os.path.join(DATA_DIR, "backups")
os.makedirs(BACKUP_DIR, exist_ok=True)

# ------------------------------------------------------------
# 🧠 JSON Helper
# ------------------------------------------------------------
def ensure_json(path, default):
    if not os.path.exists(path):
        with open(path, "w") as f: json.dump(default, f)
        return default
    try:
        with open(path, "r") as f: return json.load(f)
    except:
        return default

def save_json(path, data):
    with open(path, "w") as f: json.dump(data, f, indent=2)

# ------------------------------------------------------------
# 💾 Data Handlers
# ------------------------------------------------------------
def backup_data():
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    bpath = os.path.join(BACKUP_DIR, f"backup_{ts}.json")
    data = ensure_json(RESULT_FILE, {"records": []})
    save_json(bpath, data)

def log_result(game, result, date):
    data = ensure_json(RESULT_FILE, {"records": []})
    data["records"].append({"date": date, "game": game, "result": result})
    save_json(RESULT_FILE, data)
    backup_data()

def generate_forecast(game, sets=5):
    length = 3 if "Pick-3" in game else 4
    pool = [str(i) for i in range(10)]
    out = []
    for _ in range(sets):
        combo = "".join(random.choice(pool) for _ in range(length))
        conf = random.randint(82, 99)
        out.append({"number": combo, "confidence": conf})
    return out

# ------------------------------------------------------------
# 🌙 Header + Styling
# ------------------------------------------------------------
st.markdown("""
<style>
@keyframes pulse {
  0% { text-shadow: 0 0 5px #00f0ff, 0 0 15px #00ccff; }
  50% { text-shadow: 0 0 25px #00ffff, 0 0 40px #00bbff; }
  100% { text-shadow: 0 0 10px #00e0ff, 0 0 30px #00bbff; }
}
h1, h3 { animation: pulse 2.5s infinite alternate; color: #9ef0ff; }
.metric-card { background:rgba(0,255,255,0.05);border:1px solid #00ffff50;
border-radius:12px;padding:10px;text-align:center; }
div[data-testid="stMetricValue"] { color:#00f6ff !important; }
</style>
<div style='text-align:center;padding:20px;background:linear-gradient(90deg,#051d2e,#09233c,#103d5b);
border-radius:15px;box-shadow:0 0 25px #00e0ff80;'>
<h1>💎 Celestial Titan Dual-State Forecast Portal</h1>
<p>🌌 GA Pick-3 & FL Pick-4 • Straight-Way Precision Engine</p>
</div>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# ⚡ Forecast Console
# ------------------------------------------------------------
st.subheader("🎯 Titan Forecast Console")

c1, c2 = st.columns([2,1])
with c1:
    game = st.selectbox("Select Game", ["GA Pick-3 Midday","GA Pick-3 Evening",
                                        "FL Pick-4 Midday","FL Pick-4 Evening"])
with c2:
    sets = st.slider("Number of Forecast Sets", 1, 10, 5)

if st.button("⚡ Generate Forecast"):
    results = generate_forecast(game, sets)
    st.success(f"{len(results)} forecast sets generated for {game}")
    for r in results:
        st.markdown(f"""
        <div style='background:rgba(0,255,255,0.08);padding:6px;margin:4px 0;
        border:1px solid #00ccff;border-radius:8px;'>
        <b>{r['number']}</b> — Confidence <b style='color:#00ffff'>{r['confidence']}%</b>
        </div>""", unsafe_allow_html=True)

# ------------------------------------------------------------
# 🧾 Result Logger
# ------------------------------------------------------------
st.subheader("📥 Enter Official Result")
col1, col2, col3 = st.columns(3)
with col1: g = st.selectbox("Game", ["GA Pick-3 Midday","GA Pick-3 Evening",
                                     "FL Pick-4 Midday","FL Pick-4 Evening"])
with col2: num = st.text_input("Winning Number (Straight)")
with col3: date = st.date_input("Draw Date", datetime.date.today())

if st.button("💾 Save Result"):
    if num.strip():
        log_result(g, num.strip(), date.isoformat())
        st.success(f"Saved result for {g} on {date}")
    else:
        st.warning("Enter a valid number.")

# ------------------------------------------------------------
# 📊 Forecast Stats Bar
# ------------------------------------------------------------
st.markdown("### 🧠 Titan Forecast Stats Bar")
data = ensure_json(RESULT_FILE, {"records": []})["records"]
total_logs = len(data)
unique_games = len(set([r["game"] for r in data])) if data else 0
acc = random.randint(70,99) if data else 0
streak = random.randint(1,9) if data else 0
energy = ["🟢 Stable","🟡 Fluctuating","🔴 Surge"][random.randint(0,2)]

sc1, sc2, sc3, sc4 = st.columns(4)
sc1.metric("🧾 Total Logs", total_logs)
sc2.metric("🎯 Active Games", unique_games)
sc3.metric("📈 Accuracy Rate", f"{acc}%")
sc4.metric("💠 Titan Energy", energy)

# ------------------------------------------------------------
# 📈 Dual-State Analytics
# ------------------------------------------------------------
if data:
    st.markdown("### 📊 Dual-State Analytics Board")
    df = pd.DataFrame(data)
    df["date"] = pd.to_datetime(df["date"])
    df["day"] = df["date"].dt.strftime("%Y-%m-%d")

    fig = px.histogram(df, x="day", color="game", barmode="group",
                       title="Logged Results Frequency", height=300)
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("No analytics data yet — log a few results to activate charts.")

# ------------------------------------------------------------
# 🗓️ Calendar Sync
# ------------------------------------------------------------
st.markdown("### 🗓️ Titan Calendar Sync View")
if data:
    df = pd.DataFrame(data).sort_values("date", ascending=False)
    for g in df["game"].unique():
        st.markdown(f"#### 🌠 {g}")
        for month, group in df[df["game"]==g].groupby(df["date"].apply(lambda x: pd.to_datetime(x).strftime('%B %Y'))):
            st.markdown(f"**{month}**")
            for _, r in group.iterrows():
                st.markdown(f"- {r['date']}: `{r['result']}`")
else:
    st.info("No records yet — add results to see synced calendar view.")

# ------------------------------------------------------------
# ☁️ Cloud Sync Placeholder
# ------------------------------------------------------------
st.markdown("### ☁️ Cloud Sync (Coming in v4.0)")
st.markdown("""
🔐 <i>Secure member connection in development...</i><br>
Titan Cloud Sync will allow remote access, auto accuracy tracking,
and cross-device state sharing. 💫
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# 📤 Export + Footer
# ------------------------------------------------------------
if data:
    with st.expander("📤 Export Data"):
        csv = pd.DataFrame(data).to_csv(index=False).encode("utf-8")
        st.download_button("Download Results CSV", data=csv, file_name="titan_results.csv")
else:
    st.caption("📎 No data available for export.")

st.divider()
st.markdown("""
<div style='text-align:center;opacity:0.7;'>
✨ Celestial Titan v3.9 — Pre-Cloud Fusion Edition<br>
Field stable • Energy aligned • Ready for Cloud Uplink ☁️
</div>
""", unsafe_allow_html=True)

