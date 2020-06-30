from .models import Plant_group, Pan_data
from background_task import background
from datetime import date, datetime, timedelta


@background(schedule=300)
def logger(pandata):
    """This makes a pan_data object log the waterlevel. expected to run every 5 mins"""
    pandata.log()


@background
def pan_checker():
    '''
    This creates a new pandata object, and schedules the logging to happen every 5 mins for that day.
    Expected to run daily'''
    pandata = Pan_data()
    pandata.save()
    logger(pandata, repeat=300, repeat_until=(
        datetime.now() + timedelta(days=1)))


@background
def water_time(plantgroup):
    '''
    This schedules water_now to be called at a specific time. 
    Used only in group_watering
    '''
    plantgroup.water_now()


@background
def group_watering():
    '''
    This will schedule the watering times of all groups daily. 
    '''
    for pg in Plant_group.objects.all():
        t1 = pg.water_t1
        t2 = pg.water_t2
        today = datetime.today()
        today.hour = t1.hour
        today.minute = t1.minute
        water_time(pg, schedule=today)
        today.hour = t2.hour
        today.minute = t2.minute
        water_time(pg, schedule=today)
