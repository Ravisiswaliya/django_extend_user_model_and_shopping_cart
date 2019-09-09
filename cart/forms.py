from django import forms
from .models import ProductInfo

class ProductCreate(forms.ModelForm):

    class Meta:
        model = ProductInfo
        fields = ("product_cat", "product_brand", "product_name",
                  "product_image", "product_price", "product_description", )


QUANTITY_CHOICES = [(i, str(i)) for i in range(1,21)]

class CartAddProductsForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICES,coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)