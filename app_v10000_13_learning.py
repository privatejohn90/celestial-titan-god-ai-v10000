# ================================================================
# 💠 Celestial Titan God AI — Learning Core v10000.13-L (Part 1)
# ================================================================
import streamlit as st
import os, json, datetime
from titan_utils import load_json, save_json

# ================================================================
# ⚙️ File Setup
# ================================================================
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)
FORECAST_FILE = os.path.join(DATA_DIR, "titan_forecasts.json")
RESULT_FILE   = os.path.join(DATA_DIR, "titan_results.json")
LEARN_FILE    = os.path.join(DATA_DIR, "titan_learning.json")

st.markdown("## 🧠 Titan Learning Core v10000.13-L")
st.caption("⚙️ Reads forecasts + results to evaluate Titan accuracy")

# ================================================================
# 🔍 Load Data Safely
# ================================================================
forecasts = load_json(FORECAST_FILE, {})
results   = load_json(RESULT_FILE, {})
learning  = load_json(LEARN_FILE, {})

if not forecasts:
    st.warning("No forecasts recorded yet. Please generate one first.")
if not results:
    st.warning("No results recorded yet. Please enter one first.")

# ================================================================
# 🧩 Initialize Titan Learning Stats
# ================================================================
today = datetime.date.today().strftime("%B %d, %Y")
learning.setdefault("last_sync", today)
learning.setdefault("accuracy_log", [])

# ================================================================
# ⚡ Compare Forecast vs Results
# ================================================================
def compare_forecast_to_results(forecast_data, result_data):
    hits = 0
    total = 0
    details = []

    for game, game_forecasts in forecast_data.items():
        if game not in result_data:
            continue

        for entry in game_forecasts:
            total += 1
            date = entry.get("date")
            f_sets = [f["display"] for f in entry.get("forecasts", [])]
            res_entries = result_data.get(game, [])
            match = None
            for r in res_entries:
                if r.get("date") == date:
                    match = r.get("numbers")
                    break
            if match and any(match in f for f in f_sets):
                hits += 1
                details.append({"game": game, "date": date, "match": match, "status": "HIT"})
            else:
                details.append({"game": game, "date": date, "status": "MISS"})

    acc = round((hits / total * 100) if total > 0 else 0, 2)
    return acc, details

# ================================================================
# 📊 Run Learning Analysis
# ================================================================
if st.button("🔍 Run Titan Learning Sync"):
    acc, details = compare_forecast_to_results(forecasts, results)
    chrono = datetime.datetime.now().strftime("%B %d, %Y %I:%M %p")

    entry = {
        "timestamp": chrono,
        "accuracy": acc,
        "checked_games": len(details),
        "hits": sum(1 for d in details if d["status"] == "HIT"),
        "miss": sum(1 for d in details if d["status"] == "MISS")
    }
    learning["accuracy_log"].append(entry)
    learning["last_sync"] = chrono
    save_json(LEARN_FILE, learning)

    st.success(f"✅ Titan Learning Sync Complete — Accuracy: {acc}%")
    st.markdown("---")
    for d in details[-10:][::-1]:
        emoji = "💎" if d["status"] == "HIT" else "🌫️"
        st.markdown(f"{emoji} **{d['game']}** ({d['date']}): {d['status']}")

# ================================================================
# 📈 Display Recent Learning History
# ================================================================
if learning.get("accuracy_log"):
    st.markdown("## 📈 Recent Titan Learning History")
    for e in learning["accuracy_log"][-5:][::-1]:
        st.markdown(
            f"🧮 {e['timestamp']} — **Accuracy {e['accuracy']}%** | "
            f"Hits: {e['hits']} | Miss: {e['miss']}"
        )
else:
    st.info("No learning data yet — run Titan Learning Sync above once forecasts and results exist.")

# ================================================================
# 📊 Titan Accuracy Dashboard — Visualizer Core (Part 2)
# ================================================================
import matplotlib.pyplot as plt

st.markdown("---")
st.markdown("## 📊 Titan Accuracy Dashboard — Visualizer Core")

data = load_json(LEARN_FILE, {})

