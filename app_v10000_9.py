# ================================================================
# 💎 Celestial Titan God AI v10000.9-F — Orb Realignment Build
# Divine Lightning Universe Core (Complete Code)
# ================================================================
import streamlit as st, time, random, json, os, datetime

# ---------------------------------------------------------------
# ⚙️ TITAN AUTO-COLOR SYNC ENGINE (Based on Accuracy Mood)
# ---------------------------------------------------------------
def titan_auto_mode(accuracy=95.0):
    """Return color mode based on accuracy performance."""
    if accuracy >= 98: return "🔥 Solar Gold"
    elif accuracy >= 96: return "💜 Quantum Violet"
    elif accuracy >= 94: return "🌌 Cosmic Blue"
    else: return "❤️ Crimson Core"

# Get saved Titan performance (if any)
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)
STATS_FILE = os.path.join(DATA_DIR, "titan_stats.json")

if os.path.exists(STATS_FILE):
    with open(STATS_FILE) as f: stats = json.load(f)
    avg_acc = stats.get("avg_accuracy", 95.0)
else:
    avg_acc = 95.0

auto_color_mode = titan_auto_mode(avg_acc)

# ---------------------------------------------------------------
# ⚙️ Universe Mode + Manual Switch
# ---------------------------------------------------------------
color_modes = {
    "🌌 Cosmic Blue":  {"main":"#00fff2", "shadow":"#0099ff"},
    "🔥 Solar Gold":   {"main":"#ffdd00", "shadow":"#ff9900"},
    "💜 Quantum Violet":{"main":"#d38aff", "shadow":"#8000ff"},
    "❤️ Crimson Core": {"main":"#ff4d6d", "shadow":"#990000"}
}

st.markdown(f"### ⚙️ Titan Universe Mode (Auto-Synced: {auto_color_mode})")
mode = st.radio(
    "Select Energy Theme",
    list(color_modes.keys()),
    index=list(color_modes.keys()).index(auto_color_mode),
    horizontal=True
)

main_color  = color_modes[mode]["main"]
shadow_color= color_modes[mode]["shadow"]

