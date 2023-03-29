import os
from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'turboshop.settings')

app = Celery('turboshop')

app.config_from_object('django.conf:settings')
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.autodiscover_tasks()
