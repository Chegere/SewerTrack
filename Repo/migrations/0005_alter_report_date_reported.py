# Generated by Django 4.2.dev20220930042619 on 2023-02-24 07:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Repo', '0004_report_date_occurred_alter_report_date_reported'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='date_reported',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
