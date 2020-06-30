from django.contrib import admin
from django.urls import include, path
from . import views
from h2os import views as h2os_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', h2os_views.group_list, name="home"),
    path('about/', views.about),
    path('h2os/', include('h2os.urls')),
    path('accounts/', include('accounts.urls')),
]
