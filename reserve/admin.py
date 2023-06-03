from django.contrib import admin

from .models import *


# Register your models here.
class ExtraReserveTabular(admin.TabularInline):
    model = ExtraReserve
    extra = 2


class ReserveAdmin(admin.ModelAdmin):
    list_display = ('user', 'car',)
    inlines = [ExtraReserveTabular]


admin.site.register(Reserve, ReserveAdmin)
