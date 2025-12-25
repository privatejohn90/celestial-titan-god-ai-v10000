import streamlit as st
import os, json, datetime, random

# ==========================================================
# 🔱 TITAN GOD AI v10,000 — ULTRA CLEAN FOUNDATION
# ==========================================================

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# ==========================================================
# 🧬 JSON AUTO-CREATE SYSTEM (CLEAN & SAFE)
# ==========================================================

def ensure_json(filename, default):
    path = os.path.join(BASE_PATH, filename)

    # Create file if missing
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump(default, f, indent=4)
        return path

    # Ensure correct structure
    try:
        with open(path) as f:
            data = json.load(f)
    except:
        data = default

    # Auto-repair missing keys
    for key in default:
        if key not in data:
            data[key] = default[key]

    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    return path

memory_file   = ensure_json("titan_memory.json",   {"messages": []})
codex_file    = ensure_json("titan_codex.json",    {"rules": []})
results_file  = ensure_json("titan_results.json",  {"records": []})
settings_file = ensure_json("titan_settings.json", {"theme": "dark"})
calendar_file = ensure_json("titan_calendar.json", {"events": []})

def load_json(path):
    # Try reading JSON
    try:
        with open(path) as f:
            data = json.load(f)
    except:
        data = {}

    # AUTO-REPAIR SYSTEM
    if path.endswith("titan_memory.json"):
        if "messages" not in data:
            data["messages"] = []

    if path.endswith("titan_codex.json"):
        if "rules" not in data:
            data["rules"] = []

    if path.endswith("titan_results.json"):
        if "records" not in data:
            data["records"] = []

    if path.endswith("titan_settings.json"):
        if "theme" not in data:
            data["theme"] = "dark"

    if path.endswith("titan_calendar.json"):
        if "events" not in data:
            data["events"] = []

    # Always rewrite repaired data
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    return data

    # Auto-repair for each JSON type
    if path.endswith("titan_memory.json"):
        data.setdefault("messages", [])
    if path.endswith("titan_codex.json"):
        data.setdefault("rules", [])
    if path.endswith("titan_results.json"):
        data.setdefault("records", [])
    if path.endswith("titan_settings.json"):
        data.setdefault("theme", "dark")
    if path.endswith("titan_calendar.json"):
        data.setdefault("events", [])

    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    return data

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

# ==========================================================
# 🧠 MEMORY ENGINE
# ==========================================================

def get_memory(limit=20):
    data = load_json(memory_file)
    data["messages"].insert(0, {
        "timestamp": str(datetime.datetime.now()),
        "message": msg
    })
    save_json(memory_file, data)

def get_memory(limit=20):
    return load_json(memory_file)["messages"][:limit]

# ==========================================================
# 📜 LEVEL 5 — STRUCTURED CODEX ENGINE
# ==========================================================

def add_rule(text, category="general"):
    data = load_json(codex_file)

    entry = {
        "category": category,
        "timestamp": str(datetime.datetime.now()),
        "text": text
    }

    data["rules"].insert(0, entry)
    save_json(codex_file, data)

def get_rules(category=None, limit=50):
    data = load_json(codex_file)["rules"]

    if category:
        data = [x for x in data if x["category"] == category]

    return data[:limit]

# ==========================================================
# 🎯 LEVEL 6 — STRUCTURED RESULTS ENGINE
# ==========================================================

def save_lottery(state, game, numbers, draw_time):
    data = load_json(results_file)

    entry = {
        "state": state,
        "state_code": state.upper()[:2],   # FL, GA, NC, TX, VA, CA
        "game": game,
        "game_type": "P3" if game == "Pick 3" else "P4" if game == "Pick 4" else "P5",
        "numbers": [int(x) for x in numbers if x.isdigit()],
        "draw_time": draw_time,
        "timestamp": str(datetime.datetime.now()),
        "source": "manual"
    }

    data["records"].insert(0, entry)
    save_json(results_file, data)

