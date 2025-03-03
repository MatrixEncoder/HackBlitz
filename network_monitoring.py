# This module will integrate with Nagios or Prometheus for monitoring

import requests
import streamlit as st
import numpy as np
import pandas as pd
import time
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

class NetworkMonitoring:
    def __init__(self, monitoring_url):
        self.monitoring_url = monitoring_url

    def check_health(self):
        try:
            response = requests.get(f'{self.monitoring_url}/health')
            if response.status_code == 200:
                print('Network is healthy')
            else:
                print('Network is unhealthy')
        except requests.exceptions.RequestException as e:
            print('Error checking network health:', e)

    def collect_metrics(self):
        try:
            response = requests.get(f'{self.monitoring_url}/metrics')
            metrics = response.json()
            print('Collected metrics:', metrics)
        except requests.exceptions.RequestException as e:
            print('Error collecting metrics:', e)

# Function to generate simulated data
def generate_simulated_data(num_samples=100):
    # Simulate random data
    data = {
        'Time': pd.date_range(start='2025-02-10', periods=num_samples, freq='T'),
        'Value': np.random.rand(num_samples) * 100
    }
    return pd.DataFrame(data)

# Function to simulate cost estimation
def simulate_cost_estimation(num_samples=100):
    # Simulate random cost data
    costs = np.random.rand(num_samples) * 1000  # Random costs between 0 and 1000
    return costs

# Function to simulate energy efficiency
def simulate_energy_efficiency(num_samples=100):
    # Simulate random energy consumption data
    energy = np.random.rand(num_samples) * 500  # Random energy consumption between 0 and 500
    return energy

# Function to generate realistic network metrics
def generate_realistic_network_data(num_samples=100):
    # Simulate realistic network data
    data = {
        'Time': pd.date_range(start='2025-02-10', periods=num_samples, freq='T'),
        'Latency': np.random.normal(loc=20, scale=5, size=num_samples),  # Normal distribution around 20ms
        'Throughput': np.random.normal(loc=100, scale=20, size=num_samples)  # Normal distribution around 100 Mbps
    }
    return pd.DataFrame(data)

# Function to simulate fault prediction with detailed information
def simulate_fault_prediction(num_samples=100):
    # Simulate random fault predictions based on equipment health metrics
    faults = np.random.choice(['No Fault', 'Minor Fault', 'Major Fault'], size=num_samples, p=[0.7, 0.2, 0.1])
    models = np.random.choice(['Random Forest', 'Neural Network'], size=num_samples)
    causes = np.where(faults == 'No Fault', '', np.random.choice(['Overheating', 'Wear and Tear', 'Electrical Failure'], size=num_samples))
    return pd.DataFrame({'Sample': range(num_samples), 'Fault Prediction': faults, 'Model Used': models, 'Cause': causes})

# Function to export data to Excel with appropriate column widths
def export_to_excel(data, filename):
    # Ensure the Time column is formatted correctly when exporting
    with pd.ExcelWriter(filename, engine='xlsxwriter') as writer:
        data.to_excel(writer, index=False, sheet_name='Data')
        worksheet = writer.sheets['Data']
        # Set column widths for better visibility
        for i, col in enumerate(data.columns):
            if col == 'Cause':
                max_len = max(data[col].astype(str).map(len).max(), len(col)) + 15  # Add more padding for longer text
            else:
                max_len = max(data[col].astype(str).map(len).max(), len(col)) + 5  # Add more padding for longer text
            worksheet.set_column(i, i, max_len)

