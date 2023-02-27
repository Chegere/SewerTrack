from django.db import models
import psycopg2
from django.contrib.gis.db import models 
from django.contrib.gis.db import models as gis_models
import PIL
from django.utils import timezone
import datetime

# Create your models here.
Incident_Type = [
    ('Sewer Choke','Sewer_Choke'),
    ('Manhole Clog','Manhole_Clog'),
    ('Sewer Pipe Burst','Sewer_Pipe_Burst'),
    ('Sewer Pipe Clog','Sewer_Pipe_Clog'),
    ('Manhole Burst','Manhole_Burst'),
    ('Sewer Pipe Leakage','Sewer_Pipe_Leakage'),
    ('Open Sewage Flowing','Open_Sewage_Flowing'),
    ('Any Other Kind', 'Any_Other_Kind'),

]



class Report(models.Model):
    full_name = models.CharField(max_length = 200, null = True)
    phone_number = models.CharField(help_text='Enter your Phone number', max_length=10)
    type_of_incident = models.CharField(max_length = 100,choices = Incident_Type)
    images = models.FileField(upload_to= 'files/',null=True)
    description = models.TextField(blank = True)
    location = gis_models.PointField(geography=False,  verbose_name=('location'), null=True,)
    date_reported = models.DateTimeField(verbose_name='Date Reported', default=timezone.now)
    date_occurred = models.DateField(default=datetime.date.today)


    def __str__(self):
        return f'Sewer incident reported on {self.date_reported}'

    class Meta:
        verbose_name_plural = 'Sewer incidents'
        
    def __str__(self):
        return self.full_name
