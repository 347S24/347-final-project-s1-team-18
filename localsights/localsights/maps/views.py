from django.views.generic import ListView, DetailView, CreateView
from .models import Map, Location
from .forms import createMapForm

from django.shortcuts import render

def showMaps(request):
    maps = Map.objects.all()
    context = {
        "maps": maps
    }
    return render(request, "pages/maps.html", context)

class AddMapView(CreateView):
    model = Map
    template_name = "maps/createMap.html"
    fields = ['name', 'creator', 'zoom_level']

class MapDetailView(DetailView):
    model = Map
    template = "maps/map_detail.html"

def locationListView(request):
    locations = Location.objects.all()
    context = {
        "locations": locations
    }
    return render(request, "locations/location_list.html", context)

