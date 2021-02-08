import numpy as np
from flask import Flask, request, jsonify, abort
from marshmallow import Schema, fields
import pickle

app = Flask(__name__)
reading_filepath = 'models/logistic_regression.pkl'
model = pickle.load(open(reading_filepath,'rb'))

class InputSchema(Schema):
    VisitsLastYear = fields.Integer(required=True)
    QuestionTextLength = fields.Integer(required=True)

input_schema = InputSchema()

@app.route('/predict',methods=['POST'])
def predict():
    if request.is_json:
        data = request.get_json()
        sanity_check = input_schema.load(data)
        if sanity_check:
            abort(400)
        features = np.array([data['VisitsLastYear'], data['QuestionTextLength']]).reshape(1, -1)
        prediction_proba = model.predict_proba(features)
        prediction_proba_class_1 = float(prediction_proba[0][1])
        return jsonify(PredictionProbabilityClass1=prediction_proba_class_1)
    else:
        return abort(400)

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
