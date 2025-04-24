from django.contrib import admin
from .models import Product,ProductImage


@admin.register(ProductImage)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','image','product']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','user','brand','name','color','price','quantity','condition','description','created_at','updated_at']

