from django.contrib.gis import forms
from django.forms import ModelForm
from .models import Report 
from django.contrib.gis.db import models
from SewerTrack.settings import MAP_WIDGETS
from mapwidgets.widgets import GooglePointFieldWidget


#create a form
class SewerForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['full_name', 'phone_number', 'type_of_incident', 'images', 'description', 'location','date_reported', 'date_occurred']
        widgets = {
            'location': GooglePointFieldWidget,
            'images' : forms.ClearableFileInput(attrs={'multiple': True}),
            'date_occurred': forms.DateInput(attrs={'type': 'date'})
        }


