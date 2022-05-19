
from django.urls import path
from product.views import category, search, vendor , ProductDetailView

urlpatterns = [

    path('category/' , category , name = 'products_page'),             
    path('search/' , search),                       
    path('vendor/' , vendor),                       
    path('product/<int:pk>/', ProductDetailView.as_view(), name="product_detail"),

]