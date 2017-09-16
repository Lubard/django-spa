from rest_framework import serializers
from .models import *

class BookingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingItem
        fields='__all__'
        lookup_field = 'id'