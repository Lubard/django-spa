# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Venue(models.Model):
    name = models.CharField(max_length=255, null=False)
    class Meta:
        db_table = 'venues'

class Item(models.Model):
    venue = models.ForeignKey(Venue)
    name = models.CharField(max_length=255, null=False)
    class Meta:
        db_table = 'items'

class Space(models.Model):
    item = models.ForeignKey(Item)
    hour_price = models.FloatField(null=False)
    class Meta:
        db_table = 'spaces'

class Product(models.Model):
    item = models.ForeignKey(Item)
    price = models.FloatField(null=False)
    class Meta:
        db_table = 'products'

class User(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    registered = models.IntegerField(null=False, default=0)
    email = models.CharField(max_length=255, null=False)
    class Meta:
        db_table = 'users'

class Booker(models.Model):
    user = models.ForeignKey(User)
    created = models.IntegerField(null=False, default=0)
    class Meta:
        db_table = 'bookers'

class Booking(models.Model):
    booker = models.ForeignKey(Booker)
    created = models.IntegerField(null=False, default=0)
    class Meta:
        db_table = 'bookings'

class BookingItem(models.Model):
    booking = models.ForeignKey(Booking)
    item = models.ForeignKey(Item)
    quantity = models.IntegerField(null=False)
    locked_piece_price = models.FloatField(null=False)
    locked_total_price = models.FloatField(null=False)
    start_timestamp = models.IntegerField(null=False)
    end_timestamp = models.IntegerField(null=False)
    class Meta:
        db_table = 'booking_items'
