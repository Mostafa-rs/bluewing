# Generated by Django 4.1.5 on 2023-06-02 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_order_full_pay'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pickup_time',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='return_time',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
