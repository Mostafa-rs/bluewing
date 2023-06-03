import django_filters
from django import forms

from .models import *


class CarsFilter(django_filters.FilterSet):
    choice_1 = {
        ('گران ترین','گران ترین'),
        ('ارزان ترین','ارزان ترین'),
    }


    price_1 = django_filters.NumberFilter(field_name='unit_price', lookup_expr='gte')
    price_2 = django_filters.NumberFilter(field_name='unit_price', lookup_expr='lte')
    brand = django_filters.ModelMultipleChoiceFilter(queryset=Brand.objects.all(), widget=forms.CheckboxSelectMultiple)
    price = django_filters.ChoiceFilter(choices=choice_1,method='price_filter')


    def price_filter(self,queryset,name,value):
        data = 'unit_price' if value == 'ارزان ترین' else '-unit_price'
        return queryset.order_by(data)
