# ================================================================
# 💎 Celestial Titan God AI v1.0 — Ultimate Core Console
# Unified Forecast System | US + PH | Full Console Mode
# ================================================================

import streamlit as st
import random, json, os, datetime

# ================================================================
# ⚙️ Config
# ================================================================
st.set_page_config(
    page_title="Celestial Titan God AI v1.0 — Ultimate Core Console",
    page_icon="💎",
    layout="wide"
)

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)
FORECAST_FILE = os.path.join(DATA_DIR, "titan_forecasts.json")
RESULT_FILE = os.path.join(DATA_DIR, "titan_results.json")
MEMORY_FILE = os.path.join(DATA_DIR, "titan_memory.json")

# ================================================================
# 🌙 Cosmic Theme (UI Add-on)
# ================================================================
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at 20% 20%, #0b0b13, #050509 80%);
        color: #e6e6e6;
    }
    h1, h2, h3, h4 {
        color: #f4d03f !important;
    }
    div.stButton>button {
        background: linear-gradient(90deg, #f4d03f, #f39c12);
        color: black;
        font-weight: bold;
        border: none;
        border-radius: 6px;
        padding: 0.5rem 1rem;
    }
    div.stButton>button:hover {
        background: linear-gradient(90deg, #ffe066, #f4d03f);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ================================================================
# 💫 Header
# ================================================================
st.title("💎 Celestial Titan God AI v1.0 — Ultimate Core Console")
st.caption("🌌 Unified Forecast Console | Powered by Titan Confidence Core | US + PH Integrated")

st.markdown("---")

# ================================================================
# 🧭 Titan Control Panel — Sidebar
# ================================================================
with st.sidebar:
    st.header("🧭 Titan Control Panel")
    st.caption("Configure Forecast Parameters")

    category = st.selectbox(
        "Select Game Category",
        ["Daily Games", "Major Games", "Philippine Games"]
    )

    set_count = st.slider("Number of Sets", 1, 10, 5)
    draw_date = st.date_input("Draw Date", datetime.date.today())

    st.markdown("---")
    st.caption("⚙️ Powered by Titan Confidence Engine")

# ================================================================
# 🎯 Game Library Definitions
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
    "Powerball": [],
    "Mega Millions": []
}

ph_games = {
    "PH 3D Lotto (Swertres)": ["2PM", "5PM", "9PM"],
    "PH 4D Lotto": ["Mon", "Wed", "Fri"],
    "PH STL Game": ["10:30AM", "3PM", "7PM"]
}

# ================================================================
# 🧩 Select Specific Game
# ================================================================
if category == "Daily Games":
    game = st.selectbox("Select Game", list(daily_games.keys()))
    time_option = st.selectbox("Select Draw Time", daily_games.get(game, []))
elif category == "Major Games":
    game = st.selectbox("Select Game", list(major_games.keys()))
    time_option = ""
else:
    game = st.selectbox("Select Game", list(ph_games.keys()))
    time_option = st.selectbox("Select Draw Time", ph_games.get(game, []))

generate_button = st.button("⚡ Generate Forecast")

# ================================================================
# 💠 Core Logic — Forecast Generator + Auto-Save + Memory Sync (Fixed)
# ================================================================
if generate_button:
    st.subheader(f"🔮 {game} {time_option} Titan Forecasts")
    st.caption(f"🗓️ Draw Date: {draw_date.strftime('%B %d, %Y')}")
    st.markdown("---")

    all_sets = []
    for i in range(set_count):
        # ============================================================
        # 🎲 Generate Numbers per Game Type
        # ============================================================
        if "Pick 3" in game:
            nums = random.sample(range(0, 10), 3)
        elif "Pick 4" in game:
            nums = random.sample(range(0, 10), 4)
        elif "Pick 5" in game and "Fantasy" not in game:
            nums = random.sample(range(0, 10), 5)
        elif "Fantasy 5" in game:
            nums = sorted(random.sample(range(1, 40), 5))
        elif "SuperLotto" in game:
            nums = sorted(random.sample(range(1, 48), 5))
            nums.append(random.randint(1, 27))
        elif "Powerball" in game:
            nums = sorted(random.sample(range(1, 70), 5))
            nums.append(random.randint(1, 26))
        elif "Mega Millions" in game:
            nums = sorted(random.sample(range(1, 70), 5))
            nums.append(random.randint(1, 25))
        elif "PH 3D" in game:
            nums = random.sample(range(0, 10), 3)
        elif "PH 4D" in game:
            nums = random.sample(range(0, 10), 4)
        elif "PH STL" in game:
            nums = random.sample(range(0, 10), 3)
        else:
            nums = random.sample(range(0, 10), 3)

        # ============================================================
        # 🌟 Confidence Generator + Forecast Record
        # ============================================================
        conf = random.uniform(90, 100)
        forecast = {
            "date": str(draw_date),
            "category": category,
            "game": game,
            "time": time_option,
            "numbers": nums,
            "confidence": round(conf, 2)
        }
        all_sets.append(forecast)

        # ============================================================
        # 🌟 Titan Priority Pick Display (Enhanced + Fixed)
        # ============================================================
        formatted_nums = " ".join(map(str, nums[:-1])) if len(nums) > 3 else " ".join(map(str, nums))

        # Add proper label for special balls
        if "Powerball" in game:
            formatted_nums += f" PB {nums[-1]}"
        elif "Mega Millions" in game:
            formatted_nums += f" MB {nums[-1]}"
        elif "SuperLotto" in game:
            formatted_nums += f" MEGA {nums[-1]}"

        # Identify Titan’s top-confidence forecast
        if conf == max([r["confidence"] for r in all_sets]):
            st.markdown(
                f"✅ **Titan Priority Pick:** `{formatted_nums}` — Confidence **{round(conf,2)}%** — Date: {draw_date.strftime('%B %d, %Y')}"
            )
        else:
            st.write(f"• `{formatted_nums}` — Confidence: **{round(conf,2)}%** — Date: {draw_date.strftime('%B %d, %Y')}")

    # ============================================================
    # 💾 Auto-Save Forecasts (Stable + Clean)
    # ============================================================
    os.makedirs("data", exist_ok=True)
    if os.path.exists(FORECAST_FILE):
        with open(FORECAST_FILE, "r") as f:
            try:
                saved_data = json.load(f)
                if isinstance(saved_data, dict):
                    saved_data = [saved_data]
            except:
                saved_data = []
    else:
        saved_data = []

    if not isinstance(saved_data, list):
        saved_data = []

    saved_data.extend(all_sets)

    with open(FORECAST_FILE, "w") as f:
        json.dump(saved_data, f, indent=2)

    st.success("✅ Auto-saved forecast successfully!")
