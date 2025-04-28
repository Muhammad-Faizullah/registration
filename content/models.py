from django.db import models
from account.models import User


class Product(models.Model):
    Product_Condition = [
        ('Brand New','Brand New'),
        ('Used','Used')
    ]
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    brand = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=30)
    price = models.IntegerField()
    quantity = models.IntegerField()
    condition = models.CharField(max_length=10,choices=Product_Condition)
    description = models.CharField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True,related_name='product_image')
    image_file = models.ImageField(upload_to="ProductImage/",null=True,blank=True)