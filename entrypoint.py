import os
import socket
import time

services = [
    ('MySQL', os.getenv('MYSQL_HOST', 'mysql'), int(os.getenv('MYSQL_PORT', '3306'))),
    ('PostgreSQL', os.getenv('POSTGRES_HOST', 'postgres'), int(os.getenv('POSTGRES_PORT', '5432'))),
    ('MongoDB', 'mongo', 27017),
]

for name, host, port in services:
    print(f'Waiting for {name} at {host}:{port}...')
    for attempt in range(60):
        try:
            with socket.create_connection((host, port), timeout=2):
                print(f'{name} is ready.')
                break
        except OSError:
            time.sleep(2)
    else:
        raise SystemExit(f'{name} did not become ready in time.')
