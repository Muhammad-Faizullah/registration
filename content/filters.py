import django_filters
from content.models import Category,Product


class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = ['name']

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['name','category']