# Generated by Django 4.1.5 on 2023-06-02 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0065_alter_times_car_alter_times_pickup_date_and_more'),
        ('order', '0011_itemorder_later_pay_cost_itemorder_now_pay_cost_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='extra_services',
        ),
        migrations.AddField(
            model_name='itemorder',
            name='extra_services',
            field=models.ManyToManyField(blank=True, to='home.extras'),
        ),
    ]