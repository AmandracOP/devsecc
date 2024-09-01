import streamlit as st
import requests

def app():
    st.title("Site Monitoring")

    st.header("Monitoring Sites")

    # Example: Fetch site status (Here you would actually ping the sites or use a monitoring tool)
    sites = ["https://www.example.com", "https://www.test.com"]
    for site in sites:
        status = requests.get(site).status_code
        st.write(f"Site: {site}, Status: {status}")
