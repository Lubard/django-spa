# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import Q
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from itertools import chain


class Venue(models.Model):
    name = models.CharField(max_length=255, null=False)
    class Meta:
        db_table = 'venues'

class Item(models.Model):
    venue = models.ForeignKey(Venue, related_name='items')
    name = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = 'items'

    def __unicode__(self):
        return '%s' % (self.name)


class Space(models.Model):
    item = models.ForeignKey(Item, related_name='spaces')
    hour_price = models.FloatField(null=False)

    class Meta:
        db_table = 'spaces'

    def __unicode__(self):
        return '%f' % self.hour_price


class Product(models.Model):
    item = models.ForeignKey(Item, related_name='products')
    price = models.FloatField(null=False)

    class Meta:
        db_table = 'products'

    def __unicode__(self):
        return '%f' % self.price


class User(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    registered = models.IntegerField(null=False, default=0)
    email = models.CharField(max_length=255, null=False)
    class Meta:
        db_table = 'users'

class Booker(models.Model):
    user = models.ForeignKey(User, related_name='bookers')
    created = models.IntegerField(null=False, default=0)
    class Meta:
        db_table = 'bookers'

class Booking(models.Model):
    booker = models.ForeignKey(Booker, related_name='bookings')
    created = models.IntegerField(null=False, default=0)
    class Meta:
        db_table = 'bookings'


class BookingItemManager(models.Manager):
    def search_for(self, query):
        if (query is None) or (''==query):
            return self

        user = User.objects.filter(Q(first_name__contains=query)|Q(last_name__contains=query)|Q(email__contains=query))
        return self.filter(Q(item__name__contains=query) |
                           Q(booking__id__contains=query) |
                           Q(item__venue__name__contains=query) |
                           Q(booking__booker__user__id__in=user.values_list('id',flat=True))
                           )


class BookingItem(models.Model):
    booking = models.ForeignKey(Booking, related_name='bookingItems')
    item = models.ForeignKey(Item, related_name='bookingItems')
    quantity = models.IntegerField(null=False)
    locked_piece_price = models.FloatField(null=False)
    locked_total_price = models.FloatField(null=False)
    start_timestamp = models.IntegerField(null=False)
    end_timestamp = models.IntegerField(null=False)

    objects = BookingItemManager()

    # Get names
    def get_venue(self):
        return self.item.venue.name

    def get_item(self):
        return self.item.name

    def get_booker(self):
        return self.booking.booker

    def get_user(self):
        return self.get_booker.user

    class Meta:
        db_table = 'booking_items'
