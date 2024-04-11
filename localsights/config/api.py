from tokenize import String
from ninja import NinjaAPI, Schema
from localsights.users.models import User #, Maps, Locations
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group
from typing import List

api = NinjaAPI()

class UserOut(Schema):
    id: int
    name: str
    first_name: str
    last_name: str
    username: str
    email: str

class LocationOut(Schema):
    id: int
    name: str

class LocationIn(Schema):
    name: str
    address: str
    city: str
    state: str
    country: str
    zipcode: int

class MapIn(Schema):
    name: str
    area: LocationIn
    locations: List[LocationIn]

class MapOut(Schema):
    id: int
    name: str
    # add more latter


# Searching

# User Searches
@api.get("/search/users/username/{string}", response=List[UserOut])
def search_users_by_username(request, string: str):
    users = User.objects.filter(username__icontains=string).all().order_by('username')[:10:1]
    return users

@api.get("/search/users/first_name/{string}", response=List[UserOut])
def search_users_by_first_name(request, string: str):
    users = User.objects.filter(first_name__icontains=string).all().order_by('username')[:10:1]
    return users

@api.get("/search/users/last_name/{string}", response=List[UserOut])
def search_users_by_last_name(request, string: str):
    users = User.objects.filter(last_name__icontains=string).all().order_by('username')[:10:1]
    return users

@api.get("/search/users/email/{string}", response=List[UserOut])
def search_users_by_email(request, string: str):
    users = User.objects.filter(email__icontains=string).all().order_by('username')[:10:1]
    return users


# For when map and location models are implemnted

# # Map Searches
# @api.get("/search/maps/name/{string}", response=List[MapOut])
# def search_maps_by_name(request, string: str):
#     maps = Map.objects.filter(mame__icontains=string).all().order_by('name')[:10:1]
#     return maps

# @api.get("/search/maps/", response=List[MapOut])
# def search_maps_by_area(request, payload: LocationIn):
#     # some time of search bassed on location schema
#     return maps


# # Location searches
# @api.get("/search/locations/name/{string}", response=List[MapOut])
# def search_locations_by_name(request, string: str):
#     maps = Location.objects.filter(mame__icontains=string).all().order_by('name')[:10:1]
#     return maps

# @api.get("/search/locations/", response=List[MapOut])
# def search_locations_by_location(request, payload: LocationIn):
#     # some time of search bassed on location schema
#     return locations


# Getting

# get user by id
@api.get("/user/{id}", response=UserOut)
def get_user(request, id ):
    user = get_object_or_404(User, id = id)
    return user

# # gets map by id
# @api.get("/map/{id}", response=MapOut)
# def get_map(request, id ):
#     maps = get_object_or_404(Map, id = id)
#     return maps

# # gets location by id
# @api.get("/location/{id}", response=LocationOut)
# def get_location(request, id ):
#     locations = get_object_or_404(Location, id = id)
#     return locations


# Creating

# # Create new map
# @api.post("/map")
# def create_map(request, payload: MapIn):
#     return {"id": map.id}

# @api.post("/location")
# def create_location(request, payload: LocationIn):
#     Location.objects.create(**payload.dict());
#     return {"id": map.id}


# Editing

# @api.put("/map/{id}")
# def update_map(request, id: int, payload: MapIn):
#     map = get_object_or_404(request.User.maps, id=id)
#     for attr, value in payload.dict().items():
#         setattr(map, attr, value)
#     map.save()
#     return {"success": True}

# @api.put("/location/{id}")
# def update_location(request, id: int, payload: MapIn):
#     location = get_object_or_404(Location, id=id)
#     for attr, value in payload.dict().items():
#         setattr(location, attr, value)
#     location.save()
#     return {"success": True}

# Removing

# removes map from user 
# @api.delete("/map/{id}")
# def delete_map(request, id: int):
#     user = get_object_or_404(request.User.Maps, id=id)
#     user.delete()
#     return {"success": True}