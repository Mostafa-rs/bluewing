# Generated by Django 4.1.5 on 2023-02-06 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_car_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='time',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.time'),
        ),
    ]
