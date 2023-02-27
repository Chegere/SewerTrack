# Generated by Django 4.2.dev20220930042619 on 2023-02-27 11:44

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Repo', '0013_alter_report_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, default=None, null=True, srid=4326, verbose_name='Location'),
        ),
    ]
