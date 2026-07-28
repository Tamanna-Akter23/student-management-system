# Deployment Guide

## Local Docker deployment

1. Install and start Docker Desktop.
2. Open this project folder in VS Code.
3. Run:

```powershell
docker compose up --build
```

4. In another terminal, create the first account:

```powershell
docker compose exec web python manage.py createsuperuser
```

5. Open `http://127.0.0.1:8000` and sign in.

The web container waits for MySQL, PostgreSQL, and MongoDB before applying migrations.

## Restart later

```powershell
docker compose up
```

## Stop

```powershell
docker compose down
```

## Production checklist

- Set a strong `SECRET_KEY` environment variable.
- Set `DEBUG=False`.
- Set `ALLOWED_HOSTS` to your domain.
- Use managed MySQL and PostgreSQL services.
- Use MongoDB Atlas or another secured MongoDB service.
- Enable database authentication and TLS.
- Run `python manage.py collectstatic`.
- Serve Django with Gunicorn behind HTTPS.
- Back up all three databases regularly.
