
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# এন্ট্রি পয়েন্ট ফাইলে এক্সিকিউট পারমিশন দেওয়া
RUN chmod +x entrypoint.sh

# এন্ট্রি পয়েন্ট রান করা
CMD ["./entrypoint.sh"]