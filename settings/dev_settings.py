import os
from dotenv import load_dotenv

load_dotenv("environs/.env.database")

# initialization of database's environmental variables

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.getenv("NAME"),
            'USER': os.getenv("USER"),
            'PASSWORD': os.getenv("PASSWORD"),
            'HOST': os.getenv("HOST"),
            'PORT': os.getenv("PORT")
        }
    }