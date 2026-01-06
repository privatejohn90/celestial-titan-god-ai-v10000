# ================================================================
# 💎 Celestial Titan God AI — Forecast Console v10000.13-F (Multi-State)
# ================================================================

import os
import json
import random
import datetime
import streamlit as st

# ==========================
# TITAN FORECAST CONSOLE v10000.13 (DATE-PATCH)
# ==========================

st.set_page_config(page_title="Titan Forecast Console v10000.13", layout="centered")

DATA_DIR = "data"
FORECAST_FILE = os.path.join(DATA_DIR, "titan_forecasts.json")
RESULT_FILE = os.path.join(DATA_DIR, "titan_results.json")

def ensure_data_dir():
    os.makedirs(DATA_DIR, exist_ok=True)

def load_json(path, default):
    try:
        if not os.path.exists(path):
            return default
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default

def save_json(path, data):
    ensure_data_dir()
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def now_ts():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def today_str(d: datetime.date):
    return d.strftime("%Y-%m-%d")

# ---- Game maps (edit anytime)
daily_games = {
    "CA Daily 3": ["Midday", "Evening"],
    "CA Daily 4": ["Evening"],
    "GA Pick 3": ["Midday", "Evening"," Night"],
    "GA Pick 4": ["Midday", "Evening"," Night"],
    "GA Pick 5": ["Midday", "Evening"],
    "FL Pick 3": ["Midday", "Evening"],
    "FL Pick 4": ["Midday", "Evening"],
    "FL Pick 5": ["Midday", "Evening"],
    "NC Pick 3": ["Midday", "Evening"],
    "NC Pick 4": ["Midday", "Evening"],
    "NJ Pick 3": ["Midday", "Evening"],
    "NJ Pick 4": ["Midday", "Evening"],
    "VA Pick 3": ["Midday", "Evening"],
    "VA Pick 4": ["Midday", "Evening"],
    "VA Pick 5": ["Midday", "Evening"],
    "NY Pick 3": ["Midday", "Evening"],
    "NY Pick 4": ["Midday", "Evening"],
"TX Pick 3": ["Morning", "Day", "Evening", "Night"],
"TX Pick 4": ["Morning", "Day", "Evening", "Night"],
}
major_games = {
    "Mega Millions": ["Main Draw"],
    "Powerball": ["Main Draw"],
    "SuperLotto Plus (CA)": ["Main Draw"],
    "Fantasy 5 (CA)": ["Main Draw"],
}

ph_games = {
    "EZ2": ["2PM", "5PM", "9PM"],
    "Swertres": ["2PM", "5PM", "9PM"],
    "6/42": ["Main Draw"],
    "6/45": ["Main Draw"],
    "6/49": ["Main Draw"],
    "6/55": ["Main Draw"],
    "6/58": ["Main Draw"],
}

# ---- Simple helper to infer digit length for Pick games
def infer_pick_len(game: str):
    g = game.lower()
    if "pick 3" in g or "daily 3" in g or "swertres" in g:
        return 3
    if "pick 4" in g or "daily 4" in g:
        return 4
    if "pick 5" in g:
        return 5
    return None

def normalize_num_str(s: str, length: int):
    s = "".join(ch for ch in s if ch.isdigit())
    if length is None:
        return s
    return s.zfill(length)[:length]

def get_recent_results_for_game(game: str, draw_time: str, limit: int = 50):
    """
    Reads from data/titan_results.json if available.
    Expected format: data[game] = list of entries with keys: date, draw_time, number, region
    """
    data = load_json(RESULT_FILE, {})
    arr = data.get(game, [])
    filtered = [x for x in arr if str(x.get("draw_time","")) == str(draw_time)]
    # most recent last usually; we take last N
    return filtered[-limit:]

def build_digit_bias(game: str, draw_time: str):
    """
    Very light "real" logic:
    - if results exist, bias digits by recent frequency
    - else fallback random
    """
    pick_len = infer_pick_len(game)
    if pick_len is None:
        return None

    recent = get_recent_results_for_game(game, draw_time, limit=120)
    if not recent:
        return None

    # Count digit frequencies per position
    counts = [dict((str(d), 1) for d in range(10)) for _ in range(pick_len)]  # start at 1 smoothing
    for r in recent:
        num = normalize_num_str(str(r.get("number","")), pick_len)
        if len(num) != pick_len:
            continue
        for i, ch in enumerate(num):
            counts[i][ch] = counts[i].get(ch, 0) + 1

    # Convert to weighted lists
    weights = []
    for i in range(pick_len):
        digits = []
        w = []
        for d in range(10):
            ds = str(d)
            digits.append(ds)
            w.append(counts[i].get(ds, 1))
        weights.append((digits, w))
    return weights

def weighted_pick(digits, weights):
    return random.choices(digits, weights=weights, k=1)[0]

def generate_pick_numbers(game: str, draw_time: str, n_sets: int):
    """
    Generates n_sets candidate numbers for Pick games using digit-bias if results exist.
    """
    pick_len = infer_pick_len(game)
    if pick_len is None:
        return []

    bias = build_digit_bias(game, draw_time)

    out = []
    used = set()

    # generate a bit more to avoid duplicates
    attempts = 0
    while len(out) < n_sets and attempts < 2000:
        attempts += 1
        if bias:
            s = "".join(weighted_pick(bias[i][0], bias[i][1]) for i in range(pick_len))
        else:
            s = "".join(str(random.randint(0, 9)) for _ in range(pick_len))
        if s not in used:
            used.add(s)
            out.append(s)

    return out

