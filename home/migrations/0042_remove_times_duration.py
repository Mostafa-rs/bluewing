# Generated by Django 4.1.5 on 2023-02-06 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0041_times_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='times',
            name='duration',
        ),
    ]
