# Generated by Django 4.1.5 on 2023-02-07 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0049_times_total_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='times',
            name='total_cost',
        ),
    ]
