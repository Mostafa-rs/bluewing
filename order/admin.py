from django.contrib import admin

from .models import *


# Register your models here.

class ItemInlines(admin.StackedInline):
    model = ItemOrder
    fields = ['car', 'full_pay', 'now_pay_cost', 'later_pay_cost', 'total_cost', 'extra_services',
              'pickup_location', 'pickup_date', 'pickup_time', 'return_location', 'return_date', 'return_time']
    readonly_fields = ['car', 'full_pay', 'now_pay_cost', 'later_pay_cost', 'total_cost', 'extra_services',
                       'pickup_location', 'pickup_date', 'pickup_time', 'return_location', 'return_date', 'return_time']
    can_delete = False
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'paid', 'f_name', 'l_name', 'now_pay_cost', 'later_pay_cost', 'total_cost'
                    , 'create', 'sex', 'phone', 'nationality', 'city', 'date_of_birth',]
    inlines = [ItemInlines]
    list_editable = ('paid',)
    readonly_fields = ('later_pay_cost', 'later_pay_cost', 'total_cost')




admin.site.register(Order, OrderAdmin)
admin.site.register(ItemOrder)
