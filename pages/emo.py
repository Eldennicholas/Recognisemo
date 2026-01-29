import streamlit as st
import pickle
import numpy as np
import requests

with open("../improved_mood_model(1).pkl", "rb") as f:
    model = pickle.load(f)

with open("../improved_tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)


# Mood-based static responses (except sad, which will use API)
responses = {
    "happy": {
        "title": "You're Radiating Joy! 🎉",
        "content": "Here's a feel-good song for you: [Happy - Pharrell Williams](https://www.youtube.com/watch?v=ZbZSe6N_BXs)"
    },
    "neutral": {
        "title": "Chill Vibes Only 😌",
        "content": "Here's a gentle nudge of inspiration:\n\n> “Every day may not be good... but there's something good in every day.”"
    },
    "depression": {
        "title": "We're With You 💜",
        "content": "You matter. Please don’t hesitate to seek support. Try these:\n- [iCall Support](https://icallhelpline.org)\n- [7 Cups](https://www.7cups.com)\n- Talk to a friend or professional therapist."
    },
    "anxiety": {
        "title": "Breathe In, Breathe Out 🧘‍♂️",
        "content": "Try this 4-7-8 breathing technique:\n1. Inhale through your nose for 4 seconds\n2. Hold your breath for 7 seconds\n3. Exhale through your mouth for 8 seconds\n\nRepeat for 3–4 cycles."
    }
}

# Function to fetch a motivational quote
def get_motivational_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random")
        if response.status_code == 200:
            data = response.json()
            quote = data[0]["q"]
            author = data[0]["a"]
            return f"> “{quote}”\n\n— *{author}*"
        else:
            return "> “This too shall pass.”"
    except:
        return "> “Keep going. Everything you need will come to you at the perfect time.”"

# EmoSphere UI
def emosphere_page(username):
    st.title("🌈 Welcome to EmoSphere")
    st.markdown(f"Hello, **{username}**! Let's understand how you're feeling today.")

    user_input = st.text_area("📝 Share what's on your mind...", placeholder="Type your thoughts here...")

    if st.button("Analyze Mood"):
        if user_input.strip() == "":
            st.warning("Please enter some text before analyzing.")
            return

        # Transform input and predict mood
        X_input = vectorizer.transform([user_input])
        prediction = model.predict(X_input)[0]

        # Display result
        st.success(f"Predicted Mood: **{prediction.capitalize()}**")
        st.subheader("Mood Insight 💡")

        if prediction == "sad":
            st.markdown("### Hey, It's Okay to Feel Sad 💙")
            quote = get_motivational_quote()
            st.markdown("Here's a motivational quote for you:")
            st.markdown(quote)
        else:
            st.subheader(responses[prediction]["title"])
            st.markdown(responses[prediction]["content"])

# Example use (during integration)
# emosphere_page("Elden")
