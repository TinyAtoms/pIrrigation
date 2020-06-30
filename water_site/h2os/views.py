from django.shortcuts import render, redirect
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Plant_group, Plant
from . import forms 
from django.contrib.auth.decorators import login_required 


def group_list(request):
    all_groups = Plant_group.objects.all().order_by('loc_id')
    return render(request, 'h2os/group_list.html', {'groups': all_groups} )

def plant_list(request):
    all_plants = Plant.objects.all().order_by('id')                         # Puts all plant objects in 'id' order in array
    return render(request, 'h2os/plant_list.html', {'plants': all_plants} ) # Sends array to html for display


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


@login_required(login_url="/accounts/login/")       # Requires user to be logged in in order to create a group
def group_create(request):
    if request.method == 'POST':                    
        form = forms.CreatePlantGroup(request.POST) # Assigns data to form -- Add request.Files if necessary to upload files
        if form.is_valid():                         # Checks to see if form is valid
            form.save()
            return redirect('h2os:group_list')      # Redirects to group_list page
    else:
        form = forms.CreatePlantGroup()             # Assigns creation form 
    return render(request, 'h2os/group_create.html', {'form':form}) # Send form to html for display

