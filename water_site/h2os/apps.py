from django.apps import AppConfig
from .scheduling import pan_checker, group_watering
from datetime import datetime, timedelta


class H2OsConfig(AppConfig):
    name = 'h2os'
    # debug: this is not working because apps not loaded yet
    # def ready(self):
    #     '''
    #     This is a function that readies the app. For now, it's used to schedule the tasks
    #     '''
    #     now = datetime.now() + timedelta(minutes=1)
    #     group_watering(schedule=now, repeat=Task.DAILY)
    #     pan_checker(schedule=now, repeat=Task.DAILY)
