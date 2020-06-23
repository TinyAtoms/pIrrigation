from django.urls import path

from . import views

app_name = 'h2os'

urlpatterns = [
    path('groups/', views.group_list, name='group_list'),
    path('groups/create/', views.group_create, name='create'),
    path('plants/', views.plant_list, name='plant_list'),
    path('plants/<int:pk>/', views.PlantDetailView.as_view(), name='plant-detail'),
    path("group/<int:pk>/", views.Plant_groupDetailView.as_view(), name="plant-group-detail")
    #wip path('group/<int:pk>', views.GroupDetailView.as_view(), name='group-detail'),
]