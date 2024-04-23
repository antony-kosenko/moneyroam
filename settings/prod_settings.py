import dj_database_url
from environs import Env


# initialization of database's environmental variables
db_config = Env()
db_config.read_env("environs/.env.database")


ALLOWED_HOSTS = ["*"]

DATABASES = {
	"default": dj_database_url.parse(db_config("DB_URL"))
}