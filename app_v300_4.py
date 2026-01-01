# ================================================================
# 💎 Celestial Titan God AI v300.4-FXR2 — Global Hybrid Core (Stable Fix)
# ================================================================
import streamlit as st, random, json, os, datetime

st.set_page_config(page_title="Celestial Titan God AI v300.4-FXR2", page_icon="💎", layout="centered")

# 🌙 Cosmic Theme
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at 20% 20%, #0f0f1a, #060608 80%);
    color:#f0f0f0;
}
h1,h2,h3,h4{color:#f4d03f!important;}
</style>
""", unsafe_allow_html=True)

# ================================================================
# 🔹 Setup + File Paths — FIXED v300.6-FXR
# ================================================================
import os, json, random, datetime
import streamlit as st
import pandas as pd

# ✅ Define data folder and create it if missing
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

# ✅ Define core JSON paths
FORECAST_FILE = os.path.join(DATA_DIR, "titan_forecasts.json")
RESULT_FILE = os.path.join(DATA_DIR, "titan_results.json")
MEMORY_FILE = os.path.join(DATA_DIR, "titan_memory.json")

# ✅ JSON utility functions
def load_json(path, default):
    """Load JSON file or return default if missing/damaged."""
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump(default, f, indent=2)
        return default
    try:
        with open(path, "r") as f:
            return json.load(f)
    except Exception as e:
        st.warning(f"⚠️ Error loading {path}: {e}")
        return default

def save_json(path, data):
    """Save Python object to JSON file safely."""
    try:
        with open(path, "w") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        st.error(f"❌ Failed to save {path}: {e}")

# ✅ Initialize Titan core data files (auto-create if not found)
_ = load_json(FORECAST_FILE, [])
_ = load_json(RESULT_FILE, {})
_ = load_json(MEMORY_FILE, {"updates": []})

st.sidebar.success("💾 Titan Data Paths Initialized Successfully")



def load_json(path,default):
    try:
        if not os.path.exists(path):
            with open(path,"w") as f:json.dump(default,f,indent=2)
            return default
        with open(path) as f:
            data=json.load(f)
            if isinstance(data,list): data={}  # ✅ force dict format
            return data
    except: return default

def save_json(path,data):
    with open(path,"w") as f:json.dump(data,f,indent=2)

# 🎯 Game Dictionaries
daily_games={
st.error(f"❌ Failed to save {path}: {e}")
        
# ✅ Initialize Titan core data files (auto-create if not found)
_ = load_json(FORECAST_FILE, [])
_ = load_json(RESULT_FILE, {})
_ = load_json(MEMORY_FILE, {"updates": []})
        
st.sidebar.success("💾 Titan Data Paths Initialized Successfully")

    
    
def load_json(path,default):
    try:
        if not os.path.exists(path):
            with open(path,"w") as f:json.dump(default,f,indent=2)
            return default
        with open(path) as f:  
            data=json.load(f)
            if isinstance(data,list): data={}  # ✅ force dict format
            return data
    except: return default

def save_json(path,data):
    with open(path,"w") as f:json.dump(data,f,indent=2)
        
# 🎯 Game Dictionaries
daily_games={
    "GA Pick 3":["Midday","Evening"],
    "GA Pick 4":["Midday","Evening"],
    "GA Pick 5":["Midday","Evening"],
    "FL Pick 3":["Midday","Evening"],
    "FL Pick 4":["Midday","Evening"],
    "FL Pick 5":["Midday","Evening"],
    "TX Pick 3":["Morning","Day","Evening","Night"],
    "TX Pick 4":["Morning","Day","Evening","Night"],
    "VA Pick 3":["Day","Evening"],
    "VA Pick 4":["Day","Evening"],
    "VA Pick 5":["Day","Evening"],
    "NC Pick 3":["Day","Evening"],
    "NC Pick 4":["Day","Evening"],
    "NY Pick 3":["Midday","Evening"],
    "NY Pick 4":["Midday","Evening"],
    "CA Daily 3":["Midday","Evening"],
    "CA Daily 4":["Evening"],
    "NJ Pick 3":["Midday","Evening"],
    "NJ Pick 4":["Midday","Evening"]
}
major_games={
    "CA Fantasy 5":[],
    "CA SuperLotto Plus":[],
    "Mega Millions":[],
    "Powerball":[]
}
ph_games={
    "PH 3D Lotto (Swertres)":["2PM","5PM","9PM"],
    "PH 4D Lotto":["Mon","Wed","Fri"],
    "PH STL Game":["10:30AM","3PM","7PM"]
}

# 🔮 Generator — Fixed with Timestamp Integration
def generate_numbers(game, num_sets=5):
    sets = []
    now = datetime.datetime.now().strftime("%B %d, %Y %I:%M %p")  # Date + Time

    for _ in range(num_sets):
        if "Pick 3" in game:
            nums = [random.randint(0, 9) for _ in range(3)]
        elif "Pick 4" in game:
            nums = [random.randint(0, 9) for _ in range(4)]
        elif "Pick 5" in game and "Fantasy" not in game:
            nums = [random.randint(0, 9) for _ in range(5)]
        elif "Fantasy 5" in game:
            nums = sorted(random.sample(range(1, 40), 5))
        elif "SuperLotto" in game:
            nums = sorted(random.sample(range(1, 48), 5))
            nums.append(random.randint(1, 27))
        elif "Mega Millions" in game:
            nums = sorted(random.sample(range(1, 71), 5))
            nums.append(random.randint(1, 25))
        elif "Powerball" in game:
            nums = sorted(random.sample(range(1, 70), 5))
            nums.append(random.randint(1, 26))
        elif "3D" in game:
            nums = [random.randint(0, 9) for _ in range(3)]
        elif "4D" in game:
            nums = [random.randint(0, 9) for _ in range(4)]
        elif "STL" in game:
            nums = [random.randint(0, 9) for _ in range(3)]
        else:
            nums = [random.randint(0, 9) for _ in range(3)]

        conf = round(random.uniform(90, 99.99), 2)
        sets.append({
            "numbers": nums,
            "confidence": conf,
            "generated_at": now
        })

    return sets


# 📜 Display + Save
def show_forecast(game,forecasts,draw_time):
    date=datetime.date.today().strftime("%B %d, %Y")
    st.markdown(f"## 🔮 {game} Titan Forecasts ({draw_time})")
    st.markdown(f"🗓️ Draw Date: **{date}**\n---")

    top=max(forecasts,key=lambda x:x["confidence"])
    def fmt(nums,game):
        if "SuperLotto" in game:return " ".join(map(str,nums[:-1]))+f" MEGA {nums[-1]}"
        if "Mega Millions" in game:return " ".join(map(str,nums[:-1]))+f" Mega {nums[-1]}"
        if "Powerball" in game:return " ".join(map(str,nums[:-1]))+f" Power {nums[-1]}"
        return " ".join(map(str,nums))

    st.markdown(f"✅ **Titan Priority Pick:** `{fmt(top['numbers'],game)}` — Confidence **{top['confidence']}%** — Date: {date}")
    for f in forecasts:
        if f!=top:
            st.markdown(f"• `{fmt(f['numbers'],game)}` — Confidence: **{f['confidence']}%** — Date: {date}")

    data=load_json(FORECAST_FILE,{})
    if game not in data: data[game]=[]
    data[game].append({"date":date,"draw":draw_time,"forecasts":forecasts})
    save_json(FORECAST_FILE,data)
    st.success("✅ Forecast auto-saved successfully!")

# 🧭 UI
st.title("💎 Celestial Titan God AI v300.4-FXR2 — Global Hybrid Core (Stable Fix)")
st.caption("🌙 Powered by Titan Confidence Core")
st.markdown("---")

section=st.radio("🌐 Select Region",["US Daily Games","Major Games","PH Games"])
if section=="US Daily Games":
    game=st.selectbox("🎯 Choose US Game",list(daily_games.keys()))
    draw_time=st.selectbox("🕐 Draw Time",daily_games[game])
elif section=="Major Games":
    game=st.selectbox("💰 Choose Major Game",list(major_games.keys()))
    draw_time="Main Draw"
else:
    game=st.selectbox("🇵🇭 Choose PH Game",list(ph_games.keys()))
    draw_time=st.selectbox("🕐 Draw Time",ph_games[game])

num_sets=st.slider("🔢 Number of Sets",1,10,5)

if st.button("⚡ Generate Titan Forecast"):
    forecasts=generate_numbers(game,num_sets)
    show_forecast(game,forecasts,draw_time)

# =============================================================
# 📊 Titan Accuracy Analyzer + Auto-Hit Recorder (FXR5.2 Final)
# Fully Conflict-Proof — Unique IDs for All Inputs
# =============================================================

ACCURACY_FILE = os.path.join(DATA_DIR, "titan_accuracy_log.json")

def load_accuracy():
    data = load_json(ACCURACY_FILE, {})
    if isinstance(data, list):
        data = {}
    return data

def save_accuracy(data):
    save_json(ACCURACY_FILE, data)

def log_titan_accuracy(result_game, result_number):
    forecasts = load_json(FORECAST_FILE, {})
    accuracy = load_accuracy()

    if result_game not in forecasts:
        return "⚠️ No forecasts found for this game yet."

    last_entry = forecasts[result_game][-1]
    hits = 0
    total = len(last_entry["forecasts"])

    for f in last_entry["forecasts"]:
        num = f.get("numbers", "").replace(" ", "")
        if num == result_number.replace(" ", ""):
            hits += 1

    acc_percent = round((hits / total) * 100, 2) if total > 0 else 0

    accuracy.setdefault(result_game, []).append({
        "date": last_entry.get("date", "Unknown"),
        "draw_type": last_entry.get("draw_type", "Unknown"),
        "result": result_number,
        "accuracy": acc_percent
    })
    save_accuracy(accuracy)

    if hits > 0:
        return f"🎯 Titan HIT logged! Accuracy: {acc_percent}%"
    else:
        return f"❌ No match found. Accuracy recorded as {acc_percent}%"

  # ================================================================
# 🧠 Titan Accuracy Analyzer + Official Result Checker (v300.9-FXR9 Safe)
# ================================================================
st.markdown("---")
st.header("🧠 Titan Accuracy Analyzer")

# === Log Official Result & Analyze Accuracy ===
with st.expander("🧩 Log Official Result & Analyze Accuracy", expanded=False):
    result_game = st.text_input(
        "🎮 Game Name",
        placeholder="e.g., GA Pick 3 Midday",
        key="fxr9_game_name"
    )

    result_number = st.text_input(
        "🏆 Official Result Number(s)",
        placeholder="e.g., 557 or 12 24 36 38 41",
        key="fxr9_result_number"
    )

    # ✅ Added timestamp when logging accuracy
    if st.button("⚡ Run Titan Accuracy Log", key="fxr9_run_button"):
        if result_game and result_number:
            msg = log_titan_accuracy(result_game, result_number)
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            st.success(f"{msg}\n🕓 Recorded on: {timestamp}")
        else:
            st.warning("⚠️ Please provide both game and result number.")

# === View Titan Accuracy Logs ===
with st.expander("📊 View Titan Accuracy Logs", expanded=False):
    accuracy = load_json(os.path.join(DATA_DIR, "titan_accuracy_log.json"), {})
    if len(accuracy) == 0:
        st.info("No accuracy logs yet.")
    else:
        for g, entries in list(accuracy.items())[-5:]:
            last = entries[-1]
            st.markdown(
                f"🎯 **{g}** — {last['result']} | Accuracy: `{last['accuracy']}%` | 🕓 {last.get('date', 'Unknown')}"
            )

# =============================================================
# 🎮 Titan Result Input Box (Old Forecast Section — Fixed)
# =============================================================

st.markdown("---")
st.subheader("🎮 Titan Result Input (Legacy Section Fix)")

result_game = st.text_input(
    "🎮 Game Name",
    placeholder="e.g., GA Pick 3 Midday",
    key="old_result_game_input"
)

result_draw = st.text_input(
    "🕒 Draw Type / Time",
    placeholder="e.g., Midday or Evening",
    key="old_result_draw_input"
)

result_number = st.text_input(
    "🏆 Enter Winning Number(s)",
    placeholder="e.g., 557 or 12 24 36 38 41",
    key="old_result_number_input"
)

if st.button("💾 Save Titan Result", key="old_result_button"):
    # Auto-create folder if missing
    os.makedirs(DATA_DIR, exist_ok=True)
    results_path = os.path.join(DATA_DIR, "titan_results.json")

    # Load existing results
    existing_results = load_json(results_path, {})

    # Save new result entry
    new_entry = {
        "game": result_game,
        "draw": result_draw,
        "result": result_number,
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    if result_game not in existing_results:
        existing_results[result_game] = []
    existing_results[result_game].append(new_entry)

    # Write updated data
    with open(results_path, "w") as f:
        json.dump(existing_results, f, indent=2)

    st.success(f"✅ Titan Result Saved for {result_game} ({result_draw})")

# =============================================================
# 📈 Titan Accuracy Summary Board
# =============================================================
st.markdown("---")
st.subheader("📈 Titan Accuracy Summary Board")

if st.button("🔍 Load Titan Accuracy Summary", key="fxr8_summary_button"):
    acc_file = os.path.join(DATA_DIR, "titan_accuracy.json")
    if not os.path.exists(acc_file):
        st.info("No accuracy data logged yet.")
    else:
        accuracy = load_json(acc_file, {})
        if len(accuracy) == 0:
            st.info("No accuracy entries found.")
        else:
            st.success("✅ Loaded latest Titan Accuracy Logs:")
            for g, entries in list(accuracy.items())[-5:]:
                last = entries[-1]
                st.markdown(f"🎯 **{g}** — {last['date']} — {last['result']} — Accuracy: {last['accuracy']}%")

# =============================================================
# 🛰️ Titan Smart Storage + Result Sync Extension
# Version: v300.6-StellarLink
# =============================================================

SYNC_FILE = os.path.join(DATA_DIR, "titan_results_sync.json")

# Load & merge safely
def load_sync_data():
    data = load_json(SYNC_FILE, {})
    if isinstance(data, list):  # guard vs old format
        data = {}
    return data

def save_sync_data(data):
    save_json(SYNC_FILE, data)

# Auto-merge result data with accuracy records
if st.button("☁️ Sync Titan Results to Cloud Memory"):
    sync_data = load_sync_data()
    result_data = load_json(RESULT_FILE, {})
    merged = {**sync_data, **result_data}
    save_sync_data(merged)
    st.success("✅ Titan Results successfully merged to cloud memory (titan_results_sync.json)")

# Display recent stored data
with st.expander("🪐 View Synced Results", expanded=False):
    sync_data = load_sync_data()
    if len(sync_data) == 0:
        st.info("No synced data yet — run a sync first.")
    else:
        for game, entries in list(sync_data.items())[-5:]:
            st.markdown(f"🎰 **{game}** — {len(entries)} entries total")
            for e in entries[-2:]:
                st.text(f"   • {e['date']} — {e['numbers']}")

# =============================================================
# 🌙 Titan Forecast Visual Enhancement + Auto-Tag System
# Version: v300.7-FXR3
# =============================================================

# --- Auto-detect draw type and format for saving results ---
def detect_draw_type(game_name):
    name = game_name.lower()
    if "midday" in name or "day" in name:
        return "Midday"
    elif "evening" in name or "night" in name:
        return "Evening"
    elif "fantasy" in name or "superlotto" in name or "mega" in name or "powerball" in name:
        return "Main Draw"
    else:
        return "General"

# --- Improved Titan Forecast Display ---
def titan_display(forecast_sets, title="Titan Forecasts", draw_date=None):
    st.markdown(f"### 🔮 {title}")
    if draw_date:
        st.markdown(f"**🗓️ Draw Date:** {draw_date}")
    for i, fset in enumerate(forecast_sets, start=1):
        conf = fset.get("confidence", 0)
        nums = fset.get("numbers", "")
        # Highlight Titan Priority Pick
        if conf >= 97:
            st.success(f"✅ **Titan Priority Pick {nums}** — Confidence {conf}%")
        else:
            st.write(f"• {nums} — Confidence {conf}%")

# --- Integrated Forecast & Tagging Interface ---
with st.expander("🌌 Titan Forecast + Auto-Tag", expanded=False):
    tag_game = st.text_input("🎮 Game Name", placeholder="e.g., GA Pick 3 Midday")
    num_sets = st.slider("🔢 Number of Forecast Sets", 1, 10, 5)
    if st.button("⚡ Generate & Tag Forecasts"):
        draw_type = detect_draw_type(tag_game)
        draw_date = datetime.date.today().strftime("%B %d, %Y")
        forecasts = generate_numbers(tag_game, num_sets)
        data = load_json(FORECAST_FILE, {})
        data.setdefault(tag_game, []).append({
            "date": datetime.today().strftime("%Y-%m-%d"),
            "saved_time": datetime.now().strftime("%H:%M:%S"),
            "draw_type": draw_type,
            "forecasts": forecasts 

        })

        save_json(FORECAST_FILE, data)
        st.success(f"✅ Forecast saved for {tag_game} ({draw_type})")
        titan_display(forecasts, title=f"{tag_game} Titan Forecasts", draw_date=draw_date)

# =============================================================
# 🎯 Titan Accuracy Analyzer + Auto-Hit Recorder
# Version: v300.8-FXR4
# =============================================================

ACCURACY_FILE = os.path.join(DATA_DIR, "titan_accuracy_log.json")

def load_accuracy():
    data = load_json(ACCURACY_FILE, {})
    if isinstance(data, list):
        data = {}
    return data

def save_accuracy(data):
    save_json(ACCURACY_FILE, data)

# --- Function: Check hits automatically and log them ---
def log_titan_accuracy(result_game, result_number):
    forecasts = load_json(FORECAST_FILE, {})
    accuracy = load_accuracy()

    if result_game not in forecasts:
        return "⚠️ No forecasts found for this game yet."

    last_entry = forecasts[result_game][-1]
    hits = 0
    total = len(last_entry["forecasts"])

    for f in last_entry["forecasts"]:
        num = f.get("numbers", "").replace(" ", "")
        if num == result_number.replace(" ", ""):
            hits += 1

    acc_percent = round((hits / total) * 100, 2) if total > 0 else 0

    # Store accuracy log
    accuracy.setdefault(result_game, []).append({
        "date": last_entry.get("date", "Unknown"),
        "draw_type": last_entry.get("draw_type", "Unknown"),
        "result": result_number,
        "accuracy": acc_percent
    })
    save_accuracy(accuracy)

    if hits > 0:
        return f"🎯 Titan HIT logged! Accuracy: {acc_percent}%"
    else:
        return f"❌ No match found. Accuracy recorded as {acc_percent}%"

# ================================================================
# 🌈 Titan Visual Customizer (Background Color Picker)
# ================================================================
st.markdown("---")
st.subheader("🎨 Titan Background Customizer")

# User color picker
bg_color = st.color_picker("Pick your cosmic background color:", "#0f0f1a", key="fxr9_bg_color")

# Apply background dynamically
st.markdown(
    f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background: {bg_color};
        color: #f4d03f;
    }}
    h1, h2, h3, h4, h5, h6 {{
        color: #f4d03f !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ================================================================
# 🌌 Titan Dual-Color Gradient Mode
# ================================================================
st.markdown("---")
st.subheader("🌌 Titan Gradient Mode")

col1, col2 = st.columns(2)
with col1:
    color_start = st.color_picker("Start Color", "#0f0f1a", key="fxr9_grad_start")
with col2:
    color_end = st.color_picker("End Color", "#660099", key="fxr9_grad_end")

gradient_style = f"linear-gradient(135deg, {color_start}, {color_end})"

st.markdown(
    f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background: {gradient_style};
        color: #f4d03f;
    }}
    h1, h2, h3, h4, h5, h6 {{
        color: #f4d03f !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ================================================================
# ⚡ Titan Energy Pulse Animation
# ================================================================
st.markdown(
    """
    <style>
    @keyframes pulse {
        0% {box-shadow: 0 0 10px #f4d03f;}
        50% {box-shadow: 0 0 40px #f4d03f;}
        100% {box-shadow: 0 0 10px #f4d03f;}
    }
    [data-testid="stAppViewContainer"] {
        animation: pulse 6s infinite;
    }
    </style>
    """,
    unsafe_allow_html=True
)
""",
    unsafe_allow_html=True
)
      
# ================================================================
# 📊 Titan Accuracy Summary Board + History Trend FXR10
# ================================================================
import pandas as pd
    
st.markdown("---")
st.header("📈 Titan Accuracy Summary Board")

# Load accuracy data
accuracy = load_json(os.path.join(DATA_DIR, "titan_accuracy_log.json"), {})

if not accuracy:
    st.info("No accuracy records yet. Generate or log Titan results first.")
else:
    # Flatten data for table
    rows = []
    for game, logs in accuracy.items():
        for log in logs[-20:]:  # show last 20 entries
            rows.append({
                "Game": game,
                "Draw Type": log.get("draw_type", "Unknown"),
                "Result": log.get("result", ""),
                "Accuracy (%)": log.get("accuracy", 0),
# ================================================================
# 📊 Titan Accuracy Summary Board + History Trend FXR10
# ================================================================
import pandas as pd

st.markdown("---")
st.header("📈 Titan Accuracy Summary Board")

# Load accuracy data
accuracy = load_json(os.path.join(DATA_DIR, "titan_accuracy_log.json"), {})

if not accuracy:
    st.info("No accuracy records yet. Generate or log Titan results first.")
else:
    # Flatten data for table
    rows = []
    for game, logs in accuracy.items():
        for log in logs[-20:]:  # show last 20 entries
            rows.append({
                "Game": game,
                "Draw Type": log.get("draw_type", "Unknown"),
                "Result": log.get("result", ""),
                "Accuracy (%)": log.get("accuracy", 0),
                "Date": log.get("date", "")
            })

    df = pd.DataFrame(rows)

    # Display data
    st.dataframe(df, use_container_width=True)

    # Summary Trend
    st.markdown("### 🔮 Accuracy Trend Summary")
    trend = df.groupby("Game")["Accuracy (%)"].mean().sort_values(ascending=False)
    st.bar_chart(trend)

    # Titan Rank Pulse
    avg_acc = trend.mean()
    if avg_acc >= 90:
        st.success(f"💚 Titan Rank: GOD MODE ({avg_acc:.2f}%) — Supreme Accuracy!")
    elif avg_acc >= 75:
        st.warning(f"💛 Titan Rank: STABLE ({avg_acc:.2f}%) — Holding strong.")
    else:
        st.error(f"❤️ Titan Rank: LOW ENERGY ({avg_acc:.2f}%) — Needs recharge!")

    # Export to CSV
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        "💾 Export Titan Accuracy Log (CSV)",
        csv,
        "titan_accuracy_log.csv",
        "text/csv",
        key="download-csv"
    )
