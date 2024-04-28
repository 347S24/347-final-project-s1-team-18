from django.db import models

# Create your models here.

from django.urls import reverse  # To generate URLS by reversing URL patterns
import uuid # Required for unique location instances


class Location(models.Model):
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    zipcode = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    edited_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    latitude = models.DecimalField(max_digits = 9, decimal_places = 6, blank=True, null=True) 
    longitude = models.DecimalField(max_digits = 9, decimal_places = 6, blank=True, null=True) 
    place_id = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('location-detail', args=[str(self.id)])
    
class Map(models.Model):
    name = models.CharField(
        max_length=200,
        unique=False,
        help_text="",
        default=''
    )

    creator = models.CharField(
        max_length=200,
        unique=False,
        help_text="",
        default=''
    )


    locations = models.ManyToManyField(
        'Location',
        related_name='locations'
    )

    date = models.DateField()

    zoom_level = models.FloatField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('map-detail', args=[str(self.id)])
    
class Distances (models.Model):
    from_location = models.ForeignKey(Location, related_name = 'from_location', on_delete=models.CASCADE)
    to_location = models.ForeignKey(Location, related_name = 'to_location', on_delete=models.CASCADE)
    mode = models.CharField(max_length=200, blank=True, null=True)
    distance_km = models.DecimalField(max_digits=10, decimal_places=2)
    duration_mins = models.DecimalField(max_digits=10, decimal_places=2)
    duration_traffic_mins = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id

