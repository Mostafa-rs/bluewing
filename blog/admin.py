from django.contrib import admin

from .models import *


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'create', 'update', 'status', 'author')


admin.site.register(Post, PostAdmin)
