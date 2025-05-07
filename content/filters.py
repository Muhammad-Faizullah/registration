from django_filters import FilterSet
from content.models import Category,Product,Variant


class CategoryFilter(FilterSet):
    class Meta:
        model = Category
        fields = ['name']

class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = ['name','category','publish']
        
    