from django import views
from django.urls import path, re_path
from order.views import (
    CreateOrderView, 
    order_success,
    wish_list,   
    cart,
    ajaxcolor
)


urlpatterns = [
    path('checkout/' , CreateOrderView.as_view() ), 
    path('order-success/' , order_success, name='order-success'),
    path('wishlist/' , wish_list),
    path('cart/' , cart, name='cart'),
    path('ajaxcolor/' ,ajaxcolor, name='ajaxcolor'),
    
]