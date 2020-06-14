from django.db import models

class Plant_group(models.Model):
    loc_id = models.CharField(max_length = 2)
    plant_name = models.CharField(max_length = 50)
    growth_day = models.CharField(max_length = 4) # example 1.12 means first growth phase on the 2th day
    distance = models.FloatField()
    water_flowrate = models.FloatField()
    last_irrigated = models.DateTimeField()
    #add in a picture later


def __str__(self):
    return self.loc_id

