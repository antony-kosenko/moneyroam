import os

from pathlib import Path
from dotenv import load_dotenv

from moneyroam.utils import get_django_token


# ENVS -----------------------------------------------
load_dotenv("environs/.env.settings")
# ----------------------------------------------------

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INTERNAL_IPS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third party packages
    "mptt",
    "crispy_forms",
    "crispy_bootstrap4",
    "django_filters",
    'django_cleanup',
    "debug_toolbar",

    # project apps
    "invoices",
    "accounts",
    "preferences",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

ROOT_URLCONF = 'moneyroam.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'moneyroam.context_processors.current_date_context',
                'accounts.context_processors.profile_update_form',
                'invoices.context_processors.create_transaction_form',
                'preferences.context_processors.preferences_update_form',
            ],
        },
    },
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

WSGI_APPLICATION = 'moneyroam.wsgi.application'

# Logging config 

# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,

#     # Filters
#     "filters": {
#         "info_only": {
#             "()": "logger.filters.InfoLogsOnlyFilter"
#         },
#         "exclude_django_logs": {
#             "()": "logger.filters.ExcludeDjangoLogs"
#         }
#     },

#     # Formatters
#     "formatters": {
#         "base": {
#             "format": "[{asctime}][{levelname}] {name} -> {funcName} :: {message} [line {lineno}]",
#             "datefmt": "%d/%m/%Y | %H:%M:%S",
#             "style": "{",
#         },
#         "info": {
#             "format": "[{asctime} ] {name} -> {funcName} :: {message} [line {lineno}]",
#             "datefmt": "%d/%m/%Y | %H:%M:%S",
#             "style": "{",
#         }
#     },

#     # Handlers
#     "handlers": {
#         "important_to_file": {
#             "level": "WARNING",
#             "class": "logging.handlers.RotatingFileHandler",
#             "filename": BASE_DIR / "logger/logs/important/important.log",
#             "maxBytes": 5 * 1024 * 1024,  # 5 MB log file size to rotate
#             "backupCount": 3,
#             "filters": ["exclude_django_logs"],
#             "formatter": "base",
#         },

#         "base_info_to_file": {
#             "level": "INFO",
#             "class": "logging.handlers.RotatingFileHandler",
#             "filename": BASE_DIR / "logger/logs/info/base_info.log",
#             "filters": ["info_only", "exclude_django_logs"],
#             "maxBytes": 5 * 1024 * 1024,  # 5 MB log file size to rotate
#             "backupCount": 3,
#             "formatter": "info"
#         },

#         "django_to_file": {
#             "level": "INFO",
#             "class": "logging.handlers.RotatingFileHandler",
#             "filename": BASE_DIR / "logger/logs/info/django_logs.log",
#             "maxBytes": 5 * 1024 * 1024,  # 5 MB log file size to rotate
#             "backupCount": 3,
#             "formatter": "base"
#         }
#     },

#     # Loggers
#     "loggers": {
#         "root": {
#             "handlers": ["important_to_file", "base_info_to_file"],
#             "level": "INFO",
#             "propagate": True
#         },
#         "django": {
#             "handlers": ["django_to_file"],
#             "level": "INFO",
#             "propagate": True
#         }
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = "accounts.CustomUser"
LOGIN_URL = 'accounts:login'

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = '/media/'


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Image resizing 

DJANGORESIZED_DEFAULT_SIZE = [500, 500]
DJANGORESIZED_DEFAULT_SCALE = 0.5
DJANGORESIZED_DEFAULT_QUALITY = 95
DJANGORESIZED_DEFAULT_KEEP_META = True
DJANGORESIZED_DEFAULT_FORCE_FORMAT = "WEBP"
DJANGORESIZED_DEFAULT_FORMAT_EXTENSIONS = {'JPEG': ".jpg", "WEBP": ".webp"}
DJANGORESIZED_DEFAULT_NORMALIZE_ROTATION = True


if DEBUG:
    from settings.dev_settings import *
    SECRET_KEY = os.environ.get("KEY")
else:
    SECRET_KEY = get_django_token() 
    from settings.prod_settings import *
