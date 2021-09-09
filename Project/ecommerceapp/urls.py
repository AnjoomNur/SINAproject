from django.urls import path
from .views import Home,product_single

urlpatterns = [
    path('',Home , name='home'),
    path('product/<int:id>/', product_single, name='product_single'),
    
]