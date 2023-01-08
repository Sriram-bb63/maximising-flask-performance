from flask import Flask, render_template, jsonify
import requests
from flask_cors import CORS
import time


app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type, Access-Control-Allow-Origin'

HOST = "127.0.0.1"
PORT = 5000
i = 1
data = {
    "total": 0,
    "i1": 0,
    "i2": 0,
    "i3": 0,
    "i4": 0,
    "i5": 0
}

@app.route("/", methods=["GET"])
def main():
    global i
    global data
    res = requests.get(f"http://127.0.0.1:500{i}/")
    print(f"{i} {res.status_code}")
    data[f"i{i}"] = data[f"i{i}"] + 1
    data["total"] = data["total"] + 1
    i = i + 1
    if i > 5:
        i = 1
    return res.json()

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/dashboard/req-per-sec")
def dashboard_data():
    global data
    res = data
    data = {
        "total": 0,
        "i1": 0,
        "i2": 0,
        "i3": 0,
        "i4": 0,
        "i5": 0
    }
    return jsonify(res), 200

if __name__ == "__main__":
    app.run(port=PORT, debug=True)