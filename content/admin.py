from django.contrib import admin
from .models import Product,ProductImage,Category


@admin.register(ProductImage)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','image_file','product']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','user','category','brand','name','color','price','quantity','description','created_at','updated_at']

@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['id','name','description']