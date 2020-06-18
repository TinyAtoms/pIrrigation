from django.contrib import admin
from .models import Plant_group, Plant, Water_usage
# Register your models here.

admin.site.register(Plant_group)


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ("id", "name")




@admin.register(Water_usage)
class UsageAdmin(admin.ModelAdmin):
    list_display = ("group", "usage")