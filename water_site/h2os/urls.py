from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('factuur/<int:pk>', views.PlantDetailView.as_view(), name='plant-detail'),
]