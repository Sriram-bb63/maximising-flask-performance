# load_balancer.py
import json
from flask import Flask, render_template, jsonify
import random
import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import requests

app = Flask(__name__)

request_counters = {f"http://localhost:500{i}": 0 for i in range(1, 6)}
request_history = {app_url: [] for app_url in request_counters}

ports = [5001, 5002, 5003, 5004, 5005]
current_port_index = 0

def cyclic_port():
    global current_port_index
    next_port = ports[current_port_index]
    current_port_index = (current_port_index + 1) % len(ports)
    return ports[current_port_index]

@app.route('/')
def index():
    # app_url = random.choice(list(request_counters.keys())) # Random URL to forward the requests
    app_url = f"http://localhost:{cyclic_port()}" # Cyclic URL to forward the requests
    res = requests.get(app_url)
    request_counters[app_url] += 1
    request_history[app_url].append(request_counters[app_url])
    return res.content

@app.route('/cpu-bound')
def cpu_bound():
    # app_url = random.choice(list(request_counters.keys())) # Random URL to forward the requests
    app_url = f"http://localhost:{cyclic_port()}" # Cyclic URL to forward the requests
    res = requests.get(app_url + "/cpu-bound")
    request_counters[app_url] += 1
    request_history[app_url].append(request_counters[app_url])
    return res.content

@app.route('/io-bound')
def io_bound():
    # app_url = random.choice(list(request_counters.keys())) # Random URL to forward the requests
    app_url = f"http://localhost:{cyclic_port()}" # Cyclic URL to forward the requests
    res = requests.get(app_url + "/io-bound")
    request_counters[app_url] += 1
    request_history[app_url].append(request_counters[app_url])
    return res.content

@app.route('/stats')
def stats():
    fig = make_subplots(rows=1, cols=1)
    for app_url, history in request_history.items():
        fig.add_trace(go.Scatter(x=list(range(len(history))), y=history, name=app_url))
    fig.update_layout(title='Live Request Statistics',
                      xaxis_title='Time',
                      yaxis_title='Number of Requests')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('stats.html', graphJSON=graphJSON)

if __name__ == '__main__':
    app.run(port=5000)
