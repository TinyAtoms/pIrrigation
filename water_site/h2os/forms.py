from django import forms
from . import models

class CreatePlantGroup(forms.ModelForm):
    class Meta:
        models = models.Plant_group
        fields=['loc_id','plant','growth_stage','growth_day','distance','water_flowrate','water_t1','water_t2','last_irrigated']