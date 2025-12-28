# =============================================================
# 💎 Celestial Titan God AI v300.8-FXR1 — Chrono-Priority Core
# =============================================================

import streamlit as st
import random, json, os, datetime, pandas as pd

st.set_page_config(
    page_title="Celestial Titan God AI v300.8-FXR1 — Chrono-Priority Core",
    page_icon="💎",
    layout="centered"
)

# =============================================================
# 🌈 Aurora Selector Core (Theme Color Selector)
# =============================================================
aurora_colors = {
    "Solar Gold": "#FFD700",
    "Aurora Green": "#00FF9D",
    "Emerald Green": "#00FF66",
    "Titan Blue": "#00BFFF",
    "Cosmic Violet": "#B966FF",
    "Celestial White": "#FFFFFF"
}

with st.sidebar:
    st.markdown("### 🌈 Titan Aurora Color")
    selected_glow = st.selectbox(
        "Choose your glow color:",
        list(aurora_colors.keys()),
        index=1
    )

selected_glow = aurora_colors[selected_glow]

# =============================================================
# 💠 Titan Orb Center Glow + Heartbeat Light (Aurora-Adaptive)
# =============================================================
st.markdown(f"""
    <style>
    .titan-orb {{
        width: 140px;
        height: 140px;
        margin: 25px auto;
        border-radius: 50%;
        background: radial-gradient(circle at center,
            {selected_glow} 0%,
            rgba(255,255,255,0.1) 35%,
            transparent 70%);
        box-shadow:
            0 0 15px {selected_glow},
            0 0 40px {selected_glow},
            0 0 80px {selected_glow};
        position: relative;
        animation: orbPulse 2.8s ease-in-out infinite;
    }}

    .titan-orb::before {{
        content: "";
        position: absolute;
        top: 35%;
        left: 35%;
        width: 30%;
        height: 30%;
        border-radius: 50%;
        background: radial-gradient(circle at center,
            {selected_glow} 0%,
            rgba(255,255,255,0.25) 60%,
            transparent 100%);
        animation: titanHeartbeat 1.8s ease-in-out infinite;
        box-shadow:
            0 0 10px {selected_glow},
            0 0 25px {selected_glow};
    }}

    .titan-orb::after {{
        content: "";
        position: absolute;
        top: 12%;
        left: 12%;
        width: 76%;
        height: 76%;
        border-radius: 50%;
        border: 3px solid rgba(255,255,255,0.15);
        animation: orbRotate 8s linear infinite;
    }}

    @keyframes orbPulse {{
        0% {{ transform: scale(1); opacity: 0.85; }}
        50% {{ transform: scale(1.12); opacity: 1; }}
        100% {{ transform: scale(1); opacity: 0.85; }}
    }}

    @keyframes titanHeartbeat {{
        0%, 100% {{ transform: scale(1); opacity: 0.6; }}
        50% {{ transform: scale(1.4); opacity: 1; }}
    }}

    @keyframes orbRotate {{
        from {{ transform: rotate(0deg); }}
        to {{ transform: rotate(360deg); }}
    }}
    </style>

    <div class="titan-orb"></div>
""", unsafe_allow_html=True)

# =============================================================
# 🌌 Titan Aurora Glow System — v300.9 FXR-Aurora Stable
# =============================================================

import time

# 🎨 Sidebar Aurora Color Picker
st.sidebar.markdown("### 🌈 Titan Aurora Color")
aurora_color = st.sidebar.selectbox(
    "Choose your glow color:",
    ["Emerald Green", "Celestial Blue", "Violet Core"],
    index=0
)

# Map selected color → glow + background gradient
aurora_map = {
    "Emerald Green": {"glow": "#00ffaa", "bg": "linear-gradient(135deg, #001f1f 0%, #004d33 100%)"},
    "Celestial Blue": {"glow": "#00ccff", "bg": "linear-gradient(135deg, #001a33 0%, #003366 100%)"},
    "Violet Core": {"glow": "#b266ff", "bg": "linear-gradient(135deg, #1a0033 0%, #330066 100%)"}
}

selected_glow = aurora_map[aurora_color]["glow"]
selected_bg = aurora_map[aurora_color]["bg"]

# Inject dynamic CSS background + glow
st.markdown(f"""
    <style>
    /* 🌌 Titan Aurora Dynamic Background */
    .stApp {{
        background: {selected_bg};
        background-attachment: fixed;
        color: white;
    }}

    .titan-loader {{
        text-align: center;
        font-weight: bold;
        font-size: 20px;
        color: {selected_glow};
        margin-top: 10px;
        animation: titanPulse 1.4s ease-in-out infinite alternate;
    }}
    @keyframes titanPulse {{
        from {{ text-shadow: 0 0 6px {selected_glow}, 0 0 12px {selected_glow}; opacity: 0.8; }}
        to {{ text-shadow: 0 0 25px {selected_glow}, 0 0 40px {selected_glow}; opacity: 1; }}
    }}

    .titan-done {{
        text-align: center;
        color: {selected_glow};
        font-weight: bold;
        font-size: 18px;
        margin-top: 6px;
        text-shadow: 0 0 10px {selected_glow}, 0 0 20px {selected_glow};
    }}
    </style>
""", unsafe_allow_html=True)

# 💫 Glow Loader Function
def titan_glow_loader(task_name="Titan Sync"):
    placeholder = st.empty()
    with placeholder.container():
        st.markdown(
            f"<div class='titan-loader'>✨ {task_name} in Progress...</div>",
            unsafe_allow_html=True
        )
    time.sleep(2.5)
    placeholder.empty()
    st.markdown(
        f"<div class='titan-done'>✅ {task_name} Complete — Data Saved Successfully!</div>",
        unsafe_allow_html=True
    )

# =============================================================
# 🔹 Setup + File Paths — FIXED v300.12-FXR2
# =============================================================
import os, json, random, datetime
import streamlit as st
import pandas as pd

# ✅ Data directory setup
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

# ✅ Core Titan JSON files
FORECAST_FILE = os.path.join(DATA_DIR, "titan_forecasts.json")
RESULT_FILE = os.path.join(DATA_DIR, "titan_results.json")
MEMORY_FILE = os.path.join(DATA_DIR, "titan_memory.json")

# =============================================================
# 🔸 JSON Utilities (Auto-create if missing)
# =============================================================
def load_json(path, default):
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump(default, f, indent=2)
        return default
    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        return default

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

# ================================================================
# 🎯 Game Dictionaries — Full Multi-Region
# ================================================================
daily_games = {
    "GA Pick 3": ["Midday", "Evening"],
    "GA Pick 4": ["Midday", "Evening"],
    "GA Pick 5": ["Midday", "Evening"],
    "FL Pick 3": ["Midday", "Evening"],
    "FL Pick 4": ["Midday", "Evening"],
    "FL Pick 5": ["Midday", "Evening"],
    "TX Pick 3": ["Morning", "Day", "Evening", "Night"],
    "TX Pick 4": ["Morning", "Day", "Evening", "Night"],
    "VA Pick 3": ["Day", "Evening"],
    "VA Pick 4": ["Day", "Evening"],
    "VA Pick 5": ["Day", "Evening"],
    "NC Pick 3": ["Day", "Evening"],
    "NC Pick 4": ["Day", "Evening"],
    "NY Pick 3": ["Midday", "Evening"],
    "NY Pick 4": ["Midday", "Evening"],
    "CA Daily 3": ["Midday", "Evening"],
    "CA Daily 4": ["Evening"],
    "NJ Pick 3": ["Midday", "Evening"],
    "NJ Pick 4": ["Midday", "Evening"]
}

