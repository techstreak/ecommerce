# store/serializers.py

from rest_framework import serializers
from .models import Product, Order
from rest_framework import serializers
from .models import Client, Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["name",  "password", ]


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ["token", "created_at", "expires_at", "user_id", "is_used"]



class ProductSerializer(serializers.ModelSerializer):
    image_source = serializers.ReadOnlyField()
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
