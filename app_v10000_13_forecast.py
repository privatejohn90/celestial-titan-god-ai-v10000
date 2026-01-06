# ================================================================
# 💎 Celestial Titan God AI — Forecast Console v10000.13-F (Multi-State)
# ================================================================
import streamlit as st
import json, os, datetime, random      
from titan_utils import load_json, save_json
    
# ================================================================
# ⚙️ Setup + Paths
# ================================================================
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)   
FORECAST_FILE = os.path.join(DATA_DIR, "titan_forecasts.json")
 
st.markdown("## 🔮 Titan Forecast Console v10000.13-F")
st.caption("🌙 Generates multi-region predictions with Titan Lock Analyzer$    
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
# 🔮 Forecast Generator + Titan Priority Logic
# ================================================================
def generate_numbers(game, num_sets=5):
    sets = []
    chrono = datetime.datetime.now().strftime("%B %d, %Y %I:%M %p")
    
    def format_numbers(nums, game):
        if "SuperLotto" in game:
            return f"{' '.join(map(str, nums[:-1]))} 🟡 MEGA {nums[-1]}"
        elif "Mega Millions" in game:  
            return f"{' '.join(map(str, nums[:-1]))} 🟣 Mega Ball {nums[-1$        elif "Powerball" in game:
            return f"{' '.join(map(str, nums[:-1]))} 🔴 Power Ball {nums[-$        else:  
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
            nums = sorted(random.sample(range(1,48),5)) + [random.randint($
        elif "Mega Millions" in game:
            nums = sorted(random.sample(range(1,71),5)) + [random.randint($
        elif "Powerball" in game:  
            nums = sorted(random.sample(range(1,70),5)) + [random.randint($
        elif "3D" in game:
            nums = [random.randint(0,9) for _ in range(3)]
        elif "4D" in game:
            nums = [random.randint(0,9) for _ in range(4)]
        elif "STL" in game:
            nums = [random.randint(0,9) for _ in range(3)]
        else:
            nums = [random.randint(0,9) for _ in range(3)]
    
        conf = round(random.uniform(90, 99.99), 2)
        sets.append({
            "numbers": nums,   
            "display": format_numbers(nums, game),
            "confidence": conf,
            "generated_at": chrono
        })
  return sets
        
# ================================================================
# 🔮 TITAN FORECAST CONSOLE — FIXED & FINAL (US + MAJOR + PH)
# ================================================================
st.markdown("## 🔮 Titan Forecast Console")
st.caption("⚡ Generate aligned numbers based on Titan learning field")
        
# -------------------------------
# 🌍 REGION SELECT
# -------------------------------
forecast_region = st.radio(
    "🌍 Select Region",
    ["US Daily Games", "Major Games", "PH Games"],
    key="forecast_region_select"
)
            
# -------------------------------
# 🎮 GAME + DRAW TIME
# -------------------------------
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
# -------------------------------
# 🔢 FORECAST SETTINGS
# -------------------------------  
forecast_sets = st.slider(
    "🔢 Number of Forecast Sets",
    1, 10, 5,
    key="forecast_sets"
)
# ✅ DATE PICKER (FIX)
st.markdown("### 📅 Forecast Date")
forecast_date = st.date_input(
    "📅 Select Forecast Date",
    value=datetime.date.today(),
    key="forecast_date"
        
# -------------------------------
# ⚡ GENERATE FORECAST
# -------------------------------
if st.button("⚡ Generate Titan Forecast", key="forecast_generate_btn"):
    results = []

    for _ in range(forecast_sets):
        if "Pick 3" in forecast_game or "Daily 3" in forecast_game or "3D"$
            nums = [random.randint(0, 9) for _ in range(3)]
        elif "Pick 4" in forecast_game or "Daily 4" in forecast_game or "4$
            nums = [random.randint(0, 9) for _ in range(4)]
        elif "Pick 5" in forecast_game:
            nums = [random.randint(0, 9) for _ in range(5)]
        elif "Fantasy 5" in forecast_game:
            nums = sorted(random.sample(range(1, 40), 5))
        elif "Mega Millions" in forecast_game:
            nums = sorted(random.sample(range(1, 71), 5)) + [random.randin$
 elif "Powerball" in forecast_game:
            nums = sorted(random.sample(range(1, 70), 5)) + [random.randint(1, 26)]
        else:
            nums = []

        confidence = round(random.uniform(90.0, 99.9), 2)
        results.append({
            "numbers": " ".join(map(str, nums)),
            "confidence": confidence
        })

    st.markdown(f"### 🎯 {forecast_game} — {forecast_draw_time}")

    top = max(results, key=lambda x: x["confidence"])

    st.success(
        f"💎 **Titan Priority Pick:** `{top['numbers']}` "
        f"(Confidence {top['confidence']}%)"
    )

    for r in sorted(results, key=lambda x: -x["confidence"]):
        if r != top:
            st.markdown(f"• `{r['numbers']}` — {r['confidence']}%")

# ================================================================
# 🔒 Titan 1–3 Set Lock Analyzer
# ================================================================
if 'forecasts' in locals() and forecasts: 
    st.markdown("## 🔒 Titan 1–3 Set Lock Analyzer")
    sorted_sets = sorted(forecasts, key=lambda x: -x['confidence'])[:3]
    lock_labels = ["💎 Titan Prime Lock", "🌀 Echo Lock", "🌗 Reserve Lock"]
    for idx, lock in enumerate(sorted_sets):
        st.markdown(f"{lock_labels[idx]} — `{lock['display']}` | Confidence: **{lock['confid$
        
    avg_conf = sum([f['confidence'] for f in sorted_sets]) / len(sorted_sets)
    st.info(f"🧠 Titan Confidence Sync: Average Lock Confidence — {avg_conf:.2f}%")
          
    if avg_conf >= 98:
        st.success("🌞 Titan Reflection: ‘Energy field perfectly aligned. Expect harmonic ac$
    elif avg_conf >= 96:
        st.warning("🌙 Titan Reflection: ‘Patterns stable — Stay within 1–2 draw cycles.’")      else:
        st.info("💤 Titan Reflection: ‘Low stability — Observe before next entry.’")
        
        
   
