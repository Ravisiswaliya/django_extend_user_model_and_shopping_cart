from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('product_list', views.product_list, name='product_list'),
    path('product_create', views.product_create, name='product_create'),
    path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('', views.cart_detail, name='cart_detail'),
    path('cart_add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove')
]
