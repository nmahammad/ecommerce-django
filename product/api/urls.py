from django.urls import path
from product.api.views import CategoryAPI, CategoryDetailAPI, ProductDetail, ProductList


urlpatterns = [

    path("categories", CategoryAPI.as_view(),),
    path("categories/<int:pk>", CategoryDetailAPI.as_view(),),

    path('products/',ProductList.as_view(),name='product-list'),
    path('products/<int:pk>/',ProductDetail.as_view(),name='product-detail '),
    path("categories", CategoryAPI.as_view(),),
    path("categories/<int:pk>", CategoryDetailAPI.as_view(),),

]