def get_results(limit=20, state_code=None):
    data = load_json(results_file)["records"]

    if state_code:
        data = [x for x in data if x["state_code"] == state_code.upper()]

    return data[:limit]

# ==========================================================
# 🔮 LEVEL 7 — ADVANCED FORECAST ENGINE
# ==========================================================

def titan_forecast(game):
    now = datetime.datetime.now()

    # Stronger seed: day + hour + minute
    seed_value = now.day + now.hour + now.minute
    random.seed(seed_value)

    # Forecast length
    length = 3 if game == "Pick 3" else 4 if game == "Pick 4" else 5

    # Base digits
    digits = list(range(10))

    # Avoid repeating same digit 3+ times
    forecast = []

    for i in range(length):
        digit = random.choice(digits)

        # Light pattern logic:
        # If last two digits are the same, avoid repeating
        if len(forecast) >= 2 and forecast[-1] == forecast[-2]:
            remaining = [d for d in digits if d != forecast[-1]]
            digit = random.choice(remaining)

        forecast.append(digit)

        # Harmonic shuffle: reshuffle digits slightly each pick
        random.shuffle(digits)

    # Return as string
    return "".join(str(d) for d in forecast)

# ==========================================================
# 🌙 CALENDAR ENGINE
# ==========================================================

def add_event(title, date):
    data = load_json(calendar_file)
    data["events"].append({"title": title, "date": date})
    save_json(calendar_file, data)

def get_events():
    return load_json(calendar_file)["events"]

# ==========================================================
# 🔢 PATTERN MATRIX UI
# ==========================================================

elif menu == "Patterns":
    st.subheader("🔢 Titan Pattern Matrix")

    freq = get_digit_frequency()
    hot, cold = get_hot_cold_digits()

    st.write("### Digit Frequency (0–9)")
    st.write(freq)

    st.write("### 🔥 Hot Digits")
    st.write(hot)

    st.write("### ❄️ Cold Digits")
    st.write(cold)

    st.info("Pattern Matrix is active. More pattern logic will be added in Level 8 Part 2.")

# ==========================================================
# 🏛️ TITAN UI — CLEAN NAVIGATION
# ==========================================================

st.set_page_config(page_title="Titan v10,000", layout="wide")

# ============================================
# 🎨 LEVEL 2 — CLEAN UI ENHANCEMENT
# ============================================
st.markdown("""
<style>

html, body {
    background-color: #0f0f15;
    color: #e6e6f5;
    font-family: 'Inter', sans-serif;
}

/* Clean container style */
section.main > div {
    background: rgba(255, 255, 255, 0.03);
    padding: 18px;
    border-radius: 12px;
    border: 1px solid rgba(255, 255, 255, 0.05);
    margin-bottom: 20px;
}

/* Sidebar clean design */
[data-testid="stSidebar"] {
    background: #0b0b12;
    border-right: 1px solid #1d1d2e;
}

/* Title colors */
h1, h2, h3 {
    color: #c9d6ff;
}

/* Buttons */
.stButton>button {
    background: #1b1b2b;
    border-radius: 7px;
    border: 1px solid #2c2c45;
    color: #dfe0ff;
    padding: 7px 12px;
}
.stButton>button:hover {
    background: #26263a;
}

</style>
""", unsafe_allow_html=True)

st.title("🌌 Titan God AI v10,000 — Clean Base Build")

menu = st.sidebar.radio("Navigation", [
    "Dashboard",
    "Memory",
    "Codex",
    "Results",
    "Forecast",
    "Patterns",
    "Calendar"
])
# ==========================================================
# 🏠 DASHBOARD
# ==========================================================

if menu == "Dashboard":
    st.subheader("🔭 Titan Status")
    st.metric("Memories", len(load_json(memory_file)["messages"]))
    st.metric("Rules", len(load_json(codex_file)["rules"]))
    st.metric("Results", len(load_json(results_file)["records"]))
    st.metric("Events", len(load_json(calendar_file)["events"]))

