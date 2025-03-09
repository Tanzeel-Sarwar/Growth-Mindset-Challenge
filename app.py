import streamlit as st
import random
import datetime

# Set page title and icon
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="💡", layout="centered")

# Custom CSS for better UI design
st.markdown(
    """
    <style>
    body {
        background-color: #f4f4f4;
    }
    .stApp {
        background: linear-gradient(to bottom, #4facfe, #00f2fe);
        color: white;
    }
    .title {
        font-size: 32px;
        font-weight: bold;
        text-align: center;
        color: #fff;
    }
    .box {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
    }
    .button {
        background: #ff5f6d;
        color: white;
        padding: 10px;
        border-radius: 8px;
        text-align: center;
        font-weight: bold;
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
]

# Motivational quotes
quotes = [
    "“The only way to grow is to challenge yourself.”",
    "“Failure is an opportunity to learn.”",
    "“Small progress each day leads to big results.”",
    "“With effort, you can always improve.”",
    "“Your potential is limitless with the right mindset.”",
]

# Generate a challenge based on the day
today = datetime.date.today().strftime("%Y-%m-%d")
random.seed(today)  # Ensures the challenge remains the same for the day
daily_challenge = random.choice(challenges)
motivational_quote = random.choice(quotes)

# UI Layout
st.markdown('<p class="title">🌱 Growth Mindset Challenge</p>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.subheader("✨ Today's Challenge")
    st.write(f"👉 {daily_challenge}")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.subheader("💡 Motivational Quote")
    st.write(f"📝 {motivational_quote}")
    st.markdown("</div>", unsafe_allow_html=True)

# User Reflection
st.subheader("📝 Your Reflection")
reflection = st.text_area("Write about your experience with today's challenge:")

if st.button("Submit Reflection"):
    if reflection.strip():
        st.success("✅ Reflection saved! Keep growing! 🌱")
    else:
        st.warning("⚠️ Please write something before submitting.")

# Footer
st.markdown("---")
st.write("💖 Keep pushing forward with a growth mindset!")

