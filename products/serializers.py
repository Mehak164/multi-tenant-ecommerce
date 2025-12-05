from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'tenant', 'created_by', 'created_at']
        read_only_fields = ['tenant', 'created_by', 'created_at']
