from .models import Report
from django.contrib.gis import admin
from mapwidgets.widgets import GooglePointFieldWidget
from django.contrib.gis.db import models as gis_models
from .forms import SewerForm
from Repo.api.serializers import ReportSerializer
import requests


# Register your models here.

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    formfield_overrides = {
        gis_models.PolygonField: {'widget': GooglePointFieldWidget}
    }

