# Generated by Django 4.1.5 on 2023-06-02 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0066_alter_currency_change_alter_currency_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='change',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
