# Generated by Django 4.1.5 on 2023-02-06 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_remove_time_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='time',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.time'),
        ),
    ]
