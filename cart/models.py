from django.db import models
from django.conf import settings


class ProductInfo(models.Model):
    product_cat = models.CharField(max_length=100)
    product_brand = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    product_image = models.ImageField()
    product_price = models.DecimalField(max_digits=8, decimal_places=2)
    product_description = models.TextField()

    def __str__(self):
        return self.product_name






