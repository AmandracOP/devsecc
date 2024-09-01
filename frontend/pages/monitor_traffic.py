import streamlit as st
import pandas as pd
import time

# Streamlit title and description
st.title("Simulated Real-Time Traffic Data (Wireshark-Like Display)")
st.subheader("Live updating table based on static CSV data")

# User-controlled parameters
update_interval = st.slider("Update Interval (seconds)", min_value=0.1, max_value=5.0, value=1.0, step=0.1)
max_data_points = st.slider("Max Data Points", min_value=10, max_value=100, value=50, step=10)

# Start/stop button
start_button = st.button("Start")
stop_button = st.button("Stop")

# Placeholder for the table
table_placeholder = st.empty()

# Load the CSV file
df = pd.read_csv('dataset.csv')

# Initialize simulation variables
current_index = 0
is_running = False

if start_button:
    is_running = True

# Run the simulation
while is_running:
    if stop_button:
        is_running = False
        st.write("Stopped")
        break
    
    # Simulate real-time by incrementally showing more data
    current_index += 1
    
    # Extract a subset of the dataframe to display
    display_df = df.iloc[:current_index]

    # Limit the dataframe to the max_data_points
    if len(display_df) > max_data_points:
        display_df = display_df.iloc[-max_data_points:]

    # Display the data in a table format similar to Wireshark
    table_placeholder.table(display_df)

    # Add a delay for real-time effect
    time.sleep(update_interval)

    # Stop if we have displayed all data
    if current_index >= len(df):
        st.write("End of data")
        break
