from ast import Or
from pyexpat import model
from django.shortcuts import render, HttpResponse, redirect
from order.forms import OrderForm 
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.contrib import messages
from order.models import BillingDetail

# Create your views here.
def cart_products(request):
    return render(request, 'cart.html' )

def order_success(request):
    return render(request, 'order-success.html')

def wish_list(request):
    return render(request, 'wishlist.html')

class CreateOrderView(CreateView, LoginRequiredMixin):
    form_class = OrderForm
    template_name = 'checkout.html'
    success_url = reverse_lazy('order-success')
    #context_object_name = 'order_form'  ???? 

    def form_valid(self, form):
        return super().form_valid(form)
    
    def get(self, request, *args, **kwargs):
        context = {'order_form': OrderForm()}
        return render(request, 'checkout.html', context)