# Streamlit app layout
def run_streamlit_app():
    st.set_page_config(page_title='AI Powered Network Guardian', layout='wide')
    st.title('AI Powered Network Guardian')
    st.image('path-to-logo.webp', width=100)  # Use relative path for the image

    # Team information
    st.write('Team Name: Threat Al-liance')
    st.write('Team Members:')
    st.write('1: Suryansh Srivastava 👑')
    st.write('2: Ashutosh Sharma')

    # Column navigation layout
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        if st.button('Home'):
            st.session_state.page = 'Home'
    with col2:
        if st.button('Network Stats'):
            st.session_state.page = 'Network Stats'
    with col3:
        if st.button('Cost Optimization'):
            st.session_state.page = 'Cost Optimization'
    with col4:
        if st.button('Energy Efficiency'):
            st.session_state.page = 'Energy Efficiency'
    with col5:
        if st.button('Possible Fixes'):
            st.session_state.page = 'Possible Fixes'
    with col6:
        if st.button('Fault Prediction'):
            st.session_state.page = 'Fault Prediction'

    # Set default page if not set
    if 'page' not in st.session_state:
        st.session_state.page = 'Home'

    # Page content based on selection
    if st.session_state.page == 'Home':
        st.subheader('Welcome to the AI Powered Network Guardian!')
        st.write('Our goal is to help organizations monitor their network health, reduce costs, and improve energy efficiency through AI-driven solutions.')
        st.write('Key Features:')
        st.write('- Predictive Maintenance: Detect and prevent network failures before they happen.')
        st.write('- Cost Optimization: Identify inefficient components and suggest Total Cost of Ownership (TCO) reductions.')
        st.write('- Energy Efficiency: Implement dynamic load balancing and power management to reduce energy consumption.')
        st.write('- Automated Response System: Real-time issue detection and self-healing capabilities using open-source automation tools.')
        st.write('- Fault Prediction System: Use AI to monitor and predict equipment failures, enabling proactive repairs and reducing downtime.')
        st.write('- Maintenance Scheduling Assistant: Design tools to automate maintenance schedules, improving efficiency and minimizing service interruptions.')

    elif st.session_state.page == 'Network Stats':
        st.subheader('Network Statistics')
        num_samples = st.slider('Number of samples (used for generating data)', min_value=10, max_value=1000, value=100)
        with st.spinner('Fetching Data...'):
            try:
                logging.debug('Fetching network data...')
                time.sleep(1)  # Simulating data fetching delay
                network_data = generate_realistic_network_data(num_samples)
                avg_latency = network_data['Latency'].mean()
                avg_throughput = network_data['Throughput'].mean()
                st.write(f'Average Latency: {avg_latency:.2f} ms')
                st.write(f'Average Throughput: {avg_throughput:.2f} Mbps')
                st.line_chart(network_data.set_index('Time'))
                # Display data in a table
                st.subheader('Network Data Table')
                # Apply consistent styling to the dataframe
                styled_network_df = network_data.style.set_properties(**{
                    'white-space': 'pre-wrap',
                    'text-align': 'left'
                })
                
                # Display the styled dataframe with specific dimensions
                st.dataframe(styled_network_df, height=400, width=800)
                st.write('Latency (ms) and Throughput (Mbps) over time. Monitoring these metrics is crucial for maintaining optimal network performance.')
                if st.button('Export to Excel'):
                    export_to_excel(network_data[['Time', 'Latency', 'Throughput']], 'network_data.xlsx')
                    st.success('Downloaded network_data.xlsx')
            except Exception as e:
                logging.error(f'Error fetching network data: {e}')
                st.error(f'Error fetching network data: {e}')

    elif st.session_state.page == 'Cost Optimization':
        st.subheader('Cost Optimization')
        num_samples = st.slider('Number of samples (used for generating data)', min_value=10, max_value=1000, value=100)
        with st.spinner('Fetching Data...'):
            try:
                logging.debug('Fetching cost data...')
                time.sleep(1)  # Simulating data fetching delay
                cost_data = simulate_cost_estimation(num_samples)
                avg_cost = cost_data.mean()
                st.write(f'Average Cost: {avg_cost:.2f} USD')
                st.line_chart(cost_data)
                # Display data in a table
                st.subheader('Cost Data Table')
                cost_df = pd.DataFrame({
                    'Cost Sample': range(num_samples),  # Renamed column
                    'Cost (USD)': cost_data
                })
                
                # Apply consistent styling to the dataframe
                styled_cost_df = cost_df.style.set_properties(**{
                    'white-space': 'pre-wrap',
                    'text-align': 'left'
                })
                
                # Display the styled dataframe with specific dimensions
                st.dataframe(styled_cost_df, height=400, width=800)
                st.write('Estimated costs based on network usage and inefficiencies. This data can help identify areas for cost reduction and efficiency improvements.')
                if st.button('Export to Excel'):
                    export_to_excel(cost_df, 'cost_data.xlsx')
                    st.success('Downloaded cost_data.xlsx')
            except Exception as e:
                logging.error(f'Error fetching cost data: {e}')
                st.error(f'Error fetching cost data: {e}')

    elif st.session_state.page == 'Energy Efficiency':
        st.subheader('Energy Efficiency')
        num_samples = st.slider('Number of samples (used for generating data)', min_value=10, max_value=1000, value=100)
        with st.spinner('Fetching Data...'):
            try:
                logging.debug('Fetching energy data...')
                time.sleep(1)  # Simulating data fetching delay
                energy_data = simulate_energy_efficiency(num_samples)
                avg_energy = energy_data.mean()
                st.write(f'Average Energy Consumption: {avg_energy:.2f} units')
                st.line_chart(energy_data)
                # Display data in a table
                st.subheader('Energy Data Table')
                energy_df = pd.DataFrame({
                    'Energy Sample': range(num_samples),  # Renamed column
                    'Energy Consumption (in Units)': energy_data
                })
                
                # Apply consistent styling to the dataframe
                styled_energy_df = energy_df.style.set_properties(**{
                    'white-space': 'pre-wrap',
                    'text-align': 'left'
                })
                
                # Display the styled dataframe with specific dimensions
                st.dataframe(styled_energy_df, height=400, width=800)
                st.write('Energy consumption metrics. Reducing energy consumption not only lowers costs but also contributes to sustainability efforts.')
                if st.button('Export to Excel'):
                    export_to_excel(energy_df, 'energy_data.xlsx')
                    st.success('Downloaded energy_data.xlsx')
            except Exception as e:
                logging.error(f'Error fetching energy data: {e}')
                st.error(f'Error fetching energy data: {e}')

    elif st.session_state.page == 'Fault Prediction':
        st.subheader('Fault Prediction')
        num_samples = st.slider('Number of samples (used for generating data)', min_value=10, max_value=1000, value=100)
        with st.spinner('Fetching Data...'):
            try:
                logging.debug('Fetching fault prediction data...')
                time.sleep(1)  # Simulating data fetching delay
                fault_data = simulate_fault_prediction(num_samples)
                fault_data['Cause'] = fault_data['Cause'].astype(str)  # Ensure Cause column is treated as string
                # Create a custom CSS for the dataframe with specific column widths
                # Specifically make the Cause column much wider
                custom_css = {
                    "selector": "th:nth-child(4), td:nth-child(4)",  # Target the 4th column (Cause)
                    "props": [("min-width", "300px"), ("width", "300px")]
                }
                
                # Apply the styling to the dataframe
                styled_df = fault_data.style.set_properties(**{
                    'white-space': 'pre-wrap',
                    'text-align': 'left'
                }).set_table_styles([custom_css])
                
                # Display the styled dataframe with a specific height to ensure scrollability
                st.dataframe(styled_df, height=400, width=800)
                st.write('Fault prediction metrics. This data can help identify potential equipment failures and enable proactive repairs.')
                if st.button('Export to Excel'):
                    export_to_excel(pd.DataFrame(fault_data), 'fault_data.xlsx')
                    st.success('Downloaded fault_data.xlsx')
            except Exception as e:
                logging.error(f'Error fetching fault prediction data: {e}')
                st.error(f'Error fetching fault prediction data: {e}')

    elif st.session_state.page == 'Possible Fixes':
        st.subheader('Possible Fixes')
        st.write('This section will provide recommendations for potential fixes based on the analysis. Consider the following actions:')
        st.write('- Upgrade outdated hardware to improve performance and efficiency.')
        st.write('- Implement load balancing to distribute traffic evenly across servers.')
        st.write('- Utilize automated monitoring tools to detect and address issues in real-time.')
        st.write('Based on the displayed graphs, here are some potential problems and solutions:')
        st.write('- High latency may indicate network congestion; consider upgrading bandwidth or optimizing routes.')
        st.write('- Low throughput can suggest insufficient resources; investigate resource allocation and usage patterns.')
        st.write('- High energy consumption may point to inefficient hardware; consider energy-efficient alternatives.')

# Example usage
if __name__ == '__main__':
    nm = NetworkMonitoring('http://localhost:9090')  # Replace with actual monitoring tool URL
    nm.check_health()
    nm.collect_metrics()
    run_streamlit_app()
