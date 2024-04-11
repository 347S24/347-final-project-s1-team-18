from django.db import models

# Create your models here.

from django.urls import reverse  # To generate URLS by reversing URL patterns
import uuid # Required for unique location instances


class Location(models.Model):
    club = models.CharField(max_length=500,blank=True, null=True)
    name = models.CharField(max_length=500)
    zipcode = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Map(models.Model):
    name = models.CharField(
        max_length=200,
        unique=False,
        help_text="Enter a name for your Map",
        default='SOME STRING'
    )

    creator = models.CharField(
        max_length=200,
        unique=False,
        help_text="Enter your name",
        default='SOME STRING'
    )


    locations = models.ManyToManyField(
        'Location',
        related_name='locations'
    )

    zoom_level = models.FloatField()
    

