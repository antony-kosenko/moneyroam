import os

from dotenv import load_dotenv
import dj_database_url

load_dotenv()

# initialization of database's environmental variables



ALLOWED_HOSTS = ["*"]

DATABASES = {
	"default": dj_database_url.parse(os.getenv("DB_URL"))
}
