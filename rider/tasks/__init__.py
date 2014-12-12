from celery import Celery
from celery.task import task
from rider import conf

application = Celery()
application.config_from_object(conf.tasks)
