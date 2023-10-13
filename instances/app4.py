import math
from flask import Flask, jsonify
import os
import sqlite3
import requests

app = Flask(__name__)

@app.route('/')
def get_info():
    pid = os.getpid()
    return jsonify({"pid": pid, "url": "http://localhost:5004"})

@app.route('/cpu-bound', methods=['GET'])
def cpu_bound_task():
    pid = os.getpid()
    result = math.factorial(100)
    return jsonify({"pid": pid, "result": result})

@app.route("/io-bound", methods=['GET'])
def io_bound_task():
    pid = os.getpid()
    conn = sqlite3.connect("sample.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, age FROM sample_table LIMIT 5")  # Change the LIMIT as needed
    data = cursor.fetchall()
    results = []
    for row in data:
        result = {
            "id": row[0],
            "name": row[1],
            "age": row[2]
        }
        results.append(result)
    conn.close()
    return jsonify({"pid": pid, "result": results})

    

if __name__ == "__main__":
    app.run(port=5004)
