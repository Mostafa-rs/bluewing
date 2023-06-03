from django.contrib.auth.models import User
from django.forms import ModelForm
from django_countries.fields import CountryField

from home.models import *


# Create your models here.

class Order(models.Model):
    SEX = [
        ("M", "مرد"),
        ("F", "خانم")
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    email = models.EmailField(null=True, blank=True)
    sex = models.CharField(max_length=1, choices=SEX, null=True, blank=True)
    f_name = models.CharField(max_length=60, null=True, blank=True, verbose_name='First name')
    l_name = models.CharField(max_length=60, null=True, blank=True, verbose_name='Last name')
    phone = models.CharField(max_length=11, null=True, blank=True)
    nationality = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=60, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    passport_front_image = models.ImageField(upload_to='passport_front', null=True, blank=True)
    passport_back_image = models.ImageField(upload_to='passport_back', blank=True, null=True)
    driving_license_front_image = models.ImageField(upload_to='driving_license_front', null=True, blank=True)
    driving_license_back_image = models.ImageField(upload_to='driving_license_back', blank=True, null=True)

    def __str__(self):
        return self.user.username

    @property
    def total_cost(self):
        items = self.order_item.all()
        total_cost = 0
        for item in items:
            total_cost += item.total_cost
        return total_cost

    @property
    def now_pay_cost(self):
        items = self.order_item.all()
        now_pay_cost = 0
        for item in items:
            now_pay_cost += item.now_pay_cost
        return now_pay_cost

    @property
    def later_pay_cost(self):
        items = self.order_item.all()
        later_pay_cost = 0
        for item in items:
            later_pay_cost += item.later_pay_cost
        return later_pay_cost


class ItemOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_item')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    full_pay = models.BooleanField(default=False)
    now_pay_cost = models.FloatField(default=0)
    later_pay_cost = models.FloatField(default=0)
    total_cost = models.FloatField(default=0)
    extra_services = models.ManyToManyField(Extras, blank=True)
    pickup_location = models.TextField(null=True, blank=True)
    pickup_date = models.CharField(max_length=200, null=True, blank=True)
    pickup_time = models.CharField(max_length=200, null=True, blank=True)
    return_location = models.TextField(null=True, blank=True)
    return_date = models.CharField(max_length=200, null=True, blank=True)
    return_time = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Ordered Cars'


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['email','sex', 'f_name', 'l_name', 'phone', 'city',
                  'date_of_birth', 'passport_front_image', 'passport_back_image', 'driving_license_front_image',
                  'driving_license_back_image']
