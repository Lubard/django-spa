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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

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
    booking = BookingSerializer()
    item = ItemSerializer()
    # space = SpaceSerializer(source='item', many=True)
    # product = ProductSerializer(source='item', many=True)
    class Meta:
        model = BookingItem
        fields=('id','booking', 'item', 'quantity', 'locked_piece_price', 'locked_total_price', 'start_timestamp',
                'end_timestamp')
        lookup_field = 'id'
