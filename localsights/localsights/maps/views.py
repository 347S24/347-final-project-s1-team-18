from django.views.generic import ListView, DetailView
from .models import Map
from maps.forms import createMapForm

from django.shortcuts import render


def createMap(request):
    context = {}
    map_form = createMapForm()
    context['form'] = map_form
    return render(request, "createMap.html")