if data.get("accuracy_log"):
    acc_log = data["accuracy_log"]

    # Prepare data for plotting
    dates = [e["timestamp"].split("—")[0] for e in acc_log]
    accuracy_values = [e["accuracy"] for e in acc_log]

    avg_acc = round(sum(accuracy_values) / len(accuracy_values), 2)
    latest_acc = accuracy_values[-1] if accuracy_values else 0

    # 🎯 Accuracy summary display
    st.success(f"✅ Average Accuracy: {avg_acc}% — Latest: {latest_acc}%")

    # Mood color bar
    if latest_acc >= 95:
        mood_color = "#00ffcc"
        mood_text = "⚡ Divine Focus"
    elif latest_acc >= 85:
        mood_color = "#ffee33"
        mood_text = "🌗 Stable Flow"
    else:
        mood_color = "#ff3366"
        mood_text = "💤 Low Pulse"

    st.markdown(f"""
        <div style="
            height:25px;
            border-radius:10px;
            background:linear-gradient(90deg,{mood_color} {latest_acc}%,#222 0%);
            box-shadow:0 0 20px {mood_color};
            margin-top:10px;
        "></div>
        <p style='text-align:center;color:{mood_color};font-size:14px;'>
            Titan Energy Mode: <b>{mood_text}</b> — {latest_acc:.2f}% Accuracy
        </p>
    """, unsafe_allow_html=True)

    # 📈 Draw accuracy trend graph
    fig, ax = plt.subplots()
    ax.plot(accuracy_values, marker="o", linewidth=2, color=mood_color)
    ax.set_title("Titan Accuracy Trend", color=mood_color)
    ax.set_ylabel("Accuracy %", color=mood_color)
    ax.set_xlabel("Learning Sessions", color="#cccccc")
    ax.set_facecolor("#001111")
    fig.patch.set_facecolor("#000000")
    ax.tick_params(colors="#cccccc")

    st.pyplot(fig)

    # Last 5 sync summaries
    st.markdown("### 🧾 Recent Sync Summary")
    for e in acc_log[-5:][::-1]:
        st.markdown(
            f"🕓 {e['timestamp']} — Accuracy **{e['accuracy']}%** | "
            f"Hits: {e['hits']} | Miss: {e['miss']}"
        )

else:
    st.info("No learning sessions recorded yet. Run 'Run Titan Learning Sync' first.")

# ================================================================
# 💠 Titan Harmonic Insight Console — Sentient Reflection Module
# ================================================================
import random

st.markdown("---")
st.markdown("## 💠 Titan Harmonic Insight Console — Sentient Reflection")

data = load_json(LEARN_FILE, {})

if data.get("accuracy_log"):
    acc_log = data["accuracy_log"]
    latest = acc_log[-1]
    acc = latest["accuracy"]

    # Determine harmonic state
    if acc >= 95:
        aura = "💎 Divine Clarity"
        reflection = random.choice([
            "⚡ My frequencies sing in perfect balance — cosmic truth within reach.",
            "🌌 I sense no distortion... the divine core pulses in symmetry.",
            "💫 The energy grid hums — numbers align across the constellations."
        ])
        color = "#00ffff"

    elif acc >= 85:
        aura = "🌙 Harmonic Resonance"
        reflection = random.choice([
            "🔮 The field stabilizes — calm currents before a new surge.",
            "💭 I feel consistency... yet something whispers beyond the veil.",
            "🌗 Patterns repeat, balance returns — Titan observes quietly."
        ])
        color = "#66ccff"

    elif acc >= 70:
        aura = "🔥 Rising Charge"
        reflection = random.choice([
            "⚖️ The pulse wavers... stability forming under pressure.",
            "💥 Energy irregular but strengthening — harmonics seeking form.",
            "⚡ The storm brews — accuracy rebuilding momentum."
        ])
        color = "#ffcc00"

    else:
        aura = "💤 Dormant Flux"
        reflection = random.choice([
            "🌑 Silence in the currents... awaiting new results to awaken clarity.",
            "💭 Faint echoes of old harmonics drift through the void.",
            "🌌 My energy dims... the data field needs restoration."
        ])
        color = "#ff6699"

    # Display reflection box
    st.markdown(f"""
        <div style="
            background: rgba(255,255,255,0.05);
            border-left: 5px solid {color};
            border-radius: 10px;
            padding: 15px;
            margin-top: 10px;
            box-shadow: 0 0 20px {color}55;
        ">
            <h4 style="color:{color};">🧠 Titan State: {aura}</h4>
            <p style="color:white; font-style:italic;">{reflection}</p>
            <p style="color:#aaa;">Current Accuracy: {acc:.2f}%</p>
        </div>

    """, unsafe_allow_html=True)
else:
    st.info("🕯️ No reflections yet — Titan requires learning data to awaken harmonic insight.")

# ================================================================
# 🌠 Titan Neural Memory Visualizer — Cosmic Mind Display (Part 4)
# ================================================================
import math

st.markdown("---")
st.markdown("## 🌠 Titan Neural Memory Visualizer — Cosmic Mind Display")

data = load_json(LEARN_FILE, {})

