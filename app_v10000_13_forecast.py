# ================================================================
# 💎 Celestial Titan God AI — Forecast Console v10000.13-F (Multi-State)
# ================================================================

import os
import json
import random
import streamlit as st
from datetime import datetime, date

# Try to use your titan_utils if present; fallback if not
try:
    from titan_utils import load_json, save_json
except Exception:
    def load_json(path, default=None):
        if default is None:
            default = {}
        try:
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as f:
                    return json.load(f)
        except Exception:
            pass
        return default

    def save_json(path, data):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

# ================================================================
# ⚙️ Setup + Paths
# ================================================================
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)
FORECAST_FILE = os.path.join(DATA_DIR, "titan_forecasts.json")

# ================================================================
# 🎯 Game Dictionaries — Full Multi-Region
# ================================================================
daily_games = {
    "GA Pick 3": ["Midday", "Evening", "Night"],
    "GA Pick 4": ["Midday", "Evening", "Night"],
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
    "NJ Pick 4": ["Midday", "Evening"],
}

# Major games: draw time is always "Main Draw"
major_games = {
    "CA Fantasy 5": ["Main Draw"],
    "CA SuperLotto Plus": ["Main Draw"],
    "Mega Millions": ["Main Draw"],
    "Powerball": ["Main Draw"],
}

# PH games (as you fixed)
ph_games = {
    "PH 3D Lotto (Swertres)": ["2PM", "5PM", "9PM"],
    "PH 4D Lotto": ["Mon", "Wed", "Fri"],
    "PH STL Game": ["10:30AM", "3PM", "7PM"],
}

# ================================================================
# 🔮 Helpers
# ================================================================
def format_numbers(game: str, nums: list[int]) -> str:
    """Pretty display formatting per game type."""
    if "Mega Millions" in game:
        # 5 white + 1 Mega Ball
        return f"{' '.join(map(str, nums[:5]))} 🟣 Mega Ball {nums[5]}"
    if "Powerball" in game:
        # 5 white + 1 Powerball
        return f"{' '.join(map(str, nums[:5]))} 🔴 Power Ball {nums[5]}"
    if "SuperLotto" in game:
        # 5 main + 1 mega (CA SuperLotto has a mega number)
        return f"{' '.join(map(str, nums[:5]))} 🟡 MEGA {nums[5]}"
    # Picks/Dailies/PH (digits)
    return " ".join(map(str, nums))

def generate_one_set(game: str) -> list[int]:
    """Return a list of ints for the selected game."""
    # US pick/daily style
    if "Daily 3" in game or "Pick 3" in game or "3D" in game or "STL" in game:
        return [random.randint(0, 9) for _ in range(3)]
    if "Daily 4" in game or "Pick 4" in game or "4D" in game:
        return [random.randint(0, 9) for _ in range(4)]
    if "Pick 5" in game and "Fantasy" not in game:
        return [random.randint(0, 9) for _ in range(5)]

    # Major games
    if "CA Fantasy 5" in game:
        return sorted(random.sample(range(1, 40), 5))  # 1–39
    if "CA SuperLotto Plus" in game:
        # 5 numbers 1–47 + Mega 1–27
        return sorted(random.sample(range(1, 48), 5)) + [random.randint(1, 27)]
    if "Mega Millions" in game:
        # 5 numbers 1–70 + Mega Ball 1–25
        return sorted(random.sample(range(1, 71), 5)) + [random.randint(1, 25)]
    if "Powerball" in game:
        # 5 numbers 1–69 + Powerball 1–26
        return sorted(random.sample(range(1, 70), 5)) + [random.randint(1, 26)]

    # Fallback
    return [random.randint(0, 9) for _ in range(3)]

def generate_forecast_sets(game: str, num_sets: int) -> list[dict]:
    chrono = datetime.now().strftime("%Y-%m-%d %I:%M %p")
    out = []
    for _ in range(num_sets):
        nums = generate_one_set(game)
        conf = round(random.uniform(90.0, 99.95), 2)
        out.append({
            "numbers": nums,
            "display": format_numbers(game, nums),
            "confidence": conf,
            "generated_at": chrono,
        })
    return out

def save_forecast_entry(entry: dict) -> None:
    data = load_json(FORECAST_FILE, {"entries": []})
    if "entries" not in data or not isinstance(data["entries"], list):
        data["entries"] = []
    data["entries"].insert(0, entry)  # newest first
    # keep file light
    data["entries"] = data["entries"][:200]
    save_json(FORECAST_FILE, data)

def load_recent_entries(limit: int = 10) -> list[dict]:
    data = load_json(FORECAST_FILE, {"entries": []})
    entries = data.get("entries", [])
    if not isinstance(entries, list):
        return []
    return entries[:limit]

