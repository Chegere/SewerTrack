from .models import Report
from django.contrib.gis import admin
from mapwidgets.widgets import MapboxPointFieldWidget
from django.contrib.gis.db import models as gis_models
from .forms import SewerForm


# Register your models here.


class ReportAdmin(admin.ModelAdmin):
    autocomplete_fields = ('location',)
    formfield_overrides = {
        gis_models.PointField: {'widget': MapboxPointFieldWidget}
    }