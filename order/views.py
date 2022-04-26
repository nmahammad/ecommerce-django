from django.shortcuts import render, HttpResponse, redirect
from order.forms import OrderForm 
from django.urls import reverse_lazy

# Create your views here.
def cart_products(request):
    return render(request, 'cart.html' )

def order_success(request):
    return render(request, 'order-success.html')

def wish_list(request):
    return render(request, 'wishlist.html')



def checkout(request):
    order_form = OrderForm()
    if request.method == 'POST':
        order_form = OrderForm(data=request.POST)
        if order_form.is_valid():
            order_form.save()
            return redirect(reverse_lazy('order-success'))
    context = {
        'order_form': order_form
    }
    return render(request, 'checkout.html', context)
