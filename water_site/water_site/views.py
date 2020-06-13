from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    #return HttpResponse("Hello, world. You're at the watersite homepage.")
    return render(request,'water_site/homepage.html')
def about(request):
    #return HttpResponse("This is the about page.")
    return render(request,'about.html')