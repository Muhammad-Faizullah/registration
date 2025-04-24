from rest_framework import serializers
from .models import Product,ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductImage
        fields = ['id','product','image']

class ProductSerializer(serializers.ModelSerializer):
    product_image = ProductImageSerializer(many=True)
    
    class Meta:
        model = Product
        fields = ['id','user','brand','name','color','price','quantity','condition','description','product_image']
        
    def create(self, validated_data):
        img = validated_data.pop('product_image')
        print('validated_data',validated_data)
        data = Product.objects.create(**validated_data)
        for i in img:
            ProductImage.objects.create(**i)
        return data
    
    
        

    
    

