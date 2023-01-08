from flask import Flask, jsonify

app = Flask(__name__)

HOST = "127.0.0.1"
PORT = 5002
count = 0

@app.route("/", methods=["GET"])
def main():
    global count
    count += 1
    print(count)
    return jsonify({
        "instance": 2,
        "url": f"{HOST}:{PORT}"
    }), 200

if __name__ == "__main__":
    app.run(port=PORT)