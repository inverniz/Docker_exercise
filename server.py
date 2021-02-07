import numpy as np
from flask import Flask, request, jsonify, abort
import pickle

app = Flask(__name__)
reading_filepath = 'models/logistic_regression.pkl'
model = pickle.load(open(reading_filepath,'rb'))

@app.route('/predict',methods=['POST'])
def predict():
    if request.is_json:
        data = request.get_json()
        features = np.array([int(data['VisitsLastYear']),
                            int(data['QuestionTextLength'])]).reshape(1, -1)
        prediction_probability_class_1 = float(model.predict_proba(features)[0][1])
        return jsonify(PredictionProbabilityClass1=prediction_probability_class_1)
    else:
        return abort(400)

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