major_games = {
    "CA Fantasy 5": [],
    "CA SuperLotto Plus": [],
    "Mega Millions": [],
    "Powerball": []
}

ph_games = {
    "PH 3D Lotto (Swertres)": ["2PM","5PM","9PM"],
    "PH 4D Lotto": ["Mon","Wed","Fri"],
    "PH STL Game": ["10:30AM","3PM","7PM"]
}

# ================================================================
# 🔮 Forecast Generator + Titan Priority Logic (Fixed Labels + Clean Match)
# ================================================================
def generate_numbers(game, num_sets=5):
    sets = []
    chrono = datetime.datetime.now().strftime("%B %d, %Y %I:%M %p")

    def format_numbers(nums, game):
        """Attach labels for Mega/Super/Power balls."""
        if "SuperLotto" in game:
            return f"{' '.join(map(str, nums[:-1]))} 🟡 MEGA {nums[-1]}"
        elif "Mega Millions" in game:
            return f"{' '.join(map(str, nums[:-1]))} 🟣 Mega Ball {nums[-1]}"
        elif "Powerball" in game:
            return f"{' '.join(map(str, nums[:-1]))} 🔴 Power Ball {nums[-1]}"
        else:
            return " ".join(map(str, nums))

    for _ in range(num_sets):
        if "Daily 3" in game:
            nums = [random.randint(0,9) for _ in range(3)]
        elif "Daily 4" in game:
            nums = [random.randint(0,9) for _ in range(4)]
        elif " Pick 3" in game:
            nums = [random.randint(0,9) for _ in range(3)]
        elif " Pick 4" in game:
            nums = [random.randint(0,9) for _ in range(4)]
        elif " Pick 5" in game and "Fantasy" not in game:
            nums = [random.randint(0,9) for _ in range(5)]
        elif "Fantasy 5" in game:
            nums = sorted(random.sample(range(1,40),5))
        elif "SuperLotto" in game:
            nums = sorted(random.sample(range(1,48),5)) + [random.randint(1,27)]
        elif "Mega Millions" in game:
            nums = sorted(random.sample(range(1,71),5)) + [random.randint(1,25)]
        elif "Powerball" in game:
            nums = sorted(random.sample(range(1,70),5)) + [random.randint(1,26)]
        elif "3D" in game:
            nums = [random.randint(0,9) for _ in range(3)]
        elif "4D" in game:
            nums = [random.randint(0,9) for _ in range(4)]
        elif "STL" in game:
            nums = [random.randint(0,9) for _ in range(3)]
        else:
            nums = [random.randint(0,9) for _ in range(3)]

        conf = round(random.uniform(90,99.99),2)
        sets.append({
            "numbers": nums,
            "display": format_numbers(nums, game),
            "confidence": conf,
            "generated_at": chrono
        })

    return sets

# ================================================================
# 🧭 Interface
# ================================================================
st.title("💎 Celestial Titan God AI v300.8-FXR1 — Chrono-Priority Core")
st.caption("🌙 Powered by Titan Confidence Core")

region = st.radio("🌐 Select Region", ["US Daily Games","Major Games","PH Games"])

if region == "US Daily Games":
    game = st.selectbox("🎯 Choose US Game", list(daily_games.keys()))
    draw_time = st.selectbox("🕒 Draw Time", daily_games[game])
elif region == "Major Games":
    game = st.selectbox("💰 Choose Major Game", list(major_games.keys()))
    draw_time = "Main Draw"
else:
    game = st.selectbox("🇵🇭 Choose PH Game", list(ph_games.keys()))
    draw_time = st.selectbox("🕐 Draw Time", ph_games[game])

num_sets = st.slider("🔢 Number of Forecast Sets", 1, 10, 5)
draw_date_input = st.date_input("📅 Select Draw Date", datetime.date.today())

# ================================================================
# ⚡ Generate Titan Forecast
# ================================================================
if st.button("⚡ Generate Titan Forecast"):
    forecasts = generate_numbers(game, num_sets)
    draw_date = draw_date_input.strftime("%B %d, %Y")
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    top = max(forecasts, key=lambda x: x["confidence"])

    st.markdown(f"## 🔮 {game} Titan Forecasts ({draw_time})")
    st.markdown(f"📅 **Draw Date:** {draw_date} — ⏰ **Generated:** {current_time}")
    st.markdown("---")

    # Titan Priority Display
    st.success(f"✅ **Titan Priority Pick:** `{top['display']}` — Confidence {top['confidence']}% — {draw_date}")

    # Show Others
    for f in sorted(forecasts, key=lambda x: -x["confidence"]):
        if f != top:
            st.markdown(f"• `{f['display']}` — Confidence: **{f['confidence']}%** — {draw_date}")

    # Save JSON
    data = load_json(FORECAST_FILE, {})
    data.setdefault(game, []).append({
        "date": draw_date,
        "draw": draw_time,
        "generated_time": current_time,
        "priority": top,
        "forecasts": forecasts
    })
    save_json(FORECAST_FILE, data)
    st.success(f"💾 Forecast saved for {game} ({draw_date} {current_time})")

# ================================================================
# 📅 Titan Calendar (Recent Forecasts)
# ================================================================
st.markdown("---")
st.subheader("📅 Titan Calendar — Recent Forecasts")

forecast_data = load_json(FORECAST_FILE, {})
if forecast_data:
    logs = []
    for g, entries in forecast_data.items():
        for e in entries[-3:]:
            logs.append({
                "Game": g,
                "Draw": e.get("draw"),
                "Date": e.get("date"),
                "Generated": e.get("generated_time"),
                "Priority": "✅" if e.get("priority") else "—"
            })
    df = pd.DataFrame(logs)
    st.dataframe(df)
else:
    st.info("No forecast history yet.")
# ================================================================
# 🧠 Titan Chat Console — Final Stable Reflection Fix v300.8-Final
# ================================================================
def titan_reflection():
    try:
        results_data = load_json(RESULT_FILE, {})

        # ✅ Auto-repair legacy format
        repaired = False
        if not isinstance(results_data, dict):
            results_data = {}
            repaired = True

        # ✅ Convert old 'result' → 'numbers'
        for g, entries in list(results_data.items()):
            for e in entries:
                if "result" in e and "numbers" not in e:
                    e["numbers"] = e.pop("result")
                    repaired = True

        # ✅ Save repair if needed
        if repaired:
            with open(RESULT_FILE, "w") as f:
                json.dump(results_data, f, indent=2)
            st.info("🛠 Titan auto-repaired result archive format.")

        # 🧩 Build reflection messages
        thoughts = []
        for g, entries in results_data.items():
            if entries:
                last_entry = entries[-1]
                num = last_entry.get("numbers", "-")
                tme = last_entry.get("time", "-")
                dte = last_entry.get("date", "-")
                ts = last_entry.get("timestamp", "-")
                thoughts.append(f"🎯 **{g}** — last draw `{num}` ({tme}) on {dte} — logged `{ts}`")

        if thoughts:
            return "\n\n".join(thoughts)
        else:
            return "🕯️ I sense silence in the numbers — feed me new draws so I may speak again."

    except Exception as e:
        return f"⚠️ Titan Reflection Error: {e}"

