from rest_framework import serializers
from catalogue.models import Product

class ProductSerialier(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'