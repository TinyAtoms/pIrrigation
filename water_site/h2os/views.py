from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Plant_group, Plant


def home(request):
    all_groups = Plant_group.objects.all().order_by('loc_id')
    return render(request, 'h2os/home.html', {'groups': all_groups} )

#def home(request):
 #   return HttpResponse("Hello, world. You're at the h2os application homepage.")


class PlantDetailView(generic.DetailView):
    model = Plant
    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get the context
    #     context = super(FactuurDetailView, self).get_context_data(**kwargs)
    #     # context['korting'] = context["factuur"].Korting_percent * context["factuur"].Subtotal / 100
    #     # context["beforetax"] = context["factuur"].Subtotal - context["korting"]
    #     # context["tax"] = context["beforetax"] * 0.08
    #     return context