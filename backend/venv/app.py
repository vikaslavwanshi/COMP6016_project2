# # backend/app.py
# import pandas as pd
# from sklearn.ensemble import RandomForestClassifier
# import joblib
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import logging

# logging.basicConfig(level=logging.DEBUG)

# app = Flask(__name__)
# CORS(app)

# # Load your trained model
# model = joblib.load('random_forest_model.pkl')

# def predict_attack(raw_data_file, test_data_file):
#     # Load and preprocess your data
#     raw_data = pd.read_csv(raw_data_file)
#     test_data = pd.read_csv(test_data_file)
    
#     # Strip any leading/trailing spaces from column names
#     raw_data.columns = raw_data.columns.str.strip()
#     test_data.columns = test_data.columns.str.strip()
    
#     app.logger.debug(f"Raw data columns: {list(raw_data.columns)}")
#     app.logger.debug(f"Test data columns: {list(test_data.columns)}")

#     # Drop the datetime column from the test data
#     if 'Timestamp' in test_data.columns:
#         test_data = test_data.drop(columns=['Timestamp'])
#     else:
#         error_msg = "Timestamp column not found in test data"
#         app.logger.error(error_msg)
#         return {'error': error_msg}

#     # Assume the test_data contains the features needed for prediction
#     if 'Normal/Attack' in test_data.columns:
#         features = test_data.drop(columns=['Normal/Attack'])
#     else:
#         error_msg = "Normal/Attack column not found in test data"
#         app.logger.error(error_msg)
#         return {'error': error_msg}

#     # Make predictions
#     predictions = model.predict(features)

#     # Return the results as a DataFrame or any other suitable format
#     result_df = pd.DataFrame({'predictions': predictions})
#     return result_df

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
        
#         # Check if there's an error in the result
#         if 'error' in result:
#             return jsonify(result), 400
        
#         # Return the predictions
#         return jsonify(result.to_dict(orient='records'))
#     except Exception as e:
#         app.logger.error(f'Error: {str(e)}')
#         return jsonify({'error': str(e)}), 400

# if __name__ == '__main__':
#     app.run(debug=True)

# backend/app.py
# import pandas as pd
# from sklearn.ensemble import RandomForestClassifier
# import joblib
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import logging

# logging.basicConfig(level=logging.DEBUG)

# app = Flask(__name__)
# CORS(app)

# # Load your trained model
# model = joblib.load('random_forest_model.pkl')

# def predict_attack(raw_data_file, test_data_file):
#     # Load and preprocess your data
#     raw_data = pd.read_csv(raw_data_file)
#     test_data = pd.read_csv(test_data_file)
    
#     # Strip any leading/trailing spaces from column names
#     raw_data.columns = raw_data.columns.str.strip()
#     test_data.columns = test_data.columns.str.strip()
    
#     app.logger.debug(f"Raw data columns: {list(raw_data.columns)}")
#     app.logger.debug(f"Test data columns: {list(test_data.columns)}")

#     # Assume the test_data contains the features needed for prediction
#     if 'Normal/Attack' in test_data.columns:
#         features = test_data.drop(columns=['Normal/Attack'])
#     else:
#         error_msg = "Normal/Attack column not found in test data"
#         app.logger.error(error_msg)
#         return {'error': error_msg}

#     # Make predictions
#     predictions = model.predict(features)

#     # Return the results as a DataFrame or any other suitable format
#     result_df = pd.DataFrame({'predictions': predictions})
#     return result_df

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
        
#         # Check if there's an error in the result
#         if 'error' in result:
#             return jsonify(result), 400
        
#         # Return the predictions
#         return jsonify(result.to_dict(orient='records'))
#     except Exception as e:
#         app.logger.error(f'Error: {str(e)}')
#         return jsonify({'error': str(e)}), 400

# if __name__ == '__main__':
#     app.run(debug=True)

import pandas as pd
import joblib
from flask import Flask, request, jsonify
from flask_cors import CORS
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
CORS(app)

# Load your trained model
model = joblib.load('random_forest_model.pkl')

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

if __name__ == '__main__':
    app.run(debug=True)

