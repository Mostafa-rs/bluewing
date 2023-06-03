import admin_thumbnails
from django.contrib import admin
from django.forms import CheckboxSelectMultiple
import django_jalali.admin as jadmin
from django_jalali.admin.filters import JDateFieldListFilter
from .models import *


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'create', 'update')
    prepopulated_fields = {
        'slug': ('name',)
    }


class ExtrasAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'create', 'update')


class FeaturesAdmin(admin.ModelAdmin):
    list_display = ('name', 'create', 'update')


@admin_thumbnails.thumbnail('image')
class ImageInLines(admin.TabularInline):
    model = Images
    extra = 2


class TimesAdmin(admin.ModelAdmin):
    list_display = ('pickup_date', 'pickup_time', 'return_date', 'return_time', 'duration',)


class CarAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'create', 'update', 'categories', 'doors', 'seater', 'mileage_limit', 'engine_petrol',
        'automatic_transmission',
        'available',
        'unit_price', 'discount', 'total_price')
    inlines = [ImageInLines]
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    list_editable = ('unit_price',)
    search_fields = ('name',)


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'change', 'date', 'do_update', 'last_update')
    list_filter = (
        ('date', JDateFieldListFilter),
    )
    form = CryptoForm


class CurrencyApiAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')
    form = CryptoCurrencyApiForm


admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Features, FeaturesAdmin)
admin.site.register(Extras, ExtrasAdmin)
admin.site.register(Images)
admin.site.register(Times, TimesAdmin)
admin.site.register(Brand)
admin.site.register(CurrencyApi, CurrencyApiAdmin)
