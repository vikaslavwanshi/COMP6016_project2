# import subprocess
# import pandas as pd
# import joblib
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import logging
# import requests

# logging.basicConfig(level=logging.DEBUG)

# app = Flask(__name__)
# CORS(app)

# # Load your trained model
# model = joblib.load('random_forest_model.pkl')

# def inject_traffic_with_sudo(dataset_file):
#     """
#     Calls an external Mininet script to simulate the SQL injection attack.
#     Runs the script with sudo.
#     """
#     # Save the dataset file temporarily
#     dataset_file_path = "/home/vikas/Downloads/Project-comp6016/COMP6016_project2/backend/venv/modified_SWaT_Dataset.csv"
#     dataset_file.save(dataset_file_path)

#     # Define the path to your external Mininet script
#     script_path = "/path/to/mn_traffic_injection.py"  # Update this path
    
#     # Run the external script with sudo
#     command = ['sudo', 'python3', script_path, dataset_file_path]
#     result = subprocess.run(command, capture_output=True, text=True)
    
#     # Check the result
#     if result.returncode == 0:
#         app.logger.debug("SQL Injection attack simulated successfully.")
#     else:
#         app.logger.error(f"Failed to simulate attack: {result.stderr}")
#         raise Exception(result.stderr)

# def predict_attack(raw_data_file, test_data_file):
#     # Load and preprocess your data
#     raw_data = pd.read_csv(raw_data_file)
#     test_data = pd.read_csv(test_data_file)

#     # Strip any leading/trailing spaces from column names
#     raw_data.columns = raw_data.columns.str.strip()
#     test_data.columns = test_data.columns.str.strip()

#     app.logger.debug(f"Raw data columns: {list(raw_data.columns)}")
#     app.logger.debug(f"Test data columns: {list(test_data.columns)}")

#     # Check if there are any discrepancies between raw and test data
#     discrepancies = (raw_data != test_data).any(axis=None)

#     if discrepancies:
#         message = "Possible attack detected! We've found some discrepancies between raw and test data. Please check Wireshark logs."
#     else:
#         message = "No attack detected. System is operating normally."

#     return {'message': message}

# @app.route('/')
# def home():
#     return "Welcome to the Prediction API"

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         raw_data_file = request.files['raw_data_file']
#         test_data_file = request.files['test_data_file']
#         app.logger.debug(f'Received files: {raw_data_file.filename}, {test_data_file.filename}')

#         # Process the files and make predictions
#         result = predict_attack(raw_data_file, test_data_file)

#         # Return the result message
#         return jsonify(result)
#     except Exception as e:
#         app.logger.error(f'Error: {str(e)}')
#         return jsonify({'error': str(e)}), 400

# @app.route('/simulate_attack', methods=['POST'])
# def simulate_attack():
#     try:
#         # Receive the dataset file to simulate the attack
#         dataset_file = request.files['dataset_file']

#         # Inject SQL injection attack in Mininet using sudo
#         inject_traffic_with_sudo(dataset_file)

#         return jsonify({'message': 'SQL Injection Attack simulated in Mininet'}), 200
#     except Exception as e:
#         app.logger.error(f'Error: {str(e)}')
#         return jsonify({'error': str(e)}), 400

# @app.route('/process_traffic', methods=['POST'])
# def process_traffic():
#     try:
#         traffic_data = request.get_json()
#         app.logger.debug(f"Received traffic data: {traffic_data}")

#         # Send the traffic data to the ML server for predictions
#         ml_server_url = "http://127.0.0.1:5002/process_traffic"
#         ml_response = requests.post(ml_server_url, json=traffic_data)

#         if ml_response.status_code == 200:
#             return jsonify(ml_response.json()), 200
#         else:
#             app.logger.error(f"Failed to send traffic data to ML server. Status code: {ml_response.status_code}")
#             return jsonify({'error': 'Failed to process traffic data with ML server'}), 400

#     except Exception as e:
#         app.logger.error(f'Error processing traffic data: {str(e)}')
#         return jsonify({'error': str(e)}), 400


# if __name__ == '__main__':
#     app.run(debug=True)

# import subprocess
# import pandas as pd
# import joblib
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import logging
# import tempfile

