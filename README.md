# Load testing Flask API

## Traffic

- Max concurrent users: 1000
- User spawn rate: 100
- Time period: 1 minute
## Result

|                                                | Requests/sec | Failures/sec |
|------------------------------------------------|--------------|--------------|
| Single instance                                | 164.3        | 1.4          |
| Reverse proxy (Random)                         | 79.7         | 4.5          |
| Reverse proxy (Cyclic)                         | 68.8         | 3.7          |
| Gunicorn (5 workers [Recommended for 2 cores]) | 271.8        | 0.0          |
| Gunicorn (10 workers [2x recommended value])   | 223.8        | 0.0          |

## Detailed reports

- [Single instance](reports/single-instance.pdf)
- [Reverse proxy (Random)](reports/reverse-proxy-random.pdf)
- [Reverse proxy (Cyclic)](reports/reverse-proxy-cyclic.pdf)
- [Gunicorn (5 workers [Recommended for 2 cores])](reports/gunicorn-5w.pdf)
- [Gunicorn (10 workers [2x recommended workers])](reports/gunicorn-10w.pdf)