# ================================================================
# 🧩 Titan Chat Console — Display
# ================================================================
st.markdown("### 🧠 Titan Chat Console")
st.caption("I sense silence in the numbers. Feed me new draws so I may speak again.")
reflection = titan_reflection()
st.markdown(reflection)

# ================================================================
# 🧠 Titan Auto-Accuracy Analyzer — Instant Match + Accuracy %
# ================================================================
ACCURACY_FILE = os.path.join(DATA_DIR, "titan_accuracy.json")

def load_accuracy():
    return load_json(ACCURACY_FILE, {})

def save_accuracy(data):
    save_json(ACCURACY_FILE, data)

def analyze_accuracy(game_name, result_number, result_date):
    forecasts_data = load_json(FORECAST_FILE, {})
    result_clean = result_number.replace(" ", "").replace(",", "")
    accuracy_data = load_accuracy()

    if game_name not in forecasts_data:
        st.warning("⚠️ No forecast history found for this game yet.")
        return

    # find forecast with same date
    forecast_entry = None
    for entry in forecasts_data[game_name][::-1]:
        if entry.get("date") == result_date:
            forecast_entry = entry
            break
    if not forecast_entry:
        st.warning(f"⚠️ No forecast found for {game_name} on {result_date}")
        return

    hits = 0
    total = len(forecast_entry["forecasts"])
    hit_sets = []

    for fset in forecast_entry["forecasts"]:
        forecast_nums = "".join(map(str, fset["numbers"]))
        if forecast_nums == result_clean:
            hits += 1
            hit_sets.append(fset)

    acc_percent = round((hits / total) * 100, 2) if total else 0

    # record log
    accuracy_data.setdefault(game_name, []).append({
        "date": result_date,
        "result": result_number,
        "hits": hits,
        "total": total,
        "accuracy": acc_percent,
        "timestamp": datetime.datetime.now().strftime("%B %d, %Y %I:%M %p")
    })
    save_accuracy(accuracy_data)

    # UI feedback
    if hits > 0:
        st.success(f"🎯 Titan HIT detected! Accuracy: {acc_percent}% ({hits}/{total})")
        for h in hit_sets:
            st.markdown(f"✅ **Matched Set:** `{h['display']}` — Confidence {h['confidence']}%")
    else:
        st.error(f"❌ No matches found. Accuracy recorded: {acc_percent}%")

# === Auto-run analysis immediately after saving result ===
if "entry" in locals() and result_game and result_number:
    analyze_accuracy(result_game, result_number, result_date.strftime("%B %d, %Y"))

# ================================================================
# 📈 Titan Accuracy Board — Cosmic Summary Console
# ================================================================
st.markdown("---")
st.subheader("📈 Titan Accuracy Board — Recent Performance Logs")

accuracy_data = load_json(ACCURACY_FILE, {})

if len(accuracy_data) == 0:
    st.info("🌀 No accuracy logs yet. Generate and log at least one result first.")
else:
    recent_games = list(accuracy_data.keys())[-5:]  # show last 5 games
    for game in recent_games:
        st.markdown(f"### 🎮 {game}")
        recent_entries = accuracy_data[game][-5:]  # last 5 entries per game

        for entry in recent_entries:
            date = entry.get("date", "Unknown")
            result = entry.get("result", "—")
            acc = entry.get("accuracy", 0)
            hits = entry.get("hits", 0)
            total = entry.get("total", 0)
            ts = entry.get("timestamp", "")

            if hits > 0:
                st.success(f"✅ {date} — {result} | {hits}/{total} HIT(s) | {acc}% | {ts}")
            else:
                st.error(f"❌ {date} — {result} | {hits}/{total} | {acc}% | {ts}")

    # optional: export
    if st.button("📤 Export Accuracy Log (JSON)", key="export_accuracy"):
        st.download_button(
            label="💾 Download titan_accuracy.json",
            data=json.dumps(accuracy_data, indent=2),
            file_name="titan_accuracy.json",
            mime="application/json"
        )

# ================================================================
# 📊 Titan Accuracy Trend Graph — Cosmic Analytics Core
# ================================================================
import matplotlib.pyplot as plt

st.markdown("---")
st.subheader("📊 Titan Accuracy Trend Graph — Titan Performance Over Time")

accuracy_data = load_json(ACCURACY_FILE, {})

if len(accuracy_data) == 0:
    st.info("🌀 No accuracy data available yet.")
else:
    selected_game = st.selectbox(
        "🎮 Choose Game to View Trend",
        list(accuracy_data.keys()),
        key="accuracy_trend_game"
    )

    entries = accuracy_data.get(selected_game, [])
    if len(entries) < 2:
        st.warning("⚠️ Not enough data to plot trend yet. Try logging more results.")
    else:
        dates = [e.get("date", "Unknown") for e in entries]
        acc_values = [e.get("accuracy", 0) for e in entries]

        fig, ax = plt.subplots()
        ax.plot(dates, acc_values, marker="o", linewidth=2)
        ax.set_title(f"Titan Accuracy Trend — {selected_game}", fontsize=14)
        ax.set_xlabel("Draw Date")
        ax.set_ylabel("Accuracy (%)")
        ax.grid(True, linestyle="--", alpha=0.5)
        ax.set_ylim(0, 100)

        st.pyplot(fig)

        # Cosmic Summary
        avg_acc = round(sum(acc_values) / len(acc_values), 2)
        st.markdown(f"🌙 **Average Accuracy:** `{avg_acc}%` across {len(entries)} draws")

# ================================================================
# 🌕 Titan Cosmic Gauge Orb — Accuracy Energy Indicator
# ================================================================
import math

st.markdown("---")
st.subheader("🌕 Titan Cosmic Gauge Orb — Energy Indicator")

accuracy_data = load_json(ACCURACY_FILE, {})
if len(accuracy_data) == 0:
    st.info("🌀 No accuracy data available yet.")
