# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
from .models import *
from rest_framework import status, generics
from serializer import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import BookingSearchForm
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

def index(request):
    # search_query = request.GET.get('search_text')
    # booking_items = BookingItem.objects.search_for(search_query).order_by('-quantity')
    #
    # paginator = Paginator(booking_items, 10)
    # page = request.GET.get('page')
    # try:
    #     booking_items = paginator.page(page)
    # except PageNotAnInteger:
    #     booking_items = paginator.page(1)
    # except EmptyPage:
    #     booking_items = paginator.page(paginator.num_pages)

    template = loader.get_template('booker/index.html')
    context = {
        # 'booking_items': booking_items,
        'form': BookingSearchForm
        # 'search_query': search_query
    }
    return HttpResponse(template.render(context, request))


class BookingItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookingItem.objects.all()
    serializer_class = BookingItemDetailSerializer
    lookup_field = 'id'


def booking_item_list(request):

    search_query = request.GET.get('search_text')
    booking_items = BookingItem.objects.search_for(search_query).order_by('-quantity')

    paginator = Paginator(booking_items, 20)
    page = request.GET.get('page')
    try:
        booking_items = paginator.page(page)
    except PageNotAnInteger:
        booking_items = paginator.page(1)
    except EmptyPage:
        booking_items = paginator.page(paginator.num_pages)

    serializer = BookingItemSerializer(booking_items, many=True)
    return JsonResponse(serializer.data, safe=False)