import streamlit as st
from pages import login, dashboard, monitor_traffic, monitor_anomalies, firewall_policies, site_monitoring

PAGES = {
    "Login": login,
    "Dashboard": dashboard,
    "Monitor Traffic": monitor_traffic,
    "Monitor Anomalies": monitor_anomalies,
    "Firewall Policies": firewall_policies,
    "Site Monitoring": site_monitoring
}

def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]
    page.app()

if __name__ == "__main__":
    main()
