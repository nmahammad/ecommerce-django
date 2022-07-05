from ast import Or
from django.shortcuts import render
from .models import Product, ProductVersion, Cart, CartItem, Order, ShopCart, ShopCartForm
import json
from django.template.loader import render_to_string
from multiprocessing import context
from pyexpat import model
from django.http import HttpResponse, HttpResponseRedirect
import re
from django.utils import timezone
from django.shortcuts import render, redirect
from requests import request
from order.forms import OrderForm 
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required



# Create your views here.
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


def cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart, created = Cart.objects.get_or_create(owner = user,  completed=False)
        cartitems = cart.cart_items.all()
        
    context = {
        "cartitems" : cartitems ,
        'cart' : cart,
       
    }
    return render(request, 'cart.html', context)


def cart_quantity(request):
    if request.user.is_authenticated:
        user = request.user
        cart, created = Cart.objects.get_or_create(owner = user,  completed=False)
        cartitems = cart.cart_items.all()
        
    context = {
        "cartitems" : cartitems ,
        'cart' : cart,
       
    }
    return render(request, 'base.html', context)


def ajaxcolor(request):
    data = {}
    if request.POST.get('action') == 'post':
        size_id = request.POST.get('size')
        productid = request.POST.get('productid')
        colors = ProductVersion.objects.filter(product_id=productid, property_value=size_id)
        context = {
            'size_id': size_id,
            'productid': productid,
            'colors': colors,
        }
        data = {'rendered_table': render_to_string('color_list.html', context=context)}
        return JsonResponse(data)
    return JsonResponse(data)

@login_required(login_url='/login') # Check login
def addtoshopcart(request,id):
    url = request.META.get('HTTP_REFERER')  # get last url
    current_user = request.user  # Access User Session information
    product= Product.objects.get(pk=id)

    if product.variant != 'None':
        variantid = request.POST.get('variantid')  # from variant add to cart
        checkinvariant = ShopCart.objects.filter(variant_id=variantid, user_id=current_user.id)  # Check product in shopcart
        if checkinvariant:
            control = 1 # The product is in the cart
        else:
            control = 0 # The product is not in the cart"""
    else:
        checkinproduct = ShopCart.objects.filter(product_id=id, user_id=current_user.id) # Check product in shopcart
        if checkinproduct:
            control = 1 # The product is in the cart
        else:
            control = 0 # The product is not in the cart"""

    if request.method == 'POST':  # if there is a post
        form = ShopCartForm(request.POST)
        if form.is_valid():
            if control==1: # Update  shopcart
                if product.variant == 'None':
                    data = ShopCart.objects.get(product_id=id, user_id=current_user.id)
                else:
                    data = ShopCart.objects.get(product_id=id, variant_id=variantid, user_id=current_user.id)
                data.quantity += form.cleaned_data['quantity']
                data.save()  # save data
            else : # Inser to Shopcart
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id =id
                data.variant_id = variantid
                data.quantity = form.cleaned_data['quantity']
                data.save()
        messages.success(request, "Product added to Shopcart ")
        return HttpResponseRedirect(url)

    else: # if there is no post
        if control == 1:  # Update  shopcart
            data = ShopCart.objects.get(product_id=id, user_id=current_user.id)
            data.quantity += 1
            data.save()  #
        else:  #  Inser to Shopcart
            data = ShopCart()  # model ile bağlantı kur
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            data.variant_id =None
            data.save()  #
        messages.success(request, "Product added to Shopcart")
        return HttpResponseRedirect(url)