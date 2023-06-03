# Generated by Django 4.1.5 on 2023-06-02 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_remove_order_extra_services_itemorder_extra_services'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='full_pay',
        ),
        migrations.RemoveField(
            model_name='order',
            name='pickup_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='pickup_location',
        ),
        migrations.RemoveField(
            model_name='order',
            name='pickup_time',
        ),
        migrations.RemoveField(
            model_name='order',
            name='return_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='return_location',
        ),
        migrations.RemoveField(
            model_name='order',
            name='return_time',
        ),
        migrations.AddField(
            model_name='itemorder',
            name='full_pay',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='itemorder',
            name='pickup_date',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='itemorder',
            name='pickup_location',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='itemorder',
            name='pickup_time',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='itemorder',
            name='return_date',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='itemorder',
            name='return_location',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='itemorder',
            name='return_time',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
