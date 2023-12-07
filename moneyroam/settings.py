from pathlib import Path
from environs import Env

# initialization of config's enviromental variables
conf= Env()
conf.read_env("environs/.env.settings")
# initialization of database's enviromental variables
db_config = Env()
db_config.read_env("environs/.env.database")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = conf("KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


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

    # custom apps
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
]

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
                'invoices.context_processors.create_transaction_form'
            ],
        },
    },
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

WSGI_APPLICATION = 'moneyroam.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': db_config("NAME"),
        'USER': db_config("USER"),
        'PASSWORD': db_config("PASSWORD"),
        'HOST': db_config("HOST"),
        'PORT': db_config("PORT")
    }
}

# Logging config 

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,

    # Formatters:

    "formatters": {
        "base": {
            "format": "[{asctime}][{levelname}] {message}",
            "datefmt": "%d/%m/%Y %H:%M",
            "style": "{"
        }
    },

    # Handlers:

    "handlers": {
        "file": {
            "level": "WARNING",
            "class": "logging.FileHandler",
            "formatter": "base",           
            "filename": BASE_DIR / "logs/general.log"
        },
    },

    # loggers:

    "loggers": {
        "standart": {
            "handlers": ["file"],
            "level": "WARNING",
            "propagate": True
        }
    }
}

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

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
