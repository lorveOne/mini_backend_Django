from rest_framework import serializers
from .models import Product, Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        filterset_fields = ['name', 'price', 'stock']

    #validar stock 
    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("Stock cannot be negative")
        return value
    #validar precio 
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price cannot be negative")
        return value

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        filterset_fields = ['customer_email', 'status', 'created_at']

    def validate_total_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Total price cannot be negative")
        return value