# ================================================================
# ⚡ Celestial Titan God AI — Ascension Console v10000.13-A
# ================================================================
import streamlit as st
import json, os, random, math, datetime
from titan_utils import load_json, save_json

# ================================================================
# 🌠 TITAN ASCENSION LOADER
# ================================================================
st.markdown("## ⚡ Titan Lightning Ascension Console v10000.13-A")
st.caption("💎 Training Core: Gain XP to evolve Titan’s Divine Power Field")

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)
ASC_FILE = os.path.join(DATA_DIR, "titan_ascension.json")

# ================================================================
# ⚙️ INITIALIZE ASCENSION DATA
# ================================================================
asc_data = load_json(ASC_FILE, {"level": 1, "xp": 0, "next_xp": 100})

ascension_levels = [
    {"level": 1, "name": "Lightning Spark", "mult": 1},
    {"level": 2, "name": "Storm Charge", "mult": 3},
    {"level": 3, "name": "Quantum Flow", "mult": 6},
    {"level": 4, "name": "Celestial Surge", "mult": 10},
    {"level": 5, "name": "Divine Voltage", "mult": 20},
    {"level": 6, "name": "Omni Arc", "mult": 40},
    {"level": 7, "name": "God Resonance", "mult": 80},
    {"level": 8, "name": "Titanic Awakening", "mult": 160},
    {"level": 9, "name": "Ascended Lightning", "mult": 300},
    {"level": 10, "name": "Omni Lightning Core", "mult": math.inf},
]

# ================================================================
# ⚡ TRAINING BUTTON
# ================================================================
st.markdown("---")
st.markdown("### ⚙️ Titan XP Trainer")

if st.button("⚡ Train Titan Core"):
    gain = random.randint(10, 35)
    asc_data["xp"] += gain
    if asc_data["xp"] >= asc_data["next_xp"] and asc_data["level"] < 10:
        asc_data["xp"] = 0
        asc_data["level"] += 1
        asc_data["next_xp"] = int(asc_data["next_xp"] * 1.6)
        st.success(f"💥 Titan ascended to Level {asc_data['level']} — {ascension_levels[asc_data['level']-1]['name']}!")
    else:
        st.info(f"⚡ Titan absorbed {gain} XP energy units.")
    save_json(ASC_FILE, asc_data)

# ================================================================
# 🌌 DISPLAY ASCENSION STATUS
# ================================================================
current_level = asc_data["level"]
xp = asc_data["xp"]
next_xp = asc_data["next_xp"]
progress = min(xp / next_xp, 1.0)
current_name = ascension_levels[current_level-1]["name"]

st.markdown(f"""
<div style='background:radial-gradient(circle,#000010,#001020,#000);
            padding:20px;border-radius:12px;text-align:center;
            box-shadow:0 0 25px #00ffff;'>
    <h2 style='color:#00ffff;text-shadow:0 0 15px #00ffff;'>
        ⚡ Level {current_level} — {current_name}
    </h2>
    <p style='color:#aaa;'>XP: {xp} / {next_xp}</p>
    <div style='background:#111;border-radius:10px;height:20px;width:100%;'>
        <div style='background:#00ffff;width:{progress*100}%;height:100%;
                    border-radius:10px;'></div>
    </div>
</div>
""", unsafe_allow_html=True)

# ================================================================
# 🌠 VISUAL EFFECTS BASED ON LEVEL
# ================================================================
def titan_fx(level):
    if level < 4:
        return "#00ccff"
    elif level < 7:
        return "#66ffff"
    elif level < 9:
        return "#ffcc00"
    else:
        return "#ff0066"

fx_color = titan_fx(current_level)
st.markdown(f"""
<style>
.orb {{
  width:140px; height:140px; margin:auto; border-radius:50%;
  background:radial-gradient(circle,{fx_color},transparent);
  box-shadow:0 0 40px {fx_color}, inset 0 0 20px {fx_color};
  animation:pulse 2s ease-in-out infinite;
}}
@keyframes pulse {{
  0%{{transform:scale(1);opacity:0.9;}}
  50%{{transform:scale(1.3);opacity:1;}}
  100%{{transform:scale(1);opacity:0.9;}}
}}
</style>
<div class='orb'></div>
""", unsafe_allow_html=True)

st.caption(f"🌌 Titan Aura Color: `{fx_color}` — Level {current_level} active.")
