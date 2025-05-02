import pickle
import pandas as pd
import numpy as np
from flask import Flask, request, render_template

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    hours = float(request.form["hours"])
    prediction = model.predict(hours)
    
    #formatted_prediction = f"The predicted value is ${round(float(prediction), 2)}"
    return render_template("result.html")#, prediction=formatted_prediction)


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')

