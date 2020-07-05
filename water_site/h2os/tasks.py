from .models import Plant_group, Pan_data
from .hardware import waterlevel
from background_task import background
from datetime import date, datetime, timedelta


@background(schedule=300)
def logger(pandataID):
    """This makes a pan_data object log the waterlevel. expected to run every 5 mins"""
    pandata = Pan_data.objects.latest("id")
    pandata.log()


@background
def pan_checker():
    '''
    This creates a new pandata object, and schedules the logging to happen every 5 mins for that day.
    Expected to run daily'''
    level_now = waterlevel()
    pandata = Pan_data(start_level=level_now, last_level=level_now)
    pandata.save()
    # cuz i get null as id otherwise...
    pandata = Pan_data.objects.latest("id")
    logger(pandata.id, repeat=300, repeat_until=(  # change back to 300 later, wehich is 5 mins
        datetime.now() + timedelta(days=1)))


@background
def water_time(pg_id):
    '''
    This schedules water_now to be called at a specific time. 
    Used only in group_watering
    '''
    print(" WATERING SCHEDULE COMMENCE")

    plantgroup = Plant_group.objects.get(loc_id=pg_id)
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
        pg_id = pg.loc_id
        today = today.replace(hour=t1.hour, minute=t1.minute)
        water_time(pg_id, schedule=today)
        today = today.replace(hour=t2.hour, minute=t2.minute)
        water_time(pg_id, schedule=today)
