from django.contrib import admin

# # Register your models here.

from user.models import  WishList, BasketItem, Basket

admin.site.register([WishList, BasketItem, Basket])

