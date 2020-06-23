from django.shortcuts import render, redirect
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Plant_group, Plant
from . import forms 


def group_list(request):
    all_groups = Plant_group.objects.all().order_by('loc_id')
    return render(request, 'h2os/group_list.html', {'groups': all_groups} )

def plant_list(request):
    all_plants = Plant.objects.all().order_by('id')
    return render(request, 'h2os/plant_list.html', {'plants': all_plants} )

class Plant_groupDetailView(generic.DetailView):
    model = Plant_group

class PlantDetailView(generic.DetailView):
    model = Plant
    ## example of how to add things to context. ignore. // TODO: remove when done
    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get the context
    #     context = super(FactuurDetailView, self).get_context_data(**kwargs)
    #     # context['korting'] = context["factuur"].Korting_percent * context["factuur"].Subtotal / 100
    #     # context["beforetax"] = context["factuur"].Subtotal - context["korting"]
    #     # context["tax"] = context["beforetax"] * 0.08
    #     return context
    
def group_create(request):
    if request.method == 'POST':
        form = forms.CreatePlantGroup(request.POST, request.FILES)
        if form.is_valid():
            return redirect('h2os:group_list')
            #save to db
    else:
        form = forms.CreatePlantGroup()
    return render(request, 'h2os/group_create.html', {'form':form})