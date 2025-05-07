from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['size','color','quantity','country','city','address','phone_number','payment_method']
    