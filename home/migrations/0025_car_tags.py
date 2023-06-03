# Generated by Django 4.1.5 on 2023-02-01 11:48

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('home', '0024_extras_car_extras'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]