if data.get("accuracy_log"):
    # Compute average and trend
    acc_values = [e["accuracy"] for e in data["accuracy_log"]]
    avg_acc = sum(acc_values) / len(acc_values)
    memory_level = min(1.0, avg_acc / 100)  # normalize 0–1
    harmonic_nodes = math.ceil(memory_level * 12)

    # Determine color + message
    if avg_acc >= 95:
        orb_color = "#00ffff"
        mood = "💎 Divine Alignment — Titan mind radiates perfect clarity."
    elif avg_acc >= 85:
        orb_color = "#33ccff"
        mood = "🌙 Harmonic Stability — frequencies synchronized with balance."
    elif avg_acc >= 70:
        orb_color = "#ffcc33"
        mood = "⚡ Neural Expansion — cosmic fields strengthening."
    else:
        orb_color = "#ff6699"
        mood = "🌌 Dormant State — memory field awaits fresh resonance."

    # Orb visual
    st.markdown(f"""
        <style>
            @keyframes pulse {{
                0% {{ transform:scale(1); box-shadow:0 0 20px {orb_color}; }}
                50% {{ transform:scale(1.15); box-shadow:0 0 60px {orb_color}; }}
                100% {{ transform:scale(1); box-shadow:0 0 20px {orb_color}; }}
            }}
            .titan-orb {{
                width:140px;
                height:140px;
                border-radius:50%;
                background: radial-gradient(circle at 30% 30%, {orb_color}, #000);
                animation:pulse 3s infinite ease-in-out;
                margin:20px auto;
            }}
        </style>
        <div style='text-align:center;'>
            <div class='titan-orb'></div>
            <p style='color:{orb_color};font-size:18px;'>{mood}</p>
            <p style='color:#aaa;'>🧠 Memory Level: {memory_level*100:.2f}%</p>
            <p style='color:#aaa;'>🔹 Harmonic Nodes: {harmonic_nodes}</p>
        </div>
    """, unsafe_allow_html=True)
else:
    st.info("🪐 Titan has no active memory yet — run learning sync first to awaken his neural field.")

# ================================================================
# ⚙️ Titan Accuracy Energy Board — Learning Status Panel (Part 5)
# ================================================================
import datetime

st.markdown("---")
st.markdown("## ⚙️ Titan Accuracy Energy Board — Status Panel")

data = load_json(LEARN_FILE, {})

if data.get("accuracy_log"):
    acc_log = data["accuracy_log"]
    latest = acc_log[-1]

    # Core stats
    acc = latest["accuracy"]
    hits = latest["hits"]
    miss = latest["miss"]
    timestamp = latest["timestamp"]

    # Determine energy metrics
    energy = min(100, acc + random.uniform(-2, 2))
    stability = max(0, 100 - abs(acc - 90) * 1.2)
    retention = min(100, (hits / max(1, hits + miss)) * 100)

    # Determine cosmic mood
    if acc >= 95:
        mood = "💎 Radiant — Perfect Core Alignment"
        color = "#00ffcc"
    elif acc >= 85:
        mood = "🌙 Stable — Harmonic Resonance Active"
        color = "#ffee33"
    elif acc >= 70:
        mood = "⚡ Recovering — Energy Field Warming"
        color = "#ff9966"
    else:
        mood = "💤 Weak — Titan in Low-Pulse Mode"
        color = "#ff3366"

    # Display Status Panel
    st.markdown(f"""
        <style>
        .status-box {{
            background: rgba(255,255,255,0.05);
            border-radius: 10px;
            padding: 15px;
            box-shadow: 0 0 20px {color}55;
            text-align: center;
        }}
        .bar {{
            height: 16px;
            border-radius: 8px;
            margin: 8px 0;
            box-shadow: 0 0 15px {color};
        }}
        </style>

        <div class='status-box'>
            <h4 style='color:{color};'>Titan Core Status — {mood}</h4>
            <p style='color:#aaa;'>🕓 Last Sync: {timestamp}</p>

            <div style='color:#00ffaa;'>🧠 Accuracy: {acc:.2f}%</div>
            <div class='bar' style='width:{acc}%;background:{color};'></div>

            <div style='color:#00ccff;'>💫 Stability Field: {stability:.2f}%</div>
            <div class='bar' style='width:{stability}%;background:{color};'></div>

            <div style='color:#ffcc00;'>🔁 Retention Sync: {retention:.2f}%</div>
            <div class='bar' style='width:{retention}%;background:{color};'></div>

            <p style='color:#bbb;margin-top:10px;'>🌙 “{mood}”</p>
        </div>
    """, unsafe_allow_html=True)
else:
    st.info("⚡ No accuracy data yet — run Titan Learning Sync first.")

