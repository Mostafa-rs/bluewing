# Generated by Django 4.1.5 on 2023-06-02 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_order_later_pay_cost_order_now_pay_cost_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='later_pay_cost',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='now_pay_cost',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_cost',
            field=models.FloatField(default=0),
        ),
    ]