def append_forecast_entry(entry: dict):
    data = load_json(FORECAST_FILE, {})
    game = entry["game"]
    data.setdefault(game, []).append(entry)
    save_json(FORECAST_FILE, data)

# ==========================
# UI
# ==========================

st.markdown("## 🔮 Titan Forecast Console")
st.caption("⚡ Generate aligned numbers based on Titan learning field (with dated logs).")

# REGION
forecast_region = st.radio(
    "🌍 Select Region",
    ["US Daily Games", "Major Games", "PH Games"],
    key="forecast_region_select"
)

# GAME + DRAW TIME
if forecast_region == "US Daily Games":
    forecast_game = st.selectbox("🎮 Select US Game", list(daily_games.keys()), key="forecast_us_game")
    forecast_draw_time = st.selectbox("🕒 Draw Time", daily_games[forecast_game], key="forecast_us_draw_time")
elif forecast_region == "Major Games":
    forecast_game = st.selectbox("🎮 Select Major Game", list(major_games.keys()), key="forecast_major_game")
    forecast_draw_time = "Main Draw"
else:
    forecast_game = st.selectbox("🎮 Select PH Game", list(ph_games.keys()), key="forecast_ph_game")
    forecast_draw_time = st.selectbox("🕒 Draw Time", ph_games[forecast_game], key="forecast_ph_draw_time")

# ✅ DATE PICKER (FIX)
st.markdown("### 📅 Forecast Date")
forecast_date = st.date_input(
    "📅 Select Forecast Date",
    value=datetime.date.today(),
    key="forecast_date"
)

# SET COUNT
n_sets = st.slider("🔢 Number of Forecast Sets", min_value=1, max_value=10, value=3, key="forecast_sets")

# GENERATE
if st.button("⚡ Generate Titan Forecast", key="forecast_generate_btn"):
    pick_len = infer_pick_len(forecast_game)

    if pick_len is None:
        st.warning("⚠️ This forecast file currently auto-generates only Pick-style games (Pick3/4/5 & Daily3/4).")
    else:
        picks = generate_pick_numbers(forecast_game, forecast_draw_time, n_sets)

        # Save forecast entry with DATE
        entry = {
            "date": today_str(forecast_date),                 # ✅ selected date (not just today)
            "created_at": now_ts(),
            "region": forecast_region,
            "game": forecast_game,
            "draw_time": forecast_draw_time,
            "sets": picks
        }
        append_forecast_entry(entry)

        st.success(f"✅ Forecast saved: **{forecast_game} — {forecast_draw_time}** (Date: {today_str(forecast_date)})")

        # Display
        st.markdown("### 🎯 Forecast Sets")
        for i, p in enumerate(picks, start=1):
            st.write(f"**Set {i}:** `{p}`")

# RECENT FORECASTS
st.markdown("---")
st.markdown("### 🧾 Recent Forecasts (saved)")
all_forecasts = load_json(FORECAST_FILE, {})

recent_rows = []
for g, arr in all_forecasts.items():
    for item in arr[-10:]:
        recent_rows.append(item)

# sort by created_at if possible
def sort_key(x):
    return x.get("created_at", "")

recent_rows = sorted(recent_rows, key=sort_key, reverse=True)[:15]

if not recent_rows:
    st.info("No forecasts saved yet.")
else:
    for item in recent_rows:
        st.markdown(
            f"**{item.get('game')}** — {item.get('draw_time')}  \n"
            f"📅 Date: `{item.get('date','')}` • 🕒 Logged: `{item.get('created_at','')}`  \n"
            f"Sets: `{', '.join(item.get('sets', []))}`"
        )
        st.markdown("---")

st.caption("🧊 Titan stays quiet. Forecasts are logged with date for tracking + wobble compare.")

# ================================================================
# 🔒 Titan 1–3 Set Lock Analyzer
# ================================================================
if 'forecasts' in locals() and forecasts:
    st.markdown("## 🔒 Titan 1–3 Set Lock Analyzer")
    sorted_sets = sorted(forecasts, key=lambda x: -x['confidence'])[:3]
    lock_labels = ["💎 Titan Prime Lock", "🌀 Echo Lock", "🌗 Reserve Lock"]
    for idx, lock in enumerate(sorted_sets):
        st.markdown(f"{lock_labels[idx]} — `{lock['display']}` | Confidence: **{lock['confidence']}%**")

    avg_conf = sum([f['confidence'] for f in sorted_sets]) / len(sorted_sets)
    st.info(f"🧠 Titan Confidence Sync: Average Lock Confidence — {avg_conf:.2f}%")

    if avg_conf >= 98:
        st.success("🌞 Titan Reflection: ‘Energy field perfectly aligned. Expect harmonic accuracy.’")
    elif avg_conf >= 96:
        st.warning("🌙 Titan Reflection: ‘Patterns stable — Stay within 1–2 draw cycles.’")
    else:
        st.info("💤 Titan Reflection: ‘Low stability — Observe before next entry.’")
