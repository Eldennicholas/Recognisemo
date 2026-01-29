'''import streamlit as st
from textblob import TextBlob
import random
from database import save_mood

songs = ["https://open.spotify.com/track/1zB4vmk8tFRmM9UULNzbLB"]
quotes = ["Believe in yourself. Every day is a new chance."]
tips = ["Take a walk. Breathe. Hydrate. Listen to calm music."]

st.title("🌈 EmoSphere")

if "email" not in st.session_state:
    st.warning("Please login first.")
    st.stop()

st.markdown(f"**Logged in as: {st.session_state.email}**", unsafe_allow_html=True)
user_input = st.text_area("📝 Write about your day:", height=200)

def detect_mood(text):
    if not text:
        return "neutral"
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.3:
        return "happy"
    elif polarity < -0.1:
        return "sad"
    else:
        return "neutral"

if st.button("Analyze Mood"):
    mood = detect_mood(user_input)
    save_mood(st.session_state.username, mood)
    st.success(f"Detected Mood: **{mood.capitalize()}**")

    if mood == "happy":
        st.markdown(f"[🎶 Enjoy this song]({random.choice(songs)})")
    elif mood == "neutral":
        st.markdown(f"💬 Motivation: *{random.choice(quotes)}*")
    elif mood == "sad":
        st.markdown(f"🧘 Mental Health Tip: {random.choice(tips)}")

    st.page_link("pages/3_SenseLab.py", label="👉 Go to Sense Lab", icon="📊")'''
