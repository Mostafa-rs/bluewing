# Generated by Django 4.1.5 on 2023-02-07 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0050_remove_times_total_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='times',
            name='total_cost',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