# # Set logging to INFO level and log to a file
# logging.basicConfig(level=logging.INFO, filename='traffic_log.txt',
#                     format='%(asctime)s - %(levelname)s - %(message)s')

# app = Flask(__name__)
# CORS(app)

# # Load your trained model
# model = joblib.load('random_forest_model.pkl')

# def inject_traffic_with_sudo(dataset_file_path):
#     """
#     Calls an external Mininet script to simulate the SQL injection attack.
#     Runs the script with sudo.
#     """
#     # Define the path to your external Mininet script
#     script_path = "/home/vikas/Downloads/Project-comp6016/COMP6016_project2/backend/venv/mn_traffic_injection.py"  # Update this path

#     # Run the external script with sudo
#     command = ['sudo', 'python3', script_path, dataset_file_path]
#     result = subprocess.run(command, capture_output=True, text=True)

#     # Check the result
#     if result.returncode == 0:
#         app.logger.debug("SQL Injection attack simulated successfully.")
#     else:
#         app.logger.error(f"Failed to simulate attack: {result.stderr}")
#         raise Exception("Failed to simulate attack. Please check logs for details.")

# def predict_attack(raw_data_file, test_data_file):
#     # Load and preprocess your data
#     raw_data = pd.read_csv(raw_data_file)
#     test_data = pd.read_csv(test_data_file)

#     # Strip any leading/trailing spaces from column names
#     raw_data.columns = raw_data.columns.str.strip()
#     test_data.columns = test_data.columns.str.strip()

#     app.logger.debug(f"Raw data columns: {list(raw_data.columns)}")
#     app.logger.debug(f"Test data columns: {list(test_data.columns)}")

#     # Check if there are any discrepancies between raw and test data
#     discrepancies = (raw_data != test_data).any(axis=None)

#     if discrepancies:
#         message = "Possible attack detected! We've found some discrepancies between raw and test data. Please check Wireshark logs."
#     else:
#         message = "No attack detected. System is operating normally."

#     return {'message': message}

# @app.route('/')
# def home():
#     return "Welcome to the Prediction API"

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         raw_data_file = request.files['raw_data_file']
#         test_data_file = request.files['test_data_file']
#         app.logger.debug(f'Received files: {raw_data_file.filename}, {test_data_file.filename}')

#         # Process the files and make predictions
#         result = predict_attack(raw_data_file, test_data_file)

#         # Return the result message
#         return jsonify(result)
#     except Exception as e:
#         app.logger.error(f'Error: {str(e)}')
#         return jsonify({'error': str(e)}), 400

# @app.route('/simulate_attack', methods=['POST'])
# def simulate_attack():
#     try:
#         # Receive the dataset file to simulate the attack
#         dataset_file = request.files['dataset_file']
        
#         # Use a temporary file to store the dataset
#         with tempfile.NamedTemporaryFile(delete=False) as temp_file:
#             dataset_file.save(temp_file.name)
#             inject_traffic_with_sudo(temp_file.name)

#         return jsonify({'message': 'SQL Injection Attack simulated in Mininet'}), 200
#     except Exception as e:
#         app.logger.error(f'Error: {str(e)}')
#         return jsonify({'error': str(e)}), 400

# @app.route('/process_traffic', methods=['POST'])
# def process_traffic():
#     try:
#         # Parse the incoming JSON traffic data
#         traffic_data = request.json
#         logging.info('Received traffic data: %s', traffic_data)  # Log actual traffic data

#         # Here, you could further process traffic data or send it to an ML model

#         return jsonify({'message': 'Traffic data received successfully'}), 200

#     except Exception as e:
#         app.logger.error(f'Error processing traffic data: {str(e)}')
#         return jsonify({'error': str(e)}), 400
    
# @app.route('/logs', methods=['GET'])
# def get_logs():
#     try:
#         with open('traffic_log.txt', 'r') as log_file:
#             logs = log_file.read().splitlines()  # Read lines into a list
#         return jsonify({'logs': logs}), 200
#     except Exception as e:
#         app.logger.error(f'Error reading log file: {str(e)}')
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5002, debug=True)

import subprocess
import pandas as pd
import joblib
from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
import tempfile

# Set logging to INFO level and log to a file
logging.basicConfig(level=logging.INFO, filename='traffic_log.txt',
                    format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)
