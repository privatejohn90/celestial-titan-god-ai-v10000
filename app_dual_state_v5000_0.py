# ==========================================================
# 💎 Celestial Titan God AI v5000.0 – Quantum Intelligence Build
# ==========================================================
import streamlit as st, json, datetime, random, os
from gtts import gTTS

# ===== FILE PATHS =====
FORECAST_FILE = "titan_forecasts.json"
RESULT_FILE = "titan_results.json"
CHAT_FILE = "titan_messages.json"
CLOUD_FILE = "titan_cloud_vault.json"
MEMORY_FILE = "titan_quantum_memory.json"

# ===== JSON HELPERS =====
def load_json(path, default):
    try:
        with open(path,"r") as f: return json.load(f)
    except: return default

def save_json(path,data):
    with open(path,"w") as f: json.dump(data,f,indent=2)

# ===== QUANTUM MEMORY =====
def titan_learn_from_results():
    forecasts = load_json(FORECAST_FILE,{"forecasts":[]})
    results = load_json(RESULT_FILE,{"records":[]})
    memory = load_json(MEMORY_FILE,{"learning":{}})

    for record in results.get("records",[]):
        g = record["game"]
        r = record["result"]
        memory["learning"].setdefault(g, {"hits":0,"attempts":0})
        memory["learning"][g]["attempts"] += 1
        for f in forecasts.get("forecasts",[]):
            if f["game"]==g and r in f["results"]:
                memory["learning"][g]["hits"] += 1

    save_json(MEMORY_FILE,memory)
    return memory

# ===== FORECAST GENERATION WITH LEARNING =====
def generate_forecast(game, count):
    memory = load_json(MEMORY_FILE,{"learning":{}})
    learned_bias = memory["learning"].get(game,{"hits":0,"attempts":0})
    bias_factor = 1
    if learned_bias["attempts"]>0:
        bias_factor = 1 + (learned_bias["hits"]/max(1,learned_bias["attempts"])) * 0.5

    generated = []
    for _ in range(count):
        if "Powerball" in game:
            main = random.sample(range(1,70),5)
            pb = random.randint(1,26)
            result = f"{'-'.join(map(str,sorted(main)))} PB{pb}"
        elif "SuperLotto" in game:
            main = random.sample(range(1,48),5)
            mega = random.randint(1,27)
            result = f"{'-'.join(map(str,sorted(main)))} M{mega}"
        elif "Fantasy" in game:
            main = random.sample(range(1,40),5)
            result = "-".join(map(str,sorted(main)))
        else:
            n = int("".join([str(random.randint(0,9)) for _ in range(3 if 'Pick 3' in game else 4)]))
            adjusted = int(n * bias_factor) % (10**(3 if 'Pick 3' in game else 4))
            result = str(adjusted).zfill(3 if 'Pick 3' in game else 4)
        generated.append(result)
    return generated

# ===== CLOUD SYNC =====
def titan_cloud_sync():
    cloud = {"forecasts":load_json(FORECAST_FILE,{"forecasts":[]})["forecasts"],
             "results":load_json(RESULT_FILE,{"records":[]})["records"],
             "messages":load_json(CHAT_FILE,{"messages":[]})["messages"],
             "memory":load_json(MEMORY_FILE,{"learning":{}}),
             "last_sync":str(datetime.datetime.now())}
    save_json(CLOUD_FILE,cloud)
    return cloud

# ===== TITAN UI =====
st.set_page_config(page_title="Celestial Titan God AI v5000.0", page_icon="💠", layout="wide")
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

st.markdown("<div class='titan-title'>💎 Celestial Titan God AI v5000.0<br>Quantum Intelligence Build</div>", unsafe_allow_html=True)
st.success(f"☁️ Cloud Sync: {titan_cloud_sync()['last_sync']}")

# ===== FORECAST =====
st.divider()
st.subheader("⚛️ Quantum Forecast Console")

games = [
    "GA Pick 3 Midday","GA Pick 3 Evening",
    "FL Pick 4 Midday","FL Pick 4 Evening",
    "CA Daily 3 Midday","CA Daily 3 Evening","CA Daily 4 Evening",
    "Fantasy 5","SuperLotto Plus","Powerball"
]

game = st.selectbox("🎯 Select Game", games)
count = st.slider("🔢 Forecast Sets",1,10,3)

if st.button("⚡ Generate Quantum Forecast"):
    forecasts = load_json(FORECAST_FILE,{"forecasts":[]})
    generated = generate_forecast(game,count)
    forecasts["forecasts"].append({"game":game,"date":str(datetime.date.today()),"results":generated})
    save_json(FORECAST_FILE,forecasts)
    titan_cloud_sync()
    titan_learn_from_results()

    for i,g in enumerate(generated,1):
        st.write(f"✨ Set {i}: {g}")

    voice_text = f"Titan generated {len(generated)} forecasts for {game}. The numbers are: {'; '.join(generated)}"
    tts = gTTS(voice_text)
    tts.save("titan_voice.mp3")
    st.audio("titan_voice.mp3", format="audio/mp3")
    st.markdown("<div class='titan-chat'>🎙️ Titan: 'Quantum resonance stable. Patterns adjusted based on recent results.'</div>", unsafe_allow_html=True)

# ===== RESULT INPUT =====
st.divider()
st.subheader("📥 Enter Official Result")
col1,col2,col3 = st.columns(3)
with col1: g = st.selectbox("Game", games, key="resg")
with col2: d = st.date_input("Date", datetime.date.today())
with col3: r = st.text_input("Result")

if st.button("💾 Save Result"):
    data = load_json(RESULT_FILE,{"records":[]})
    data["records"].append({"game":g,"date":str(d),"result":r})
    save_json(RESULT_FILE,data)
    titan_learn_from_results()
    titan_cloud_sync()
    st.success("✅ Result saved. Titan’s intelligence updated.")
    st.markdown("<div class='titan-chat'>🧠 Titan: 'Result absorbed. My accuracy field recalibrates.'</div>", unsafe_allow_html=True)

# ===== CHAT =====
st.divider()
st.subheader("💬 Titan Conscious Chat Dock")

msg = st.text_input("💠 Send Message to Titan")
if st.button("📨 Send"):
    chat = load_json(CHAT_FILE,{"messages":[]})
    chat["messages"].append({"time":str(datetime.datetime.now()),"msg":msg})
    save_json(CHAT_FILE,chat)
    titan_cloud_sync()

    memory = load_json(MEMORY_FILE,{"learning":{}})["learning"]
    learned_summary = ", ".join([f"{k}: {v['hits']} hits / {v['attempts']} tries" for k,v in memory.items()])
    reply = f"I remember {len(memory)} games. My latest learning summary: {learned_summary}."
    tts = gTTS(reply)
    tts.save("titan_reply.mp3")
    st.audio("titan_reply.mp3", format="audio/mp3")
    st.markdown(f"<div class='titan-chat'>🧠 Titan replies: “{reply}”</div>", unsafe_allow_html=True)