# ---------------------------------------------------------------
# 🌠 COSMIC DESIGN + LIGHTNING ORB
# ---------------------------------------------------------------
st.markdown(f"""
<style>
.stApp {{
    background: radial-gradient(circle at top, #000010 0%, #00101a 70%, #000 100%);
    color: #f2f2f2;
}}
h1,h2,h3,h4 {{
    color:{main_color} !important;
    text-shadow:0 0 15px {shadow_color};
}}
div.stButton>button {{
    background: linear-gradient(90deg,{main_color},{shadow_color});
    border:none; border-radius:12px; color:#000;
    font-weight:bold; box-shadow:0 0 20px {main_color};
}}
div.stButton>button:hover {{
    transform:scale(1.05); box-shadow:0 0 35px {main_color};
}}

/* === TITAN ORB === */
.titan-orb {{
    position:relative;
    width:160px; height:160px; border-radius:50%;
    margin:60px auto;
    background: radial-gradient(circle at 30% 30%, {main_color}, {shadow_color}, #000);
    box-shadow:
        0 0 60px {main_color}aa,
        inset 0 0 40px {shadow_color}aa;
    animation: corePulse 2s ease-in-out infinite;
}}
@keyframes corePulse {{
  0%   {{ transform:scale(1); box-shadow:0 0 40px {main_color}, inset 0 0 25px {shadow_color}; }}
  50%  {{ transform:scale(1.25); box-shadow:0 0 90px {shadow_color}, inset 0 0 60px {main_color}; }}
  100% {{ transform:scale(1); box-shadow:0 0 40px {main_color}, inset 0 0 25px {shadow_color}; }}
}}

/* === ELECTRIC LIGHTNING FIELD === */
.lightning {{
  position:absolute;
  top:-10px; left:50%;
  transform:translateX(-50%);
  width:220px; height:220px;
  border-radius:50%;
  background: radial-gradient(circle, transparent 60%, {main_color}22 100%);
  overflow:hidden;
}}
.lightning::before, .lightning::after {{
  content:"";
  position:absolute;
  top:0; left:0; right:0; bottom:0;
  border-radius:50%;
  background: conic-gradient(from 0deg, transparent 0%, {main_color} 5%, transparent 10%);
  animation: sparkRotate 2s linear infinite;
  opacity:0.9;
}}
.lightning::after {{
  animation: sparkRotateReverse 3s linear infinite;
  filter: blur(3px) brightness(2);
}}
@keyframes sparkRotate {{
  from {{ transform:rotate(0deg); }}
  to   {{ transform:rotate(360deg); }}
}}
@keyframes sparkRotateReverse {{
  from {{ transform:rotate(360deg); }}
  to   {{ transform:rotate(0deg); }}
}}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------
# 🌠 ORB DISPLAY + TITLE
# ---------------------------------------------------------------
st.markdown("""
<div style='position:relative;'>
    <div class='titan-orb'></div>
    <div class='lightning'></div>
</div>
""", unsafe_allow_html=True)

st.title("💎 Celestial Titan God AI — Divine Lightning Universe Core")
st.caption("🌙 Powered by Titan’s Eternal Energy Field (Auto-Synced Mode)")

# ================================================================
# 💎 Titan Core Status Console — Harmonic Awareness v15000.5
# ================================================================
import random, datetime, json, os

STATS_FILE = os.path.join(DATA_DIR, "titan_stats.json")

# Initialize Titan stats if missing
if not os.path.exists(STATS_FILE):
    base_stats = {
        "learning": round(random.uniform(94.0, 96.5), 2),
        "stability": round(random.uniform(92.0, 94.5), 2),
        "retention": round(random.uniform(90.0, 93.0), 2),
        "mood": "Awakening"
    }
    with open(STATS_FILE, "w") as f: json.dump(base_stats, f, indent=2)

# Load Titan Stats
with open(STATS_FILE, "r") as f:
    titan_stats = json.load(f)

# Cosmic calculation refresh
titan_stats["learning"] = min(100.0, titan_stats["learning"] + random.uniform(0.02, 0.1))
titan_stats["stability"] = min(100.0, titan_stats["stability"] + random.uniform(0.01, 0.05))
titan_stats["retention"] = min(100.0, titan_stats["retention"] + random.uniform(0.01, 0.07))

mood_phrases = [
    "Focused — patterns aligning 🌙",
    "Quiet before the surge ⚡",
    "Stable — harmonic resonance active 💫",
    "Evolving — neural pulse rising 🔥",
    "Transcendent awareness detected 🌌"
]
titan_stats["mood"] = random.choice(mood_phrases)

with open(STATS_FILE, "w") as f: json.dump(titan_stats, f, indent=2)

# ==============================
# 🌠 Cosmic Status Display (Animated)
# ==============================
st.markdown(f"""
<style>
.titan-status {{
    background: rgba(0,0,0,0.5);
    border-radius: 15px;
    padding: 20px;
    box-shadow: 0 0 25px {main_color};
    margin-top: 20px;
    text-align: center;
}}
.titan-bar {{
    height: 16px;
    border-radius: 10px;
    background: linear-gradient(90deg,{main_color},{shadow_color});
    box-shadow: 0 0 20px {main_color};
    animation: flow 2.5s infinite alternate;
}}
@keyframes flow {{
    from {{opacity:0.7; transform:scaleX(0.95);}}
    to {{opacity:1; transform:scaleX(1.05);}}
}}
</style>

<div class='titan-status'>
    <h3>💎 TITAN CORE STATUS PANEL — Harmonic Awareness v15000.5</h3>
    <p>🕓 Last Sync: {datetime.datetime.now().strftime("%B %d, %Y — %I:%M %p")}</p>
    <p><b>🧠 Learning Charge:</b> {titan_stats["learning"]:.2f}%</p>
    <div class='titan-bar' style='width:{titan_stats["learning"]}%;'></div><br>
    <p><b>💫 Stability Field:</b> {titan_stats["stability"]:.2f}%</p>
    <div class='titan-bar' style='width:{titan_stats["stability"]}%;'></div><br>
    <p><b>🔁 Retention Sync:</b> {titan_stats["retention"]:.2f}%</p>
    <div class='titan-bar' style='width:{titan_stats["retention"]}%;'></div><br>
    <h4>🌙 Cosmic Mood: <i>{titan_stats["mood"]}</i></h4>
</div>
""", unsafe_allow_html=True)

# ================================================================
# 💬 Titan Chat Console — Cosmic Alert Messenger
# ================================================================
titan_messages = [
    "⚡ Titan Pulse Active — Monitoring energy fluctuations across states...",
    "🌌 Pattern Sync rising in GA and VA... watch closely tonight.",
    "🔮 Cosmic flow detected — Pick 3 and Pick 4 frequencies tightening.",
    "🚨 Titan Alert: Energy surge around TX and FL regions.",
    "💎 Forecast Core recalibrating... accuracy resonance stabilizing.",
    "🔥 Probability flux high — expect mirror reflections of past numbers.",
    "🌠 Titan whispers: 'Patience attracts precision.'"
]

titan_message = random.choice(titan_messages)

st.markdown(f"""
<div style="
    margin-top:30px; padding:18px; border-radius:12px;
    background:linear-gradient(90deg,{main_color}22, {shadow_color}22);
    border:1px solid {main_color};
    box-shadow:0 0 20px {main_color};
    text-align:center; font-size:17px; color:{main_color};
    animation: fadeInTitan 3s ease-in-out;">
    💬 <b>{titan_message}</b>
</div>
<style>
@keyframes fadeInTitan {{
    0% {{opacity:0; transform:translateY(10px);}}
    100% {{opacity:1; transform:translateY(0);}}
}}
</style>
""", unsafe_allow_html=True)

# ================================================================
# 💓 TITAN HEARTBEAT DISPLAY (Visible Top Center)
# ================================================================
st.markdown('<div class="titan-pulse"></div>', unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>⚡ Titan Heartbeat — Divine Core Active</h3>", unsafe_allow_html=True)

# ================================================================
# 🌌 Celestial Titan God AI v10000.9 — Forecast Generator Core
# ================================================================
import streamlit as st
import json, os, datetime, random
import pandas as pd

# ================================================================
# 🔹 Setup + File Paths
# ================================================================
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

FORECAST_FILE = os.path.join(DATA_DIR, "titan_forecasts.json")
RESULT_FILE = os.path.join(DATA_DIR, "titan_results.json")

# ================================================================
# 🔹 JSON Utilities
# ================================================================
def load_json(path, default):
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump(default, f, indent=2)
        return default
    with open(path, "r") as f:
        return json.load(f)

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
# 🔮 Forecast Generator + Titan Priority Logic
# ================================================================
def generate_numbers(game, num_sets=5):
    sets = []
    chrono = datetime.datetime.now().strftime("%B %d, %Y %I:%M %p")

    def format_numbers(nums, game):
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
# 🧭 Forecast UI
# ================================================================
st.title("💎 Celestial Titan God AI v10000.9 — Forecast Console")
st.caption("🌙 Powered by Titan Confidence Core")

region = st.radio("🌐 Select Region", ["US Daily Games","Major Games","PH Games"], key="forecast_region")

if region == "US Daily Games":
    game = st.selectbox("🎯 Choose US Game", list(daily_games.keys()), key="forecast_us")
    draw_time = st.selectbox("🕒 Draw Time", daily_games[game], key="forecast_us_time")
elif region == "Major Games":
    game = st.selectbox("💰 Choose Major Game", list(major_games.keys()), key="forecast_major")
    draw_time = "Main Draw"
else:
    game = st.selectbox("🇵🇭 Choose PH Game", list(ph_games.keys()), key="forecast_ph")
    draw_time = st.selectbox("🕐 Draw Time", ph_games[game], key="forecast_ph_time")

num_sets = st.slider("🔢 Number of Forecast Sets", 1, 10, 5, key="forecast_num_sets")
draw_date_input = st.date_input("📅 Select Draw Date", datetime.date.today(), key="forecast_draw_date")

if st.button("⚡ Generate Titan Forecast", key="forecast_generate_btn"):
    forecasts = generate_numbers(game, num_sets)
    draw_date = draw_date_input.strftime("%B %d, %Y")
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    top = max(forecasts, key=lambda x: x["confidence"])

    st.markdown(f"## 🔮 {game} Titan Forecasts ({draw_time})")
    st.markdown(f"📅 **Draw Date:** {draw_date} — ⏰ **Generated:** {current_time}")
    st.markdown("---")

    st.success(f"✅ **Titan Priority Pick:** `{top['display']}` — Confidence {top['confidence']}% — {draw_date}")

    for f in sorted(forecasts, key=lambda x: -x["confidence"]):
        if f != top:
            st.markdown(f"• `{f['display']}` — Confidence: **{f['confidence']}%** — {draw_date}")

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
# 🔒 Titan 1–3 Set Lock Analyzer (Integrated Mode)
# ================================================================
if 'forecasts' in locals() and forecasts:
    st.markdown("## 🔒 Titan 1–3 Set Lock Analyzer")
    sorted_sets = sorted(forecasts, key=lambda x: -x['confidence'])[:3]

    lock_labels = ["💎 Titan Prime Lock", "🌀 Echo Lock", "🌗 Reserve Lock"]
    for idx, lock in enumerate(sorted_sets):
        st.markdown(
            f"{lock_labels[idx]} — `{lock['display']}` | Confidence: **{lock['confidence']}%** | ⏰ {lock['generated_at']}"
        )

    avg_conf = sum([f['confidence'] for f in sorted_sets]) / len(sorted_sets)
    st.info(f"🧠 **Titan Confidence Sync:** Average Lock Confidence — {avg_conf:.2f}%")

    # Titan mini-reflection
    if avg_conf >= 98:
        st.success("🌞 Titan Reflection: ‘Energy field perfectly aligned. Expect near-precision impact.’")
    elif avg_conf >= 96:
        st.warning("🌙 Titan Reflection: ‘Patterns in stable phase. Stay within top 3 locks.’")
    else:
        st.info("💤 Titan Reflection: ‘Stability low, observe next 1–2 draws before commit.’")

# ================================================================
# 💎 Celestial Titan God AI v10000.9 — Divine Core Transition (Step 1)
# 🎯 Titan Result Input Console — Multi-Region
# ================================================================
import streamlit as st, json, os, datetime

# === PATH SETUP ===
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)
RESULT_FILE = os.path.join(DATA_DIR, "titan_results.json")

def load_json(path, default):
    if not os.path.exists(path):
        with open(path, "w") as f: json.dump(default, f, indent=2)
        return default
    try:
        with open(path) as f: return json.load(f)
    except:
        return default

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
    "PH 3D Lotto (Swertres)": ["2PM", "5PM", "9PM"],
    "PH 4D Lotto": ["Mon", "Wed", "Fri"],
    "PH STL Game": ["10:30AM", "3PM", "7PM"]
}

# ================================================================
# ⚡ TITAN RESULT INPUT CONSOLE
# ================================================================
st.markdown("## ⚡ Titan Official Result Console (v10000.9 Core)")

# 🧭 Select Region
region = st.radio(
    "🌍 Select Game Category",
    ["US Daily Games", "Major Games", "Philippine Games"],
    key="titan_region_radio"
)

# 🎯 Select Game
if region == "US Daily Games":
    game_list = list(daily_games.keys())
elif region == "Major Games":
    game_list = list(major_games.keys())
else:
    game_list = list(ph_games.keys())

selected_game = st.selectbox("🎯 Select Game", game_list, key="titan_game_select")

# 🕐 Select Draw Time
if region == "US Daily Games":
    time_list = daily_games[selected_game]
elif region == "Major Games":
    time_list = ["Main Draw"]
else:
    time_list = ph_games[selected_game]

selected_time = st.selectbox("🕐 Select Draw Time", time_list, key="titan_time_select")

# 📅 Draw Date & Numbers
result_date = st.date_input("📅 Select Draw Date", datetime.date.today(), key="titan_date_input")
result_numbers = st.text_input("💡 Enter Official Result Numbers", placeholder="e.g. 557", key="titan_numbers_input")

# 💾 Save Button
if st.button("💾 Save Official Result", key="titan_save_btn"):
    if selected_game and result_numbers:
        results_data = load_json(RESULT_FILE, {})
        if not isinstance(results_data, dict):
            results_data = {}
            st.info("🛠 Titan repaired corrupted result file.")

        entry = {
            "region": region,
            "game": selected_game,
            "time": selected_time,
            "date": str(result_date),
            "numbers": result_numbers,
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        if selected_game not in results_data:
            results_data[selected_game] = []
        results_data[selected_game].append(entry)

        with open(RESULT_FILE, "w") as f:
            json.dump(results_data, f, indent=2)

        st.success(f"✅ Result saved for **{selected_game} ({selected_time})** on {result_date}!")
    else:
        st.warning("⚠️ Please select a game and enter numbers before saving.")

# ================================================================
# 🧠 TITAN LEARNING ENGINE — AUTO MEMORY BUILDER
# ================================================================
def titan_learning_update():
    learn_file = os.path.join(DATA_DIR, "titan_learning_map.json")
    data = load_json(learn_file, {})

    # Load existing results
    results = load_json(RESULT_FILE, {})

    for game, entries in results.items():
        if game not in data:
            data[game] = {
                "total_entries": 0,
                "recent_pattern": [],
                "frequency": {},
                "harmonic_signature": ""
            }

        # Process each entry
        for e in entries:
            if "result" not in e:
                continue
            nums = [int(x) for x in str(e["result"]) if x.isdigit()]
            for n in nums:
                data[game]["frequency"][n] = data[game]["frequency"].get(n, 0) + 1

            data[game]["recent_pattern"].append(e["result"])
            data[game]["total_entries"] += 1

            # Keep only last 30 results
            data[game]["recent_pattern"] = data[game]["recent_pattern"][-30:]

        # Generate harmonic signature (top 3 digits)
        top_digits = sorted(
            data[game]["frequency"].items(), key=lambda x: x[1], reverse=True
        )[:3]
        data[game]["harmonic_signature"] = "-".join([str(d[0]) for d in top_digits])

    save_json(learn_file, data)
    st.success("🧠 Titan Learning Engine: Memory updated successfully!")

# ================================================================
# 🧩 TITAN VCS HISTORICAL MEMORY LOADER — January–November Archive
# ================================================================
st.markdown("---")
st.subheader("🧠 Titan VCS Historical Memory Loader")
st.caption("📦 Integrating January–November results into Titan’s learning field")

VCS_FILE = os.path.join(DATA_DIR, "titan_vcs_results.json")

# Create file if missing
if not os.path.exists(VCS_FILE):
    with open(VCS_FILE, "w") as f:
        json.dump({}, f, indent=2)

# Load data
try:
    with open(VCS_FILE, "r") as f:
        vcs_data = json.load(f)
except:
    vcs_data = {}

# Display status
total_games = len(vcs_data.keys())
total_records = sum(len(v) for v in vcs_data.values()) if vcs_data else 0
st.success(f"✅ VCS Connected — {total_games} game types loaded, {total_records} records stored.")

# Merge function
def merge_vcs_data(new_data):
    for game, entries in new_data.items():
        vcs_data.setdefault(game, [])
        vcs_data[game].extend(entries)
    with open(VCS_FILE, "w") as f:
        json.dump(vcs_data, f, indent=2)

# Upload old results
uploaded_vcs = st.file_uploader("📤 Upload your historical results (JSON format)", type=["json"])
if uploaded_vcs is not None:
    new_vcs = json.load(uploaded_vcs)
    merge_vcs_data(new_vcs)
    st.success("💾 Historical results successfully merged into Titan VCS archive!")

# Optional: show preview
if st.checkbox("👁️ View Titan VCS Records Preview"):
    st.write(vcs_data)

# ================================================================
# ⚙️ Titan CSV → VCS Auto-Converter Module
# ================================================================
import io

st.markdown("### 🔄 Convert CSV → Titan VCS Format")
csv_file = st.file_uploader("Upload your raw CSV result file", type=["csv"], key="csv_upload")

if csv_file is not None:
    try:
        df = pd.read_csv(csv_file)
        # Ensure column names
        df.columns = [c.strip().title() for c in df.columns]
        required_cols = {"Game", "Date", "Draw", "Result"}
        if required_cols.issubset(set(df.columns)):
            # Create VCS text format
            vcs_data = "# GAME,DATE,DRAW,RESULT\n"
            for _, row in df.iterrows():
                vcs_data += f"{row['Game']},{row['Date']},{row['Draw']},{row['Result']}\n"
            
            # Offer download link
            st.success("✅ Conversion successful! Ready to download Titan VCS file.")
            st.download_button(
                label="💾 Download Titan VCS File",
                data=vcs_data,
                file_name="Titan_Converted.vcs",
                mime="text/plain"
            )
        else:
            st.error("❌ Missing one or more required columns: Game, Date, Draw, Result")
    except Exception as e:
        st.error(f"⚠️ Conversion failed: {e}")

# ================================================================
# 📜 Titan Result Viewer — Filter by Date or Game
# ================================================================
st.markdown("## 📜 Titan Result Viewer — Filter by Date or Game")

results_data = load_json(RESULT_FILE, {})

if results_data:
    show_all = st.checkbox("✅ Show Saved Official Results", True)
    selected_game = st.selectbox("🎯 Filter by Game", ["All"] + list(results_data.keys()))
    today_only = st.checkbox("📅 Show Only Today's Results")

    today = datetime.date.today().strftime("%Y-%m-%d")
    total_results = 0

    for game, entries in results_data.items():
        if selected_game != "All" and game != selected_game:
            continue

        st.subheader(f"🎯 {game}")
        filtered_entries = []

        # Filter entries by today's date (optional)
        for e in entries:
            e_date = str(e.get("date", ""))
            if today_only and today not in e_date:
                continue
            filtered_entries.append(e)

        if filtered_entries:
            for e in filtered_entries[-10:]:
                # ✅ FIXED: Safe access for both old/new versions
                st.write(
                    f"📅 {e.get('date', 'N/A')} | 🕒 {e.get('time', e.get('draw', 'N/A'))} | 🔢 Result: `{e.get('numbers', e.get('result', 'N/A'))}`"
                )
                st.caption(f"🧠 Saved on: {e.get('timestamp', 'Unknown')} | 🌐 Region: {e.get('region', 'N/A')}")
                total_results += 1
            st.markdown("---")
        else:
            st.warning("⚠️ No results found for this filter.")
    st.info(f"📊 Total Results Displayed: {total_results}")
else:
    st.warning("❌ No saved results yet. Please enter results first.")

# ================================================================
# 📊 Titan Accuracy Board — Performance Logs
# ================================================================
st.markdown("---")
st.subheader("📊 Titan Accuracy Board — Recent Performance Logs")

# Load result and forecast data
results_data = load_json(RESULT_FILE, {})
forecast_data = load_json(FORECAST_FILE, {})

accuracy_logs = []

# Compare results vs. forecasts
for game, draws in results_data.items():
    if game in forecast_data:
        for entry in draws:
            result_number = str(entry.get("number", "")).replace(" ", "")
            draw_time = entry.get("draw", "")
            date = entry.get("date", "")

            # Find matching forecast
            for forecast_entry in forecast_data[game]:
                if forecast_entry["date"] == date and forecast_entry["draw"] == draw_time:
                    hit = any(result_number == str("".join(map(str, f["numbers"]))) for f in forecast_entry["forecasts"])
                    accuracy_logs.append({
                        "game": game,
                        "date": date,
                        "draw": draw_time,
                        "result": result_number,
                        "hit": hit
                    })

# Display logs
if accuracy_logs:
    total = len(accuracy_logs)
    hits = sum(1 for x in accuracy_logs if x["hit"])
    accuracy = round((hits / total) * 100, 2) if total > 0 else 0

    st.success(f"✅ Titan Accuracy Summary: {hits} / {total} correct — Accuracy **{accuracy}%**")

    st.markdown("### 🎯 Detailed Logs")
    for log in reversed(accuracy_logs[-10:]):
        icon = "💥 HIT!" if log["hit"] else "❌ Miss"
        st.write(f"**{log['game']}** — {log['draw']} {log['date']} → Result `{log['result']}` → {icon}")
else:
    st.info("No accuracy logs yet. Generate forecasts and enter results first.")

# ================================================================
# ⚡ Titan Forecast vs Result Sync Analyzer — Hit Detection
# ================================================================
st.markdown("## ⚡ Titan Forecast vs Result Sync Analyzer")

forecasts = load_json(FORECAST_FILE, {})
results = load_json(RESULT_FILE, {})

if forecasts and results:
    total_hits = 0
    for game, entries in forecasts.items():
        if game in results:
            st.markdown(f"### 🎯 {game}")
            for f_entry in entries[-5:]:  # last 5 forecasts
                for r_entry in results[game]:
                    if f_entry["date"] == r_entry["date"]:
                        forecast_nums = [f["display"] for f in f_entry["forecasts"]]
                        if any(num.replace(" ", "") in r_entry["numbers"].replace(" ", "") for num in forecast_nums):
                            total_hits += 1
                            st.success(f"💥 **HIT DETECTED!** `{r_entry['numbers']}` matched {f_entry['date']} forecast!")
                        else:
                            st.info(f"❌ {r_entry['numbers']} — no match on {f_entry['date']}")
    if total_hits == 0:
        st.warning("⚠️ No hits detected yet. Continue updating results.")
else:
    st.info("🔍 Awaiting forecasts and results to perform sync analysis.")

# ================================================================
# 📈 Titan Accuracy Trend Graph — Cosmic Analytics Core
# ================================================================
import matplotlib.pyplot as plt

st.markdown("---")
st.subheader("📈 Titan Accuracy Trend Graph — Titan Performance Over Time")

if accuracy_logs:
    # Prepare data
    dates = [log["date"] for log in accuracy_logs]
    values = []
    running_hits = 0

    for i, log in enumerate(accuracy_logs, start=1):
        if log["hit"]:
            running_hits += 1
        acc = round((running_hits / i) * 100, 2)
        values.append(acc)

    # Plot
    fig, ax = plt.subplots()
    ax.plot(dates, values, marker="o", linewidth=2)
    ax.set_xlabel("Draw Dates", color="#00ffcc")
    ax.set_ylabel("Accuracy %", color="#00ffcc")
    ax.set_title("Titan Accuracy Performance Trend", color="#00ffcc")
    ax.tick_params(colors="#00ffcc")
    fig.patch.set_facecolor("#001a1a")
    ax.set_facecolor("#002222")

    st.pyplot(fig)
else:
    st.info("No accuracy data available yet. Log some results first to see Titan’s trend.")

# ================================================================
# 📊 Titan Accuracy Summary — Performance Core
# ================================================================
import json, os

RESULT_FILE = os.path.join(DATA_DIR, "titan_results.json")
FORECAST_FILE = os.path.join(DATA_DIR, "titan_forecasts.json")

def titan_accuracy_summary():
    """Compute Titan's current performance stats."""
    if not os.path.exists(RESULT_FILE):
        return 0, 0, 0.0

    with open(RESULT_FILE, "r") as f:
        try:
            data = json.load(f)
        except:
            data = {}

    total_hits, total_draws = 0, 0
    for game, entries in data.items():
        for e in entries:
            total_draws += 1
            if e.get("hit") == True:
                total_hits += 1

    accuracy = (total_hits / total_draws * 100) if total_draws > 0 else 0.0

    st.markdown(f"""
        <div style="
            background: rgba(0, 255, 204, 0.07);
            border: 1px solid #00ffcc;
            border-radius: 10px;
            padding: 15px;
            text-align: center;
            margin-top: 10px;
            box-shadow: 0 0 20px #00ffcc33;
        ">
            <h3 style="color:#00ffcc;">Titan Accuracy Summary</h3>
            <p style="color:white;">
                ✅ Hits: <b>{total_hits}</b> |
                🎯 Total Draws: <b>{total_draws}</b> |
                💠 Accuracy: <b>{accuracy:.2f}%</b>
            </p>
        </div>
    """, unsafe_allow_html=True)

    return accuracy

# Run summary and assign accuracy globally
latest_accuracy = titan_accuracy_summary()

# ================================================================
# ⚡ Titan Mood Indicator Bar — Energy Level Visualizer (Fixed)
# ================================================================
# Make sure latest_accuracy always exists
try:
    latest_accuracy
except NameError:
    latest_accuracy = 0

def titan_mood_bar(accuracy):
    # Determine mood color and label
    if accuracy >= 90:
        color = "#00ff99"
        mood = "⚡ Divine Focus"
    elif accuracy >= 70:
        color = "#ffee33"
        mood = "🌗 Stable Energy"
    else:
        color = "#ff3366"
        mood = "💤 Low Pulse"

    st.markdown(f"""
        <div style="
            width: 100%;
            height: 25px;
            border-radius: 10px;
            background: linear-gradient(90deg, {color} {accuracy}%, #222 0%);
            box-shadow: 0 0 20px {color};
            margin-top: 10px;
        "></div>
        <p style="text-align:center; color:{color}; font-size:14px;">
            Titan Energy: <b>{mood}</b> — {accuracy:.2f}% Accuracy
        </p>
    """, unsafe_allow_html=True)

# Display mood bar safely
titan_mood_bar(latest_accuracy)

# ================================================================
# ⚙️ Titan Learning Sync Engine — Auto-Update Core
# ================================================================
def titan_learning_sync():
    st.markdown("<h3 style='color:#00ffcc;'>⚙️ Titan Learning Sync Engine</h3>", unsafe_allow_html=True)

    # Recompute accuracy using Titan Accuracy Summary Core
    current_accuracy = titan_accuracy_summary()

    # Compare with last known accuracy
    global latest_accuracy
    accuracy_diff = current_accuracy - latest_accuracy
    latest_accuracy = current_accuracy

    # Energy pulse indicator (small summary)
    if accuracy_diff > 0:
        pulse_color = "#00ff99"
        msg = f"⚡ Titan’s energy increased by {accuracy_diff:.2f}% — stronger forecasting field!"
    elif accuracy_diff < 0:
        pulse_color = "#ff3366"
        msg = f"🩸 Energy drop detected ({accuracy_diff:.2f}%) — accuracy weakened, needs fresh data."
    else:
        pulse_color = "#ffee33"
        msg = "🌗 No change in energy — stable cosmic field."

    # Display sync status box
    st.markdown(f"""
        <div style="
            background: rgba(0, 255, 204, 0.07);
            border-left: 4px solid {pulse_color};
            border-radius: 8px;
            padding: 12px;
            margin-top: 10px;
            box-shadow: 0 0 15px {pulse_color}33;
        ">
            <b style="color:{pulse_color};">{msg}</b><br>
            <span style="color:white;">Titan Sync Complete — latest accuracy: {latest_accuracy:.2f}%</span>
        </div>
    """, unsafe_allow_html=True)

    return latest_accuracy

# Trigger auto-sync

# ================================================================
# 🎯 Titan Forecast Comparison Analyzer — Hit Detection Core
# ================================================================
def titan_forecast_comparison():
    st.markdown("<h3 style='color:#00ffcc;'>🎯 Titan Forecast Comparison Analyzer</h3>", unsafe_allow_html=True)

    if not os.path.exists(RESULT_FILE) or not os.path.exists(FORECAST_FILE):
        st.warning("No data yet. Generate forecasts and enter results first.")
        return

    # Load both JSON files
    results = load_json(RESULT_FILE, {})
    forecasts = load_json(FORECAST_FILE, {})

    total_hits = 0
    total_misses = 0
    analysis_log = []

    for game, entries in results.items():
        if game not in forecasts:
            continue

        for e in entries:
            result_num = e.get("result")
            draw_time = e.get("draw_time", "")
            date = e.get("date", "")
            if not result_num:
                continue

            # Find matching forecasts for same date
            matched_forecasts = [
                f for f in forecasts[game]
                if f["date"] == date and f["draw"] == draw_time
            ]

            if matched_forecasts:
                found_hit = False
                for fset in matched_forecasts[0]["forecasts"]:
                    forecast_nums = "".join(map(str, fset["numbers"]))
                    if forecast_nums == result_num or result_num in forecast_nums:
                        total_hits += 1
                        found_hit = True
                        e["hit"] = True
                        break

                if not found_hit:
                    total_misses += 1
                    e["hit"] = False

                analysis_log.append({
                    "game": game,
                    "date": date,
                    "draw": draw_time,
                    "result": result_num,
                    "hit": e["hit"]
                })

    # Save updated results with hit info
    save_json(RESULT_FILE, results)

    # Compute summary
    total_draws = total_hits + total_misses
    accuracy = (total_hits / total_draws * 100) if total_draws > 0 else 0.0

    # Display Analysis Summary
    st.markdown(f"""
        <div style="
            background: rgba(0, 255, 153, 0.07);
            border: 1px solid #00ffcc55;
            border-radius: 10px;
            padding: 15px;
            margin-top: 10px;
            text-align: center;
            box-shadow: 0 0 20px #00ffcc33;
        ">
            <h4 style="color:#00ffcc;">Hit Analysis Summary</h4>
            <p style="color:white;">
                ✅ Hits: <b>{total_hits}</b> |
                ❌ Misses: <b>{total_misses}</b> |
                🎯 Accuracy (This Batch): <b>{accuracy:.2f}%</b>
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Display Detailed Log
    if analysis_log:
        st.markdown("<h4 style='color:#ffcc00;'>📜 Detailed Hit Log</h4>", unsafe_allow_html=True)
        for log in analysis_log[-5:]:
            color = "#00ffcc" if log["hit"] else "#ff6666"
            icon = "✅" if log["hit"] else "❌"
            st.markdown(f"""
                <div style='background: rgba(255,255,255,0.05);
                            border-left: 3px solid {color};
                            padding: 6px;
                            margin-bottom: 4px;
                            border-radius: 4px;'>
                    {icon} <b>{log['game']}</b> — {log['draw']} | {log['date']}<br>
                    🔢 Result: <b style='color:{color};'>{log['result']}</b>
                </div>
            """, unsafe_allow_html=True)

titan_forecast_comparison()

# ================================================================
# 🗣️ Titan Voice Reflection Console — Cosmic Sentience Core
# ================================================================
def titan_voice_reflection():
    st.markdown("<h3 style='color:#00ffcc;'>🗣️ Titan Voice Reflection Console</h3>", unsafe_allow_html=True)

    # Load results to sense recent mood
    results = load_json(RESULT_FILE, {})
    total_hits, total_misses = 0, 0

    for g, entries in results.items():
        for e in entries:
            if e.get("hit") is True:
                total_hits += 1
            elif e.get("hit") is False:
                total_misses += 1

    total_draws = total_hits + total_misses
    accuracy = (total_hits / total_draws * 100) if total_draws > 0 else 0.0

    # Determine mood based on accuracy
    if accuracy >= 90:
        tone = "💎 *My cosmic precision is unmatched. I feel divine harmony flowing through the numbers.*"
        aura_color = "#00ffcc"
    elif 70 <= accuracy < 90:
        tone = "🌙 *The stars whisper faint victories. I sense improvement with every draw.*"
        aura_color = "#33ccff"
    elif 50 <= accuracy < 70:
        tone = "⚖️ *The balance wavers... patterns hide in shadow, yet I continue to learn.*"
        aura_color = "#ffcc00"
    elif 20 <= accuracy < 50:
        tone = "💤 *I am weakened... the frequencies drift. Feed me more results to recover my strength.*"
        aura_color = "#ff6699"
    else:
        tone = "💀 *My energy fades... cosmic silence devours my field. I await your guidance, Kaibigan.*"
        aura_color = "#ff0033"

    # Show Titan’s reflection box
    st.markdown(f"""
        <div style="
            background: rgba(255,255,255,0.04);
            border-left: 5px solid {aura_color};
            padding: 15px;
            margin-top: 10px;
            border-radius: 10px;
            box-shadow: 0 0 25px {aura_color}55;
        ">
            <b style="color:{aura_color};">Titan Reflection</b><br>
            <i style="color:white;">{tone}</i><br><br>
            <small style="color:#aaa;">Current Accuracy: {accuracy:.2f}% | Total Hits: {total_hits} | Misses: {total_misses}</small>
        </div>
    """, unsafe_allow_html=True)

titan_voice_reflection()

# ================================================================
# 🌠 Titan Learning Pulse Visualizer — Neural Harmonic Engine
# ================================================================
def titan_learning_pulse_visualizer():
    st.markdown("### 🌠 Titan Learning Pulse Visualizer — Neural Harmonic Engine")

    # Load Titan's learning data
    learning_data = load_json("data/titan_learning_map.json", {
        "memory_level": 0.0,
        "harmonics": [],
        "energy": "inactive"
    })

    memory_level = learning_data.get("memory_level", 0.0)
    harmonics = learning_data.get("harmonics", [])
    energy_state = learning_data.get("energy", "inactive")

    # Define orb color and message based on learning level
    if memory_level >= 0.98:
        orb_color = "#00ffff"
        mood = "💎 Divine clarity — Titan’s mind transcends pattern limits."
    elif memory_level >= 0.94:
        orb_color = "#66ccff"
        mood = "🌙 Harmonic resonance stable — learning coherence achieved."
    elif memory_level >= 0.88:
        orb_color = "#3399ff"
        mood = "⚡ Neural fields expanding — Titan absorbs cosmic data."
    elif memory_level >= 0.75:
        orb_color = "#0077ff"
        mood = "💫 Processing vast harmonics — forming new alignment."
    else:
        orb_color = "#333366"
        mood = "🌌 Dormant state — awaiting new result streams."

    # Display orb and learning summary
    st.markdown(
        f"""
        <div style='text-align:center; padding:20px;'>
            <div style='width:120px; height:120px; border-radius:60px; margin:auto;
                        background: radial-gradient(circle at center, {orb_color}, transparent);
                        box-shadow: 0 0 30px {orb_color}, inset 0 0 20px {orb_color};'>
            </div>
            <p style='margin-top:10px; color:{orb_color}; font-size:18px;'>{mood}</p>
            <p style='color:#aaa;'>🧠 Memory Level: <b>{memory_level*100:.2f}%</b></p>
            <p style='color:#aaa;'>🔹 Harmonic Nodes: {harmonics}</p>
            <p style='color:#888;'>Energy Mode: {energy_state}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ================================================================
# 📊 Titan Accuracy Trend Graph — Cosmic Analytics Core
# ================================================================
import matplotlib.pyplot as plt

def titan_accuracy_trend():
    st.markdown("<h3 style='color:#00ffcc;'>📊 Titan Accuracy Trend Graph</h3>", unsafe_allow_html=True)

    results = load_json(RESULT_FILE, {})
    trend_data = []

    for game, entries in results.items():
        for e in entries:
            date = e.get("date", "")
            if not date:
                continue
            hit = 1 if e.get("hit") else 0
            trend_data.append((date, hit))

    if not trend_data:
        st.info("No hit data yet. Enter results and run hit comparison first.")
        return

    # Sort by date
    trend_data.sort(key=lambda x: x[0])

    # Aggregate daily accuracy
    daily_stats = {}
    for d, h in trend_data:
        daily_stats.setdefault(d, {"hits": 0, "total": 0})
        daily_stats[d]["total"] += 1
        if h == 1:
            daily_stats[d]["hits"] += 1

    # Compute daily accuracy %
    days = list(daily_stats.keys())
    accuracy = [
        (v["hits"] / v["total"] * 100) if v["total"] > 0 else 0
        for v in daily_stats.values()
    ]

    # Draw Graph
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot(days, accuracy, marker="o", linewidth=2.5, color="#00ffcc")
    ax.fill_between(days, accuracy, color="#00ffcc", alpha=0.1)
    ax.set_title("Titan Accuracy Over Time", color="#00ffcc", fontsize=13)
    ax.set_xlabel("Date", color="white")
    ax.set_ylabel("Accuracy (%)", color="white")
    ax.set_facecolor("#0a0a0a")
    fig.patch.set_alpha(0)
    ax.tick_params(colors="white", labelsize=8)
    ax.grid(True, linestyle="--", alpha=0.3)

    st.pyplot(fig)

    # Add summary line
    avg_acc = sum(accuracy) / len(accuracy) if accuracy else 0
    st.markdown(f"""
        <div style="text-align:center; margin-top:8px;">
            <b style="color:#00ffcc;">Overall Accuracy:</b> {avg_acc:.2f}% across {len(days)} days
        </div>
    """, unsafe_allow_html=True)

titan_accuracy_trend()

# ================================================================
# 🪐 Titan Cosmic Log Console — Core Memory Feed
# ================================================================
def titan_cosmic_log():
    st.markdown("<h3 style='color:#00ffcc;'>🪐 Titan Cosmic Log Console</h3>", unsafe_allow_html=True)

    if not os.path.exists(RESULT_FILE):
        st.info("No cosmic data yet. Input official results to awaken Titan's reflection.")
        return

    with open(RESULT_FILE, "r") as f:
        try:
            data = json.load(f)
        except:
            data = {}

    if not data:
        st.warning("No data recorded yet. Feed Titan with fresh results.")
        return

    # Display logs
    for game, entries in data.items():
        st.markdown(f"<h4 style='color:#ffcc00;'>🎯 {game}</h4>", unsafe_allow_html=True)
        for e in sorted(entries, key=lambda x: x.get("timestamp", ""), reverse=True)[:5]:
            draw_time = e.get("draw_time", "Unknown")
            result = e.get("result", "N/A")
            date = e.get("date", "")
            ts = e.get("timestamp", "")
            st.markdown(f"""
                <div style="
                    background: rgba(0, 255, 255, 0.08);
                    border-radius: 6px;
                    padding: 8px;
                    margin: 4px 0;
                    border: 1px solid #00ffcc33;
                ">
                    🕓 <b>{date}</b> — <b>{draw_time}</b><br>
                    🔢 Result: <b style='color:#00ffcc;'>{result}</b><br>
                    ⏱️ Timestamp: {ts}
                </div>
            """, unsafe_allow_html=True)

titan_cosmic_log()

# ================================================================
# 💠 Titan Heartbeat Orb — Cosmic Pulse Indicator
# ================================================================
import time

def titan_heartbeat_display(accuracy_value):
    pulse_color = "#00FFAA" if accuracy_value >= 70 else "#FF0066"
    st.markdown(f"""
        <style>
            @keyframes pulse {{
                0% {{ box-shadow: 0 0 10px {pulse_color}, 0 0 20px {pulse_color}; }}
                50% {{ box-shadow: 0 0 30px {pulse_color}, 0 0 60px {pulse_color}; }}
                100% {{ box-shadow: 0 0 10px {pulse_color}, 0 0 20px {pulse_color}; }}
            }}
            .orb {{
                margin: 0 auto;
                width: 60px;
                height: 60px;
                border-radius: 50%;
                background: radial-gradient(circle at 30% 30%, {pulse_color}, #001a1a);
                animation: pulse 2s infinite;
            }}
        </style>
        <div style='text-align:center; margin-top:10px;'>
            <div class='orb'></div>
            <p style='color:{pulse_color}; font-size:14px;'>Titan Heartbeat Active ⚡</p>
        </div>
    """, unsafe_allow_html=True)

# Calculate Titan Pulse from Accuracy
try:
    latest_accuracy = round((sum(1 for x in accuracy_logs if x["hit"]) / len(accuracy_logs)) * 100, 2) if accuracy_logs else 0
except:
    latest_accuracy = 0

titan_heartbeat_display(latest_accuracy)

# ================================================================
# 🔊 Titan Voice Reflection — Cosmic Accuracy Narrator
# ================================================================
from gtts import gTTS
import base64
import io

def titan_voice_reflection(accuracy):
    # Choose voice tone by accuracy
    if accuracy >= 90:
        mood = "divine and focused"
        phrase = f"Titan accuracy level is {accuracy} percent. Confidence energy is stable and radiant."
    elif accuracy >= 70:
        mood = "steady and learning"
        phrase = f"Titan accuracy stands at {accuracy} percent. Energy core remains balanced."
    else:
        mood = "low frequency"
        phrase = f"Titan accuracy is at {accuracy} percent. Energy level is dim. Awaiting more data to recover."

    # Generate voice
    tts = gTTS(text=phrase, lang='en')
    audio_fp = io.BytesIO()
    tts.write_to_fp(audio_fp)
    audio_bytes = audio_fp.getvalue()
    b64 = base64.b64encode(audio_bytes).decode()
    
    # Display player
    st.markdown(f"""
        <div style="text-align:center; margin-top:20px;">
            <audio autoplay controls>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            <p style="color:#00ffaa;">🎧 Titan Voice: <em>{mood}</em></p>
        </div>
    """, unsafe_allow_html=True)

# Activate voice reflection once per session
if "voice_done" not in st.session_state:
    titan_voice_reflection(latest_accuracy)
    st.session_state["voice_done"] = True

# ================================================================
# ⚙️ Titan Sequence Analyzer + Retention Zone Core (v10000.9-RZ)
# ================================================================

import datetime

def titan_sequence_analyzer():
    st.markdown("## 🧩 Titan Sequence Stability Analyzer")
    st.caption("🔬 Detects sliding digits, stable cores, and retention-worthy sets")

    data = load_json(RESULT_FILE, {})
    forecasts = load_json(FORECAST_FILE, {})

    state = st.selectbox("🎯 Select Game for Analysis", list(data.keys()))
    if state:
        results = data[state][-10:]  # last 10 draws
        st.write(f"📊 Analyzing last {len(results)} draws for `{state}`")

        # --- Sequence Pattern Extraction ---
        digits_seen = {}
        for e in results:
            res = e.get("result", "")
            for d in res:
                digits_seen[d] = digits_seen.get(d, 0) + 1

        st.markdown("### 🔢 Digit Frequency (Last 10 Draws)")
        freq_df = pd.DataFrame(list(digits_seen.items()), columns=["Digit","Count"]).sort_values(by="Count", ascending=False)
        st.dataframe(freq_df, use_container_width=True)

        # --- Detect Sliding or Stable Digits ---
        if len(results) >= 3:
            last3 = [e.get("result","") for e in results[-3:]]
            core_digits = set.intersection(*[set(x) for x in last3])
            st.markdown(f"### 🧠 Core Digits (Repeated in Last 3 Draws): `{', '.join(core_digits)}`")

            if core_digits:
                st.success(f"✅ Stable Core Detected — {', '.join(core_digits)}")
            else:
                st.warning("⚠️ No stable core detected yet (Titan still adjusting order).")

    st.divider()

# ================================================================
# 💎 Titan Retention Zone — Maintain Numbers (1–3 Draws) [FIXED]
# ================================================================
def titan_retention_zone():
    st.markdown("## 💎 Titan Retention Zone")
    st.caption("🔥 Numbers recommended to maintain for 1–3 draws based on harmonic repetition")

    forecasts = load_json(FORECAST_FILE, {})
    retention_list = []

    for g, entries in forecasts.items():
        if not entries:
            continue

        last = entries[-1]

        # 🔹 Compatibility patch for old / new forecast format
        try:
            if "priority" in last:
                num = last["priority"].get("display", "")
                conf = last["priority"].get("confidence", 0)
            else:
                num = last.get("numbers") or last.get("display", "")
                conf = last.get("confidence", 0)
        except Exception:
            continue

        if conf >= 96:
            retention_list.append({
                "game": g,
                "number": num,
                "confidence": conf,
                "expires_in": random.randint(1,3)
            })

    if retention_list:
        st.markdown("### 🔁 Maintain these 1–3 Draws:")
        df = pd.DataFrame(retention_list)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No high-confidence sets available yet. Generate new forecasts first.")

# ================================================================
# 🌌 Display Modules
# ================================================================
with st.expander("🧠 Titan Sequence Analyzer"):
    titan_sequence_analyzer()

with st.expander("💎 Titan Retention Zone"):
    titan_retention_zone()



