from django.urls import path
from .views import ProductList, ProductDetail, create_product

urlpatterns = [
    path('', ProductList.as_view()),
    path('<int:pk>', ProductDetail.as_view()),
    path('create/', create_product, name='product_create'),
]