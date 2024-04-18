from django.views.generic import ListView, DetailView, CreateView
from django.views import View
from .models import *
from django.views.generic import ListView
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
import googlemaps
from django.conf import settings
from .form import *
from datetime import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

# def showMaps(request):
#     maps = Map.objects.all()
#     context = {
#         "maps": maps
#     }
#     return render(request, "pages/maps.html", context)

# def createMap(request):
#     form = createMapForm()
#     context = {
#         'form': form
#     }
#     return render(request, "createMap.html", context)

# class MapView(View): 
#     template_name = "pages/maps.html"

#     def get(self,request): 
#         key = getattr(settings, 'GOOGLE_API_KEY', None)
        
#         if not key:
#             # Handle the case when the API key is not set in settings
#             # You can raise an error, set a default key, or handle it as needed
#             raise ValueError("GOOGLE_API_KEY is not set in settings")
#         eligable_locations = Location.objects.filter(place_id__isnull=False)
#         locations = []

#         for a in eligable_locations: 
#             data = {
#                 'lat': float(a.lat), 
#                   lng': float(a    lng), 
#                 'name': a.name
#             }

#             locations.append(data)


#         context = {
#             "key":key, 
#             "locations": locations
#         }

#         return render(request, self.template_name, context)
    
class MapView(ListView):
    template_name = "pages/maps.html"
    context_object_name = 'mydata'
    model = Location
    success_url = "/"


class HomeView(ListView):
    template_name = "pages/home.html"
    context_object_name = 'mydata'
    model = Location
    success_url = "/"


class GeocodingView(View):
    template_name = "pages/geocoding.html"

    def get(self,request,pk): 
        location = Location.objects.get(pk=pk)

        if location.lng and location.lat and location.place_id != None: 
            lat = location.lat
            lng = location.lng
            place_id = location.place_id
            label = "from my database"

        if location.address and location.country and location.zipcode and location.city != None: 
            address_string = str(location.address)+", "+str(location.zipcode)+", "+str(location.city)+", "+str(location.country)
            key = getattr(settings, 'GOOGLE_API_KEY', None)
            gmaps = googlemaps.Client(key)
            result = gmaps.geocode(address_string)[0]
            
            lat = result.get('geometry', {}).get('location', {}).get('lat', None)
            lng = result.get('geometry', {}).get('location', {}).get('lng', None)
            place_id = result.get('place_id', {})
            label = "from my api call"
            location.lat = lat
            location.lng =  lng
            location.place_id = place_id
            location.save()

        else: 
            result = ""
            lat = ""
            lng = ""
            place_id = ""
            label = "no call made"


        context = {
            'result':result,
            'location':location,
            'lat':lat, 
            'lng':lng, 
            'place_id':place_id, 
            'label':label
        }
        
        return render(request, self.template_name, context)
    