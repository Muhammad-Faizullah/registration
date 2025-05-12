from rest_framework import serializers
from content.serializer import VariantSerializer
from drf_writable_nested import WritableNestedModelSerializer
from .models import Order,OrderProduct,Payment
from content.models import Product
from rest_framework.response import Response
from content.models import Variant


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ['id','order','product','size','color','quantity']
        read_only_fields = ['order']

class OrderSerializer(WritableNestedModelSerializer):
    order_product = OrderProductSerializer(many=True)
    class Meta:
        model = Order
        fields = ['user','order_product','country','city','address','phone_number','payment_method','status']
        
            
    def validate(self,attrs):
        request = self.context.get('request')
        attrs['user'] = request.user
        order_product = attrs.get('order_product')
        for data in order_product:
            product = data.get('product')
            size = data.get('size')
            color = data.get('color')
            quantity = data.get('quantity')
            variant = Variant.objects.filter(product=product)
            for i in variant:
                if size == i.size and color == i.color:
                    if i.quantity == 0:
                        raise serializers.ValidationError({"error":"Sold Out"})
                    elif i.quantity < 0:
                        i.quantity = 0
                        i.save()
                    elif i.quantity - quantity < 0:
                        raise serializers.ValidationError({"error":f"We have {i.quantity} {i.color } {product.name} in {i.size} size"})
        return attrs 
        
class OrderListSerializer(serializers.ModelSerializer):
    order_product = OrderProductSerializer(many=True,read_only=True)
    
    class Meta:
        model = Order
        fields = ['user','order_product','country','city','address','phone_number','payment_method','status']
 
class PaymentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Payment
        fields = ['order','amount_paid']
    
    def validate(self, attrs):
        order = attrs.get('order')
        amount = attrs.get('amount_paid')
        if amount is None:
            raise serializers.ValidationError({"error":"You should pay for your order"})
        order.status = "Payed"
        order.save()
        return attrs
            
        