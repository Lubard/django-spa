# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.apps import apps
from django.contrib import admin
from .models import *

class BookingItemAdmin(admin.ModelAdmin):
    list_display = ('id','booking','item', 'quantity', 'locked_piece_price', 'locked_total_price')
    search_fields = ['booking']


# Register your models here.
app = apps.get_app_config('page')

# for model_name, model in app.models.items():
    # admin.site.register(model)
admin.site.register(BookingItem, BookingItemAdmin)

