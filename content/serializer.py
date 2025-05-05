from rest_framework import serializers
from account.serializer import UserProfileSerializer
from account.models import User
from .models import Product,ProductImage,Category,Color,Quantity,Size
from drf_writable_nested.serializers import WritableNestedModelSerializer


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id','name','description']


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id','name']

class QuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Quantity
        fields = ['id','total']
        
class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id','size']
        
class ProductImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    image_file = serializers.CharField(max_length=200)
    
    class Meta:
        model = ProductImage
        fields = ['id','product','image_file']      
class ProductSerializer(WritableNestedModelSerializer):
    product_image = ProductImageSerializer(many=True)
    product_color = ColorSerializer()
    product_quantity = QuantitySerializer()
    product_size = SizeSerializer()
    class Meta:
        model = Product
        fields = ['id','user','category','brand','name','product_color','price','','product_quantity','description','product_image','publish']       
    
    
class ProductListSerializer(serializers.ModelSerializer):
    product_image = ProductImageSerializer(many=True,read_only=True)
    # user_email = serializers.CharField(source='user.email', read_only=True))
    user_detail = serializers.SerializerMethodField()
    category_detail = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ['id','brand','name','color','price','quantity','description','product_image','user_detail','category_detail','publish']
        
        
    def get_user_detail(self, obj):
        if obj.user:
            return {
                    "id":obj.user.id,
                    "email":obj.user.email
                }

        else:
            return ''
        
    def get_category_detail(self,obj):
        if obj.category:
            return {
                    "id":obj.category.id,
                    "name":obj.category.name
                }

        else:
            return ''