# ==========================================================
# 🧠 MEMORY
# ==========================================================

elif menu == "Memory":
    st.subheader("🧠 Titan Memory")

    col1, col2 = st.columns([3,1])

    with col1:
        msg = st.text_input("Enter memory:")

    with col2:
        mtype = st.selectbox("Type", ["general", "note", "event", "rule", "system"])

    if st.button("Save Memory"):
        add_memory(msg, mtype)
        st.success("Saved!")

    st.write(get_memory())

# ==========================================================
# 📜 CODEX
# ==========================================================

elif menu == "Codex":
    st.subheader("📜 Titan Codex")

    col1, col2 = st.columns([3,1])

    with col1:
        rule = st.text_input("Enter rule:")

    with col2:
        category = st.selectbox("Category", [
            "general",
            "forecast",
            "memory",
            "behavior",
            "system"
        ])

    if st.button("Save Rule"):
        add_rule(rule, category)
        st.success("Rule Saved!")

    st.write(get_rules())

# ==========================================================
# 🎯 RESULTS
# ==========================================================

elif menu == "Results":
    st.subheader("🎯 Titan Results Engine")

    col1, col2, col3 = st.columns(3)

    with col1:
        state = st.text_input("State (ex: FL, GA, NC, TX, VA, CA)")

    with col2:
        game = st.selectbox("Game", ["Pick 3", "Pick 4", "Pick 5"])

    with col3:
        draw_time = st.selectbox("Draw Time", ["Midday", "Evening", "Night"])

    numbers = st.text_input("Winning Numbers (ex: 1 2 3 4)")

    if st.button("Save Result"):
        save_lottery(state, game, numbers, draw_time)
        st.success("Result Saved!")

    st.write(get_results())

# ==========================================================
# 🔮 FORECAST
# ==========================================================

elif menu == "Forecast":
    st.subheader("🔮 Titan Forecast")
    game = st.selectbox("Game", ["Pick 3", "Pick 4", "Pick 5"])
    if st.button("Generate Forecast"):
        st.success("Forecast: " + titan_forecast(game))

# ==========================================================
# 🌙 CALENDAR
# ==========================================================

elif menu == "Calendar":
    st.subheader("🌙 Titan Calendar")
    title = st.text_input("Event Title")
    date = st.date_input("Date")
    if st.button("Add Event"):
        add_event(title, str(date))
        st.success("Event Added!")
    st.write(get_events())

# ==========================================================
# 🧠 LEVEL 4 — STRUCTURED MEMORY ENGINE
# ==========================================================

def add_memory(text, mtype="general"):
    data = load_json(memory_file)

    entry = {
        "type": mtype,
        "timestamp": str(datetime.datetime.now()),
        "text": text
    }

    # Insert newest at the top
    data["messages"].insert(0, entry)

    save_json(memory_file, data)

def get_memory(limit=20, mtype=None):
    data = load_json(memory_file)["messages"]

    # Filter by memory type (optional)
    if mtype:
        data = [x for x in data if x["type"] == mtype]

    return data[:limit]

# ==========================================================
# 🔢 LEVEL 8 — PATTERN MATRIX ENGINE (Part 1)
# ==========================================================

def get_digit_frequency():
    """
    Count how often each digit 0–9 appears in all stored results.
    """
    data = load_json(results_file)["records"]
    freq = {str(i): 0 for i in range(10)}

    for r in data:
        for d in r["numbers"]:
            freq[str(d)] += 1

    return freq


def get_hot_cold_digits():
    """
    Determine the hot (most frequent) and cold (least frequent) digits.
    """
    freq = get_digit_frequency()

    # Sort by most → least frequent
    sorted_digits = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    hot = sorted_digits[:3]   # top 3
    cold = sorted_digits[-3:] # bottom 3

    return hot, cold

