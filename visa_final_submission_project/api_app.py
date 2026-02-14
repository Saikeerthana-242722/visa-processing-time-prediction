
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open("visa_model.pkl","rb"))

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    pred = model.predict([data["features"]])
    return jsonify({"processing_days": int(pred[0])})

app.run()
