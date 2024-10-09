# from mininet.net import Mininet
# from mininet.node import OVSSwitch, RemoteController
# from mininet.cli import CLI
# import pandas as pd
# import sys

# def inject_traffic(dataset_file_path):
#     """
#     Function to create topology and simulate SQL injection attack in Mininet.
#     """
#     # Load dataset
#     dataset = pd.read_csv(dataset_file_path)
#     dataset.columns = dataset.columns.str.strip()

#     # Define the attack parameters
#     attack_host = 'FIT101'
#     attack_command = "'; DROP TABLE SensorData; --"

#     # Ensure the 'FIT101' column exists
#     if 'FIT101' not in dataset.columns:
#         print("Error: 'FIT101' column not found in dataset. Please check the dataset structure.")
#         return

#     # Convert 'FIT101' column to string to handle the SQL injection string
#     dataset['FIT101'] = dataset['FIT101'].astype(str)

#     # Now 'Timestamp' should be accessible without the extra space
#     dataset.loc[dataset['Timestamp'] == attack_host, 'FIT101'] = attack_command

#     # Print column names to verify the structure of the dataset
#     print("Dataset columns:", dataset.columns)

#     # Setup Mininet topology
#     net = Mininet(controller=None, switch=OVSSwitch)

#     # Add switches
#     s1 = net.addSwitch('s1')

#     # Add hosts (representing sensors and actuators)
#     sensors = ['FIT101', 'LIT101', 'AIT201', 'AIT202', 'AIT203', 'FIT201', 'FIT301', 'LIT301', 'AIT401', 'AIT402']
#     actuators = ['MV101', 'P101', 'P102', 'MV201', 'P201', 'P202', 'P203', 'P204', 'P205', 'P206', 'MV301', 'MV302', 'MV303', 'MV304', 'P301', 'P302', 'P401', 'P402', 'P403', 'P404']

#     for sensor in sensors:
#         net.addHost(sensor)
#     for actuator in actuators:
#         net.addHost(actuator)

#     # Connect hosts to switches
#     for sensor in sensors:
#         net.addLink(sensor, s1)
#     for actuator in actuators:
#         net.addLink(actuator, s1)

#     # Start Mininet
#     net.start()

#     # Start the controller (POX)
#     c0 = net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6637)
#     c0.start()

#     # Assign controller to the switch
#     s1.start([c0])

#     print(f"SQL injection attack sent to host {attack_host}")

#     # Start the CLI for interaction (optional)
#     CLI(net)

#     # Stop Mininet after injection
#     net.stop()

# if __name__ == '__main__':
#     # Ensure the dataset file is passed as an argument
#     if len(sys.argv) != 2:
#         print("Usage: python3 mn_traffic_injection.py <dataset_file_path>")
#         sys.exit(1)

#     dataset_file_path = sys.argv[1]
#     inject_traffic(dataset_file_path)

from mininet.net import Mininet
from mininet.node import OVSSwitch, RemoteController
from mininet.cli import CLI
import pandas as pd
import requests
import sys

def inject_traffic(dataset_file_path):
    """
    Function to create topology and simulate SQL injection attack in Mininet.
    Sends traffic data to a Flask app.
    """
    # Load dataset
    dataset = pd.read_csv(dataset_file_path)
    dataset.columns = dataset.columns.str.strip()

    # Define the attack parameters
    attack_host = 'FIT101'
    attack_command = "'; DROP TABLE SensorData; --"

    # Ensure the 'FIT101' column exists
    if 'FIT101' not in dataset.columns:
        print("Error: 'FIT101' column not found in dataset. Please check the dataset structure.")
        return

    # Convert 'FIT101' column to string to handle the SQL injection string
    dataset['FIT101'] = dataset['FIT101'].astype(str)

    # Simulate SQL injection by modifying the dataset
    dataset.loc[dataset['Timestamp'] == attack_host, 'FIT101'] = attack_command

    # Print column names to verify the structure of the dataset
    print("Dataset columns:", dataset.columns)

    # Setup Mininet topology
    net = Mininet(controller=None, switch=OVSSwitch)

    # Add switches
    s1 = net.addSwitch('s1')

    # Add hosts (representing sensors and actuators)
    sensors = ['FIT101', 'LIT101', 'AIT201', 'AIT202', 'AIT203', 'FIT201', 'FIT301', 'LIT301', 'AIT401', 'AIT402']
    actuators = ['MV101', 'P101', 'P102', 'MV201', 'P201', 'P202', 'P203', 'P204', 'P205', 'P206', 'MV301', 'MV302', 'MV303', 'MV304', 'P301', 'P302', 'P401', 'P402', 'P403', 'P404']

    for sensor in sensors:
        net.addHost(sensor)
    for actuator in actuators:
        net.addHost(actuator)

    # Connect hosts to switches
    for sensor in sensors:
        net.addLink(sensor, s1)
    for actuator in actuators:
        net.addLink(actuator, s1)

    # Start Mininet
    net.start()

    # Start the controller (POX)
    c0 = net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6637)
    c0.start()

    # Assign controller to the switch
    s1.start([c0])

    print(f"SQL injection attack sent to host {attack_host}")

    # Send the modified dataset to the Flask app
    try:
        # Flask app's URL (replace with actual IP/Port if needed)
        flask_url = 'http://0.0.0.0:8001/process_traffic'

        # Convert dataset to JSON format to send via POST request
        dataset_json = dataset.to_json(orient='records')
        response = requests.post(flask_url, json={'traffic_data': dataset_json})

        # Log the response from Flask
        print(f"Response from Flask: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Error sending traffic data to Flask: {str(e)}")

    # Start the CLI for interaction (optional)
    CLI(net)

    # Stop Mininet after injection
    net.stop()

if __name__ == '__main__':
    # Ensure the dataset file is passed as an argument
    if len(sys.argv) != 2:
        print("Usage: python3 mn_traffic_injection.py <dataset_file_path>")
        sys.exit(1)

    dataset_file_path = sys.argv[1]
    inject_traffic(dataset_file_path)
