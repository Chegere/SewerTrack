from django import forms
from django.forms import ModelForm
from .models import Report 
import attrs


#create a form
class SewerForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('__all__')


class LocationForm(forms.ModelForm):
    latitude = forms.DecimalField(widget=forms.HiddenInput())
    longitude = forms.DecimalField(widget=forms.HiddenInput())
    
