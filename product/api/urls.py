from django.urls import path
from product.api.views import ProductAPI
from product.api.views import CategoryAPI, CategoryDetailAPI


urlpatterns = [
    
 path("category", CategoryAPI.as_view(),),
 path('products/', ProductAPI.as_view() ),
 path("category/<int:pk>", CategoryDetailAPI.as_view(),),

]
