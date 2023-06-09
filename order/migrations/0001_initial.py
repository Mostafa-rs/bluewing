# Generated by Django 4.1.5 on 2023-02-09 08:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0052_remove_times_total_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('paid', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254)),
                ('sex', models.CharField(choices=[('M', 'مرد'), ('F', 'خانم')], max_length=1)),
                ('f_name', models.CharField(max_length=60)),
                ('l_name', models.CharField(max_length=60)),
                ('pickup_location', models.TextField()),
                ('return_location', models.TextField()),
                ('phone', models.CharField(max_length=11)),
                ('city', models.CharField(max_length=60)),
                ('date_of_birth', models.DateField()),
                ('passport_front_image', models.ImageField(upload_to='passport_front')),
                ('passport_back_image', models.ImageField(blank=True, null=True, upload_to='passport_back')),
                ('driving_license_front_image', models.ImageField(upload_to='driving_license_front')),
                ('driving_license_back_image', models.ImageField(blank=True, null=True, upload_to='driving_license_back')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ItemOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.car')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_item', to='order.order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
