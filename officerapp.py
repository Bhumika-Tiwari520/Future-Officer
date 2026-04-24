import streamlit as st

st.set_page_config(page_title="NDA Prep Dashboard", layout="wide")

# ---------------------- CUSTOM CSS ----------------------
st.markdown("""
<style>

/* Background Gradient */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #3A5F0B, #F5F5DC);
    color: #1e1e1e;
}

/* Card Design */
.card {
    background: rgba(255,255,255,0.9);
    border-radius: 18px;
    padding: 20px;
    margin: 10px 0;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}

/* Header */
.header {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #2e3d1f;
}

.subheader {
    text-align: center;
    font-size: 20px;
    margin-bottom: 10px;
}

/* Quote */
.quote {
    text-align: center;
    font-style: italic;
    font-size: 18px;
    padding: 10px;
}

/* Buttons */
.stButton button {
    border-radius: 25px;
    background-color: #3A5F0B;
    color: white;
    border: none;
    padding: 10px 20px;
    transition: 0.3s;
}

.stButton button:hover {
    background-color: #2e4a08;
    transform: scale(1.05);
}

/* Divider */
.divider {
    border-top: 2px solid #3A5F0B;
    margin: 20px 0;
}

/* Glow Highlight */
.highlight {
    background: #e6f2d9;
    padding: 10px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(58,95,11,0.5);
}

</style>
""", unsafe_allow_html=True)

# ---------------------- HEADER ----------------------
st.markdown('<div class="header">🎖️ NDA Preparation Dashboard 🇮🇳</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">🎯 Your Mission: Discipline • Strategy • Success</div>', unsafe_allow_html=True)

st.markdown('<div class="quote">"Success in NDA is not luck — it is preparation meeting courage." 💂‍♂️</div>', unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ---------------------- STUDY PLAN ----------------------
st.markdown("## 📚 Study Strategy 📖")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
    <h3>📘 Mathematics 🧮</h3>
    <ul>
        <li><b>What to Study:</b> Algebra, Trigonometry, Calculus, Matrices</li>
        <li><b>How to Study:</b> Practice daily problems, revise formulas</li>
        <li><b>Strategy:</b> Focus on speed & accuracy ⏱️</li>
        <li><b>Books:</b> NCERT + Previous Year Papers</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h3>📗 General Ability Test 🧠</h3>
    <ul>
        <li><b>English:</b> Grammar, Vocabulary, Comprehension</li>
        <li><b>GK:</b> Physics, Chemistry, History, Geography</li>
        <li><b>How to Study:</b> Daily reading + notes</li>
        <li><b>Tip:</b> Stay updated with current affairs 📰</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# ---------------------- SSB PREP ----------------------
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown("## 🪖 SSB Interview Preparation 🎯")

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <div class="card">
    <h3>🧠 Psychology Tests 🧩</h3>
    <ul>
        <li>TAT, WAT, SRT, SD</li>
        <li>Focus on natural responses</li>
        <li>Practice storytelling daily ✍️</li>
        <li>Improve clarity of thought</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card">
    <h3>👥 GTO Tasks 🏃</h3>
    <ul>
        <li>Group Discussions & Planning</li>
        <li>Outdoor Tasks & Obstacles</li>
        <li>Leadership & Teamwork 🤝</li>
        <li>Stay confident & active</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# ---------------------- PHYSICAL FITNESS ----------------------
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown("## 🏃 Physical Fitness ⚡")

col5, col6 = st.columns(2)

with col5:
    st.markdown("""
    <div class="card">
    <h3>🏋️ Daily Routine</h3>
    <ul>
        <li>Running: 2–5 km daily 🏃</li>
        <li>Pushups & Situps</li>
        <li>Stamina training</li>
        <li>Flexibility exercises</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown("""
    <div class="card">
    <h3>🥗 Diet & Health</h3>
    <ul>
        <li>Protein-rich diet</li>
        <li>Stay hydrated 💧</li>
        <li>Good sleep cycle 😴</li>
        <li>Avoid junk food</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# ---------------------- MOCK TEST ----------------------
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown("## ⏱️ Practice & Mock Tests 🎯")

st.markdown("""
<div class="card">
<ul>
    <li>Attempt weekly mock tests</li>
    <li>Analyze mistakes deeply 🔍</li>
    <li>Improve time management ⏳</li>
    <li>Revise weak areas regularly</li>
</ul>
</div>
""", unsafe_allow_html=True)

if st.button("🚀 Start Practice Test"):
    st.success("🔥 Mission Started! Stay Focused Soldier!")

# ---------------------- FINAL MOTIVATION ----------------------
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="highlight">
<h3>🏅 Final Motivation</h3>
<p>
Discipline beats talent. Consistency builds officers. 
Stay focused, stay sharp, and remember — every small effort today builds the officer you want to become tomorrow 🇮🇳
</p>
</div>
""", unsafe_allow_html=True)
