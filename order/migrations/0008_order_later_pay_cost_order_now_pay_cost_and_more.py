# Generated by Django 4.1.5 on 2023-06-02 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_order_pickup_time_order_return_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='later_pay_cost',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='now_pay_cost',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='pickup_date',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='return_date',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='total_cost',
            field=models.PositiveIntegerField(default=0),
        ),
    ]