import streamlit as st
import requests
import pandas as pd
import time

# Function to monitor anomalies
def monitor_anomalies():
    st.header("Anomalies Detected")
    try:
        response = requests.get("http://localhost:5000/network/logs")
        logs = response.json()

        anomalous_logs = [log for log in logs if log['is_anomalous']]

        if anomalous_logs:
            for log in anomalous_logs:
                st.write(f"App: {log['app_name']}, Domain: {log['domain']}, Protocol: {log['protocol']}, Packet Size: {log['packet_size']}, Anomalous: {log['is_anomalous']}")
        else:
            st.write("No anomalies detected.")
    except requests.exceptions.RequestException as e:
        st.write(f"Error fetching logs: {e}")

# Function to simulate real-time data from a CSV in a Wireshark-like table
def simulate_real_time_csv():
    st.subheader("Simulated Real-Time Data (Wireshark-like View)")

    # User-controlled parameters
    update_interval = st.slider("Update Interval (seconds)", min_value=0.1, max_value=5.0, value=1.0, step=0.1)

    # Start/stop button
    start_button = st.button("Start Simulation")
    stop_button = st.button("Stop Simulation")

    # Placeholder for the table
    table_placeholder = st.empty()

    # Load the CSV file
    df = pd.read_csv('C:\\Users\\amitm\\OneDrive\\Desktop\\SIH\\devsecc\\frontend\\pages\\dataset.csv')

    # Initialize simulation variables
    current_index = 0
    is_running = False

    if start_button:
        is_running = True

    # Run the simulation
    while is_running:
        if stop_button:
            is_running = False
            st.write("Simulation Stopped")
            break

        # Simulate real-time by incrementally showing more data
        current_index += 1

        # Extract a subset of the dataframe to display
        display_df = df.iloc[:current_index]

        # Display the data in a table format similar to Wireshark
        table_placeholder.table(display_df)

        # Add a delay for real-time effect
        time.sleep(update_interval)

        # Stop if we have displayed all data
        if current_index >= len(df):
            st.write("End of data")
            break

# Main Streamlit app structure
def main():
    st.title("Monitor Anomalies & Simulate Real-Time Data")

    # Tabs to switch between functionalities
    tab = st.sidebar.selectbox("Choose a function", ["Monitor Anomalies", "Simulate Real-Time Data"])

    if tab == "Monitor Anomalies":
        monitor_anomalies()
    elif tab == "Simulate Real-Time Data":
        simulate_real_time_csv()

if __name__ == "__main__":
    main()
