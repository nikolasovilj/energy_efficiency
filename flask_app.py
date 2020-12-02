"""
Author: Nikola Sovilj
Decription:
Flask REST API that can be used for evaluation of energy efficiency of buildings
"""

import pickle
from flask import Flask, jsonify, request
import numpy as np
app = Flask(__name__)

MODEL_FILENAME = "notebook/model.pickle"

model = pickle.load(open(MODEL_FILENAME, 'rb'))

@app.route("/", methods=['POST', 'GET'])
def predict():
    """
    Accepts GET and POST requests
    """

    if request.method == 'GET':
        return 'Send data in POST request to the same endpoint /', 400
    else:
        if not request.json:
            return 'Send data in JSON format <br> { "Glazing_Area": 0.0, \
                "Wall_Area": 294.0, "Roof_Area": 380.25 }', 400
        else:
            data = request.json
            tmp = np.array(list(data.values()))
            result = model.predict(tmp.reshape(1, -1))
            result = jsonify({'efficient': str(result[0])})
            return result

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
