from django.urls import path, re_path
from order.views import (
    CreateOrderView, 
    cart_products,
    order_success,
    wish_list,   
)


urlpatterns = [
    path('cart/' , cart_products),
    path('checkout/' , CreateOrderView.as_view() ), 
    path('order-success/' , order_success, name='order-success'),
    path('wishlist/' , wish_list),
]