from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','brand','name','color','price','quantity','condition','description','created_at','updated_at']
