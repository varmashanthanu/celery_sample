import os
import random
import time
from celery import Celery

REDIS_BROKER = os.getenv('REDIS_BROKER')
REDIS_BACKEND = os.getenv('REDIS_BACKEND')

print('***************************************************************')
print('***************************************************************')
print(REDIS_BACKEND)
print(REDIS_BROKER)
print('***************************************************************')
print('***************************************************************')

celery_app = Celery('tasks', broker_url='redis://redis:6379/0', result_backend='redis://redis:6379/0')
celery_app.conf.broker_url = 'redis://redis:6379/0'
celery_app.conf.result_backend = 'redis://redis:6379/0'


@celery_app.task()
def some_task(delay: int):
    print(f'delay for {delay}')
    time.sleep(delay)
    print('end of delay')
    return random.random()
