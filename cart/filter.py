import django_filters
from .models import ProductInfo


class ProductFilter(django_filters.FilterSet):
    
    class Meta:
        model = ProductInfo
        fields = {'product_cat': ['exact'],
                  'product_brand':['exact'],
                  'product_name': ['icontains'],
                  'product_price': ['lt','gt']

        }
