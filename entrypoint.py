#!/bin/sh

# ডাটাবেজ মাইগ্রেশন রান করা
python manage.py migrate --noinput

# স্ট্যাটিক ফাইল কালেক্ট করা
python manage.py collectstatic --noinput

# সুপারইউজার তৈরি (Username: Tamanna এবং Password: admin123)
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='Tamanna').exists() or User.objects.create_superuser('Tamanna', 'tamanna@example.com', 'admin123')"

# গিউনিকর্ন সার্ভার স্টার্ট করা
exec gunicorn config.wsgi:application --bind 0.0.0.0:10000