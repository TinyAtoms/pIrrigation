from django.urls import path
from datetime import datetime, timedelta
import pysnooper

from . import views
from background_task.models import Task
from .tasks import pan_checker, group_watering
app_name = 'h2os'

urlpatterns = [
    path('groups/', views.group_list, name='group_list'),
    path('groups/create/', views.group_create, name='create'),
    path('plants/', views.plant_list, name='plant_list'),
    path('plants/<int:pk>/', views.PlantDetailView.as_view(), name='plant-detail'),
    path("group/<int:pk>/", views.Plant_groupDetailView.as_view(),
         name="plant-group-detail")
    # wip path('group/<int:pk>', views.GroupDetailView.as_view(), name='group-detail'),
]



# this schedules the tasks when the system is run for the first time
if not Task.objects.filter(verbose_name="group_watering").exists():
    group_watering(schedule=timedelta(seconds=10), repeat=Task.DAILY, verbose_name="group_watering")
if not Task.objects.filter(verbose_name="pan_checker").exists():
    pan_checker(schedule=timedelta(seconds=10), repeat=Task.DAILY, verbose_name="pan_checker")


