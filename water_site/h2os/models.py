from django.db import models
from django.urls import reverse
import datetime
from .hardware import waterlevel, water_pan


class Pan_data(models.Model):
    '''
    This is the model that tracks how much water gets evaporated. It logs the waterlevel at the start of the day and
    continues to keep track of the latest waterlevel. 
    it should get scheduled in ./scheduling.py
    '''
    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField(auto_now=True)
    start_level = models.FloatField()
    last_level = models.FloatField()
    system_change = models.FloatField()

    def __str__(self):
        return f"{self.date}"

    def get_absolute_url(self):  # when you're going to implement the detail view
        """Returns the url to access a particular  instance. For detailfiews and such"""
        return reverse('plant-detail', args=[str(self.date)])

    class Meta:
        '''Some extra options'''
        db_table = "Pan_data"
        verbose_name_plural = "Pan_data"

    @classmethod
    def create(cls):
        '''This sets the startlevel on creation'''
        start = waterlevel()
        data = cls(start_level=start, last_level=start)
        return data

    def log(self):
        '''
        Measures current waterlevel, adds water when below a treshold and keeps track of autosiphon and relay use. 
        needs to be scheduled in scheduling.py
        '''
        new_level = waterlevel()
        # should call a function that measures waterlevel
        if abs(new_level - self.last_level) > 100:  # ml
            self.system_change -= 100
        if new_level < 100:  # TODO: set actual min treshold level here
            water_pan()
            self.system_change += 100
        self.last_level = new_level
        self.save()
    @property
    def evaporated_today(self):
        '''
        returns how much water evaporated today
        '''
        return (self.last_level - self.start_level) + self.system_change


class Water_usage(models.Model):
    '''
    This keeps track of past water usage of groups
    '''
    id = models.IntegerField(primary_key=True)
    group = models.OneToOneField("Plant_group", on_delete=models.CASCADE, unique=True)
    usage = models.FloatField(verbose_name="Water usage(L)")
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''How this gets named on the website'''
        return str(self.id)

    def get_absolute_url(self):  # when you're gonna implement the detail view
        """Returns the url to access a particular  instance."""
        return reverse('water-detail', args=[str(self.id)])

    class Meta:
        db_table = "Water_Usage"
        verbose_name_plural = "Water_usage"


STAGES = [
    ('initial', 'Initial planting stage'),
    ('interpolate', 'Development stage'),
    ('mid', 'Mature state'),
    ('end', 'Harvest state')
]
t1 = datetime.time(7, 0, 0)
t2 = datetime.time(17, 0, 0)


class Plant_group(models.Model):  # want to make this group
    # unique, since only one group per id
    loc_id = models.IntegerField(unique=True)
    plant = models.OneToOneField(
        "Plant", on_delete=models.PROTECT, blank=True, null=True)
    growth_stage = models.CharField(
        max_length=20, choices=STAGES, default='initial')
    growth_day = models.CharField(max_length=4)
    area = models.FloatField()  # m^2
    water_flowrate = models.FloatField()
    water_t1 = models.TimeField(default=t1)
    water_t2 = models.TimeField(default=t2)
    last_irrigated = models.DateTimeField()

    def __str__(self):
        return f"Group {self.loc_id}"

    def get_absolute_url(self):  # when you're going to implement the detail view
        """Returns the url to access a particular  instance."""
        return reverse('plant-group-detail', args=[str(self.loc_id)])

    class Meta:
        db_table = "Plantgroup"
        verbose_name_plural = "Plantgroups"

    def water_now(self):
        '''
        This waters the group. Needs to be scheduled in scheduling.py
        '''
        evaporated = Pan_data.objects.all()[-1].evaporated_today()
        water_requirement = evaporated * \
            self.plant.crop_factor(self.growth_day) * self.distance * 1
        # todo: add pan factor to the equation
        temp_now = datetime.datetime.now()
        now = datetime.time(temp_now.hour, temp_now.minute)
        if now >= self.water_t2:
            water_requirement -= Water_usage.objects.filter(
                group=self)[-1].usage
        relay_timer = water_requirement / self.water_flowrate
        water_group(self.loc_id, relay_timer)
        usage = Water_usage(group=self, usage=water_requirement)
        usage.save()


class Plant(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=100)
    initial_kc = models.FloatField()
    mid_kc = models.FloatField()
    end_kc = models.FloatField()
    initial_length = models.IntegerField()
    interpolate_length = models.IntegerField()
    mid_length = models.IntegerField()
    end_length = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):  # when you're going to implement the detail view
        """Returns the url to access a particular  instance."""
        return reverse('plant-detail', args=[str(self.id)])

    class Meta:
        db_table = "Plant"
        verbose_name_plural = "Plants"

    def crop_factor(self, day):
        '''
        Returns the crop factor(Kc) of a given crop and how long it's in the ground.
        parameters:
        return = float
        >> crop_factor(99)
        >> 1.04
        '''
        # determining stage
        if day < self.initial_length:
            return self.initial_kc
        elif day < self.initial_length + self.interpolate_length:
            x = day - self.initial_length
            dy = (self.mid_kc - self.initial_kc) / self.interpolate_length
            total = self.initial_kc + x * dy
            return total
        elif day < self.initial_length + self.interpolate_length + self.mid_length:
            return self.mid_kc
        else:
            return self.end_kc
