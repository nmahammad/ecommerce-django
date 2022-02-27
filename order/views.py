from django.shortcuts import render, HttpResponse

# Create your views here.
def cart_products(request):
    return render(request, 'cart.html' )


    #path('checkout/' , checkout ),
    #path('order-success' , order_success),     path('cart/' , cart_products),
    #path('wishlist' , wish_list),

def checkout(request):
    return render(request, 'checkout.html')

def order_success(request):
    return render(request, 'order-success.html')

def wish_list(request):
    return render(request, 'wishlist.html')