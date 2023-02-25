from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from SewerTrack import settings
import folium
from .forms import SewerForm
from .models import Report
import googlemaps


# Create your views here

def home(request):
    incidents = Report.objects.all()
    return render(request, 'index.html', {'incidents': incidents})


def reporting(request):
    if request.method == 'POST':
        form = SewerForm(request.POST, request.FILES)
        if form.is_valid():
            reporting = form.save(commit=True)
            return redirect('home')
    else:
        form = SewerForm()
    return render(request, 'reporting.html', {'form': form})


