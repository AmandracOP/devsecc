import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import time

# Streamlit title and description
st.title("Simulated Real-Time Data from CSV")
st.subheader("Live updating graph based on static CSV data")

# User-controlled parameters
update_interval = st.slider("Update Interval (seconds)", min_value=0.1, max_value=5.0, value=1.0, step=0.1)
max_data_points = st.slider("Max Data Points", min_value=10, max_value=100, value=50, step=10)

# Start/stop button
start_button = st.button("Start")
stop_button = st.button("Stop")

# Placeholder for the plot
plot_placeholder = st.empty()

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
        st.write("Stopped")
        break
    
    # Simulate real-time by incrementally showing more data
    current_index += 1
    
    # Extract a subset of the dataframe to plot
    plot_df = df.iloc[:current_index]

    # Limit the dataframe to the max_data_points
    if len(plot_df) > max_data_points:
        plot_df = plot_df.iloc[-max_data_points:]

    # Plotting
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=plot_df['app_name'], y=plot_df['packet_size'], mode='lines+markers'))
    fig.update_layout(
        xaxis_title="X Axis",
        yaxis_title="Y Axis",
        title="Simulated Real-Time Data Plot",
    )

    # Update plot in the placeholder
    plot_placeholder.plotly_chart(fig, use_container_width=True)

    # Add a delay for real-time effect
    time.sleep(update_interval)

    # Stop if we have plotted all data
    if current_index >= len(df):
        st.write("End of data")
        break
