#!/bin/sh

# Stop if any line fails
set -e


if [ "$CELERY" = "1" ]; then
    echo "Start the Celery server.."
    exec celery --app=django_thecodebase worker --loglevel=info
elif [ "$DEBUG" = "1" ]; then
    echo "Start the Django development server.."
    exec python manage.py runserver 0.0.0.0:8000
else
    python manage.py collectstatic --noinput
    echo "Start the uWSGI server.."
    exec uwsgi --socket :8000 --master -b 32768 --enable-threads --module django_thecodebase.wsgi:application --check-static /app
fi
