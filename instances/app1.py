import math
import os
import sqlite3

from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_ujson import UJSON

load_dotenv()
USE_UJSON = int(os.environ.get("USE_UJSON"))

app = Flask(__name__)
if USE_UJSON == 1:
    print("Using UJSON")
    ultra_json = UJSON()
    ultra_json.init_app(app)


@app.route('/')
def get_info():
    pid = os.getpid()
    return jsonify({"pid": pid, "url": "http://localhost:5001"})

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

@app.route("/get-json", methods=["GET"])
def get_json():
    pid = os.getpid()
    return {
        "pid": pid,
        "glossary": {
            "title": "example glossary",
            "GlossDiv": {
                "title": "S",
                "GlossList": {
                    "GlossEntry": {
                        "ID": "SGML",
                        "SortAs": "SGML",
                        "GlossTerm": "Standard Generalized Markup Language",
                        "Acronym": "SGML",
                        "Abbrev": "ISO 8879:1986",
                        "GlossDef": {
                            "para": "A meta-markup language, used to create markup languages such as DocBook.",
                            "GlossSeeAlso": ["GML", "XML"]
                        },
                        "GlossSee": "markup"
                    }
                }
            }
        }
    }


if __name__ == "__main__":
    app.run(port=5001)
