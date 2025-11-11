"""
Flask app for predicting house prices using a pretrained sklearn model.
"""

import logging

from flask import Flask, request, jsonify
from flask.logging import create_logger


import pandas as pd
# from sklearn.externals import joblib
import joblib
from sklearn.exceptions import NotFittedError
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

def scale(payload):
    """Scales the incoming payload using StandardScaler."""

    LOG.info("Scaling Payload: %s payload", payload)
    scaler = StandardScaler().fit(payload)
    scaled_adhoc_predict = scaler.transform(payload)
    return scaled_adhoc_predict

@app.route("/")
def home():
    """Home route that returns a basic HTML response."""
    html = "<h3>Sklearn Prediction Home</h3>"
    return html.format(format)

# TO DO:  Log out the prediction value
@app.route("/predict", methods=['POST'])
def predict():
    """Handles prediction requests and returns model output."""
    # Performs an sklearn prediction

    try:
        # Load pretrained model as clf. Try any one model.
        # clf = joblib.load("./Housing_price_model/LinearRegression.joblib")
        # clf = joblib.load("./Housing_price_model/StochasticGradientDescent.joblib")
        clf = joblib.load("./Housing_price_model/LinearRegression.joblib")
    except FileNotFoundError as e:
        LOG.error("Model file not found: %s", e)
        return jsonify({"error": "Model file not found"}), 500
    except (ImportError, AttributeError) as e:
        LOG.error("Model load failed: %s", e)
        return jsonify({"error": "Model load failed"}), 500

    json_payload = request.json
    LOG.info("JSON payload: %s json_payload", json_payload)
    try:
        inference_payload = pd.DataFrame(json_payload)
        LOG.info("inference payload DataFrame: %s inference_payload", inference_payload)
        scaled_payload = scale(inference_payload)
        prediction = list(clf.predict(scaled_payload))
        return jsonify({'prediction': prediction})
    except NotFittedError:
        LOG.error("Model is not fitted")
        return jsonify({"error": "Model is not fitted"}), 500
    except (ValueError, TypeError, KeyError) as e:
        LOG.error("Invalid input payload: %s", e)
        return jsonify({"error": "Invalid input payload"}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
