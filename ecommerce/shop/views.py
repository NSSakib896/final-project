from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# path('product/', views.product, name='productpage'),
#     path('cart/', views.cart, name='cartpage'),
#     path('checkout/', views.checkout, name='checkoutpage'),

# Create your views here.

def homepage(request):
    template = loader.get_template('shop/homepage.html')
    return HttpResponse(template.render())


def product(request):
    template = loader.get_template('shop/product.html')
    return HttpResponse(template.render())

def cart(request):
    template = loader.get_template('shop/cart.html')
    return HttpResponse(template.render())

def checkout(request):
    template = loader.get_template('shop/checkout.html')
    return HttpResponse(template.render())