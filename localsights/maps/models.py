from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=50, help_text='Enter Location Name')

    lattitude = models.DecimalField(max_digits=6, decimal_places=4)
    longitude = models.DecimalField(max_digits=7, decimal_places=4)

    # "Fast food", "Monument", etc 
    tag = models.CharField(max_length=50, help_text='Enter Location Tag')

    description = models.CharField(max_length=50, help_text='Enter a brief description')

# Create your models here.
class Map(models.Model):
    creator = models.CharField(max_length=50, help_text='Enter field documentation')
    locations = models.ManyToManyField(Location)
    name = models.CharField(max_length=50, help_text='Enter field documentation')

    center = models.CharField(max_length=50, help_text='Enter field documentation')
    zoom_level = models.DecimalField(max_digits=5, decimal_places=2)



