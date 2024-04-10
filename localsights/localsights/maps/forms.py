from django import forms
from .models import Map

class createMapForm(forms.Form):
    class Meta:
        model = Map
        fields = '__all__'