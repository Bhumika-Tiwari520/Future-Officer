import streamlit as st
import random
import time

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="NDA Prep 🪖", layout="wide")

# -------------------- CUSTOM CSS --------------------
st.markdown("""
<style>

/* Background */
body {
    background-color: #f5f5dc;
}

/* Dark mode */
[data-theme="dark"] {
    background-color: #1a1a1a;
    color: white;
}

/* Card Style */
.card {
    background: #ffffff;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    margin-bottom: 15px;
}

/* Headings */
.title {
    color: #556B2F;
    font-weight: bold;
}

/* Status dots */
.red {color: red;}
.yellow {color: goldenrod;}
.green {color: green;}

</style>
""", unsafe_allow_html=True)

# -------------------- SIDEBAR --------------------
st.sidebar.title("🪖 NDA Companion")
section = st.sidebar.radio("Navigate", [
    "🏠 Home",
    "📚 Study",
    "📝 Quiz",
    "📊 Tracker",
    "💪 Fitness",
    "🧠 Tricks",
    "📖 NDA Info"
])

# -------------------- MOTIVATIONAL POPUP --------------------
messages = [
    "🔥 Great job Cadet!",
    "⚠️ You are behind today!",
    "🪖 Stay disciplined!",
    "🏅 Victory belongs to the prepared!",
]

st.toast(random.choice(messages))

# -------------------- HOME --------------------
if section == "🏠 Home":
    st.markdown("<h1 class='title'>Future Officer in Making ✨🪖</h1>", unsafe_allow_html=True)

    quotes = [
        "Discipline is the strongest weapon.",
        "Pain is temporary, pride is forever.",
        "Train hard, fight easy.",
        "You don't find willpower, you create it.",
        "Small efforts daily = Big success."
    ]

    st.markdown(f"<div class='card'>💬 {random.choice(quotes)}</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
    📅 <b>Today's Mission</b><br>
    📚 Study Maths (1 hr)<br>
    🏃 Run 1.6 km<br>
    💪 Pushups + Situps
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='card'>🔥 Streak: 3 days</div>", unsafe_allow_html=True)

    st.progress(0.6)
    st.write("Progress: 60% 🏅")

# -------------------- STUDY --------------------
elif section == "📚 Study":
    st.title("📚 Study Section")

    subjects = {
        "Maths 📐": {
            "Algebra": "Solve equations like ax+b=c easily.",
            "Trigonometry": "sin, cos, tan basics and identities.",
            "Calculus": "Understand limits and derivatives."
        },
        "English ✍️": {
            "Grammar": "Tenses, articles, sentence correction.",
            "Vocabulary": "Learn 5 words daily.",
            "Comprehension": "Read passage and answer."
        },
        "GK 🌍": {
            "History": "Freedom struggle basics.",
            "Geography": "Rivers, mountains, climate.",
            "Polity": "Constitution basics."
        }
    }

    for subject, topics in subjects.items():
        st.subheader(subject)

        for topic, note in topics.items():
            col1, col2 = st.columns([4,1])

            with col1:
                with st.expander(f"📖 {topic}"):
                    st.write(f"🧠 {note}")
                    st.write("🔁 Revise after 3 days")

            with col2:
                status = random.choice(["🔴", "🟡", "🟢"])
                st.markdown(status)

# -------------------- QUIZ --------------------
elif section == "📝 Quiz":
    st.title("📝 MCQ Quiz")

    questions = [
        {"q": "2+2=?", "a": ["3","4","5"], "ans": "4"},
        {"q": "Capital of India?", "a": ["Delhi","Mumbai","Kolkata"], "ans": "Delhi"},
        {"q": "Sun rises in?", "a": ["West","East","North"], "ans": "East"},
        {"q": "5×5=?", "a": ["10","20","25"], "ans": "25"},
        {"q": "Opposite of Good?", "a": ["Bad","Nice","Happy"], "ans": "Bad"},
        {"q": "Independence year?", "a": ["1947","1950","1930"], "ans": "1947"},
        {"q": "Water formula?", "a": ["H2O","CO2","O2"], "ans": "H2O"},
        {"q": "Largest planet?", "a": ["Earth","Mars","Jupiter"], "ans": "Jupiter"},
        {"q": "5+7=?", "a": ["10","11","12"], "ans": "12"},
        {"q": "National animal?", "a": ["Lion","Tiger","Elephant"], "ans": "Tiger"}
    ]

    st.write("⏱ Timer: 30 seconds (simulated)")
    time.sleep(1)

    answers = []

    for i, q in enumerate(questions):
        ans = st.radio(q["q"], q["a"], key=i)
        answers.append(ans)

    if st.button("Submit 🎯"):
        score = 0

        for i, q in enumerate(questions):
            if answers[i] == q["ans"]:
                st.success(f"Q{i+1}: Correct ✅")
                score += 1
            else:
                st.error(f"Q{i+1}: Wrong ❌ (Ans: {q['ans']})")

        st.markdown(f"<div class='card'>🏅 Score: {score}/10</div>", unsafe_allow_html=True)

# -------------------- TRACKER --------------------
elif section == "📊 Tracker":
    st.title("📊 Study Tracker")

    hours = st.number_input("📚 Study hours today:", 0, 12)

    st.markdown("<div class='card'>🔥 Streak: 4 days</div>", unsafe_allow_html=True)

    st.write("📅 Weekly Progress")
    st.progress(min(hours/10,1.0))

# -------------------- FITNESS --------------------
elif section == "💪 Fitness":
    st.title("💪 Physical Fitness")

    tasks = [
        "🏃 Run 1.6 km",
        "💪 Pushups (20 boys / 10 girls)",
        "🧘 Situps (25 boys / 15 girls)",
        "🏋️ Pullups (5)"
    ]

    completed = 0

    for task in tasks:
        if st.checkbox(task):
            completed += 1

    percent = int((completed/len(tasks))*100)

    st.progress(percent)
    st.markdown(f"<div class='card'>🏅 Completion: {percent}%</div>", unsafe_allow_html=True)

# -------------------- TRICKS SECTION --------------------
elif section == "🧠 Tricks":
    st.title("🧠 Memory Tricks & Mnemonics")

    st.markdown("""
    <div class='card'>
    🌍 <b>GK Trick:</b><br>
    🪖 "MUGHAL" = M → Mahmud, U → Uday, G → Ghori, H → Humayun, A → Akbar, L → Lodhi
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
    ✍️ <b>English Trick:</b><br>
    📚 FANBOYS = For, And, Nor, But, Or, Yet, So
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
    📐 <b>Math Trick:</b><br>
    ✨ (a+b)² = a² + b² + 2ab (remember with triangle shape 🔺)
    </div>
    """, unsafe_allow_html=True)

# -------------------- NDA INFO --------------------
elif section == "📖 NDA Info":
    st.title("📖 NDA Information")

    st.markdown("""
    <div class='card'>
    📝 <b>Exam Pattern</b><br>
    Maths: 300 marks<br>
    GAT: 600 marks
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
    📚 <b>Subjects</b><br>
    Maths 📐<br>
    English ✍️<br>
    GK 🌍
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
    🪖 <b>Selection Process</b><br>
    1️⃣ Written Exam<br>
    2️⃣ SSB Interview<br>
    3️⃣ Medical Test
    </div>
    """, unsafe_allow_html=True)

    st.success("✨ Stay consistent Cadet! Victory awaits 🪖")
