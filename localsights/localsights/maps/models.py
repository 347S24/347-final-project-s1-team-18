from django.db import models

# Create your models here.

from django.urls import reverse  # To generate URLS by reversing URL patterns
import uuid # Required for unique location instances


class Location(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular book across whole library")
    
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter a name for your location"
    )

    lattitude = models.FloatField()
    longtitude = models.FloatField() 
    
    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name
    
class Map:
    name = models.CharField(
        max_length=200,
        unique=False,
        help_text="Enter a name for your location"
    )

    locations = models.ManyToManyField(
        'Location',
        related_name='locations'
    )

    zoom_level = models.FloatField()
    