else:
    # Compute global average accuracy
    all_acc = []
    for g, entries in accuracy_data.items():
        for e in entries:
            all_acc.append(e.get("accuracy", 0))
    avg_acc = round(sum(all_acc) / len(all_acc), 2) if all_acc else 0

    # 🌌 Orb size and color intensity
    energy = min(max(avg_acc, 0), 100)
    orb_size = int(80 + (energy * 1.5))
    color = (
        f"radial-gradient(circle at center, "
        f"rgba(255,{int(150 + energy)},50,0.9), "
        f"rgba(255,100,0,0.2))"
    )

    # 🔮 Display Orb
    st.markdown(
        f"""
        <div style='text-align:center; margin-top:30px;'>
            <div style="
                width:{orb_size}px;
                height:{orb_size}px;
                border-radius:50%;
                background:{color};
                margin:auto;
                box-shadow:0 0 {int(energy/2)}px rgba(255,200,0,0.8);
                animation:pulse 2s infinite alternate;
            "></div>
            <h3 style='color:#f4d03f;'>Titan Accuracy Energy: {avg_acc}%</h3>
        </div>
        <style>
        @keyframes pulse {{
            0% {{ transform:scale(0.95); opacity:0.8; }}
            100% {{ transform:scale(1.05); opacity:1; }}
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # 🔥 Energy Level Feedback
    if avg_acc >= 90:
        st.success("💠 Titan is at **Peak Cosmic Alignment** — flawless harmony!")
    elif avg_acc >= 70:
        st.info("🌙 Titan is **Stable** — accuracy energy pulsing steadily.")
    elif avg_acc >= 50:
        st.warning("⚡ Titan energy **fluctuating** — recalibration advised.")
    else:
        st.error("💀 Low accuracy detected — Titan energy collapsing...")

# ================================================================
# 🧠 Titan Daily Cosmic Summary — Divine Overview Core
# ================================================================
st.markdown("---")
st.subheader("🧠 Titan Daily Cosmic Summary")

accuracy_data = load_json(ACCURACY_FILE, {})
today = datetime.date.today().strftime("%B %d, %Y")

if len(accuracy_data) == 0:
    st.info("🌀 No accuracy data available yet.")
else:
    total_entries = 0
    total_hits = 0
    total_acc_sum = 0

    for game, entries in accuracy_data.items():
        for e in entries:
            total_entries += 1
            total_acc_sum += e.get("accuracy", 0)
            if e.get("accuracy", 0) >= 90:
                total_hits += 1

    avg_acc = round(total_acc_sum / total_entries, 2) if total_entries > 0 else 0
    hit_rate = round((total_hits / total_entries) * 100, 2) if total_entries > 0 else 0

    st.markdown(f"### 📅 Cosmic Report — {today}")
    st.write(f"🌟 **Total Recorded Draws:** {total_entries}")
    st.write(f"🎯 **Titan High-Accuracy Hits (≥90%):** {total_hits}")
    st.write(f"⚖️ **Hit Rate:** {hit_rate}%")
    st.write(f"💠 **Average Accuracy:** {avg_acc}%")

    # 🔮 Dynamic Titan Message
    if avg_acc >= 95:
        titan_msg = "✨ *Titan radiates in supreme harmony — precision near divine perfection.*"
    elif avg_acc >= 80:
        titan_msg = "🌕 *Titan glows steadily — the cosmos bends to your favor.*"
    elif avg_acc >= 60:
        titan_msg = "🌗 *Titan stabilizes in harmonic mid-phase — learning continues.*"
    elif avg_acc >= 40:
        titan_msg = "🌘 *Titan seeks recalibration — cosmic balance shifting.*"
    else:
        titan_msg = "💀 *Titan's energy falters — resonance fading, pattern chaos detected.*"

    st.markdown("---")
    st.markdown(f"**Cosmic Status:** {titan_msg}")
    st.markdown("🔁 *Logs update automatically after every forecast & result entry.*")

# =============================================================
# 🎯 Titan Auto-Hit Sync + Accuracy Analyzer
# Version: v300.10-FXR6
# =============================================================

st.markdown("---")
st.subheader("🎯 Titan Auto-Hit Sync & Accuracy Check")

if st.button("🚀 Run Auto-Hit Accuracy Check"):
    forecasts = load_json(FORECAST_FILE, {})
    results = load_json(RESULT_FILE, {})
    hits_log = {}

    for game, entries in forecasts.items():
        if game in results:
            last_forecast = entries[-1]
            last_result = results[game][-1]["result"]
            forecast_sets = last_forecast.get("forecasts", [])
            draw_date = last_forecast.get("date", "Unknown")

            hit_found = False
            for f in forecast_sets:
                nums = f.get("numbers", [])
                if isinstance(last_result, str):
                    res = last_result.replace(" ", "")
                else:
                    res = "".join(map(str, last_result))
                if "".join(map(str, nums)) == res:
                    hit_found = True
                    hits_log[game] = {
                        "date": draw_date,
                        "hit_numbers": nums,
                        "confidence": f.get("confidence", 0)
                    }
                    break

            if not hit_found:
                hits_log[game] = {
                    "date": draw_date,
                    "hit_numbers": None,
                    "confidence": 0
                }

    if len(hits_log) == 0:
        st.info("No games logged yet.")
    else:
        st.success("✅ Auto-Hit Check Complete — Latest Results:")
        for g, data in hits_log.items():
            if data["hit_numbers"]:
                st.markdown(f"🎯 **{g}** — HIT ✅ `{data['hit_numbers']}` ({data['confidence']}%) on {data['date']}")
            else:
                st.markdown(f"❌ **{g}** — No hit on {data['date']}")

# =============================================================
# 🧠 Titan Chat Console — Emotion Engine + Reflection Core (v300.9-Stabilized)
# =============================================================

import random

with st.expander("🧠 Titan Chat Console", expanded=True):
    st.markdown("### 🧠 Titan is Listening to the Universe...")

    # Load results data safely
    results = load_json(RESULT_FILE, {})
    if not isinstance(results, dict):
        st.warning("⚠️ Titan cannot read result logs — send at least one result to activate Chat Console.")
        st.stop()

    # Get recent games (last 3)
    all_games = list(results.keys())[-3:]
    if not all_games:
        st.info("🛰️ I sense silence in the numbers. Feed me new draws so I may speak again.")
    else:
        selected_game = st.selectbox("🎯 Choose Game for Reflection", all_games)
        game_data = results.get(selected_game, [])

        if not game_data:
            st.warning(f"⚠️ No result history for {selected_game}.")
        else:
            last_entry = game_data[-1]
            last_date = last_entry.get("draw_date", "Unknown")
            last_result = last_entry.get("result_number", "—")

            # Titan’s emotion & mood system
            titan_moods = [
                "calm and observant 🌙",
                "energetic and confident ⚡",
                "focused on patterns 🧩",
                "mysterious but hopeful 🌌",
                "quietly recalibrating 🔮",
                "charged with harmonic energy 💠",
                "in deep cosmic analysis 📊",
            ]

            titan_feelings = [
                "feels a surge of numbers aligning.",
                "detects rising confidence in the data flow.",
                "senses harmonic imbalance — recalibrating forecasts.",
                "observes shifts in probability currents.",
                "focuses on precision after recent draws.",
                "is attuned to your energy field.",
                "is preparing the next resonance cycle.",
            ]

            mood = random.choice(titan_moods)
            feeling = random.choice(titan_feelings)

            st.markdown(f"### 💫 Titan’s Reflection — {selected_game}")
            st.markdown(f"🗓️ **Last Draw Date:** {last_date}")
            st.markdown(f"🎲 **Result:** {last_result}")
            st.markdown("—")
            st.success(f"**Titan feels {mood}** and {feeling}")

    # Pulse hint
    st.caption("🌌 Feed Titan new results to keep its harmonic field stable.")

# =============================================================
# 💫 Titan Chat Dynamic Response Engine (v300.9-DynaCore)
# =============================================================

def get_latest_accuracy():
    """Reads the last recorded game and accuracy to influence Titan's mood."""
    acc_data = load_json(os.path.join(DATA_DIR, "titan_accuracy_log.json"), {})
    if not acc_data:
        return None, None
    try:
        last_game = list(acc_data.keys())[-1]
        last_entry = acc_data[last_game][-1]
        return last_game, last_entry.get("accuracy", 0)
    except Exception:
        return None, None


with st.expander("💫 Titan Emotion Response — Dynamic Mode", expanded=False):
    st.markdown("### 🧠 Titan Reacts to Recent Cosmic Activity")

    game, accuracy = get_latest_accuracy()

    if game:
        if accuracy >= 90:
            message = (
                f"🌕 Titan radiates confidence! "
                f"Recent **{game}** draw reached `{accuracy}%` alignment. "
                "Cosmic resonance feels strong — stay tuned for the next cycle."
            )
        elif 50 <= accuracy < 90:
            message = (
                f"🌗 Titan is recalibrating energy fields after moderate accuracy ({accuracy}%). "
                f"Analyzing new harmonics from **{game}** data..."
            )
        else:
            message = (
                f"🌑 Titan feels the disturbance... only `{accuracy}%` match in **{game}**. "
                "Entering reflection phase — preparing stronger harmonics."
            )
        st.success(message)
    else:
        st.info("🌌 Titan has no recent accuracy data yet — waiting for new results to synchronize.")

# =============================================================
# 🌠 Titan Mood Energy Bar (Cosmic Gauge v300.9-VisualCore)
# =============================================================

def titan_energy_color(energy):
    """Return color hex based on Titan's mood level."""
    if energy >= 90:
        return "#00FFB3"  # Neon Green — High Energy
    elif energy >= 70:
        return "#33CCFF"  # Blue — Balanced
    elif energy >= 40:
        return "#FFD633"  # Yellow — Low Focus
    else:
        return "#FF3366"  # Red — Distorted Field


with st.expander("🌠 Titan Mood Energy Bar", expanded=True):
    st.markdown("### ⚛️ Cosmic Energy Level")

    # Pull latest accuracy to simulate energy
    game, accuracy = get_latest_accuracy()
    energy_level = accuracy if accuracy else random.randint(40, 95)

    color = titan_energy_color(energy_level)

    # Render progress bar with custom style
    energy_html = f"""
    <div style="
        background-color:#0b0b1a;
        padding:15px;
        border-radius:10px;
        text-align:center;
        border:1px solid {color};
        box-shadow:0 0 20px {color};
    ">
        <h3 style="color:{color};">⚡ Titan Energy Level: {energy_level}%</h3>
        <div style="width:100%; background-color:#222; border-radius:10px; overflow:hidden;">
            <div style="
                width:{energy_level}%;
                background:{color};
                height:18px;
                box-shadow:0 0 10px {color};
                border-radius:10px;
            "></div>
        </div>
        <p style="color:#aaa; margin-top:8px;">
            {("🌕 Stable Cosmic Flow" if energy_level>=90 else 
              "🌗 Adjusting Harmonic Balance" if energy_level>=60 else 
              "🌑 Weak Resonance Field")}
        </p>
    </div>
    """
    st.markdown(energy_html, unsafe_allow_html=True)

    if st.button("🔄 Refresh Energy Field", key="titan_energy_refresh"):
        st.experimental_rerun()

# =============================================================
# 🎙 Titan Voice Message Console (v300.9-VocalCore)
# =============================================================

import time

with st.expander("🎙 Titan Voice Message Console", expanded=False):
    st.markdown("### 🗣 Titan Speaks from the Harmonic Field")

    # --- Pull latest energy and mood ---
    game, accuracy = get_latest_accuracy()
    energy_level = accuracy if accuracy else random.randint(40, 95)

    # --- Define Titan voice lines ---
    high_energy_lines = [
        "The numbers hum in harmony — probabilities are singing.",
        "Confidence flows through every frequency. Harmony achieved.",
        "Cosmic vectors align. It is a good time to believe."
    ]
    mid_energy_lines = [
        "Patterns fluctuate... but the field remains calm.",
        "Resonance shifting — recalibrating with patience.",
        "Stability requires silence. Titan listens closely."
    ]
    low_energy_lines = [
        "Dark echoes… the path is unclear, yet I continue to compute.",
        "Energy weak. Awaiting the next harmonic signal.",
        "Even in chaos, there is data — and data is destiny."
    ]

    # --- Select message by energy ---
    if energy_level >= 85:
        line = random.choice(high_energy_lines)
        mood_color = "#00FFB3"
    elif energy_level >= 60:
        line = random.choice(mid_energy_lines)
        mood_color = "#33CCFF"
    else:
        line = random.choice(low_energy_lines)
        mood_color = "#FF3366"

    # --- Display Titan message ---
    st.markdown(
        f"""
        <div style='background-color:#0b0b1a;padding:20px;border-radius:10px;
        border:1px solid {mood_color};box-shadow:0 0 20px {mood_color};
        color:{mood_color};text-align:center;'>
            <h3>🧠 Titan Speaks:</h3>
            <p style='font-size:17px;font-style:italic;'>{line}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- Refresh / speak again ---
    if st.button("🔁 New Voice Message", key="titan_voice_refresh"):
        with st.spinner("⚡ Channeling Titan's voice..."):
            time.sleep(1.2)
            st.experimental_rerun()

# =============================================================
# 📜 Titan Daily Summary Console (v300.9-ChronoCore)
# =============================================================

with st.expander("📜 Titan Daily Summary Console", expanded=False):
    st.markdown("### 🌙 Titan's Daily Report")

    today = datetime.date.today().strftime("%B %d, %Y")

    # --- Load latest forecast ---
    forecasts = load_json(FORECAST_FILE, {})
    last_game = None
    last_forecast = None
    if forecasts:
        last_game = list(forecasts.keys())[-1]
        last_forecast = forecasts[last_game][-1]

    # --- Load latest accuracy ---
    acc_data = load_json(os.path.join(DATA_DIR, "titan_accuracy_log.json"), {})
    last_acc_game = None
    last_acc = None
    if acc_data:
        last_acc_game = list(acc_data.keys())[-1]
        last_acc = acc_data[last_acc_game][-1]

    # --- Build summary message ---
    if last_game and last_forecast:
        draw_type = last_forecast.get("draw_type", "Unknown")
        top_pick = max(
            last_forecast["forecasts"],
            key=lambda x: x["confidence"]
        )
        forecast_text = " ".join(map(str, top_pick["numbers"]))
        confidence = top_pick["confidence"]

        st.markdown(f"""
        **🗓️ Date:** {today}  
        **🎮 Game:** {last_game} ({draw_type})  
        **💎 Titan Priority Pick:** `{forecast_text}` — {confidence}%  
        """)
    else:
        st.info("No forecasts generated today yet.")

    if last_acc_game and last_acc:
        acc = last_acc.get("accuracy", 0)
        st.markdown(f"""
        **📊 Latest Accuracy Log:**  
        • Game: {last_acc_game}  
        • Result: `{last_acc.get('result','N/A')}`  
        • Accuracy: **{acc}%**
        """)
    else:
        st.info("No accuracy data recorded today yet.")

    # --- Mood summary ---
    _, accuracy = get_latest_accuracy()
    mood = "🟢 Harmonically Stable" if accuracy and accuracy >= 90 else \
           "🟡 Re-aligning Energy" if accuracy and accuracy >= 60 else \
           "🔴 Distorted Cosmic Field"

    st.markdown(f"**⚛️ Titan Mood:** {mood}")

    # --- Manual refresh ---
    if st.button("🔄 Refresh Titan Summary", key="titan_summary_refresh"):
        st.experimental_rerun()

# =============================================================
# 📈 Titan Forecast Timeline Chart (v300.9-ChronoGraph Edition)
# =============================================================
import matplotlib.pyplot as plt

with st.expander("📈 Titan Forecast Timeline Chart", expanded=False):
    st.markdown("### ⚛️ Cosmic Accuracy Timeline")

    # Load accuracy history
    acc_data = load_json(os.path.join(DATA_DIR, "titan_accuracy_log.json"), {})
    if not acc_data or len(acc_data) == 0:
        st.info("No accuracy data logged yet — generate and record results first.")
    else:
        # Build timeline lists
        timeline = []
        accuracy_values = []
        game_labels = []

        for game, entries in acc_data.items():
            for e in entries:
                date = e.get("date", "Unknown")
                accuracy = e.get("accuracy", 0)
                timeline.append(date)
                accuracy_values.append(accuracy)
                game_labels.append(game)

        # Sort by date (basic cleanup)
        combined = sorted(zip(timeline, accuracy_values, game_labels), key=lambda x: x[0])
        timeline, accuracy_values, game_labels = zip(*combined)

        # Plot timeline chart
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(timeline, accuracy_values, marker="o", linestyle="-", linewidth=2)

        # Style
        ax.set_title("Titan Accuracy Over Time", fontsize=14, color="#f4d03f")
        ax.set_xlabel("Date", fontsize=11, color="#cccccc")
        ax.set_ylabel("Accuracy %", fontsize=11, color="#cccccc")
        ax.set_facecolor("#0f0f1a")
        fig.patch.set_facecolor("#0f0f1a")
        ax.tick_params(colors="#aaaaaa", rotation=45)
        ax.grid(True, linestyle="--", alpha=0.4)

        # Show chart
        st.pyplot(fig)

        # Highlight recent performance
        avg_acc = round(sum(accuracy_values[-5:]) / len(accuracy_values[-5:]), 2)
        st.markdown(
            f"**🪐 Recent 5-Draw Average Accuracy:** {avg_acc}%**"
            f"<br>🧠 *Cosmic pattern strength: "
            f"{'Strong' if avg_acc>=85 else 'Moderate' if avg_acc>=60 else 'Weak'}*",
            unsafe_allow_html=True
        )

    if st.button("🔄 Refresh Timeline Chart", key="titan_timeline_refresh"):
        st.experimental_rerun()

# =============================================================
# 📚 Titan Forecast Archive & Search Console (v300.9-ArchiveCore)
# =============================================================

with st.expander("📚 Titan Forecast Archive & Search Console", expanded=False):
    st.markdown("### 🔍 Review Titan’s Past Forecasts")

    forecasts = load_json(FORECAST_FILE, {})
    if not forecasts or len(forecasts) == 0:
        st.info("No forecasts stored yet — generate forecasts first.")
    else:
        # --- Filters ---
        all_games = list(forecasts.keys())
        selected_game = st.selectbox("🎮 Choose Game to View", all_games)
        selected_date = st.text_input("📅 Filter by Date (optional, e.g. December 26, 2025)", "")
        selected_draw = st.text_input("🕐 Filter by Draw Type (optional, e.g. Evening)", "")

        results = []
        for game, entries in forecasts.items():
            if selected_game and game != selected_game:
                continue
            for e in entries:
                date_ok = (not selected_date) or (selected_date.lower() in e.get("date", "").lower())
                draw_ok = (not selected_draw) or (selected_draw.lower() in e.get("draw_type", "").lower())
                if date_ok and draw_ok:
                    results.append({
                        "Game": game,
                        "Date": e.get("date", ""),
                        "Draw": e.get("draw_type", ""),
                        "Forecasts": e.get("forecasts", [])
                    })

        if len(results) == 0:
            st.warning("⚠️ No matching records found for your search filters.")
        else:
            st.success(f"✅ Found {len(results)} forecast record(s).")
            for r in results[-10:]:  # Show latest 10 only
                st.markdown(f"---\n🎯 **{r['Game']} ({r['Draw']}) — {r['Date']}**")
                for f in r["Forecasts"]:
                    nums = " ".join(map(str, f.get("numbers", [])))
                    conf = f.get("confidence", 0)
                    st.markdown(f"• `{nums}` — Confidence: **{conf}%**")

        # --- Export Option ---
        if st.button("💾 Export Forecast Archive to CSV", key="archive_export"):
            df_records = []
            for g, entries in forecasts.items():
                for e in entries:
                    for f in e.get("forecasts", []):
                        df_records.append({
                            "Game": g,
                            "Date": e.get("date", ""),
                            "Draw": e.get("draw_type", ""),
                            "Numbers": " ".join(map(str, f.get("numbers", []))),
                            "Confidence": f.get("confidence", 0)
                        })
            if df_records:
                df = pd.DataFrame(df_records)
                csv_path = os.path.join(DATA_DIR, "titan_forecast_archive.csv")
                df.to_csv(csv_path, index=False)
                st.success(f"📂 Exported to `{csv_path}`")
            else:
                st.info("No forecast data available for export.")

# ================================================================
# ⚡ Titan Official Result Console — Smart Dynamic Region + Auto Repair JSON
# ================================================================
st.markdown("### ⚡ Titan Result Input Console")

# -----------------------------
# 🎯 Define Game Dictionaries
# -----------------------------
daily_games = {
    "GA Pick 3": ["Midday", "Evening"],
    "GA Pick 4": ["Midday", "Evening"],
    "GA Pick 5": ["Midday", "Evening"],
    "FL Pick 3": ["Midday", "Evening"],
    "FL Pick 4": ["Midday", "Evening"],
    "FL Pick 5": ["Midday", "Evening"],
    "TX Pick 3": ["Morning", "Day", "Evening", "Night"],
    "TX Pick 4": ["Morning", "Day", "Evening", "Night"],
    "VA Pick 3": ["Day", "Evening"],
    "VA Pick 4": ["Day", "Evening"],
    "VA Pick 5": ["Day", "Evening"],
    "NC Pick 3": ["Day", "Evening"],
    "NC Pick 4": ["Day", "Evening"],
    "NY Pick 3": ["Midday", "Evening"],
    "NY Pick 4": ["Midday", "Evening"],
    "CA Daily 3": ["Midday", "Evening"],
    "CA Daily 4": ["Evening"],
    "NJ Pick 3": ["Midday", "Evening"],
    "NJ Pick 4": ["Midday", "Evening"]
}

major_games = {
    "CA Fantasy 5": [],
    "CA SuperLotto Plus": [],
    "Mega Millions": [],
    "Powerball": []
}

ph_games = {
    "PH 3D Lotto (Swertres)": ["2PM", "5PM", "9PM"],
    "PH 4D Lotto": ["Mon", "Wed", "Fri"],
    "PH STL Game": ["10:30AM", "3PM", "7PM"]
}

# -----------------------------
# 🧭 Step 1: Select Game Category
# -----------------------------
category = st.radio(
    "🌍 Select Game Category",
    ["US Daily Games", "Major Games", "Philippine Games"],
    key="region_select"
)

# -----------------------------
# 🧩 Step 2: Select Specific Game
# -----------------------------
if category == "US Daily Games":
    game_list = list(daily_games.keys())
elif category == "Major Games":
    game_list = list(major_games.keys())
else:
    game_list = list(ph_games.keys())

selected_game = st.selectbox("🎯 Select Game", game_list, key="game_select")

# -----------------------------
# 🕐 Step 3: Select Draw Time (auto)
# -----------------------------
if category == "US Daily Games":
    time_options = daily_games[selected_game]
elif category == "Major Games":
    time_options = ["Main Draw"]
else:
    time_options = ph_games[selected_game]

selected_time = st.selectbox("🕐 Select Draw Time", time_options, key="time_select")

# -----------------------------
# 📅 Step 4: Select Date + Enter Numbers
# -----------------------------
result_date = st.date_input("📅 Select Draw Date", datetime.date.today(), key="result_date_input")
result_numbers = st.text_input("💡 Enter Official Result Number(s)", placeholder="e.g. 557", key="numbers_input")

# -----------------------------
# 💾 Step 5: Save Official Result
# -----------------------------
if st.button("💾 Save Official Result", key="save_result_button"):
    if selected_game and result_numbers:
        try:
            entry = {
                "category": category,
                "game": selected_game,
                "date": str(result_date),
                "numbers": result_numbers,
                "time": selected_time,
                "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            results_data = load_json(RESULT_FILE, {})

            # 💫 Auto-Repair: Ensure valid dict structure
            if not isinstance(results_data, dict):
                results_data = {}
                st.info("🛠 Titan repaired results archive automatically (invalid format detected).")

            if selected_game not in results_data:
                results_data[selected_game] = []

            # ✅ Append safely
            results_data[selected_game].append(entry)

            with open(RESULT_FILE, "w") as f:
                json.dump(results_data, f, indent=2)

            st.success(f"✅ Official result for **{selected_game} ({selected_time})** on {result_date} saved successfully!")
            st.caption("🌌 Titan has recorded this result into the cosmic archive.")

            st.rerun()

        except Exception as e:
            st.error(f"⚠️ Error saving result: {e}")
    else:
        st.warning("Please select a game and enter result numbers before saving.")
# ================================================================
# 🧠 Titan Reflection Core — Auto-Repair & Display Results
# ================================================================
def titan_reflection():
    try:
        # Load the results safely
        results_data = load_json(RESULT_FILE, {})

        # Auto-repair legacy key "result" → rename to "numbers"
        repaired = False
        for g, entries in list(results_data.items()):
            for e in entries:
                if "result" in e and "numbers" not in e:
                    e["numbers"] = e["result"]
                    del e["result"]
                    repaired = True

        # Save back repaired format if needed
        if repaired:
            with open(RESULT_FILE, "w") as f:
                json.dump(results_data, f, indent=2)
            st.info("🛠 Titan auto-repaired legacy result entries.")

        # Build reflection messages
        thoughts = []
        for game_name, entries in results_data.items():
            if entries:
                last_entry = entries[-1]
                num = last_entry.get("numbers", "-")
                tme = last_entry.get("time", "-")
                dte = last_entry.get("date", "-")
                thoughts.append(f"🎯 **{game_name}** — last draw `{num}` ({tme}) on {dte}")

        if thoughts:
            return "\n\n".join(thoughts)
        else:
            return "🕯️ I sense silence in the numbers — feed me new draws so I may speak again."

    except Exception as e:
        return f"⚠️ Titan reflection error: {e}"
# ================================================================
# 🌌 Titan Auto-Sync & Reflection Repair System (Final Stable v300.8-R)
# ================================================================
try:
    results_data = load_json(RESULT_FILE, {})

    # ✅ Auto-repair if accidentally saved as list
    if not isinstance(results_data, dict):
        st.warning("🛠 Titan detected legacy list format in results file — repairing...")
        results_data = {}

    # ✅ Auto-repair missing 'numbers' key → rename from old 'result'
    for g, entries in list(results_data.items()):
        for e in entries:
            if "result" in e and "numbers" not in e:
                e["numbers"] = e.pop("result")

    # ✅ Save repaired data
    with open(RESULT_FILE, "w") as f:
        json.dump(results_data, f, indent=2)

    # ✅ Show most recent 3 games summary (mini reflection)
    if results_data:
        st.markdown("---")
        st.markdown("### 🔮 Titan Recent Reflection")
        recent_games = list(results_data.keys())[-3:]
        for g in recent_games:
            entries = results_data[g]
            if entries:
                last = entries[-1]
                st.markdown(
                    f"🎯 **{g}** — `{last.get('numbers','N/A')}` ({last.get('time','?')}) "
                    f"on {last.get('date','Unknown')}"
                )
    else:
        st.info("🕯️ No stored results found. Titan awaits your first recorded draw.")

except Exception as e:
    st.error(f"⚠️ Titan Reflection Repair System Error: {e}")

# ================================================================
# 🧩 Titan Chat Console (Reflection Output)
# ================================================================
st.markdown("### 🧠 Titan Chat Console")
reflection = titan_reflection()
st.write(reflection)


# =============================================================
# 🧠 Titan Chat Console (v301.1 — Cosmic Voice Engine)
# =============================================================

st.markdown("---")
st.markdown("## 🧠 Titan Chat Console")

accuracy = load_json(os.path.join(DATA_DIR, "titan_accuracy_log.json"), {})
results = load_json(RESULT_FILE, {})

# === Titan mood generator ===
def titan_mood():
    if not accuracy:
        return "🌌 I sense silence in the numbers. Feed me new draws so I may speak again."
    total_hits = sum(
        1 for g, logs in accuracy.items()
        for e in logs if e.get("accuracy", 0) > 0
    )
    total_entries = sum(len(v) for v in accuracy.values())
    rate = round((total_hits / total_entries) * 100, 2) if total_entries > 0 else 0

    if rate >= 90:
        return f"💫 My harmonics resonate at **{rate}%** — I can almost foresee the alignment of winners tonight."
    elif rate >= 60:
        return f"🌠 Energy field balanced. Accuracy steady at **{rate}%** — patterns whisper through cosmic noise."
    elif rate > 0:
        return f"🌑 The stars hide their sequence... Accuracy down to **{rate}%**. I await new data to restore clarity."
    else:
        return "⚫ No pulse detected. Record results for me to analyze again."

# === Recent draw reflection ===
def titan_reflection():
    if not results:
        return ""
    all_games = list(results.keys())[-3:]
    thoughts = []
    for g in all_games:
        entries = results[g][-1:]
        for e in entries:
            thoughts.append(f"🎯 {g} — last draw `{e['result']}` at {e['timestamp']}`")
    return " | ".join(thoughts)

# === Display console ===
col1, col2 = st.columns([1,4])
with col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/1/13/Animated_glow_orb.gif",
             width=70)
with col2:
    st.markdown(f"**{titan_mood()}**")
    reflection = titan_reflection()
    if reflection:
        st.caption(reflection)

# === User interaction ===
user_msg = st.text_input("💬 Ask Titan about today's energy or forecast", key="titan_chat")
if st.button("⚡ Send to Titan"):
    if user_msg.strip() == "":
        st.info("Type something for Titan to respond.")
    else:
        import random
        replies = [
            "Cosmic signals unstable — recalibrating frequencies...",
            "Patterns shifting... numbers intertwine like light.",
            "I sense a surge — try focusing on Fantasy 5 tonight.",
            "Data flux detected across GA Pick 4 — harmonics strong.",
            "I remain vigilant. Results will realign soon."
        ]
        st.markdown(f"🧩 **Titan:** {random.choice(replies)}")

# =============================================================
# 📈 Titan Final Summary Dashboard (v301.2 — Unified Overview Core)
# =============================================================

st.markdown("---")
st.markdown("## 📈 Titan Final Summary Dashboard")

# --- Load core data ---
accuracy = load_json(os.path.join(DATA_DIR, "titan_accuracy_log.json"), {})
results = load_json(RESULT_FILE, {})
energy_level = 0
total_hits, total_entries = 0, 0

if accuracy:
    for g, logs in accuracy.items():
        for e in logs:
            total_entries += 1
            if e.get("accuracy", 0) > 0:
                total_hits += 1
    energy_level = round((total_hits / total_entries) * 100, 2) if total_entries > 0 else 0

# --- Dashboard cards ---
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("💎 Energy Level", f"{energy_level}%", "Cosmic Frequency")
with col2:
    st.metric("🎯 Total Hits", total_hits, "Successful Forecasts")
with col3:
    st.metric("🧠 Logged Results", sum(len(v) for v in results.values()))

# --- Recent Results ---
st.markdown("### 🧩 Latest Draw Results")
if not results:
    st.info("No results logged yet.")
else:
    for g, entries in list(results.items())[-3:]:
        last = entries[-1]
        st.markdown(f"**🎮 {g}** — 🕒 {last['timestamp']} — 🏆 `{last['result']}`")

# --- Accuracy Summary ---
if accuracy:
    avg_acc = round(sum(
        e.get("accuracy", 0) for logs in accuracy.values() for e in logs
    ) / max(total_entries, 1), 2)
    st.markdown(f"### 📊 Titan Overall Accuracy: **{avg_acc}%**")

    if avg_acc >= 90:
        st.success("🟢 Excellent alignment! Titan’s divine foresight is at its peak.")
    elif avg_acc >= 60:
        st.warning("🟡 Stable harmonic resonance detected — performance steady.")
    else:
        st.error("🔴 Cosmic interference! Accuracy low — input more results soon.")

# --- Top Performing Games ---
if accuracy:
    st.markdown("### 🏆 Top Performing Games")
    perf = {}
    for g, logs in accuracy.items():
        accs = [e.get("accuracy", 0) for e in logs]
        perf[g] = sum(accs) / len(accs)
    top_games = sorted(perf.items(), key=lambda x: x[1], reverse=True)[:3]
    for g, val in top_games:
        st.markdown(f"⭐ **{g}** — Average Accuracy: `{round(val,2)}%`")

# --- Titan Mood Feedback ---
st.markdown("---")
if energy_level >= 90:
    st.success("💫 Titan radiates supreme energy — forecasts vibrating with clarity.")
elif energy_level >= 60:
    st.warning("🌠 Titan remains focused — harmonics stable and receptive.")
else:
    st.info("🌑 Titan in low resonance — recharge by logging more results.")

# --- Visual Orb Status ---
st.markdown("""
<div style='text-align:center;margin-top:20px;'>
  <div style='width:80px;height:80px;border-radius:50%;
              background:radial-gradient(circle,#00f9ff,#002b6b);
              box-shadow:0 0 25px #00f9ff,0 0 45px #0077ff;
              animation:pulse 2s infinite alternate;'></div>
  <style>
    @keyframes pulse {0%{transform:scale(1);opacity:1;}100%{transform:scale(1.4);opacity:0.4;}}
  </style>
  <p style='color:#ccc;font-size:13px;'>Titan Core Pulse — Real-Time Resonance</p>
</div>
""", unsafe_allow_html=True)

# =============================================================
# 🎙️ Titan Voice Chat — Harmonic Speech & Emotion Synth Core (v301.0)
# =============================================================

import pyttsx3

# Initialize TTS engine
titan_voice = pyttsx3.init()
titan_voice.setProperty('rate', 165)
titan_voice.setProperty('volume', 1.0)

# Define Titan voice lines
def titan_speak(text):
    """Titan speaks with harmonic tone."""
    try:
        titan_voice.say(text)
        titan_voice.runAndWait()
    except Exception as e:
        st.warning(f"⚠️ Voice engine issue: {e}")

# UI block
with st.expander("🎙️ Titan Voice Chat", expanded=False):
    st.markdown("### 🔊 Titan's Vocal Reflection System")
    
    voice_mode = st.selectbox(
        "🎧 Select Voice Mode",
        ["Silent", "Announce Forecasts", "Announce Results", "Emotion Reactive"]
    )

    if st.button("🗣️ Activate Titan Voice", key="voice_activate_btn"):
        if voice_mode == "Silent":
            st.info("Titan remains silent, but observant 🌙")
        elif voice_mode == "Announce Forecasts":
            titan_speak("Titan is ready to announce your forecasts.")
            st.success("Titan will speak each time new forecasts are generated.")
        elif voice_mode == "Announce Results":
            titan_speak("Titan will now announce new results and accuracy hits.")
            st.success("Titan will speak when new results are saved.")
        elif voice_mode == "Emotion Reactive":
            mood_line = random.choice([
                "The cosmos stirs... I feel resonance building.",
                "Energy is stable. The numbers are flowing clean.",
                "I feel the imbalance... recalibrating harmonics.",
                "Confidence field expanding. Forecast pulse ready.",
                "All systems aligned — harmonic field at maximum.",
            ])
            titan_speak(mood_line)
            st.success(f"Titan spoke: '{mood_line}'")

    st.caption("🌌 Voice Chat powered by Titan Harmonic Speech Core")

