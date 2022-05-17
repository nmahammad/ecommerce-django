from django.urls import path
from multikart.api.views import ProductAPI

urlpatterns = [
    path('products/', ProductAPI.as_view() ),
] 