import os

from dotenv import load_dotenv

load_dotenv()

# initialization of database's environmental variables


ALLOWED_HOSTS = ["51.21.27.112"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
		"NAME": "moneyroam",
        "USER": "admin",
        "PASSWORD": "kosya523422",
        "HOST": "localhost",
        "PORT": ""
    }
}