from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('about/', views.about),
    path('h2os/', include('h2os.urls')),
    path('accounts/', include('accounts.urls')),
]
