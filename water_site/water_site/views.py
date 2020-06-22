from django.shortcuts import render
from django.http import HttpResponse

app_name='water_site'

def homepage(request):
    return render(request,'water_site/homepage.html')
def about(request):
    return render(request,'about.html')