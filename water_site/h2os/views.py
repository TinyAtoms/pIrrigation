from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Plant_group, Plant


def group_list(request):
    all_groups = Plant_group.objects.all().order_by('loc_id')
    return render(request, 'h2os/group_list.html', {'groups': all_groups} )

def plant_list(request):
    all_plants = Plant.objects.all().order_by('id')
    return render(request, 'h2os/plant_list.html', {'plants': all_plants} )


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
    

'''
def article_detail(request, slug):
    # return HttpResponse(slug)
    plant = Plant.objects.get(id=slug)
    return render(request, 'h2os/plant_detail.html', { 'plant': plant })
    '''