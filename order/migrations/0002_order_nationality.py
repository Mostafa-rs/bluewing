# Generated by Django 4.1.5 on 2023-05-22 11:55

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='nationality',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
    ]