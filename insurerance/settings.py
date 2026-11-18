
"""
Django settings for InSureRance.
Insurance Literacy Learning and Analytics System.
"""

import os
from pathlib import Path
from dotenv import load_dotenv


# BASE DIRECTORY
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env
load_dotenv(BASE_DIR / ".env")


# SECURITY SETTINGS
# Keep the secret key inside .env, not in GitHub.
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

# Development only; disable for production.
DEBUG = True

ALLOWED_HOSTS = []


# APPLICATIONS
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "accounts",
    "dashboard",
]


# MIDDLEWARE
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# URL CONFIGURATION
ROOT_URLCONF = "insurerance.urls"


# TEMPLATES
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# WSGI APPLICATION
WSGI_APPLICATION = "insurerance.wsgi.application"


# DATABASE
# SQLite is temporary for local development.
# PostgreSQL will be used for the final IM2 project.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# CUSTOM USER MODEL
AUTH_USER_MODEL = "accounts.CustomUser"


# PASSWORD VALIDATION
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# AUTHENTICATION REDIRECTS
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "dashboard"
LOGOUT_REDIRECT_URL = "login"


# INTERNATIONALIZATION
LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Manila"

USE_I18N = True
USE_TZ = True


# STATIC FILES
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]


# DEFAULT PRIMARY KEY
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# EMAIL SETTINGS
# Email messages are displayed in the terminal during development.
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
