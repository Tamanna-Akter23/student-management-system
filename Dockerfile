
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

# সরাসরি এখানে মাইগ্রেশন, স্ট্যাটিক ফাইল এবং সার্ভার স্টার্ট কমান্ড দিয়ে দেওয়া হলো
CMD python manage.py migrate --noinput && python manage.py collectstatic --noinput && python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='Tamanna').exists() or User.objects.create_superuser('Tamanna', 'tamanna@example.com', 'admin123')" && gunicorn config.wsgi:application --bind 0.0.0.0:10000