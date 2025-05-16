from celery import shared_task
from time import sleep

@shared_task
def add(x,y):
    sleep(5)
    print('Done')
    return x + y

@shared_task
def birthday_reminder(name):
    print('name',name)
    return name