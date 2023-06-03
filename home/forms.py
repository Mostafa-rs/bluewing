from django import forms

from .models import *


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100)


class FindCarForm(forms.ModelForm):
    class Meta:
        model = Times
        fields = ('pickup_date', 'pickup_time', 'return_date', 'return_time')

        widgets = {
            'pickup_date': forms.DateInput(attrs={'type': 'datetime-local'}),
            'return_date': forms.DateInput(attrs={'type': 'datetime-local'}),

        }
