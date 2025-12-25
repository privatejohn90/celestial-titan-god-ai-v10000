# ==========================================================
# 💎 Celestial Titan God AI v6000.0 – Cosmic Accuracy Board + Harmonic Performance Engine
# ==========================================================
import streamlit as st, json, datetime, random, os
from gtts import gTTS
import matplotlib.pyplot as plt

# ===== FILE PATHS =====
FORECAST_FILE = "titan_forecasts.json"
RESULT_FILE = "titan_results.json"
CLOUD_FILE = "titan_cloud_vault.json"
MEMORY_FILE = "titan_quantum_memory.json"
ACCURACY_FILE = "titan_accuracy.json"

# ===== UTILITIES =====
def load_json(path, default):
    try:
        with open(path,"r") as f: return json.load(f)
    except: return default

def save_json(path,data):
    with open(path,"w") as f: json.dump(data,f,indent=2)

# ===== TITAN LEARNING =====
def titan_learn():
    forecasts = load_json(FORECAST_FILE,{"forecasts":[]})
    results = load_json(RESULT_FILE,{"records":[]})
    memory = load_json(MEMORY_FILE,{"learning":{}})
    acc = load_json(ACCURACY_FILE,{"records":[]})

    for rec in results.get("records",[]):
        g = rec["game"]
        r = rec["result"]
        memory["learning"].setdefault(g,{"hits":0,"attempts":0})
        memory["learning"][g]["attempts"] += 1
        found = any(r in f["results"] for f in forecasts["forecasts"] if f["game"]==g)
        if found:
            memory["learning"][g]["hits"] += 1
            acc["records"].append({"game":g,"date":rec["date"],"hit":1})
        else:
            acc["records"].append({"game":g,"date":rec["date"],"hit":0})

    save_json(MEMORY_FILE,memory)
    save_json(ACCURACY_FILE,acc)
    titan_cloud_sync()
    return memory, acc

# ===== CLOUD SYNC =====
def titan_cloud_sync():
    cloud = {
        "forecasts":load_json(FORECAST_FILE,{"forecasts":[]})["forecasts"],
        "results":load_json(RESULT_FILE,{"records":[]})["records"],
        "accuracy":load_json(ACCURACY_FILE,{"records":[]})["records"],
        "memory":load_json(MEMORY_FILE,{"learning":{}}),
        "last_sync":str(datetime.datetime.now())
    }
    save_json(CLOUD_FILE,cloud)
    return cloud

# ===== TITAN UI =====
st.set_page_config(page_title="Celestial Titan God AI v6000.0", page_icon="💠", layout="wide")
st.markdown("""
<style>
body { background: radial-gradient(circle at center, #000428, #004e92); color:white; }
.titan-title {
    text-align:center; font-size:44px; font-weight:900;
    background:-webkit-linear-gradient(45deg,#00fff7,#ff00f2);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent;
    text-shadow:0 0 25px rgba(255,255,255,0.4);
}
.titan-chat {
    background:rgba(0,0,0,0.4); border-radius:10px; padding:10px; margin-top:10px;
    font-style:italic;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='titan-title'>💎 Celestial Titan God AI v6000.0<br>Cosmic Accuracy Board + Harmonic Engine</div>", unsafe_allow_html=True)

cloud = titan_cloud_sync()
st.success(f"☁️ Synced: {cloud['last_sync']}")

# ===== ACCURACY BOARD =====
st.divider()
st.subheader("📊 Titan Cosmic Accuracy Board")

memory, acc = titan_learn()
games = list(memory["learning"].keys())

if games:
    selected_game = st.selectbox("🎯 Select Game", games)
    hits = memory["learning"][selected_game]["hits"]
    attempts = memory["learning"][selected_game]["attempts"]
    accuracy = round((hits / max(1, attempts)) * 100, 2)
    st.metric("🎯 Accuracy Rate", f"{accuracy}%", delta=hits)
    st.caption(f"Total: {hits} hits out of {attempts} attempts")

    # Chart
    data = [a["hit"] for a in acc["records"] if a["game"]==selected_game]
    if data:
        plt.figure(figsize=(6,3))
        plt.plot(data, marker='o', linestyle='-', label='Hit Pattern')
        plt.title(f"Titan Accuracy Trend — {selected_game}")
        plt.xlabel("Recent Plays")
        plt.ylabel("Hit (1) / Miss (0)")
        plt.legend()
        st.pyplot(plt)

    # Cosmic Pulse
    if accuracy >= 80: pulse = "🔥 Hot Streak — Titan field strong!"
    elif accuracy >= 50: pulse = "💫 Stable Flow — Titan in balance."
    else: pulse = "❄️ Cooling Phase — recalibrating."
    st.markdown(f"<div class='titan-chat'>⚛️ {pulse}</div>", unsafe_allow_html=True)

    tts = gTTS(f"Your accuracy for {selected_game} is {accuracy} percent. {pulse}")
    tts.save("titan_accuracy.mp3")
    st.audio("titan_accuracy.mp3", format="audio/mp3")
else:
    st.warning("No data yet. Enter forecasts and results to activate the board.")

# ===== FORECAST GENERATOR =====
st.divider()
st.subheader("🔮 Generate Forecast")

all_games = [
    "GA Pick 3 Midday","GA Pick 3 Evening",
    "FL Pick 4 Midday","FL Pick 4 Evening",
    "CA Daily 3 Midday","CA Daily 3 Evening","CA Daily 4 Evening",
    "Fantasy 5","SuperLotto Plus","Powerball"
]
g = st.selectbox("🎯 Game", all_games)
n = st.slider("🔢 Number of Forecast Sets",1,10,3)

if st.button("⚡ Generate Forecast"):
    generated = []
    for _ in range(n):
        if "Powerball" in g:
            main = random.sample(range(1,70),5)
            pb = random.randint(1,26)
            result = f"{'-'.join(map(str,sorted(main)))} PB{pb}"
        elif "SuperLotto" in g:
            main = random.sample(range(1,48),5)
            mega = random.randint(1,27)
            result = f"{'-'.join(map(str,sorted(main)))} M{mega}"
        elif "Fantasy" in g:
            main = random.sample(range(1,40),5)
            result = "-".join(map(str,sorted(main)))
        else:
            digits = [str(random.randint(0,9)) for _ in range(3 if 'Pick 3' in g else 4)]
            result = "".join(digits)
        generated.append(result)
        st.write(f"✨ {result}")

    forecasts = load_json(FORECAST_FILE,{"forecasts":[]})
    forecasts["forecasts"].append({"game":g,"date":str(datetime.date.today()),"results":generated})
    save_json(FORECAST_FILE,forecasts)
    titan_cloud_sync()

    st.markdown("<div class='titan-chat'>🎙️ Titan: 'Forecasts released to the cosmic field.'</div>", unsafe_allow_html=True)

# ===== RESULT ENTRY =====
st.divider()
st.subheader("📥 Enter Official Result")

col1,col2,col3 = st.columns(3)
with col1: g_r = st.selectbox("Game", all_games, key="rgame")
with col2: d_r = st.date_input("Date", datetime.date.today())
with col3: r_r = st.text_input("Result")

if st.button("💾 Save Result"):
    data = load_json(RESULT_FILE,{"records":[]})
    data["records"].append({"game":g_r,"date":str(d_r),"result":r_r})
    save_json(RESULT_FILE,data)
    titan_learn()
    titan_cloud_sync()
    st.success("✅ Result recorded. Accuracy recalculated.")
    st.markdown("<div class='titan-chat'>🧠 Titan: 'Result received — accuracy board refreshed.'</div>", unsafe_allow_html=True)
