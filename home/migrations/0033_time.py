# Generated by Django 4.1.5 on 2023-02-06 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pickup_date', models.DateField(blank=True, null=True)),
                ('pickup_time', models.TimeField(blank=True, null=True)),
                ('return_date', models.DateField(blank=True, null=True)),
                ('return_time', models.TimeField(blank=True, null=True)),
            ],
        ),
    ]