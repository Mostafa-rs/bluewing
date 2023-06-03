# Generated by Django 4.1.5 on 2023-01-31 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_car_features_delete_carfeatures'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='features',
        ),
        migrations.AddField(
            model_name='car',
            name='features',
            field=models.ManyToManyField(blank=True, null=True, to='home.features'),
        ),
    ]