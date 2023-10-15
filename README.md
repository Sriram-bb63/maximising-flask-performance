# Load testing Flask API

This repository contains reports of load capacity of a simple Flask API deployed using different configurations:

1. Single instance: ``py app.py`` The most basic form of  flask server running in your local machine.

2. Using a load balancer built with flask: It distributes the load in a random manner.

3. Using a load balancer built with flask: It distributes the load in a cyclic manner (Similar to round robin algorithm).

4. Gunicorn: Using 5 gunicorn workers. The number of workers is decided by 2 $\times$ Cores + 1.

5. Gunicorn: Using 10 gunicorn workers. It is twice the recomeneded value.

## How to run

First clone the repository: 
```sh
git clone https://github.com/Sriram-bb63/maximising-flask-performance.git
```

To run a single instance:
```sh
py instances/app1.py
```

To run the load balancer:
```sh
chmod +x run.sh
./run.sh
```

```sh
py load_balancer.py
```
> To change between cyclic mode and random mode, open ``load_balancer.py`` and comment/uncomment the respective code blocks.

To run using Gunicorn:
```sh
gunicorn instances.app1:app
```



## Traffic

- Max concurrent users: 1000
- User spawn rate: 100
- Time period: 1 minute
## Result

|                                                | Total requests | Requests/sec | Failures/sec |
|------------------------------------------------|----------------|--------------|--------------|
| Single instance                                | 9871           | 164.3        | 1.4          |
| Load balancer (Random URL)                     | 4788           | 79.7         | 4.5          |
| Load balancer (Cyclic URL)                     | 4125           | 68.8         | 3.7          |
| Gunicorn (5 workers [Recommended for 2 cores]) | 16335          | 271.8        | 0.0          |
| Gunicorn (10 workers [2x recommened value])    | 13443          | 223.8        | 0.0          |

## Detailed reports

- [Single instance](reports/single-instance.pdf)
- [Reverse proxy (Random)](reports/reverse-proxy-random.pdf)
- [Reverse proxy (Cyclic)](reports/reverse-proxy-cyclic.pdf)
- [Gunicorn (5 workers [Recommended for 2 cores])](reports/gunicorn-5w.pdf)
- [Gunicorn (10 workers [2x recommended workers])](reports/gunicorn-10w.pdf)
