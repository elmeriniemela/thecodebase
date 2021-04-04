#!/bin/sh

# Stop if any line fails
set -e


if [ "$DEBUG" = "1" ]
then
    echo "Start the django development server.."
    python manage.py runserver 0.0.0.0:8000
else
    echo "Start the uwsgi server.."
    uwsgi --socket :8000 --master -b 32768 --enable-threads --module django_thecodebase.wsgi:application --check-static /app
fi
