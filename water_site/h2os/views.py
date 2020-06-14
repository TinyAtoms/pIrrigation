from django.shortcuts import render
from django.http import HttpResponse
from .models import Plant_group

def home(request):
    all_groups = Plant_group.objects.all().order_by('loc_id')
    return render(request, 'h2os/home.html', {'groups': all_groups} )


#def home(request):
 #   return HttpResponse("Hello, world. You're at the h2os application homepage.")