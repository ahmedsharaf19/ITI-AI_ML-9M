from django.shortcuts import render

# Create your views here.

# Products Random
products = [
    {
        "id": 1,
        "name": "iPhone 14 Pro",
        "price": 999,
        "description": "Apple smartphone with A16 Bionic chip and advanced camera system",
        "image": "https://images.unsplash.com/photo-1663499482523-1c6e671c5f3a"
    },
    {
        "id": 2,
        "name": "Samsung Galaxy S23",
        "price": 899,
        "description": "Flagship Android phone with Snapdragon processor",
        "image": "https://images.unsplash.com/photo-1678911820864-e1c1f3e0dcb8"
    },
    {
        "id": 3,
        "name": "MacBook Air M2",
        "price": 1199,
        "description": "Lightweight laptop powered by Apple M2 chip",
        "image": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8"
    },
    {
        "id": 4,
        "name": "Apple Watch Series 9",
        "price": 429,
        "description": "Smartwatch with fitness tracking and health monitoring",
        "image": "https://images.unsplash.com/photo-1516574187841-cb9cc2ca948b"
    }
]

from django.http import HttpResponse
from .models import Product
from django.shortcuts import render, redirect

# view to return All Of Products
def list_all(response):
    products = Product.objects.all()
    return render(response, 'products/home.html', {'products': products})

# return specific product 
def show(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'products/show.html', {'product': product})


# delete specific product
def delete(request, id):
    product = Product.objects.get(id=id)
    print(product)
    product.delete()
    return redirect('products.index')