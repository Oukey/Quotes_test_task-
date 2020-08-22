import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Quotes.settings')

app = Celery('price')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'get-price': {
        'task': 'Crypt.tasks.get_price',
        'schedule': crontab(minute='*/1'),
    },
}
