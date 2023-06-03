# Generated by Django 4.1.5 on 2023-06-02 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_alter_itemorder_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='f_name',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='order',
            name='l_name',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Last name'),
        ),
    ]
