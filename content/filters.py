import django_filters as filters
from content.models import Category,Product,Variant


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
    
    def filter_size(self, queryset, name, value, *args, **kwargs):
        variant_ids = Variant.objects.filter(size__iexact=value).exclude(product__isnull=True).values_list("product__id", flat=True)
        return queryset.filter(id__in=variant_ids).distinct()


    def filter_color(self,queryset,name,value,*args,**kwargs):
        variant_ids = Variant.objects.filter(color__iexact=value).exclude(product__isnull=True).values_list("product__id", flat=True)
        return queryset.filter(id__in=variant_ids).distinct()