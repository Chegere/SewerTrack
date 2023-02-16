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
        fields = ('__all__')
        widgets = {
            'location': GooglePointFieldWidget,
            'images' : forms.ClearableFileInput(attrs={'multiple': True})
        }


