from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from .models import *
from django.views.generic import ListView
from django.views import View
from django.shortcuts import render, redirect
from .models import *
import googlemaps
from django.conf import settings
from .forms import *
from datetime import datetime
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

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
    
class DistanceView(View):
    template_name = "pages/distance.html"

    def get(self, request): 
        form = DistanceForm
        distances = Distances.objects.all()
        context = {
            'form':form,
            'distances':distances
        }

        return render(request, self.template_name, context)

    def post(self, request): 
        form = DistanceForm(request.POST)
        if form.is_valid(): 
            from_location = form.cleaned_data['from_location']
            from_location_info = Location.objects.get(name=from_location)
            from_address_string = str(from_location_info.address)+", "+str(from_location_info.zipcode)+", "+str(from_location_info.city)+", "+str(from_location_info.country)

            to_location = form.cleaned_data['to_location']
            to_location_info = Location.objects.get(name=to_location)
            to_address_string = str(to_location_info.address)+", "+str(to_location_info.zipcode)+", "+str(to_location_info.city)+", "+str(to_location_info.country)

            mode = form.cleaned_data['mode']
            now = datetime.now()
            key = getattr(settings, 'GOOGLE_API_KEY', None)
            gmaps = googlemaps.Client(key)
            calculate = gmaps.distance_matrix(
                    from_address_string,
                    to_address_string,
                    mode = mode,
                    departure_time = now
            )


            duration_seconds = calculate['rows'][0]['elements'][0]['duration']['value']
            duration_minutes = duration_seconds/60

            distance_meters = calculate['rows'][0]['elements'][0]['distance']['value']
            distance_kilometers = distance_meters/1000

            if 'duration_in_traffic' in calculate['rows'][0]['elements'][0]: 
                duration_in_traffic_seconds = calculate['rows'][0]['elements'][0]['duration_in_traffic']['value']
                duration_in_traffic_minutes = duration_in_traffic_seconds/60
            else: 
                duration_in_traffic_minutes = None

            
            obj = Distances(
                from_location = Location.objects.get(name=from_location),
                to_location = Location.objects.get(name=to_location),
                mode = mode,
                distance_km = distance_kilometers,
                duration_mins = duration_minutes,
                duration_traffic_mins = duration_in_traffic_minutes
            )

            obj.save()

        else: 
            print(form.errors)
        
        return redirect('distance')
    
class DisplayMapView(View): 
    template_name = "pages/display_map.html"
    apikey = getattr(settings, 'GOOGLE_API_KEY', None)
    def get(self,request): 
        context = {
            "key": DisplayMapView.apikey
        }

        return render(request, self.template_name, context)
    
class LocationListView(ListView):
    model = Location
    template_name = "pages/locations.html"

class LocationDetailView(DetailView):
    model = Location
    template_name = "locations/location_detail.html"

class LocationCreateView(CreateView):
    model = Location
    fields = ['name', 'zipcode', 'city', 'country', 'address']
    template_name = "locations/location_form.html"

class LocationUpdateView(UpdateView):
    model = Location
    # Not recommended (potential security issue if more fields added)
    fields = ['name', 'zipcode', 'city', 'country', 'address']
    template_name = "locations/location_form.html"


class LocationDeleteView(DeleteView):
    model = Location
    success_url = reverse_lazy('locations')
    template_name = "locations/location_confirm_delete.html"

    def form_valid(self, form):
        try:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        except Exception as e:
            return HttpResponseRedirect(
                reverse("location-delete", kwargs={"pk": self.object.pk})
            )
    
    