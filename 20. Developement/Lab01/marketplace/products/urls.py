from django.urls import path
from products.views import index, show

urlpatterns = [
    path('', index, name = 'product.index'),
    path('show/<int:id>', show, name = 'products.show')   
]
