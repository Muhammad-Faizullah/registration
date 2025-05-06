from rest_framework import serializers
from content.serializer import VariantSerializer
from drf_writable_nested import WritableNestedModelSerializer
from .models import Order
from rest_framework.response import Response
from content.models import Variant

class OrderSerializer(serializers.ModelSerializer):
    # product_variant = VariantSerializer(many=True)
    class Meta:
        model = Order
        fields = ['product','size','color','quantity','country','city','address','phone_number','payment']
        
    def validate(self,attrs):
        size = attrs.get('size')
        color = attrs.get('color')
        quantity = attrs.get('quantity')
        product = attrs.get('product')
        
        try:
            variant_qs = Variant.objects.filter(product=product.id)
        except Variant.DoesNotExist:
            raise serializers.ValidationError({"error":"the variant you want does not exist"})
        
        for data in variant_qs:
            if data.size == size and data.color == color:
                if data.quantity > 0:
                    data.quantity = data.quantity - quantity
                    data.save()
                    return attrs
                else:
                    raise serializers.ValidationError({"error":"Sold Out"})
        else:
            raise serializers.ValidationError({"error":"this combination is not available"})
        
    def create(self,validated_data):
        print("validated_data",validated_data)
        return Order.objects.create(
            **validated_data
        )
                
                


            