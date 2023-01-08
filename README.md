# API load balancer

Simple load balancer which splits the incoming requests between 5 instances in a cyclic way.

## How to run

- Run the flask apps inside ``/instances`` folder
- Once all 5 of the apps are running, run ``load_balancer.py``
- Run ``requester.py`` to send unlimited requests continously. Run multiple instances of it to increase the rate of requests
- Open ``127.0.0.1:5000/`` to see live graphs of the incoming requests
