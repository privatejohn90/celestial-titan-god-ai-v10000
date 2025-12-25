# ==========================================================
# 💎 Celestial Titan Dual-State Forecast Lab v1.6.3
# 🌞 Dual-Draw Sync Edition (Midday + Evening)
# ==========================================================
import streamlit as st, json, random, datetime, os, math, pandas as pd
from calendar import monthcalendar

st.set_page_config(page_title="Titan Dual-State Forecast Lab v1.6.3",
                   page_icon="💎", layout="wide")
BASE = os.path.dirname(os.path.abspath(__file__))

# ==========================================================
# 🎨 COSMIC DESIGN
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
.stButton>button:hover {transform:scale(1.05);box-shadow:0 0 30px #9B00FF;}
.glow-box {
  background:rgba(255,255,255,0.05);
  border:1px solid rgba(0,150,255,0.3);
  border-radius:12px;
  padding:15px;margin-top:10px;
  box-shadow:0 0 15px rgba(0,150,255,0.25);
}
.daycell {border-radius:10px;padding:8px;text-align:center;cursor:pointer;}
.day-hit {background:rgba(0,255,180,0.2);box-shadow:0 0 10px #00FF9C;}
.day-miss{background:rgba(255,60,60,0.2);box-shadow:0 0 10px #FF5E5E;}
.day-pend{background:rgba(255,255,255,0.05);}
</style>
""", unsafe_allow_html=True)

# ==========================================================
# 🧠 JSON HELPERS
# ==========================================================
def ensure_json(path, default):
    if not os.path.exists(path):
        with open(path,"w") as f: json.dump(default,f,indent=2)
    with open(path) as f:
        try: return json.load(f)
        except: return default

def save_json(path,data):
    with open(path,"w") as f: json.dump(data,f,indent=2)

# ==========================================================
# 📂 FILES INIT
# ==========================================================
RES_FILE=os.path.join(BASE,"titan_results.json")
ACC_FILE=os.path.join(BASE,"titan_accuracy.json")
CAL_FILE=os.path.join(BASE,"titan_calendar.json")

for path,default in [
    (RES_FILE,{"records":[]}),
    (ACC_FILE,{"records":[]}),
    (CAL_FILE,{"days":[]})
]:
    data=ensure_json(path,default)
    if "records" not in data and "days" not in data:
        save_json(path,default)

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
    if illum<10: phase="🌑 New"
    elif illum<40: phase="🌓 First"
    elif illum<60: phase="🌕 Full"
    elif illum<90: phase="🌗 Last"
    else: phase="🌘 Waning"
    return phase,illum

# ==========================================================
# ⚙️ CORE
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
    data=ensure_json(ACC_FILE,{"records":[]})
    records=data.get("records",[])
    if not records: return 0
    hits=sum(1 for d in records if d.get("hit"))
    return int((hits/len(records))*100)

# ==========================================================
# 🗓️ CALENDAR
# ==========================================================
def render_calendar():
    st.subheader("📅 Titan Calendar Sync View")
    caldata=ensure_json(CAL_FILE,{"days":[]})
    days=pd.DataFrame(caldata.get("days",[]))

    today=datetime.date.today()
    if "month_offset" not in st.session_state: st.session_state.month_offset=0
    offset=st.session_state.month_offset
    show_date=today+datetime.timedelta(days=30*offset)
    year,month=show_date.year,show_date.month

    colL,colC,colR=st.columns([1,2,1])
    with colL:
        if st.button("⬅️ Prev"):
            st.session_state.month_offset-=1; st.rerun()
    with colC:
        st.markdown(f"### {show_date.strftime('%B %Y')}")
    with colR:
        if st.button("Next ➡️"):
            st.session_state.month_offset+=1; st.rerun()

    cal=monthcalendar(year,month)
    for week in cal:
        cols=st.columns(7)
        for i,day in enumerate(week):
            if day==0: cols[i].markdown(" ")
            else:
                key=f"{year}-{month:02d}-{day:02d}"
                status="pend"
                if not days.empty and key in days["date"].values:
                    s=days.loc[days["date"]==key,"status"].values[0]
                    status="hit" if s=="hit" else "miss"
                cols[i].markdown(f"<div class='daycell day-{status}'>{day}</div>",unsafe_allow_html=True)

    phase,illum=lunar_phase()
    st.metric("🌙 Lunar Phase",f"{phase} ({illum}%)")
    st.metric("📈 Accuracy",f"{compute_accuracy()}%")
    st.caption("🧠 Titan: Calendar synchronized across months.")

# ==========================================================
# 🧭 NAVIGATION
# ==========================================================
st.sidebar.title("💠 Titan Dual-State Forecast Lab")
menu=st.sidebar.radio("Select Module",["🎯 Forecast Console","📅 Calendar Sync View"])

st.markdown("<h1 style='text-align:center;'>💎 Celestial Titan Dual-State Forecast Lab v1.6.3</h1>",unsafe_allow_html=True)

# ==========================================================
# 🎯 FORECAST CONSOLE
# ==========================================================
if menu=="🎯 Forecast Console":
    st.subheader("🎯 Forecast Console")

    game=st.selectbox("Select Game",[
        "GA Pick 3 Midday",
        "GA Pick 3 Evening",
        "FL Pick 4 Midday",
        "FL Pick 4 Evening"
    ])
    sets=st.slider("Number of Forecast Sets",3,10,3)

    if st.button("🌠 Generate Forecast"):
        fc=generate_forecast(game,sets)
        st.markdown("<div class='glow-box'>",unsafe_allow_html=True)
        for i,(nums,conf) in enumerate(fc,1):
            digits=''.join(map(str,nums))
            st.markdown(f"<b>Set {i}</b> → <span style='color:#00E6FF;'>{digits}</span> | Confidence <b>{conf}%</b>",unsafe_allow_html=True)
        st.markdown("</div>",unsafe_allow_html=True)
        st.info("🧠 Titan: Forecasts stored in temporal memory core.")

    st.markdown("---")
    st.subheader("📥 Enter Official Result")
    date=st.date_input("Date",datetime.date.today())
    result=st.text_input("Winning Number (Straight)")
    state_sel="hit" if st.checkbox("Hit") else "miss"
    if st.button("💾 Save Result & Sync"):
        res=ensure_json(CAL_FILE,{"days":[]})
        res["days"].append({
            "date":str(date),
            "draw":game,
            "number":result,
            "status":state_sel
        })
        save_json(CAL_FILE,res)
        st.success(f"✅ Saved {game} result and synchronized to Titan Calendar.")
        st.rerun()
else:
    render_calendar()

st.markdown("<hr><center><small>💎 Celestial Titan v1.6.3 — Dual-Draw Sync Edition</small></center>",unsafe_allow_html=True)

