import streamlit as st
from database import login_user

st.set_page_config(page_title="Recognisemo - Login", page_icon="💜")

st.title("💜 Welcome to Sense")

email = st.text_input("email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    user = login_user(email, password)
    if user:
        st.session_state.email = email
        st.success(f"logged in successfully!")
        st.switch_page("pages/2_EmoSphere.py")
    else:
        st.error("Invalid credentials.")

st.markdown("Don't have an account? [Register here](pages/1_Register.py)")
