from django.shortcuts import render
from django.http import HttpResponse
from SewerTrack import settings
import folium
from .forms import SewerForm
from .forms import LocationForm

# Create your views here.
Kawangware = [-1.2823, 36.7524]

def home(request):
    #create map object
    m = folium.Map(location=Kawangware, zoom_start=15)
    m = m._repr_html_()
    context = {
        'm' : m,
    }
    return render(request, 'index.html', context)


#define your form reporting html

def reporting(request):
    form = SewerForm()
    return render(request, 'reporting.html', {'form':form})   

#capture location of user
def location_view(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']
            #do other things with the location data
    else:
        form = LocationForm()
    return render(request, 'reporting.html', {'form': form}) 