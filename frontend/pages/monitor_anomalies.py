import streamlit as st
import requests

def app():
    st.title("Monitor Anomalies")

    st.header("Anomalies Detected")
    response = requests.get("http://localhost:5000/network/logs")
    logs = response.json()

    anomalous_logs = [log for log in logs if log['is_anomalous']]

    if anomalous_logs:
        for log in anomalous_logs:
            st.write(f"App: {log['app_name']}, Domain: {log['domain']}, Protocol: {log['protocol']}, Packet Size: {log['packet_size']}, Anomalous: {log['is_anomalous']}")
    else:
        st.write("No anomalies detected.")
