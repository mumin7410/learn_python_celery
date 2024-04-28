import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mycelery.settings')

app = Celery("mycelery")
app.config_from_object("django.conf:settings", namespace="CELERY")

@app.task
def add_number():
    return 

app.autodiscover_tasks()