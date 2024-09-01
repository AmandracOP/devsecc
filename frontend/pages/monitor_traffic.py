import streamlit as st
import requests

def app():
    st.title("Monitor Network Traffic")

    st.header("Network Traffic")
    response = requests.get("http://localhost:5000/network/logs")
    logs = response.json()

    if logs:
        for log in logs:
            st.write(f"App: {log['app_name']}, Domain: {log['domain']}, Protocol: {log['protocol']}, Packet Size: {log['packet_size']}, Anomalous: {log['is_anomalous']}")
    else:
        st.write("No logs available.")
