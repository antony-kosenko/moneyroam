from environs import Env


# initialization of database's environmental variables
db_config = Env()
db_config.read_env("environs/.env.database")

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