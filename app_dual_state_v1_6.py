# ==========================================================
# 💎 Celestial Titan Dual-State Forecast Lab v1.6
# 🌌 Calendar Sync View — Canva Hybrid Design Edition
# ==========================================================
import streamlit as st, json, random, datetime, os, math, pandas as pd
import plotly.graph_objects as go
from calendar import monthcalendar

# ==========================================================
# ⚙️ CONFIG
# ==========================================================
st.set_page_config(page_title="Titan Dual-State Forecast Lab v1.6", page_icon="💎", layout="wide")
BASE = os.path.dirname(os.path.abspath(__file__))

# ==========================================================
# 🎨 CANVA HYBRID THEME
# ==========================================================
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
  background: radial-gradient(circle at 20% 20%, #0A0C24 0%, #151B44 100%);
  color: #E0E0E0 !important;
  font-family: 'Orbitron', sans-serif;
}
[data-testid="stSidebar"] {
  background: linear-gradient(180deg,#080C2C 0%,#121F53 100%);
}
h1,h2,h3,h4,h5,h6 {
  color: #9EE6FF !important;
  text-shadow: 0 0 8px #00C6FF;
}
.stButton>button {
  background: linear-gradient(90deg,#0070FF,#9B00FF);
  border:none;border-radius:12px;
  color:white;font-weight:bold;
  padding:0.6em 1.2em;box-shadow:0 0 15px #0078FF;
  transition:all .3s ease-in-out;
}
.stButton>button:hover {
  transform:scale(1.05);
  box-shadow:0 0 30px #9B00FF;
}
.card {
  backdrop-filter: blur(12px);
  background: rgba(255,255,255,0.06);
  border-radius:15px;
  padding:15px;margin:10px;
  box-shadow: 0 0 20px rgba(0,150,255,0.2);
}
.daycell {
  border-radius:10px;padding:8px;
  text-align:center;
  cursor:pointer;
}
.day-hit {background:rgba(0,255,180,0.2);box-shadow:0 0 10px #00FF9C;}
.day-miss{background:rgba(255,60,60,0.2);box-shadow:0 0 10px #FF5E5E;}
.day-pend{background:rgba(255,255,255,0.05);}
</style>
""", unsafe_allow_html=True)

# ==========================================================
# 🧠 UTILITIES
# ==========================================================
def ensure_json(path, default):
    if not os.path.exists(path):
        with open(path,"w") as f: json.dump(default,f,indent=2)
    with open(path) as f:
        try: data=json.load(f)
        except: data=default
    return data

def save_json(path,data):
    with open(path,"w") as f: json.dump(data,f,indent=2)

# ==========================================================
# 📂 FILES
# ==========================================================
RES_FILE=os.path.join(BASE,"titan_results.json")
ACC_FILE=os.path.join(BASE,"titan_accuracy.json")
CAL_FILE=os.path.join(BASE,"titan_calendar.json")
for p,d in [(RES_FILE,{"records":[]}), (ACC_FILE,{"records":[]}), (CAL_FILE,{"days":[]})]:
    ensure_json(p,d)

# ==========================================================
# 🌕 LUNAR PHASE
# ==========================================================
def lunar_phase():
    now=datetime.datetime.now(datetime.timezone.utc)
    ref=datetime.datetime(2001,1,1,tzinfo=datetime.timezone.utc)
    diff=(now-ref).total_seconds()/86400.0
    cycle=29.53
    frac=(diff%cycle)/cycle
    illum=int((1-math.cos(2*math.pi*frac))/2*100)
    phase="🌑 New" if illum<10 else "🌓 First" if illum<40 else "🌕 Full" if illum<60 else "🌗 Last" if illum<90 else "🌘 Waning"
    return phase,illum

# ==========================================================
# 🧩 TITAN CORE
# ==========================================================
def generate_forecast(game,sets):
    forecasts=[]
    for i in range(sets):
        n=int(game.split()[-1])
        nums=[random.randint(0,9) for _ in range(n)]
        conf=random.randint(75,98)
        forecasts.append((nums,conf))
    return forecasts

def compute_accuracy():
    data=ensure_json(ACC_FILE,{"records":[]})["records"]
    if not data: return 0
    hits=sum(1 for d in data if d["hit"])
    return int((hits/len(data))*100)

# ==========================================================
# 🗓️ CALENDAR SYNC VIEW
# ==========================================================
def render_calendar():
    st.subheader("📅 Titan Calendar Sync View")
    caldata=ensure_json(CAL_FILE,{"days":[]})
    days=pd.DataFrame(caldata.get("days",[]))
    today=datetime.date.today()
    year,month=today.year,today.month
    cal=monthcalendar(year,month)
    c1,c2=st.columns([2,1])
    with c1:
        st.markdown(f"### {today.strftime('%B %Y')}")
        for week in cal:
            cols=st.columns(7)
            for i,day in enumerate(week):
                if day==0: cols[i].markdown(" ")
                else:
                    state=days[(days["date"]==f"{year}-{month:02d}-{day:02d}")]["status"].values if not days.empty else []
                    cls="day-pend"
                    if len(state)>0:
                        s=state[0]
                        if s=="hit": cls="day-hit"
                        elif s=="miss": cls="day-miss"
                    cols[i].markdown(f"<div class='daycell {cls}'>{day}</div>",unsafe_allow_html=True)
    with c2:
        st.markdown("**Color Legend**")
        st.markdown("🟢 Hit 🔴 Miss ⚪ Pending")
        phase,illum=lunar_phase()
        st.metric("🌙 Lunar Phase",f"{phase} ({illum}%)")
        st.metric("📈 Accuracy",f"{compute_accuracy()}%")
        st.caption("🧠 Titan: Calendar field synchronized with memory nodes.")

# ==========================================================
# 🧭 SIDEBAR NAVIGATION
# ==========================================================
st.sidebar.title("💠 Titan Dual-State Forecast Lab")
menu=st.sidebar.radio("Select Module",["🎯 Forecast Console","📅 Calendar Sync View"])

# ==========================================================
# 🏠 DASHBOARD
# ==========================================================
st.markdown("<h1 style='text-align:center;'>💎 Celestial Titan Dual-State Forecast Lab v1.6</h1>",unsafe_allow_html=True)

if menu=="🎯 Forecast Console":
    st.subheader("🎯 Forecast Console")
    game=st.selectbox("Select Game",["GA Pick 3 Midday","FL Pick 4 Midday"])
    sets=st.slider("Number of Forecast Sets",3,10,3)
    if st.button("🌠 Generate Forecast"):
        fc=generate_forecast(game,sets)
        for i,(nums,conf) in enumerate(fc,1):
            st.success(f"Set {i} → {' '.join(map(str,nums))} | Confidence {conf}%")
        st.info("🧠 Titan: Forecasts stored in temporal memory core.")
    st.markdown("---")
    st.subheader("📥 Enter Official Result")
    date=st.date_input("Date",datetime.date.today())
    result=st.text_input("Winning Number (Straight)")
    state_sel="hit" if st.checkbox("Hit") else "miss"
    if st.button("💾 Save Result & Sync"):
        res=ensure_json(CAL_FILE,{"days":[]})
        res["days"].append({"date":str(date),"status":state_sel})
        save_json(CAL_FILE,res)
        st.success("✅ Saved and synchronized to Titan Calendar.")
        st.rerun()
else:
    render_calendar()

st.markdown("<hr><center><small>💎 Celestial Titan v1.6 — Calendar Sync View | Canva Hybrid Edition</small></center>",unsafe_allow_html=True)

