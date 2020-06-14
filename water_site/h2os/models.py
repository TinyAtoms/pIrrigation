from django.db import models
import datetime

STAGES = [('initial', 'Initial planting stage'), ('interpolate', 'Development stage'), ('mid', 'Mature state'), ('end', 'Harvest state')]
t1=datetime.time(7,0,0)
t2=datetime.time(17,0,0)

class Plant_group(models.Model):
    loc_id = models.CharField(max_length = 2, unique = True) #unique, since only one group per id
    plant_name = models.CharField(max_length = 50)
    growth_stage = models.CharField(max_length = 20, choices = STAGES, default = 'initial')
    growth_day = models.CharField(max_length = 4) 
    distance = models.FloatField()
    water_flowrate = models.FloatField()
    water_t1 = models.TimeField(default = t1)
    water_t2 = models.TimeField(default = t2)
    last_irrigated = models.DateTimeField()
    #add in a picture later


def __str__(self):
    return self.loc_id

