import streamlit as st
import random
import datetime

# Set page title and layout
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌱", layout="wide")

# Custom Styling
st.markdown(
    """
    <style>
    body {
        font-family: 'Arial', sans-serif;
    }
    .title {
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        color: #4CAF50;
    }
    .subtitle {
        font-size: 20px;
        text-align: center;
        color: #555;
        margin-bottom: 20px;
    }
    .box {
        background: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .button {
        background: #4CAF50;
        color: white;
        padding: 10px 15px;
        border-radius: 8px;
        font-size: 16px;
        border: none;
        cursor: pointer;
    }
    .button:hover {
        background: #45a049;
    }
    .text-area {
        width: 100%;
        height: 120px;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #ccc;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Growth mindset challenges
challenges = [
    "Embrace a challenge you’ve been avoiding.",
    "Reframe a past failure as a lesson learned.",
    "Give yourself positive affirmations today.",
    "Celebrate small progress instead of perfection.",
    "Ask for constructive feedback and apply it.",
    "Step outside your comfort zone today.",
    "Learn something new and share it with someone.",
]

# Motivational quotes
quotes = [
    "“The only way to grow is to challenge yourself.”",
    "“Failure is an opportunity to learn.”",
    "“Small progress each day leads to big results.”",
    "“With effort, you can always improve.”",
    "“Your potential is limitless with the right mindset.”",
]

# Get today's challenge (based on date)
today = datetime.date.today().strftime("%Y-%m-%d")
random.seed(today)
daily_challenge = random.choice(challenges)
motivational_quote = random.choice(quotes)

# App Layout
st.markdown('<p class="title">🌱 Growth Mindset Challenge</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Start your journey towards a growth mindset today!</p>', unsafe_allow_html=True)

# Section: User's Own Challenge
st.subheader("✍️ Create Your Own Challenge")
user_challenge = st.text_input("Write your own challenge for today:")

# Section: Predefined Challenge & Motivation
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.subheader("✨ Today's Challenge")
    st.write(f"👉 **{user_challenge if user_challenge else daily_challenge}**")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.subheader("💡 Motivational Quote")
    st.write(f"📝 *{motivational_quote}*")
    st.markdown("</div>", unsafe_allow_html=True)

# Progress Bar (Tracking Completion)
st.subheader("📊 Progress Tracker")
completed = st.slider("How much did you complete today?", 0, 100, 50)
st.progress(completed / 100)

# User Reflection
st.subheader("📝 Your Reflection")
reflection = st.text_area("Write about your experience with today's challenge:", height=150)

if st.button("Submit Reflection", key="reflection_submit"):
    if reflection.strip():
        st.success("✅ Reflection saved successfully! Keep pushing forward! 🌱")
    else:
        st.warning("⚠️ Please write something before submitting.")

# Section: Overcome Challenge
st.subheader("💪 Overcome Challenge")
overcome_challenge = st.text_area("Write about a past challenge you have overcome:", height=150)

if st.button("Save Overcome Challenge", key="overcome_submit"):
    if overcome_challenge.strip():
        st.success("🎉 Well done! Overcoming challenges makes you stronger! 💪")
    else:
        st.warning("⚠️ Please write something before submitting.")

# Section: Celebrate Achievements
st.subheader("🎉 Celebrate Achievements")
achievement = st.text_area("Write about something you achieved recently:", height=150)

if st.button("Save Achievement", key="achievement_submit"):
    if achievement.strip():
        st.success("🥳 Awesome! Celebrate every success, big or small! 🎊")
    else:
        st.warning("⚠️ Please write something before submitting.")

# Section: Inspiration
st.subheader("🌟 Inspiration")
st.write("🔹 **What inspires you?** Write about a person, book, or experience that keeps you motivated.")

inspiration = st.text_area("Write your source of inspiration:", height=150)

if st.button("Save Inspiration", key="inspiration_submit"):
    if inspiration.strip():
        st.success("💡 Keep this inspiration close to your heart! 🚀")
    else:
        st.warning("⚠️ Please write something before submitting.")

# Challenge History
st.subheader("📜 Previous Challenges")
if "history" not in st.session_state:
    st.session_state.history = []
    
if st.button("Save Today's Challenge"):
    st.session_state.history.append(user_challenge if user_challenge else daily_challenge)
    
if st.session_state.history:
    for idx, past_challenge in enumerate(reversed(st.session_state.history), 1):
        st.write(f"🔹 {idx}. {past_challenge}")

# Footer
st.markdown("---")
st.markdown('<p style="text-align: center; font-size: 18px;">The app is created by <b>Tanzeel Sarwar</b> 💡</p>', unsafe_allow_html=True)

