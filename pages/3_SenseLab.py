import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from database import get_mood_history

st.title("📊 Sense Lab - Mood Trends")

if "username" not in st.session_state:
    st.warning("Please login first.")
    st.stop()

history = get_mood_history(st.session_state.username)

if not history:
    st.info("No mood history found yet.")
    st.stop()

df = pd.DataFrame(history, columns=["Date", "Mood"])
mapping = {"sad": 1, "neutral": 2, "happy": 3}
df["Value"] = df["Mood"].map(mapping)

plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["Value"], marker="o", color="purple")
plt.yticks([1, 2, 3], ["Sad", "Neutral", "Happy"])
plt.xticks(rotation=45)
plt.title("Mood Trend Over 15 Days")
plt.grid(True)
st.pyplot(plt)
  

