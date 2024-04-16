from django import forms
from .models import Map

class createMapForm(forms.ModelForm):
    class Meta:
        model = Map
        fields = ['name', 'creator']