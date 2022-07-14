from ast import Or
from genericpath import exists
from django.shortcuts import render
from numpy import c_
from .models import Product, ProductVersion, Cart, CartItem, Order, ShopCart, ShopCartForm, WishList ,WishListItem
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


def addtocart(request):
    
    product_version_id = request.POST.get('product_version_id')    #product version id'ni url'den goturdu
    quantity = int(request.POST.get('quantity'))                    # product version quantity'ni inputdan goturdu
    product_version = ProductVersion.objects.get(id = product_version_id)     #hemin id-de olan product versionu tapir  
    user = request.user                                                     #userin kim oldugunu goturdu
    cart = Cart.objects.get_or_create(owner = user)                         #cart yaratdi
    cart_items = CartItem.objects.filter( cart_id_id = cart[0].id)          # cart itemleri goturdu 

    if cart_items:
        item_list = []
        for i in cart_items:
            item_list.append(i.product_version_id.id)

        if product_version.id in item_list:
            c_i = CartItem.objects.filter(cart_id_id = cart[0].id,product_version_id = product_version).first()
            c_i.quantity += quantity
            c_i.save()
        else:
            item = CartItem.objects.get_or_create(cart_id_id = cart[0].id,product_version_id = product_version, quantity = quantity )

    else:
        item = CartItem.objects.get_or_create(cart_id_id = cart[0].id,product_version_id = product_version, quantity = quantity)

    return redirect(product_version.get_absolute_url(), kwargs={'pk': id})

    
def delete_from_cart(request):
    if request.POST:
        item_id = request.POST.get('item-id')
        CartItem.objects.filter(id = item_id).delete()
    return redirect(reverse_lazy('cart'))


   



def wishlist(request):
    if request.user.is_authenticated:
        user = request.user
        wishlist, created = WishList.objects.get_or_create(user_id = user)
        wishlist_items = wishlist.wishlist_items.all()
        
    context = {
        "items" : wishlist_items ,
        'wishlist' : wishlist,     
    }
    return render(request, 'wishlist.html', context)



def add_to_wishlist(request):
    product_version_id = request.POST.get('product_version_id')
    product_version = ProductVersion.objects.get(id = product_version_id)
    user = request.user
    
    wishlist = WishList.objects.get_or_create(user_id = user)
    wishlist_items = WishListItem.objects.filter(wishlist_id_id = wishlist[0].id)

    if wishlist_items:
        item_list = []
        for i in wishlist_items:
            item_list.append(i.product_version_id.id)

        if product_version.id in item_list:
            w_i = WishListItem.objects.filter(wishlist_id_id = wishlist[0].id,product_version_id = product_version).first()
            w_i.delete()
            
        else:
            item = WishListItem.objects.get_or_create(wishlist_id_id = wishlist[0].id,product_version_id = product_version )

    else:
        item = WishListItem.objects.get_or_create(wishlist_id_id = wishlist[0].id,product_version_id = product_version)

    return redirect(product_version.get_absolute_url(), kwargs={'pk': id})



def delete_from_wishlist(request):
    if request.POST:
        item_id = request.POST.get('item-id')
        WishListItem.objects.filter(id = item_id).delete()
        
    return redirect(reverse_lazy('wishlist'))





