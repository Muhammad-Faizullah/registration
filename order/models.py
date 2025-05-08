from django.db import models
from account.models import User
from content.models import Product,Variant
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.response import Response
from rest_framework.serializers import ValidationError

class Order(models.Model):
    Payment_methods = [
        ("Credit Card","Credit Card"),
        ("Debit Card","Debit Card"),
        ("Cash On Delivery","Cash On Delivery")
    ]

    Status = [
        ('Pending','Pending'),
        ('Payed','Payed')
    ]

    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=11)
    payment_method = models.CharField(max_length=100,choices=Payment_methods,default="Cash On Delivery")
    status = models.CharField(max_length=100,choices=Status,default="Pending",null=True,blank=True)
    
class OrderProduct(models.Model):
    Choices = [
        ('S','Small'),
        ('M','Medium'),
        ('L','Large'),
        ('XL','Extra Large')
    ]
    
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='order_product')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    size = models.CharField(max_length=100,choices=Choices,null=True,blank=True)
    color = models.CharField(max_length=100,null=True,blank=True)
    quantity = models.IntegerField(null=True,blank=True)

@receiver(post_save, sender=OrderProduct)
def post_save_order(sender,instance,created,**kwargs): 
    product = instance.product
    variant_product = Variant.objects.filter(product=product)
    for data in variant_product:      
        if  data.size == instance.size and data.color == instance.color:           
            if data.quantity > instance.quantity:  
                print(instance.product,"-",instance.color,"-",instance.size,"-",instance.quantity)  
                data.quantity = data.quantity - instance.quantity
                data.save()

    
    