from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
import requests
from django_jalali.db import models as jmodels
from django.core.exceptions import ValidationError
from django import forms


# Create your models here.

class Category(models.Model):
    sub_category = models.ManyToManyField('self', null=True, blank=True, related_name='sub')
    sub_cat = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(allow_unicode=True, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='category', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:category', args=[self.slug, self.id])


class Features(models.Model):
    name = models.CharField(max_length=100)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(allow_unicode=True, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Extras(models.Model):
    name = models.CharField(max_length=100)
    cost = models.PositiveIntegerField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    category = models.ManyToManyField(Category, blank=True, related_name='category')
    categories = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    features = models.ManyToManyField(Features, null=True, blank=True, related_name='features')
    extras = models.ManyToManyField(Extras, null=True, blank=True, related_name='Extras')
    name = models.CharField(max_length=100)
    super_CDW = models.PositiveIntegerField(blank=True, null=True)
    doors = models.PositiveIntegerField()
    seater = models.PositiveIntegerField()
    mileage_limit = models.PositiveIntegerField(blank=True, null=True)
    engine_petrol = models.BooleanField(default=True)
    automatic_transmission = models.BooleanField(default=True)
    available = models.BooleanField(default=True)
    unit_price = models.PositiveIntegerField()
    # currencies = CurrencyField(unit_price, amount_fields=["unit_price"], null=True, blank=True)
    discount = models.PositiveIntegerField(blank=True, null=True)
    total_price = models.PositiveIntegerField()
    information = models.TextField(blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    tags = TaggableManager(blank=True)
    image = models.ImageField(upload_to='car')
    image_2 = models.ImageField(upload_to='car-detail', blank=True)
    like = models.ManyToManyField(User, blank=True, related_name='car_like')
    total_like = models.PositiveIntegerField(default=0)
    dislike = models.ManyToManyField(User, blank=True, related_name='car_dislike')
    total_dislike = models.PositiveIntegerField(default=0)
    brand = models.ForeignKey('brand', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    def total_like(self):
        return self.like.count()

    def total_dislike(self):
        return self.dislike.count()

    @property
    def total_price(self):
        if not self.discount:
            return self.unit_price
        elif self.discount:
            total = (self.discount * self.unit_price) / 100
            return int(self.unit_price - total)
        return self.total_price


class Times(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    session_key = models.CharField(null=True, blank=True, max_length=300)
    pickup_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    pickup_time = models.TimeField(null=True, blank=True)
    return_time = models.TimeField(null=True, blank=True)
    duration = models.DurationField(blank=True, null=True, default=1)
    total_cost = models.IntegerField(default=0, null=True, blank=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=True)

    @property
    def duration(self):
        MONTHS = {
            1:31,
            2:28,
            3:31,
            4:30,
            5:31,
            6:30,
            7:31,
            8:31,
            9:30,
            10:31,
            11:30,
            12:31
        }
        if self.pickup_date.year == self.return_date.year:
            if self.return_time.minute == self.pickup_time.minute and self.return_time.hour == self.pickup_time.hour or\
                    self.return_time < self.pickup_time:
                if self.pickup_date.month == self.return_date.month:
                    return int(self.return_date.day) - int(self.pickup_date.day)
                else:
                    result = MONTHS[self.pickup_date.month] - self.pickup_date.day + self.return_date.day
                    return int(result)
            elif self.return_time > self.pickup_time:
                if self.pickup_date.month == self.return_date.month:
                    return int(self.return_date.day) - int(self.pickup_date.day) + 1
                else:
                    result = MONTHS[self.pickup_date.month] - self.pickup_date.day + self.return_date.day + 1
                    return int(result)
        elif self.pickup_date.year < self.return_date.year:
            if self.return_time.minute == self.pickup_time.minute and self.return_time.hour == self.pickup_time.hour or\
                    self.return_time < self.pickup_time:
                result = MONTHS[self.pickup_date.month] - self.pickup_date.day
                for k, v in MONTHS.items():
                    if k > self.pickup_date.month:
                        result += v
                for k, v in MONTHS.items():
                    if k < self.pickup_date.month:
                        result += v
                return int(result)
            elif self.return_time > self.pickup_time:
                result = MONTHS[self.pickup_date.month] - self.pickup_date.day
                for k, v in MONTHS.items():
                    if k > self.pickup_date.month:
                        result += v
                for k, v in MONTHS.items():
                    if k < self.return_date.month:
                        result += v
                    elif k == self.return_date.month:
                        result += self.return_date.day
                return int(result + 1)
    @property
    def total_cost(self):
        self.cost = self.duration * self.car.unit_price
        return self.cost


class Images(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Currency(models.Model):
    api_symbol = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200)
    value = models.PositiveIntegerField(null=True, blank=True)
    change = models.IntegerField(null=True, blank=True, max_length=200)
    date = jmodels.jDateTimeField(default=False)
    do_update = models.BooleanField(default=False)
    last_update = jmodels.jDateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.do_update:
            url = CurrencyApi.objects.get(active=True).url
            response = requests.get(url)
            json_response = response.json()
            usd_sell = json_response['usd_sell']
            usd_buy = json_response['usd_buy']
            dirham_dubai = json_response['dirham_dubai']
            euro = json_response['eur']
            usd_sell_obj = Currency.objects.get(api_symbol='usd_sell')
            usd_buy_obj = Currency.objects.get(api_symbol='usd_buy')
            dirham_obj = Currency.objects.get(api_symbol='dirham_dubai')
            euro_obj = Currency.objects.get(api_symbol='eur')
            self.do_update = False
            if self.api_symbol == 'eur':
                usd_sell_obj.value = usd_sell['value']
                usd_sell_obj.change = usd_sell['change']
                usd_sell_obj.date = usd_sell['date']
                usd_sell_obj.save()
                usd_buy_obj.value = usd_buy['value']
                usd_buy_obj.change = usd_buy['change']
                usd_buy_obj.date = usd_buy['date']
                usd_buy_obj.save()
                dirham_obj.value = dirham_dubai['value']
                dirham_obj.change = dirham_dubai['change']
                dirham_obj.date = dirham_dubai['date']
                dirham_obj.save()
                self.value = euro['value']
                self.change = euro['change']
                self.date = euro['date']
            elif self.api_symbol == 'dirham_dubai':
                usd_sell_obj.value = usd_sell['value']
                usd_sell_obj.change = usd_sell['change']
                usd_sell_obj.date = usd_sell['date']
                usd_sell_obj.save()
                usd_buy_obj.value = usd_buy['value']
                usd_buy_obj.change = usd_buy['change']
                usd_buy_obj.date = usd_buy['date']
                usd_buy_obj.save()
                self.value = dirham_dubai['value']
                self.change = dirham_dubai['change']
                self.date = dirham_dubai['date']
                euro_obj.value = euro['value']
                euro_obj.change = euro['change']
                euro_obj.date = euro['date']
                euro_obj.save()
            elif self.api_symbol == 'usd_buy':
                usd_sell_obj.value = usd_sell['value']
                usd_sell_obj.change = usd_sell['change']
                usd_sell_obj.date = usd_sell['date']
                usd_sell_obj.save()
                self.value = usd_buy['value']
                self.change = usd_buy['change']
                self.date = usd_buy['date']
                dirham_obj.value = dirham_dubai['value']
                dirham_obj.change = dirham_dubai['change']
                dirham_obj.date = dirham_dubai['date']
                dirham_obj.save()
                euro_obj.value = euro['value']
                euro_obj.change = euro['change']
                euro_obj.date = euro['date']
                euro_obj.save()
            elif self.api_symbol == 'usd_sell':
                self.value = usd_sell['value']
                self.change = usd_sell['change']
                self.date = usd_sell['date']
                usd_buy_obj.value = usd_buy['value']
                usd_buy_obj.change = usd_buy['change']
                usd_buy_obj.date = usd_buy['date']
                usd_buy_obj.save()
                dirham_obj.value = dirham_dubai['value']
                dirham_obj.change = dirham_dubai['change']
                dirham_obj.date = dirham_dubai['date']
                dirham_obj.save()
                euro_obj.value = euro['value']
                euro_obj.change = euro['change']
                euro_obj.date = euro['date']
                euro_obj.save()

        super(Currency, self).save(*args, **kwargs)


class CurrencyApi(models.Model):
    name = models.CharField(max_length=255)
    url = models.TextField()
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.name


class CryptoCurrencyApiForm(forms.ModelForm):
    class Meta:
        model = CurrencyApi
        fields = '__all__'

    def clean(self):
        cd = super().clean()
        if CurrencyApi.objects.filter(active=True).exclude(id=self.instance.id).exists():
            raise ValidationError('لینک فعال دیگری وجود دارد. لطفا ابتدا آن را غیرفعال یا حذف نمایید!')


class CryptoForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = '__all__'

    def clean(self):
        cd = super().clean()
        update = cd.get('do_update')
        if update:
            if not CurrencyApi.objects.filter(active=True).exists():
                raise ValidationError('لطفا ابتدا یک لینک API در جدول مربوطه ایجاد نمایید')
