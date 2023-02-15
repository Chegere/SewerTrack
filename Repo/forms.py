from django import forms
from django.forms import ModelForm
from .models import Report 
from django.contrib.gis.db import models
from mapwidgets.widgets import MapboxPointFieldWidget


#create a form
class SewerForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('full_name', 'phone_number', 'type_of_incident', 'images', 'location', 'description')
        
        # full_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group-text'}))
        # phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group-text'}))
        # type_of_incident = forms.ChoiceField(widget=forms.ChoiceField(attrs={'class': 'input-group-text'}))
        # images = forms.ImageField(widget=forms.ImageField(attrs={'class': 'input-group-text'}))
        # description = forms.Textarea(widget=forms.Textarea(attrs={'class': 'input-group-text'}))
        # location = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group-text'}))
        widgets = {
            'location': MapboxPointFieldWidget(),
        }


