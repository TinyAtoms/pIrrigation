from django.contrib import admin
from .models import Plant_group, Plant, Water_usage, Pan_data
# Register your models here.

admin.site.register(Plant_group)


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    '''Registers the model so it's visible in the admin page '''
    list_display = ("id", "name")


@admin.register(Water_usage)
class UsageAdmin(admin.ModelAdmin):
    '''Registers the model so it's visible in the admin page '''
    list_display = ("group", "usage")


@admin.register(Pan_data)
class PanAdmin(admin.ModelAdmin):
    '''Registers the model so it's visible in the admin page '''
    list_display = ("date", "evaporated_today")
