
from __future__ import absolute_import

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_thecodebase.settings')

celery_app = Celery('proj')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
celery_app.conf.update(
    broker_url='amqp://rabbitmq//'
)

# Load task modules from all registered Django app configs.
celery_app.autodiscover_tasks()

