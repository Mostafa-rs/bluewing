# Generated by Django 4.1.5 on 2023-02-06 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_remove_car_time_car_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Times',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
    ]