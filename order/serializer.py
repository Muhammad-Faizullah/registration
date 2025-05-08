from rest_framework import serializers
from content.serializer import VariantSerializer
from drf_writable_nested import WritableNestedModelSerializer
from .models import Order,OrderProduct
from content.models import Product
from rest_framework.response import Response
from content.models import Variant

class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ['id','order','product','size','color','quantity']
        read_only_fields = ['order']
        
    # def validate(self, attrs):
    #     print('attrs',attrs)
        
    #     order_product = attrs.get('product')
    #     print(order_product)
        

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
                        print(i.quantity)
                        i.quantity = 0
                        print(i.quantity)
                        i.save()
                    elif i.quantity - quantity < 0:
                        raise serializers.ValidationError({"error":f"We have {i.quantity} {i.color } {product.name} in {i.size} size"})
        return attrs 
            
            
        # return attrs
        # try:
        #     variant_qs = Variant.objects.filter(product=product.id)
        # except Variant.DoesNotExist:
        #     raise serializers.ValidationError({"error":"the variant you want does not exist"})
        
        # for data in variant_qs:
        #     if data.size == size and data.color == color:
        #         if data.quantity > 0:
        #             quantity_left = data.quantity - quantity
        #             if quantity_left < 0:
        #                 raise serializers.ValidationError({"error":f"We only have {data.quantity} product available"})
        #             data.quantity = quantity_left
        #             data.save()
        #             attrs["user"] = user
        #             return attrs
        #         else:
        #             raise serializers.ValidationError({"error":"Sold Out"})
        # else:
        #     raise serializers.ValidationError({"error":"this combination is not available"})
        
class OrderListSerializer(serializers.ModelSerializer):
    order_product = OrderProductSerializer(many=True,read_only=True)
    
    class Meta:
        model = Order
        fields = ['user','order_product','country','city','address','phone_number','payment_method','status']
 
class PaymentSerializer(serializers.ModelSerializer):
    amount_received = serializers.IntegerField()
    
    class Meta:
        model = Order
        fields = ['amount_received']
    
    def validate(self, attrs):
        amount = attrs.get('amount_received')
        