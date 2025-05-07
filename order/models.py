from django.db import models
from account.models import User
from content.models import Product

class Order(models.Model):
    payment_method = [
        ("Credit Card","Credit Card"),
        ("Debit Card","Debit Card"),
        ("Cash","Cash")
    ]
    Choices = [
        ('S','Small'),
        ('M','Medium'),
        ('L','Large'),
        ('XL','Extra Large')
    ]

    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    size = models.CharField(max_length=100,choices=Choices,null=True,blank=True)
    color = models.CharField(max_length=100,null=True,blank=True)
    quantity = models.IntegerField(null=True,blank=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=11)
    payment = models.CharField(max_length=100,choices=payment_method)

    