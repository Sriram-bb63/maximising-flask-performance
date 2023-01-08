import requests

count = 0
while True:
    res = requests.get("http://127.0.0.1:5000/")
    count += 1
    print(count, res.status_code)
