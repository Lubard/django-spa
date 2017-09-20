from rest_framework import serializers
from .models import *


class ItemSerializer(serializers.ModelSerializer):
    spaces = serializers.StringRelatedField(many=True, read_only=True)
    products = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Item
        fields = ('id', 'name', 'venue', 'spaces', 'products')
        depth = 1


class SpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Space
        fields = ('item', 'hour_price')
        depth = 1


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('item', 'price')
        depth = 1


class BookerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booker
        fields = ('user', 'created')
        depth = 1


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('id','created', 'booker')
        depth = 2


class BookingItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = BookingItem
        fields=('id','booking', 'item', 'quantity')
        lookup_field = 'id'


class BookingItemDetailSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    booking = BookingSerializer()

    class Meta:
        model = BookingItem
        fields = ('id', 'booking', 'item', 'quantity', 'locked_piece_price', 'locked_total_price', 'start_timestamp',
                  'end_timestamp')

        depth = 1
        lookup_field = 'id'
