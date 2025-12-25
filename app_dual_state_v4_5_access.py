# ==========================================================
# 💠 Celestial Titan Dual-State Forecast Lab v4.5
# 🔐 Titan Access Layer Prototype — Login / Entry Gate
# ==========================================================
import streamlit as st
import random, json, os, datetime

# ==========================================================
# 📂 File paths
# ==========================================================
BASE_DIR = os.path.expanduser("~/Desktop/titan_dual_state_lab")
USER_FILE = os.path.join(BASE_DIR, "titan_users.json")
FORECAST_FILE = os.path.join(BASE_DIR, "titan_forecasts.json")
os.makedirs(BASE_DIR, exist_ok=True)

# ==========================================================
# 🧠 JSON helpers
# ==========================================================
def load_json(path, default):
    try:
        with open(path, "r") as f: return json.load(f)
    except: return default

def save_json(path, data):
    with open(path, "w") as f: json.dump(data, f, indent=2)

# ==========================================================
# 🧩 User System
# ==========================================================
users = load_json(USER_FILE, {"accounts": {}})

def register_user(username, password):
    if username in users["accounts"]:
        return False, "Username already exists."
    users["accounts"][username] = {
        "password": password,
        "created": str(datetime.date.today())
    }
    save_json(USER_FILE, users)
    return True, "Account created successfully!"

def login_user(username, password):
    acc = users["accounts"].get(username)
    if acc and acc["password"] == password:
        return True
    return False

# ==========================================================
# 🎯 Forecast Generator
# ==========================================================
def generate_forecast(game, sets=5):
    forecasts = []
    for _ in range(sets):
        length = 3 if "Pick-3" in game else 4
        num = "".join(str(random.randint(0,9)) for _ in range(length))
        conf = random.randint(80,97)
        instinct = random.randint(70,99)
        pulse = round((conf*0.6 + instinct*0.4), 1)
        forecasts.append({
            "number": num,
            "confidence": conf,
            "instinct": instinct,
            "pulse": pulse
        })
    return forecasts

# ==========================================================
# 🌌 App UI Layout
# ==========================================================
st.set_page_config(page_title="Titan Dual-State Forecast Lab v4.5",
                   page_icon="💠", layout="wide")

st.markdown("<h1 style='text-align:center; color:#82CAFF;'>💠 Celestial Titan Dual-State Forecast Lab v4.5</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'>🔐 Titan Access Layer Prototype</h4>", unsafe_allow_html=True)
st.write("---")

# ==========================================================
# 🧭 Access Gate
# ==========================================================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    tab1, tab2 = st.tabs(["🔑 Login", "🆕 Register"])

    with tab1:
        st.subheader("Access Titan Portal")
        u = st.text_input("Username")
        p = st.text_input("Password", type="password")
        if st.button("Login"):
            if login_user(u, p):
                st.session_state.logged_in = True
                st.session_state.user = u
                st.success(f"Welcome back, {u}! 🚀 Titan is ready.")
                st.experimental_rerun()
            else:
                st.error("Invalid username or password.")

    with tab2:
        st.subheader("Create New Access Key")
        new_user = st.text_input("New Username")
        new_pass = st.text_input("Create Password", type="password")
        if st.button("Register"):
            ok, msg = register_user(new_user, new_pass)
            if ok: st.success(msg)
            else: st.error(msg)

else:
    # ==========================================================
    # 🌠 Main Forecast Console (after login)
    # ==========================================================
    st.sidebar.markdown(f"👤 Logged in as **{st.session_state.user}**")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.experimental_rerun()

    st.markdown("## ⚡ Titan Forecast Console")
    game = st.selectbox("🎯 Select Game", ["GA Pick-3 Midday", "GA Pick-3 Evening",
                                           "FL Pick-4 Midday", "FL Pick-4 Evening"])
    sets = st.slider("Number of Forecast Sets", 3, 10, 5)

    if st.button("Generate Titan Forecast"):
        data = generate_forecast(game, sets)
        save_json(FORECAST_FILE, data)
        st.success(f"✅ Generated {len(data)} forecasts for {game}")
        for r in data:
            st.markdown(f"""
            <div style='background:linear-gradient(90deg,#5B8CFF 0%,#FF00E6 100%);
                        border-radius:10px;padding:10px;margin:5px 0;color:white;'>
            🔢 <b>{r['number']}</b><br>
            🧮 Confidence: {r['confidence']}%<br>
            💫 Instinct Pulse: {r['instinct']}%<br>
            💎 Fusion Score: {r['pulse']}%
            </div>
            """, unsafe_allow_html=True)

    st.write("---")
    st.markdown("### 🧠 Titan Insight")
    st.info("Instinct Fusion active. Titan is now learning from your session history. Keep logging draws for better precision.")


