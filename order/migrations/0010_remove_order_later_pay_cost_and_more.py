# Generated by Django 4.1.5 on 2023-06-02 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_alter_order_later_pay_cost_alter_order_now_pay_cost_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='later_pay_cost',
        ),
        migrations.RemoveField(
            model_name='order',
            name='now_pay_cost',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total_cost',
        ),
    ]