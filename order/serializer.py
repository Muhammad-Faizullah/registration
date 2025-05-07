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
        fields = ['id','order','product']
        read_only_fields = ['order']

class OrderSerializer(WritableNestedModelSerializer):
    order_product = OrderProductSerializer(many=True)
    class Meta:
        model = Order
        fields = ['user','order_product','size','color','quantity','country','city','address','phone_number','payment_method','status']
        
    def create(self, validated_data):
        pop_data = validated_data.pop('order_product')
        print('pop data',pop_data)
        order = Order.objects.create(**validated_data)
        for data in pop_data:
            print(data)
            product = data.get('product')
            print('product',product)
            for i in product:
                OrderProduct.objects.create(order=order,**i)
                print('created')

        return order
            
    # def validate(self,attrs):
    #     size = attrs.get('size')
    #     color = attrs.get('color')
    #     quantity = attrs.get('quantity')
    #     product = attrs.get('product')
    #     request = self.context.get('request')
    #     user = request.user
    #     user_email = user.email
        
    #     return attrs
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
        fields = ['user','order_product','size','color','quantity','country','city','address','phone_number','payment_method','status']
 
class PaymentSerializer(serializers.ModelSerializer):
    amount_received = serializers.IntegerField()
    
    class Meta:
        model = Order
        fields = ['user','product','amount_received']
    
    def validate(self, attrs):
        user = attrs.get('user')
        product = attrs.get('product')
        amount = attrs.get('amount_received')
        