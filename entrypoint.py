
#!/bin/sh

# ১. প্রথমে ডাটাবেজ মাইগ্রেশন রান করা বাধ্যতামূলক
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# ২. স্ট্যাটিক ফাইল কালেক্ট করা
python manage.py collectstatic --noinput

# ৩. সুপারইউজার তৈরি করা
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='Tamanna').exists() or User.objects.create_superuser('Tamanna', 'tamanna@example.com', 'admin123')"

# ৪. সার্ভার স্টার্ট করা
exec gunicorn config.wsgi:application --bind 0.0.0.0:10000