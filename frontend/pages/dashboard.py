import streamlit as st
import requests

def app():
    st.title("Dashboard")

    st.header("Traffic Overview")
    response = requests.get("http://localhost:5000/network/logs")
    logs = response.json()
    
    if logs:
        st.write("Recent Network Logs:")
        for log in logs:
            st.write(f"App: {log['app_name']}, Domain: {log['domain']}, Protocol: {log['protocol']}, Packet Size: {log['packet_size']}, Anomalous: {log['is_anomalous']}")
    else:
        st.write("No logs available.")

    st.header("Firewall Policies")
    response = requests.get("http://localhost:5000/firewall/policies")
    policies = response.json()

    if policies:
        st.write("Active Policies:")
        for policy in policies:
            st.write(f"App: {policy['app_name']}, Domain: {policy['domain']}, Protocol: {policy['protocol']}, Action: {policy['action']}")
    else:
        st.write("No policies available.")
