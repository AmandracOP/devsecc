import streamlit as st

def sidebar():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ("Home", "Page 1", "Page 2", "Contact"))

    st.sidebar.title("Settings")
    st.sidebar.write("Adjust your preferences below:")
    
    theme = st.sidebar.selectbox("Choose theme", ["Light", "Dark", "Custom"])
    notifications = st.sidebar.checkbox("Enable notifications")
    email = st.sidebar.text_input("Enter your email", "")

    st.sidebar.title("About")
    st.sidebar.info("""
        This is a sample Streamlit app demonstrating a simple layout with a navbar, sidebar, and footer.
        Visit our [website](https://www.yourcompany.com) for more information.
    """)

    return page
