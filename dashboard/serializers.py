# dashboard/serializers.py
from rest_framework import serializers
from .models import ProductSales

class ProductSalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSales
        fields = '__all__'
