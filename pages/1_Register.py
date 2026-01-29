import streamlit as st
from database import register_user

st.title("📝 Register")

username = st.text_input("Choose a Username")
email = st.text_input("Enter your email")
password = st.text_input("Choose a Password", type="password")

if st.button("Register"):
    register_user(username,email, password)
    st.success("Registered successfully. Now log in from the home page.")
