from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['id','brand','name','color','price','quantity','condition','description']
        