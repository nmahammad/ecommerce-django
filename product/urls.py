from django.urls import path
from product.views import search,vendor , ProductDetailView, CategoryListView , export


urlpatterns = [

    path('search/' , search),                       
    path('vendor/' , vendor),  


    path('product/<int:pk>/', ProductDetailView.as_view(), name="product_detail"),

    path('products/' ,CategoryListView.as_view(), name='products'),
    path('export/' ,export,name='export'),


]
