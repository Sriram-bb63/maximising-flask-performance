#!/bin/bash

# Start Flask apps
python3 ./instances/app1.py &
python3 ./instances/app2.py &
python3 ./instances/app3.py &
python3 ./instances/app4.py &
python3 ./instances/app5.py &
python3 load_balancer.py &

# Start Locust test in the background
# locust -f requester.py &

# Wait for user input to stop the apps
read -p "Press Enter to stop..."

# Stop Flask apps and Locust test
pkill -f "python3 ./instances/app1.py"
pkill -f "python3 ./instances/app2.py"
pkill -f "python3 ./instances/app3.py"
pkill -f "python3 ./instances/app4.py"
pkill -f "python3 ./instances/app5.py"
pkill -f "python3 load_balancer.py"
