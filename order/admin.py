from django.contrib import admin
from .models import Order,Payment


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['country','city','address','phone_number','payment_method']
    
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['order','amount_paid']