#!/bin/sh

# Stop if any line fails
set -e

python manage.py collectstatic --noinput

uwsgi --socket :8000 --master --enable-threads --module django_thecodebase.wsgi:application
