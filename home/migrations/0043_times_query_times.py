# Generated by Django 4.1.5 on 2023-02-06 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0042_remove_times_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='times',
            name='query_times',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