CORS(app)

# Load your trained model
model = joblib.load('random_forest_model.pkl')

def inject_traffic_with_sudo(dataset_file_path):
    """
    Calls an external Mininet script to simulate the SQL injection attack.
    Runs the script with sudo.
    """
    # Define the path to your external Mininet script
    script_path = "/home/vikas/Downloads/Project-comp6016/COMP6016_project2/backend/venv/mn_traffic_injection.py"  # Update this path

    # Run the external script with sudo
    command = ['sudo', 'python3', script_path, dataset_file_path]
    result = subprocess.run(command, capture_output=True, text=True)

    # Check the result
    if result.returncode == 0:
        app.logger.debug("SQL Injection attack simulated successfully.")
        logging.info("Mininet script executed successfully.")
    else:
        app.logger.error(f"Failed to simulate attack: {result.stderr}")
        logging.error(f"Mininet script failed: {result.stderr}")
        raise Exception("Failed to simulate attack. Please check logs for details.")

def predict_attack(raw_data_file, test_data_file):
    # Load and preprocess your data
    raw_data = pd.read_csv(raw_data_file)
    test_data = pd.read_csv(test_data_file)

    # Strip any leading/trailing spaces from column names
    raw_data.columns = raw_data.columns.str.strip()
    test_data.columns = test_data.columns.str.strip()

    app.logger.debug(f"Raw data columns: {list(raw_data.columns)}")
    app.logger.debug(f"Test data columns: {list(test_data.columns)}")

    # Check if there are any discrepancies between raw and test data
    discrepancies = (raw_data != test_data).any(axis=None)

    if discrepancies:
        message = "Possible attack detected! We've found some discrepancies between raw and test data. Please check Wireshark logs."
    else:
        message = "No attack detected. System is operating normally."

    return {'message': message}

@app.route('/')
def home():
    return "Welcome to the Prediction API"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        raw_data_file = request.files['raw_data_file']
        test_data_file = request.files['test_data_file']
        app.logger.debug(f'Received files: {raw_data_file.filename}, {test_data_file.filename}')

        # Process the files and make predictions
        result = predict_attack(raw_data_file, test_data_file)

        # Return the result message
        return jsonify(result)
    except Exception as e:
        app.logger.error(f'Error: {str(e)}')
        return jsonify({'error': str(e)}), 400

@app.route('/simulate_attack', methods=['POST'])
def simulate_attack():
    try:
        # Check if the dataset file is included in the request
        if 'dataset_file' not in request.files:
            app.logger.error('No dataset file part in the request')
            return jsonify({'error': 'No dataset file provided.'}), 400
        
        # Receive the dataset file to simulate the attack
        dataset_file = request.files['dataset_file']
        
        # Check if the dataset file is empty
        if dataset_file.filename == '':
            app.logger.error('No selected dataset file')
            return jsonify({'error': 'No selected dataset file.'}), 400
        
        # Use a temporary file to store the dataset
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            dataset_file.save(temp_file.name)
            app.logger.info(f'Dataset file saved to {temp_file.name}')
            inject_traffic_with_sudo(temp_file.name)

        return jsonify({'message': 'SQL Injection Attack simulated in Mininet'}), 200
    except Exception as e:
        app.logger.error(f'Error during attack simulation: {str(e)}')
        return jsonify({'error': str(e)}), 500

@app.route('/process_traffic', methods=['POST'])
def process_traffic():
    try:
        # Parse the incoming JSON traffic data
        traffic_data = request.json
        logging.info('Received traffic data: %s', traffic_data)  # Log actual traffic data

        # Here, you could further process traffic data or send it to an ML model

        return jsonify({'message': 'Traffic data received successfully'}), 200

    except Exception as e:
        app.logger.error(f'Error processing traffic data: {str(e)}')
        return jsonify({'error': str(e)}), 400

@app.route('/logs', methods=['GET'])
def get_logs():
    try:
        with open('traffic_log.txt', 'r') as log_file:
            logs = log_file.read().splitlines()  # Read lines into a list
        return jsonify({'logs': logs}), 200
    except Exception as e:
        app.logger.error(f'Error reading log file: {str(e)}')
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)
