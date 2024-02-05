from __future__ import absolute_import, unicode_literals
from celery import Celery
import os
from celery import Celery
import os

from celery.schedules import crontab
from pathlib import Path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.beat_schedule = {
    "delete_users_annually": {
        'task': 'app_clients.tasks.delete_user_annually',
        "schedule": crontab(minute=0, hour=0, day_of_month=1, month_of_year=1),  # Ежегодно в полночь 1 января
        "options": {
            "schedule_filename": str(Path(__file__).parent / "celerybeat-schedule")
        },
    },
}
app.conf.worker_prefetch_multiplier = 1
app.autodiscover_tasks()
