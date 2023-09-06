from pathlib import Path
from decouple import config, Csv

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECRET_KEY
SECRET_KEY = config("SECRET_KEY")

# ALLOWED_HOSTS
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

# DEBUG
DEBUG = config("DEBUG", default=False, cast=bool)

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
