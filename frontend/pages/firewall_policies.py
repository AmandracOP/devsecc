import streamlit as st
import requests

def app():
    st.title("Manage Firewall Policies")

    st.header("Active Firewall Policies")
    response = requests.get("http://localhost:5000/firewall/policies")
    policies = response.json()

    if policies:
        for policy in policies:
            st.write(f"App: {policy['app_name']}, Domain: {policy['domain']}, Protocol: {policy['protocol']}, Action: {policy['action']}")
    else:
        st.write("No policies available.")

    st.header("Add/Update Policy")
    app_name = st.text_input("Application Name")
    domain = st.text_input("Domain")
    protocol = st.selectbox("Protocol", ["TCP", "UDP", "ICMP"])
    action = st.selectbox("Action", ["Allow", "Block"])

    if st.button("Submit"):
        payload = {
            "app_name": app_name,
            "domain": domain,
            "protocol": protocol,
            "action": action
        }
        response = requests.post("http://localhost:5000/firewall/policy", json=payload)
        if response.status_code == 201:
            st.success("Policy added/updated successfully!")
        else:
            st.error("Failed to add/update policy.")
