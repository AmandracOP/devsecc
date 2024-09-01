import streamlit as st
from pages import login, dashboard, monitor_traffic, monitor_anomalies, firewall_policies, site_monitoring
from components.navbar import navbar
from components.footer import footer

# Load CSS
def load_css():
    with open('frontend/static/styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def main():
    # Load custom CSS
    load_css()

    # Initialize session state if not present
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    # Show login page if not logged in
    if not st.session_state.logged_in:
        login.app()
    else:
        # Display the navbar at the top
        selection = navbar()

        # Get the page function and execute it
        PAGES = {
            "Dashboard": dashboard,
            "Monitor Traffic": monitor_traffic,
            "Monitor Anomalies": monitor_anomalies,
            "Firewall Policies": firewall_policies,
            "Site Monitoring": site_monitoring
        }
        
        page = PAGES.get(selection)
        if page:
            st.markdown('<div class="main-content">', unsafe_allow_html=True)  # Start main content area
            page.app()
            st.markdown('</div>', unsafe_allow_html=True)  # End main content area

        # Display the footer
        footer()

if __name__ == "__main__":
    main()
