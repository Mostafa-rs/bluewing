# Generated by Django 4.1.5 on 2023-01-31 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_car_features'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='features',
        ),
        migrations.AddField(
            model_name='category',
            name='features',
            field=models.ManyToManyField(blank=True, null=True, related_name='features', to='home.category'),
        ),
    ]
