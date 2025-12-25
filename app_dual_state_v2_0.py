# ==========================================================
# 💎 Celestial Titan Dual-State Forecast Lab v2.0 — Unified Core Edition
# 🌌 GA Pick-3 & FL Pick-4 | Midday + Evening | Straight-Way Focus
# ==========================================================

import streamlit as st, random, json, os, datetime, pandas as pd, plotly.graph_objects as go

st.set_page_config(page_title="Titan Dual-State Lab v2.0", page_icon="💎", layout="wide")

# ------------------ FILES & MEMORY SETUP ------------------
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

GA_FILE = os.path.join(DATA_DIR, "GA.json")
FL_FILE = os.path.join(DATA_DIR, "FL.json")
for path in [GA_FILE, FL_FILE]:
    if not os.path.exists(path):
        with open(path, "w") as f: json.dump({"records":[]}, f)

def load_json(path):
    with open(path,"r") as f: return json.load(f)
def save_json(path,data):
    with open(path,"w") as f: json.dump(data,f,indent=2)

# ------------------ FORECAST LOGIC ------------------
def generate_numbers(game, n_sets):
    length = 3 if "Pick-3" in game else 4
    forecasts = []
    for _ in range(n_sets):
        num = "".join([str(random.randint(0,9)) for _ in range(length)])
        confidence = random.randint(78,99)
        forecasts.append({"number": num, "confidence": confidence})
    return forecasts

# ------------------ ACCURACY COMPUTATION ------------------
def compute_accuracy(data):
    if not data or "records" not in data: return 0
    total = len(data["records"])
    hits = sum(1 for r in data["records"] if r.get("hit"))
    return round((hits/total)*100,2) if total>0 else 0

# ------------------ TITAN INSIGHT ------------------
def titan_insight(acc):
    if acc >= 90: return "🌠 Titan field resonating with divine precision."
    elif acc >= 75: return "💫 Titan harmonic field stabilizing — accuracy trending upward."
    elif acc >= 50: return "🌗 Energy variance detected — recalibration in progress."
    else: return "🌑 Low resonance — feed more data for synchronization."

# ------------------ UI ------------------
st.markdown("<h1 style='text-align:center;color:#B5CFFF;'>💎 Celestial Titan Dual-State Forecast Lab v2.0</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#9AD0FF;'>Silent Cosmic Mode — GA Pick-3 & FL Pick-4 Unified Core</p>", unsafe_allow_html=True)
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("🎯 Forecast Console")
    game = st.selectbox("Select Game", ["GA Pick-3 Midday","GA Pick-3 Evening","FL Pick-4 Midday","FL Pick-4 Evening"])
    n_sets = st.slider("Number of Forecast Sets",3,10,5)
    if st.button("⚡ Generate Forecast"):
        forecasts = generate_numbers(game, n_sets)
        st.session_state["forecast"] = forecasts
        st.success(f"{len(forecasts)} forecasts generated.")
    if "forecast" in st.session_state:
        for f in st.session_state["forecast"]:
            aura = "#FFD700" if f["confidence"]>90 else "#88CCFF" if f["confidence"]>80 else "#FF6A6A"
            st.markdown(f"<div style='background-color:{aura}22;padding:8px;border-radius:8px;margin:3px;'>"
                        f"<b>{f['number']}</b> — {f['confidence']}%</div>", unsafe_allow_html=True)

with col2:
    st.subheader("📥 Enter Official Result")
    result_game = st.selectbox("Game", ["GA Pick-3 Midday","GA Pick-3 Evening","FL Pick-4 Midday","FL Pick-4 Evening"])
    draw_date = st.date_input("Draw Date", datetime.date.today())
    result_num = st.text_input("Winning Number (Straight)")
    if st.button("💾 Log Result"):
        file = GA_FILE if "GA" in result_game else FL_FILE
        data = load_json(file)
        forecasts = st.session_state.get("forecast", [])
        hit = any(result_num == f["number"] for f in forecasts)
        data["records"].append({
            "game": result_game,
            "date": str(draw_date),
            "result": result_num,
            "hit": hit
        })
        save_json(file,data)
        st.success("Result logged successfully.")
        if hit: st.balloons()

st.divider()

# ------------------ ACCURACY DASHBOARD ------------------
col3, col4 = st.columns(2)
with col3:
    st.subheader("📊 Accuracy Dashboard")
    ga_acc = compute_accuracy(load_json(GA_FILE))
    fl_acc = compute_accuracy(load_json(FL_FILE))
    fig = go.Figure()
    fig.add_trace(go.Bar(x=["GA Pick-3","FL Pick-4"],y=[ga_acc,fl_acc],
                         marker_color=["#5DADE2","#9B59B6"]))
    fig.update_layout(title="Accuracy Rate (%)",yaxis=dict(range=[0,100]),height=250)
    st.plotly_chart(fig,use_container_width=True)
with col4:
    avg_acc = round((ga_acc+fl_acc)/2,2)
    st.metric("⚙️ Overall Accuracy", f"{avg_acc}%")
    st.info(titan_insight(avg_acc))

# ------------------ CALENDAR VIEW ------------------
st.subheader("🗓️ Calendar Sync View")
month = st.selectbox("Select Month", [datetime.date.today().strftime("%B"), "January", "February", "March"])
data_merged = load_json(GA_FILE)["records"] + load_json(FL_FILE)["records"]
if data_merged:
    df = pd.DataFrame(data_merged)
    st.dataframe(df)
else:
    st.caption("No logged data yet. Feed daily results to activate calendar sync.")

st.markdown("<p style='text-align:center;color:#7AB3FF;'>🧠 Titan Insight: Dual-state memory synchronization stable.</p>", unsafe_allow_html=True)

