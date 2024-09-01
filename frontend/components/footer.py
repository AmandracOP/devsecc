import streamlit as st

def footer():
    st.markdown("""
    <style>
    .footer {
        background-color: #333;
        color: white;
        text-align: center;
        padding: 10px;
        position: fixed;
        bottom: 0;
        width: 100%;
    }
    </style>
    <div class="footer">
        <p>© 2024 DevSec</p>
    </div>
    """, unsafe_allow_html=True)
