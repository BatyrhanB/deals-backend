#!/bin/sh
pip install uwsgi
export PYTHONPATH=/opt/services/deals-backend/src:$PYTHONPATH
cd src
echo "Make migrations"
python manage.py makemigrations
echo "Migrate"
python manage.py migrate
echo "Collect static"
python manage.py collectstatic --no-input
echo "Run server"
gunicorn --workers=5 --threads=2 --worker-class=gthread -b 0.0.0.0:8000 config.wsgi --reload