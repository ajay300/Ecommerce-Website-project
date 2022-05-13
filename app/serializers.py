from rest_framework import serializers
from .models import Customer , Product


class CustomerSerializer(serializers.Serializer):
    name = serializers.CharField()
    locality = serializers.CharField()
    city = serializers.CharField()
    zipcode = serializers.IntegerField()
    state = serializers.CharField()


class ProductSerializer(serializers.Serializer):
    title = serializers.CharField()
    selling_price = serializers.FloatField()
    discounted_price = serializers.FloatField()
    description = serializers.CharField()
    brand = serializers.CharField()
