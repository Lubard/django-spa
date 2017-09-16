# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import *
from rest_framework import generics
from serializer import BookingItemSerializer

# Create your views here.
def index(request):
    booking_items = BookingItem.objects.order_by('-quantity')[:5]
    template = loader.get_template('booker/index.html')
    context = {
        'booking_items': booking_items,
    }
    return HttpResponse(template.render(context, request))

class BookingItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookingItem.objects.all()
    serializer_class = BookingItemSerializer
    lookup_field = 'id'
