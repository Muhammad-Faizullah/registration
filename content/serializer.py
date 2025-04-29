from rest_framework import serializers
from .models import Product,ProductImage
from drf_writable_nested.serializers import WritableNestedModelSerializer


class ProductImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    image_file = serializers.CharField(max_length=200)
    class Meta:
        model = ProductImage
        fields = ['id','product','image_file']
        
        
class ProductSerializer(WritableNestedModelSerializer):
    product_image = ProductImageSerializer(many=True)
    
    class Meta:
        model = Product
        fields = ['id','user','brand','name','color','price','quantity','condition','description','product_image']
        
    # def create(self, validated_data):
    #     print('validated data', validated_data)
    #     pop_data = validated_data.pop('product_image')
    #     product = Product.objects.create(**validated_data)
        
    #     for data in pop_data:
    #         ProductImage.objects.create(
    #             product=product,**data
    #         )
        
    #     return product
    
    # def update(self,instance,validated_data):
    #     product_image_data = validated_data.pop('product_image')
    #     instance.user = validated_data.get('user',instance.user)
    #     instance.brand = validated_data.get('brand',instance.brand)
    #     instance.name = validated_data.get('name',instance.name)
    #     instance.color = validated_data.get('color',instance.color)
    #     instance.price = validated_data.get('price',instance.price)
    #     instance.quantity = validated_data.get('quantity',instance.quantity)
    #     instance.condition = validated_data.get('condition',instance.condition)
    #     instance.description = validated_data.get('description',instance.description)
    #     instance.save()

    #     for data in product_image_data:            
    #         if 'id' in data.keys():
    #             id = data.get('id')
    #             if ProductImage.objects.filter(id=id).exists():
    #                 obj = ProductImage.objects.get(id=id)
    #                 # obj.product = data.get('product',obj.product)
    #                 obj.image_file = data.get('image_file',obj.image_file)
    #                 obj.save()
    #             else:
    #                 continue
    #         else:
    #             obj = ProductImage.objects.create(
    #                 **data,product=instance
    #             )
    #             print('obj',obj)
                
    #     return instance
                     

