# Generated by Django 4.2.dev20220930042619 on 2023-02-27 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Repo', '0011_remove_report_is_resolved_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='is_resolved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='report',
            name='resolved_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='type_of_incident',
            field=models.CharField(choices=[('Sewer Choke', 'Sewer_Choke'), ('Manhole Clog', 'Manhole_Clog'), ('Sewer Pipe Burst', 'Sewer_Pipe_Burst'), ('Sewer Pipe Clog', 'Sewer_Pipe_Clog'), ('Manhole Burst', 'Manhole_Burst'), ('Sewer Pipe Leakage', 'Sewer_Pipe_Leakage'), ('Open Sewage Flowing', 'Open_Sewage_Flowing'), ('Any Other Kind', 'Any_Other_Kind')], max_length=100),
        ),
    ]
