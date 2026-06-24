import streamlit as st

st.set_page_config(
    page_title="Aura AI",
    page_icon="💜",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

.stApp{
background: linear-gradient(180deg,#050816,#0c1028,#141033);
color:white;
}

.hero{
background:rgba(255,255,255,0.05);
padding:30px;
border-radius:20px;
backdrop-filter: blur(15px);
box-shadow:0px 0px 25px rgba(140,82,255,0.3);
}

.feature-card{
background:#12182d;
padding:20px;
border-radius:18px;
text-align:center;
border:1px solid rgba(255,255,255,0.1);
transition:0.3s;
}

.feature-card:hover{
transform:translateY(-5px);
}

</style>
""",unsafe_allow_html=True)

st.markdown("""
<div class='hero'>
<h1>💜 Aura AI</h1>
<h3>Your Safe Space. Your Growth Partner.</h3>
</div>
""",unsafe_allow_html=True)

st.write("")
st.write("")

col1,col2,col3,col4=st.columns(4)

with col1:
    st.info("🤖 AI Chat")

with col2:
    st.info("📓 Mood Journal")

with col3:
    st.info("🔥 Burnout Detector")

with col4:
    st.info("🛡️ Safety Tools")
import streamlit as st
import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-1.5-flash")

st.title("🤖 Aura AI Support Chat")

if "messages" not in st.session_state:
    st.session_state.messages=[]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt=st.chat_input("How are you feeling today?")

if prompt:
    st.session_state.messages.append(
        {"role":"user","content":prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)

    response=model.generate_content(
    f"""
    You are Aura AI.
    Speak gently.
    Comfort the user.
    Encourage healthy habits.
    Give practical advice.
    Never judge.
    User: {prompt}
    """
    )

    reply=response.text

    with st.chat_message("assistant"):
        st.write(reply)

    st.session_state.messages.append(
        {"role":"assistant","content":reply}
    )
import streamlit as st
from datetime import date

st.title("📓 Mood Journal")

mood=st.select_slider(
    "How are you feeling?",
    options=[
        "😊 Happy",
        "😌 Calm",
        "😔 Sad",
        "😟 Stressed",
        "😡 Angry"
    ]
)

journal=st.text_area("Write your thoughts")

if st.button("Save Entry"):
    st.success("Journal Saved 💜")
import streamlit as st

st.title("🔥 Burnout Detector")

sleep=st.slider("Hours of sleep",0,12,7)
study=st.slider("Study Hours",0,15,5)
stress=st.slider("Stress Level",1,10,5)

score=(study*5)+(stress*8)-(sleep*4)

score=max(0,min(score,100))

st.progress(score/100)

st.metric("Burnout Risk",f"{score}%")

if score<40:
    st.success("Low Risk")
elif score<70:
    st.warning("Moderate Risk")
else:
    st.error("High Risk")
import streamlit as st
import google.generativeai as genai

st.title("⚠ Situation Analyzer")

situation=st.text_area(
"Describe what happened"
)

if st.button("Analyze"):

    response=model.generate_content(
    f"""
    Analyze the situation.
    Detect:
    - Risk level
    - Peer pressure
    - Emotional manipulation
    - Safety concerns
    Give advice.

    Situation:
    {situation}
    """
    )

    st.write(response.text)
import streamlit as st

st.title("🎯 Focus Mode")

minutes=st.number_input(
"Pomodoro Minutes",
25
)

st.metric("Focus Session",f"{minutes}:00")
import streamlit as st

st.title("🛡 Safety Tools")

st.error("🚨 SOS Emergency")

if st.button("Send SOS"):
    st.success("Emergency Alert Sent")

st.button("📍 Share Location")
st.button("📞 Emergency Call")
st.button("👥 Trusted Contacts")
import streamlit as st

st.title("🌿 Wellness Hub")

st.button("🧘 Meditation")

st.button("🌬 Breathing Exercise")

st.button("🎵 Relaxing Music")

st.button("✨ Positive Affirmations")
import streamlit as st
import plotly.express as px
import pandas as pd

st.title("📈 Progress Insights")

data=pd.DataFrame({
"Day":["Mon","Tue","Wed","Thu","Fri"],
"Mood":[5,6,7,4,8]
})

fig=px.line(data,x="Day",y="Mood")

st.plotly_chart(fig)
