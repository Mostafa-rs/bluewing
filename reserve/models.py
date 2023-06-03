from django.contrib.auth.models import User

from home.models import *


# Create your models here.

class Reserve(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cdw = models.BooleanField(default=False)
    pickup_place = models.TextField(null=True, blank=True)
    pickup_date = models.DateField(null=True, blank=True)
    pickup_time = models.TimeField(null=True, blank=True)
    return_place = models.TextField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    return_time = models.TimeField(null=True, blank=True)
    rent_duration = models.PositiveIntegerField(default=0)
    full_pay = models.BooleanField(default=False)
    discount = models.PositiveIntegerField(default=0)
    to_be_paid_amount = models.PositiveIntegerField(default=0)
    pending_amount = models.PositiveIntegerField(default=0)
    total_amount = models.PositiveIntegerField(default=0)


class ExtraReserve(models.Model):
    extra = models.ForeignKey(Extras, on_delete=models.CASCADE, related_name='extra_reserves')
    reserve = models.ForeignKey(Reserve, on_delete=models.CASCADE, related_name='extra_reserves')

    def __str__(self):
        return self.extra.name