from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from SewerTrack import settings
import folium
from .forms import SewerForm
from .serializers import ReportSerializer
from .models import Report

# from .forms import LocationForm

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
    if request.method == 'POST':
        form = SewerForm(request.POST, request.FILES)
        if form.is_valid():
            reporting = form.save(commit=True)
            return redirect('home')
    else:
        form = SewerForm()
    return render(request, 'reporting.html', {'form': form})



