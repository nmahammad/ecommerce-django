from django.contrib import admin

# # Register your models here.
from order.models import  Order , BillingDetail, Cart, CartItem, ShopCart, WishList, WishListItem

admin.site.register([Order, BillingDetail, CartItem, Cart, WishListItem, WishList ])


class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['product','user','quantity','price','amount' ]
    list_filter = ['user']


admin.site.register(ShopCart,ShopCartAdmin)