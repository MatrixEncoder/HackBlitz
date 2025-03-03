# AI-Powered Network Guardian

## Problem Statement
Public sector networks in underserved regions struggle with high maintenance costs, frequent outages, and inefficient energy usage. Traditional network management relies on reactive measures, leading to downtime, increased costs, and poor service delivery.

## Solution
Our AI-powered Network Guardian leverages machine learning and predictive analytics to optimize public sector networks by:
- Predicting failures before they happen
- Reducing energy consumption through dynamic load balancing
- Providing real-time insights into network health

## Technologies Used
- TensorFlow and PyTorch for machine learning
- Nagios and Prometheus for network monitoring
- Apache Kafka for real-time data processing
- Reinforcement learning for optimization algorithms
- OpenStack for deployment
- Streamlit for interactive dashboard

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/MatrixEncoder/AI-Network-Guardian.git
   cd AI-Network-Guardian
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure your network monitoring tools (Nagios/Prometheus) if available.

## Running the Network Monitoring Dashboard

### Prerequisites
- Python 3.8 or higher
- All dependencies installed from requirements.txt
- A logo image file named 'path-to-logo.webp' in the project directory

### Step-by-Step Instructions

1. **Prepare the Environment**
   - Ensure all required data files are present:
     - cost_data.xlsx
     - fault_data.xlsx
     - network_data.xlsx

2. **Configure Monitoring URL (Optional)**
   - If you have a Nagios or Prometheus instance running:
     - Open `network_monitoring.py`
     - Update the URL in the main section:
       ```python
       nm = NetworkMonitoring('http://your-monitoring-url:port')
       ```
   - If you don't have monitoring tools, the app will use simulated data

3. **Launch the Dashboard**
   - Open a terminal in the project directory
   - Run the following command:
     ```bash
     streamlit run network_monitoring.py
     ```
   - The dashboard will automatically open in your default web browser
   - If it doesn't open automatically, visit: http://localhost:8501

4. **Using the Dashboard**
   The dashboard includes several sections:
   - **Home**: Overview of system features and capabilities
   - **Network Stats**: Real-time network performance metrics
   - **Cost Optimization**: Cost analysis and optimization recommendations
   - **Energy Efficiency**: Energy consumption metrics and efficiency insights
   - **Possible Fixes**: Automated suggestions for network issues
   - **Fault Prediction**: AI-driven predictions of potential network failures

5. **Data Export**
   - Each section allows you to export data to Excel format
   - Look for the "Export Data" button in relevant sections
   - Files will be saved in your project directory

6. **Troubleshooting**
   - If the dashboard doesn't load:
     - Check if all required packages are installed
     - Verify that port 8501 is available
     - Check the console for error messages
   - If data doesn't display:
     - Verify that all Excel files are present in the project directory
     - Check file permissions

