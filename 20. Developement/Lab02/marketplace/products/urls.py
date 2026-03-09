from django.urls import path
from products.views import list_all, show, delete

urlpatterns = [
    path('', list_all, name = 'products.list_all'),
    path('show/<int:id>', show, name = 'products.show'),
    path('delete/<int:id>', delete, name = 'products.delete')
]
