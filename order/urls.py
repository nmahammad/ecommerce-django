from django import views
from django.urls import path, re_path
from order.views import (
    CreateOrderView, 
    order_success,
    cart,
    addtocart,
    wishlist,
    add_to_wishlist,
    delete_from_wishlist,
    delete_from_cart,
)


urlpatterns = [
    path('checkout/' , CreateOrderView.as_view() , name='checkout'), 

    path('order-success/' , order_success, name='order-success'),
    path('cart/' , cart, name='cart'),
    path('add-to-cart/', addtocart, name='add-to-cart' ),
    path('wishlist/' , wishlist, name='wishlist'),
    path('add-to-wishlist/' , add_to_wishlist, name='add-to-wishlist'),
    path('delete-from-wishlist/' , delete_from_wishlist, name='delete-from-wishlist'),
    path('delete-from-cart/' , delete_from_cart, name='delete-from-cart'),
    
]