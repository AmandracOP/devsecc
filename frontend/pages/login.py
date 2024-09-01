import streamlit as st
import requests

def app():
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Correcting the keys in the JSON payload
        response = requests.post("http://localhost:5000/login", json={"username": username, "password": password})
        if response.status_code == 200:
            st.success("Login successful!")
            # Redirect to dashboard or set session state
        else:
            st.error("Invalid credentials!")