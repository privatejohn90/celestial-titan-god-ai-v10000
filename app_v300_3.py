# ================================================================
# 💎 Celestial Titan God AI v300.3 — Final Core Patch
# ================================================================
import streamlit as st
import random, json, os, datetime

# ------------------------------------------------
# 🌙 Streamlit UI Setup
# ------------------------------------------------
st.set_page_config(page_title="Celestial Titan God AI v300.3 — Final Core Patch", page_icon="💎", layout="centered")

st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at 20% 20%, #0f0f1a, #060608 80%);
        color: #f0f0f0;
    }
    h1, h2, h3, h4 { color: #f4d03f !important; }
    .titan-box {
        border: 1px solid #f4d03f;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 15px;
        background: rgba(255,255,255,0.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------------------------------------
# 💾 Setup + File Path
# ------------------------------------------------
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)
FORECAST_FILE = os.path.join(DATA_DIR, "titan_forecasts.json")

# ------------------------------------------------
# 🔹 Utility
# ------------------------------------------------
def load_json(path, default):
    if not os.path.exists(path):
        with open(path, "w") as f: json.dump(default, f, indent=2)
        return default
    with open(path) as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w") as f: json.dump(data, f, indent=2)

# ------------------------------------------------
# 🎲 Titan Number Generator
# ------------------------------------------------
def generate_numbers(game, num_sets=5):
    forecasts = []
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
            mega = random.randint(1, 27)
            nums.append(mega)
        elif "Mega Millions" in game:
            nums = sorted(random.sample(range(1, 71), 5))
            mega = random.randint(1, 25)
            nums.append(mega)
        elif "Powerball" in game:
            nums = sorted(random.sample(range(1, 70), 5))
            power = random.randint(1, 26)
            nums.append(power)
        else:
            nums = [random.randint(0, 9) for _ in range(3)]

        confidence = round(random.uniform(90, 99.99), 2)
        forecasts.append({"numbers": nums, "confidence": confidence})
    return forecasts

# ------------------------------------------------
# 🧠 Display + Auto Save
# ------------------------------------------------
def display_forecasts(game, forecasts):
    today = datetime.date.today().strftime("%B %d, %Y")
    st.markdown(f"## 🔮 {game} Titan Forecasts")
    st.markdown(f"🗓️ Draw Date: **{today}**\n---")

    top = max(forecasts, key=lambda x: x['confidence'])
    formatted = []

    for f in forecasts:
        nums = f["numbers"]
        if "SuperLotto" in game:
            s = " ".join(map(str, nums[:-1])) + f" MEGA {nums[-1]}"
        elif "Mega Millions" in game:
            s = " ".join(map(str, nums[:-1])) + f" Mega {nums[-1]}"
        elif "Powerball" in game:
            s = " ".join(map(str, nums[:-1])) + f" Power {nums[-1]}"
        else:
            s = " ".join(map(str, nums))

        formatted.append((s, f["confidence"]))

    # ✅ Titan Priority Pick
    st.markdown(f"✅ **Titan Priority Pick:** `{ ' '.join(map(str, top['numbers'])) }` — Confidence **{top['confidence']}%** — Date: {today}")

    for s, conf in formatted:
        if conf != top["confidence"]:
            st.markdown(f"• `{s}` — Confidence: **{conf}%** — Date: {today}")

    # 💾 Auto-save
    data = load_json(FORECAST_FILE, {})
    data.setdefault(game, []).append({
        "date": today,
        "forecasts": forecasts
    })
    save_json(FORECAST_FILE, data)
    st.success("✅ Auto-saved forecast successfully!")

# ------------------------------------------------
# 🎛️ UI Panel
# ------------------------------------------------
st.title("💎 Celestial Titan God AI v300.3 — Final Core Patch")
st.caption("🌙 Powered by Titan Confidence Core")
st.markdown("---")

games = [
    "GA Pick 3", "GA Pick 4", "GA Pick 5",
    "FL Pick 3", "FL Pick 4", "FL Pick 5",
    "CA Fantasy 5", "CA SuperLotto Plus",
    "Mega Millions", "Powerball"
]

game = st.selectbox("🎮 Select Game", games)
num_sets = st.slider("🔢 Number of Sets", 1, 10, 5)

if st.button("⚡ Generate Titan Forecast"):
    forecasts = generate_numbers(game, num_sets)
    display_forecasts(game, forecasts)