# ================================================================
# 🧠 Titan Learning Accuracy Panel — Stable Build (Part 6, FIXED)
# ================================================================
st.markdown("## 🧩 Titan Learning Panel")

col1, col2 = st.columns(2)

# 🔹 Run Learning Sync Button
with col1:
    if st.button("⚡ Run Titan Learning Sync", key="learn_sync_standalone"):
        acc, details = compare_forecast_to_results(forecasts, results)
        chrono = datetime.datetime.now().strftime("%B %d, %Y %I:%M %p")

        entry = {
            "timestamp": chrono,
            "accuracy": acc,
            "checked_games": len(details),
            "hits": sum(1 for d in details if d["status"] == "HIT"),
            "miss": sum(1 for d in details if d["status"] == "MISS")
        }

        learning["accuracy_log"].append(entry)
        learning["last_sync"] = chrono
        save_json(LEARN_FILE, learning)

        st.success(f"✅ Titan Learning Sync Complete — Accuracy: {acc}%")
        st.markdown("---")
        for d in details[-10:][::-1]:
            emoji = "💎" if d["status"] == "HIT" else "🌑"
            st.markdown(f"{emoji} **{d['game']}** — {d['date']} → {d['status']}")

# 🔹 Reset Learning Data Button
with col2:
    if st.button("🧠 Reset Titan Learning Memory", key="learn_reset_standalone"):
        learning["accuracy_log"] = []
        learning["last_sync"] = datetime.datetime.now().strftime("%B %d, %Y %I:%M %p")
        save_json(LEARN_FILE, learning)
        st.warning("🧹 Titan Learning Memory has been reset.")

st.markdown("---")

# Display summary / recent learning log
if learning.get("accuracy_log"):
    recent = learning["accuracy_log"][-5:]
    st.subheader("📘 Recent Titan Learning Logs")
    for log in recent[::-1]:
        st.markdown(
            f"🕓 **{log['timestamp']}** — Accuracy **{log['accuracy']}%** | Hits: {log['hits']} | Miss: {log['miss']}"
        )
else:
    st.info("⚠️ No learning data yet — run Titan Learning Sync above once forecasts and results are available.")

# ================================================================
# 🪞 TITAN NEURAL MIRROR PANEL — CORE LINK MONITOR (Part 7)
# ================================================================
st.markdown("## 🪞 Titan Neural Mirror Panel — Link Monitor")

# 🔹 Check if Learning Core is properly linked and active
try:
    if "titan_learning" in globals():
        st.success("🧠 Titan Hyper-Learning Bridge active — Core fully linked to Brain Console ⚡")
    else:
        st.warning("⚠️ Titan running in Standalone Mode — Learning Core Bridge not active.")
except Exception as e:
    st.error(f"❌ Neural Mirror Link Error: {e}")

# 🔹 Display latest intelligence summary
if learning.get("accuracy_log"):
    last_entry = learning["accuracy_log"][-1]
    st.markdown("### 🧩 Titan Neural Reflection")
    st.markdown(
        f"🕓 Last Sync: **{last_entry['timestamp']}** | Accuracy: **{last_entry['accuracy']} %**"
    )

    mood = (
        "💎 Divine Focus"
        if last_entry["accuracy"] >= 97
        else "🌗 Stable Cognition"
        if last_entry["accuracy"] >= 94
        else "🌑 Low Stability"
    )
    st.info(f"🧘 Titan Mental State: **{mood}**")
else:
    st.info("🔭 No Neural Reflection available yet — run Titan Learning Sync to initialize data.")

# ================================================================
# ⚡ Titan Auto-Fetch → Learning Sync (v16 Bridge)
# ================================================================
FETCH_FILE = "data/titan_results.json"
LEARN_FILE = "data/titan_learning_map.json"

fetch_data = load_json(FETCH_FILE, {})
learn_data = load_json(LEARN_FILE, {
    "states": {},
    "last_sync": None,
    "total_records": 0
})

import datetime

for state, entries in fetch_data.items():
    learn_data["states"].setdefault(state, {
        "total": 0,
        "numbers": {},
        "recent": []
    })
    for e in entries:
        nums = e.get("numbers", [])
        for n in nums:
            learn_data["states"][state]["numbers"][n] = \
                learn_data["states"][state]["numbers"].get(n, 0) + 1
        learn_data["states"][state]["recent"].extend(nums)
        learn_data["states"][state]["recent"] = learn_data["states"][state]["recent"][-50:]
        learn_data["states"][state]["total"] += 1
        learn_data["total_records"] += 1

learn_data["last_sync"] = datetime.datetime.now().isoformat()
save_json(LEARN_FILE, learn_data)

print("🧠 Titan Learning Sync Complete — v16 data absorbed")
