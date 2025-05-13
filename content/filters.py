import django_filters as filters
from content.models import Category,Product,Variant
from rest_framework.response import Response


class CategoryFilter(filters.FilterSet):
    class Meta:
        model = Category
        fields = ['id','name']

class ProductFilter(filters.FilterSet):
    size = filters.CharFilter(label="size",method="filter_size")
    color = filters.CharFilter(label="color",method="filter_color")
    class Meta:
        model = Product
        fields = ['id','name','category','publish','size','color']
    
    # def filter_size(self, queryset, name, value, *args, **kwargs):
    #     variant_ids = Variant.objects.filter(size__iexact=value).exclude(product__isnull=True).values_list("product__id", flat=True)
    #     return queryset.filter(id__in=variant_ids).distinct()


    def filter_color(self,queryset,name,value,*args,**kwarg):
        product_ids = Variant.objects.filter(color__iexact=value).exclude(product__isnull=True).values_list("product__id", flat=True)
        return queryset.filter(id__in=product_ids).distinct()
    
    def filter_size(self,queryset, name,value,*args,**kwargs):
        # print('SIZE',queryset.filter(product_variant__size__iexact=value).distinct())
        # return queryset.filter(product_variant__size__icontains=value).distinct()
        
        print('qs ---',queryset)
        print("filtered variants ----",Variant.objects.filter(product__in=queryset))
        product_ids = Variant.objects.filter(size=value).exclude(product__isnull=True).values_list("product__id", flat=True)
        print('value',value)
        print('product id ',product_ids)
        print('Size---',queryset.filter(id__in=product_ids).distinct())
        return queryset.filter(id__in=product_ids).distinct()
        # print('SIZE',Product.objects.filter(product_variant__size=value))


    # def filter_color(self,queryset,name,value,*arg,**kwargs):
    #     print('filtered color',queryset.filter(product_variant__color=value))
    #     return queryset.filter(product_variant__color=value)