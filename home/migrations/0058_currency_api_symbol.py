# Generated by Django 4.1.5 on 2023-05-22 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0057_currencyapi'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='api_symbol',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
