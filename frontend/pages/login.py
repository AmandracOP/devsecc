import streamlit as st
import requests

def app():
    st.title("Login")

    # Input fields for username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Button to trigger login
    if st.button("Login"):
        # Send a POST request to the login endpoint
        response = requests.post("http://localhost:5000/login", json={"username": username, "password": password})

        if response.status_code == 200:
            # On successful login, set session state and redirect to dashboard
            st.session_state.logged_in = True
            st.success("Login successful!")
            st.experimental_rerun()  # Reload the app to show the main content
        else:
            st.error("Invalid credentials!")
