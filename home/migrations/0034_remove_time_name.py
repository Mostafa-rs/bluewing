# Generated by Django 4.1.5 on 2023-02-06 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='time',
            name='name',
        ),
    ]
