# Generated by Django 4.2.dev20220930042619 on 2023-02-13 07:33

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, null=True)),
                ('phone_number', models.CharField(help_text='Enter your Phone number', max_length=10)),
                ('type_of_incident', models.CharField(choices=[('SCH', 'Sewer_Choke'), ('MANC', 'Manhole_Clog'), ('SPBU', 'Sewer_Pipe_Burst'), ('SPCL', 'Sewer_Pipe_Clog'), ('MANB', 'Manhole_Burst'), ('SPLE', 'Sewer_Pipe_Leakage'), ('OSF', 'Open_Sewage_Flowing'), ('OTR', 'Any_Other_Kind')], max_length=100)),
                ('images', models.ImageField(upload_to='')),
                ('description', models.TextField(blank=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326, verbose_name='location')),
            ],
        ),
    ]
