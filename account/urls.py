from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path("account_register/", views.account_register, name="account_register"),
    path('account_login/', views.account_login, name='account_login'),
    path('account_logout/', views.account_logout, name='account_logout'),
    
]
