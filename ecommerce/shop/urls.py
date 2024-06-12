from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='shophome'),
    path('product/', views.product, name='productpage'),
    path('cart/', views.cart, name='cartpage'),
    path('checkout/', views.checkout, name='checkoutpage'),
]