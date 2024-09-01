import streamlit as st

def navbar():
    st.markdown("""
    <style>
    .navbar {
        background-color: #333;
        overflow: hidden;
    }
    .navbar a {
        float: left;
        display: block;
        color: #f2f2f2;
        text-align: center;
        padding: 14px 20px;
        text-decoration: none;
    }
    .navbar a:hover {
        background-color: #ddd;
        color: black;
    }
    </style>
    <div class="navbar">
        <a href="#Login" onclick="setPage('Login')">Login</a>
        <a href="#Dashboard" onclick="setPage('Dashboard')">Dashboard</a>
        <a href="#Monitor Traffic" onclick="setPage('Monitor Traffic')">Monitor Traffic</a>
        <a href="#Monitor Anomalies" onclick="setPage('Monitor Anomalies')">Monitor Anomalies</a>
        <a href="#Firewall Policies" onclick="setPage('Firewall Policies')">Firewall Policies</a>
        <a href="#Site Monitoring" onclick="setPage('Site Monitoring')">Site Monitoring</a>
    </div>
    <script>
    function setPage(page) {
        window.parent.postMessage({type: 'set_page', page: page}, '*');
    }
    </script>
    """, unsafe_allow_html=True)

    # Detect the selected page based on URL hash or other method
    page = st.experimental_get_query_params().get('page', ['Login'])[0]
    return page
