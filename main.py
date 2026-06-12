import os
import pandas as pd
import numpy as np
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE_DIR, 'Boston.csv'))

X = df.iloc[:, 1:-1].values
Y = df.iloc[:, -1].values

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X, Y)

@app.route("/")
def index():
    return send_from_directory(BASE_DIR, "index.html")

@app.route("/app.js")
def js():
    return send_from_directory(BASE_DIR, "app.js")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    features = [[
        float(data["crim"]),
        float(data["zn"]),
        float(data["indus"]),
        float(data["chas"]),
        float(data["nox"]),
        float(data["rm"]),
        float(data["age"]),
        float(data["dis"]),
        float(data["rad"]),
        float(data["tax"]),
        float(data["ptratio"]),
        float(data["black"]),
        float(data["lstat"])
    ]]

    features = sc.transform(features)

    prediction = regressor.predict(features)[0]

    return jsonify({"prediction": float(prediction)})

if __name__ == "__main__":
    app.run(debug=True)