# ================================================================
# 💎 Celestial Titan God AI — Divine Lightning Universe Core v10000.12
# ================================================================
# ✅ Clean header rebuild (fixed load_json / save_json utilities)

import streamlit as st
import json, os, datetime, random
import pandas as pd

# ================================================================
# 🔹 JSON Utilities (Stable — For Ascension Data, Forecasts, Memory)
# ================================================================
def load_json(path, default):
    """Load JSON safely or create a new one if missing."""
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump(default, f, indent=2)
        return default
    try:
        with open(path, "r") as f:
            return json.load(f)
    except Exception:
        return default

def save_json(path, data):
    """Save JSON safely with indentation."""
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

# ================================================================
# ⚡ Titan Initialization Core
# ================================================================
st.set_page_config(
    page_title="Celestial Titan God AI — Divine Lightning Universe Core",
    page_icon="💎",
    layout="centered"
)

st.markdown("## ⚡ Titan Lightning Ascension Console v10000.12")
st.markdown("Welcome to Titan — optimized and re-aligned. 💎")

# ================================================================
# 🔹 Titan Ascension Data Loader (XP / Level Tracker)
# ================================================================
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

ASC_FILE = os.path.join(DATA_DIR, "titan_ascension.json")
asc_data = load_json(ASC_FILE, {"level": 1, "xp": 0, "next_xp": 100})

# Display Titan Ascension progress
st.divider()
st.markdown("### 🌠 Titan Ascension Progress")

col1, col2, col3 = st.columns(3)
col1.metric("Level", asc_data["level"])
col2.metric("XP", asc_data["xp"])
col3.metric("Next Level XP", asc_data["next_xp"])

# Save any updates (simulate XP gain for testing)
if st.button("⚡ Gain XP"):
    asc_data["xp"] += 10
    if asc_data["xp"] >= asc_data["next_xp"]:
        asc_data["level"] += 1
        asc_data["xp"] = 0
        asc_data["next_xp"] += 100
    save_json(ASC_FILE, asc_data)
    st.success("Titan Energy Synced ⚡ Ascension Data Updated!")