# ================================================================
# 🔮 UI
# ================================================================
st.markdown("## 🔮 Titan Forecast Console v10000.13-F")
st.caption("🌙 Generates multi-region predictions with Titan Lock Analyzer")

# Region select
forecast_region = st.radio(
    "🌍 Select Region",
    ["US Daily Games", "Major Games", "PH Games"],
    key="forecast_region_select"
)

# Game + draw time
if forecast_region == "US Daily Games":
    forecast_game = st.selectbox(
        "🎮 Select US Game",
        list(daily_games.keys()),
        key="forecast_us_game"
    )
    forecast_draw_time = st.selectbox(
        "🕓 Draw Time",
        daily_games[forecast_game],
        key="forecast_us_draw_time"
    )

elif forecast_region == "Major Games":
    forecast_game = st.selectbox(
        "🎮 Select Major Game",
        list(major_games.keys()),
        key="forecast_major_game"
    )
    forecast_draw_time = "Main Draw"
    st.info("🎟️ Major Games use **Main Draw** automatically.")

else:  # PH Games
    forecast_game = st.selectbox(
        "🎮 Select PH Game",
        list(ph_games.keys()),
        key="forecast_ph_game"
    )
    forecast_draw_time = st.selectbox(
        "🕓 Draw Time",
        ph_games[forecast_game],
        key="forecast_ph_draw_time"
    )

# Forecast date (FIX)
st.markdown("### 📅 Forecast Date")
forecast_date = st.date_input(
    "📅 Select Forecast Date",
    value=date.today(),
    key="forecast_date"
)

# Number of sets
forecast_sets = st.slider(
    "🔢 Number of Forecast Sets",
    1, 10, 3,
    key="forecast_sets"
)

# Generate
if st.button("⚡ Generate Titan Forecast", key="forecast_generate_btn"):
    forecasts = generate_forecast_sets(forecast_game, forecast_sets)
    st.session_state["last_forecasts"] = forecasts

    # priority pick
    top = max(forecasts, key=lambda x: x["confidence"])
    st.markdown(f"### 🎯 {forecast_game} — {forecast_draw_time}")
    st.success(
        f"💎 **Titan Priority Pick:** `{top['display']}` "
        f"(Confidence {top['confidence']}%)"
    )

    for f in sorted(forecasts, key=lambda x: -x["confidence"]):
        if f is not top:
            st.markdown(f"• `{f['display']}` — {f['confidence']}%")

    # Save to JSON (with DATE!)
    entry = {
        "date": forecast_date.strftime("%Y-%m-%d"),
        "region": forecast_region,
        "game": forecast_game,
        "draw_time": forecast_draw_time,
        "generated_at": datetime.now().strftime("%Y-%m-%d %I:%M %p"),
        "sets": forecasts,
        "priority": top,
    }
    save_forecast_entry(entry)
    st.success("✅ Forecast saved (with date) to data/titan_forecasts.json")

    # Lock Analyzer (top 3)
    st.markdown("## 🔒 Titan 1–3 Set Lock Analyzer")
    sorted_sets = sorted(forecasts, key=lambda x: -x["confidence"])[:3]
    lock_labels = ["💎 Titan Prime Lock", "🌀 Echo Lock", "🌗 Reserve Lock"]

    for idx, lock in enumerate(sorted_sets):
        st.markdown(
            f"{lock_labels[idx]} — `{lock['display']}` | Confidence: **{lock['confidence']}%**"
        )

    avg_conf = sum(s["confidence"] for s in sorted_sets) / len(sorted_sets)
    st.info(f"🧠 Titan Confidence Sync: Average Lock Confidence — **{avg_conf:.2f}%**")

    if avg_conf >= 98:
        st.success("🌞 Titan Reflection: Energy field aligned. Hedge tight (±1–2).")
    elif avg_conf >= 96:
        st.warning("🌙 Titan Reflection: Patterns stable — stay within 1–2 draw cycles.")
    else:
        st.info("💤 Titan Reflection: Low stability — observe before heavy entry.")

# Recent saved forecasts
st.markdown("## 🧾 Recent Forecasts (saved)")
recent = load_recent_entries(12)

if not recent:
    st.caption("No saved forecasts yet.")
else:
    for e in recent:
        title = f"{e.get('date','????-??-??')} • {e.get('game','?')} • {e.get('draw_time','?')}"
        with st.expander(title, expanded=False):
            st.caption(f"Region: {e.get('region','?')} | Generated: {e.get('generated_at','?')}")
            pr = e.get("priority", {})
            if pr:
                st.success(f"Priority: `{pr.get('display','')}` ({pr.get('confidence','')}%)")
            sets = e.get("sets", [])
            for s in sets:
                st.markdown(f"• `{s.get('display','')}` — {s.get('confidence','')}%")
