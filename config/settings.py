import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "temporary-development-secret-key"
)

DEBUG = os.environ.get("DEBUG", "False").lower() == "true"

ALLOWED_HOSTS = [
    host.strip()
    for host in os.environ.get(
        "ALLOWED_HOSTS",
        "127.0.0.1,localhost"
    ).split(",")
    if host.strip()
]

CSRF_TRUSTED_ORIGINS = [
    origin.strip()
    for origin in os.environ.get(
        "CSRF_TRUSTED_ORIGINS",
        ""
    ).split(",")
    if origin.strip()
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'students',
    'courses',
    'notes',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [BASE_DIR / 'templates'],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ]
    },
}]
WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',

    'NAME': os.getenv(
        'MYSQLDATABASE',
        os.getenv('MYSQL_DATABASE', 'student_db')
    ),

    'USER': os.getenv(
        'MYSQLUSER',
        os.getenv('MYSQL_USER', 'student_user')
    ),

    'PASSWORD': os.getenv(
        'MYSQLPASSWORD',
        os.getenv('MYSQL_PASSWORD', 'student_pass')
    ),

    'HOST': os.getenv(
        'MYSQLHOST',
        os.getenv('MYSQL_HOST', 'mysql')
    ),

    'PORT': os.getenv(
        'MYSQLPORT',
        os.getenv('MYSQL_PORT', '3306')
    ),

    'OPTIONS': {
        'charset': 'utf8mb4',
    },
},'postgres': {
    'ENGINE': 'django.db.backends.postgresql',

    'NAME': os.getenv(
        'PGDATABASE',
        os.getenv('POSTGRES_DB', 'course_db')
    ),

    'USER': os.getenv(
        'PGUSER',
        os.getenv('POSTGRES_USER', 'course_user')
    ),

    'PASSWORD': os.getenv(
        'PGPASSWORD',
        os.getenv('POSTGRES_PASSWORD', 'course_pass')
    ),

    'HOST': os.getenv(
        'PGHOST',
        os.getenv('POSTGRES_HOST', 'postgres')
    ),

    'PORT': os.getenv(
        'PGPORT',
        os.getenv('POSTGRES_PORT', '5432')
    ),
},
}
DATABASE_ROUTERS = ['config.router.DatabaseRouter']

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MONGO_URI = os.getenv(
    'MONGO_URI',
    'mongodb://mongo:27017/'
)

MONGO_DB = os.getenv(
    'MONGO_DB',
    'student_notes'
)

LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/accounts/login/"

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    },
}
