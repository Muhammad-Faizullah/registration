from django.contrib import admin
from .models import Product,ProductImage,Category,Variant


# @admin.register(ProductImage)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','image_file','product']
    list_per_page = 15
    
# @admin.register(Variant)
class VariantInline(admin.TabularInline):
    model = Variant
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','category','brand','name','price']
    inlines = [VariantInline]
    list_filter = ['category']
    search_fields = ['name','brand']
    list_per_page = 15

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    search_fields = ['name']
    

admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoriesAdmin)
admin.site.register(ProductImage,ImageAdmin)
admin.site.register(Variant)