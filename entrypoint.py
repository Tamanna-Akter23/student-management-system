
#!/bin/sh

echo "Running database migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Creating superuser..."
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='Tamanna').exists() or User.objects.create_superuser('Tamanna', 'tamanna@example.com', 'admin123')"

echo "Starting Gunicorn server..."
exec gunicorn config.wsgi:application --bind 0.0.0.0:10000