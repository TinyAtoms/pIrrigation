from django.db import models
from django.urls import reverse
import datetime

STAGES = [('initial', 'Initial planting stage'), ('interpolate',
                                                  'Development stage'), ('mid', 'Mature state'), ('end', 'Harvest state')]
t1 = datetime.time(7, 0, 0)
t2 = datetime.time(17, 0, 0)


class Plant_group(models.Model):  # want to make this groups
    # unique, since only one group per id
    loc_id = models.IntegerField(unique=True)
    plant = models.OneToOneField(
        "Plant", on_delete=models.PROTECT, blank=True, null=True)
    growth_stage = models.CharField(
        max_length=20, choices=STAGES, default='initial')
    growth_day = models.CharField(max_length=4)
    distance = models.FloatField()
    water_flowrate = models.FloatField()
    water_t1 = models.TimeField(default=t1)
    water_t2 = models.TimeField(default=t2)
    last_irrigated = models.DateTimeField()

    def __str__(self):
        return f"Group {self.loc_id}"

    def get_absolute_url(self):  # when you're gonna implement the detail view
        """Returns the url to access a particular  instance."""
        return reverse('plant-group-detail', args=[str(self.loc_id)])

    class Meta:
        db_table = "Plantgroup"
        verbose_name_plural = "Plantgroups"


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

    def get_absolute_url(self):  # when you're gonna implement the detail view
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


class Water_usage(models.Model):  # want to make this groups
    # unique, since only one group per id
    id = models.IntegerField(primary_key=True)
    group = models.OneToOneField("Plant_group", on_delete=models.CASCADE)
    usage = models.FloatField(verbose_name="Water usage(L)")

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):  # when you're gonna implement the detail view
        """Returns the url to access a particular  instance."""
        return reverse('water-detail', args=[str(self.id)])

    class Meta:
        db_table = "Water_Usage"
        verbose_name_plural = "Water_usage"
