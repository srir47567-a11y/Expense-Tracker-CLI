import random 
from datetime import datetime,timedelta

ips = ["192.168.1.5","10.0.0.42","45.132.10.5","172.16.0.10","203.0.113.25"]
paths = ["/","/login","/products","/admin","/api/users","/about","/contact"]
methods = ["GET", "GET", "GET", "GET", "GET", "POST"]
statuses = [200, 200, 200, 200, 404, 404, 500, 403]

start_date = datetime(2025, 1, 15)

with open('sample.log','w') as file:
    for _ in range(200):
        random_date=start_date+ timedelta(days=random.randint(0,6),seconds=random.randint(0,86399))

        ip=random.choice(ips)
        path=random.choice(paths)
        method=random.choice(methods)
        status=random.choice(statuses)
        size=random.randint(100,10000)

        line = (
            f'{ip} - - '
            f'[{random_date.strftime("%d/%b/%Y:%H:%M:%S")} +0000] '
            f'"{method} {path} HTTP/1.1" '
            f'{status} {size}\n'
        )

        file.write(line)
