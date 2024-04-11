from django.views.generic import ListView, DetailView
from .models import Map
from .forms import createMapForm

from django.shortcuts import render

def showMaps(request):
    maps = Map.objects.all()
    context = {
        "maps": maps
    }
    return render(request, "pages/maps.html", context)

def createMap(request):
    form = createMapForm()
    context = {
        'form': form
    }
    return render(request, "createMap.html", context)