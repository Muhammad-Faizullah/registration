from django.db import models
from account.models import User


class Color(models.Model):
    name = models.CharField(max_length=100)

class Quantity(models.Model):
    total = models.IntegerField()
    
class Size(models.Model):
    Choices = [
        ('S','Small'),
        ('M','Medium'),
        ('L','Large'),
        ('XL','Extra Large')
    ]
    
    size = models.CharField(max_length=100,choices=Choices)

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=10000)
    
    def __str__(self):
        return f'{self.name}'

class Product(models.Model):    
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    brand = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    color = models.ForeignKey(Color,on_delete=models.CASCADE,null=True,blank=True)
    price = models.IntegerField()
    size = models.ForeignKey(Size,on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.ForeignKey(Quantity,on_delete=models.CASCADE,null=True,blank=True)
    description = models.CharField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.name}'
    # @property
    # def user_email(self):
    #     return self.user.email
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True,related_name='product_image')
    image_file = models.ImageField(upload_to="ProductImage/",null=True,blank=True)