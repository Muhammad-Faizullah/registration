from django.db import models
from account.models import User


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
    color = models.CharField(max_length=30)
    price = models.IntegerField()
    quantity = models.IntegerField()
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
    
    

    