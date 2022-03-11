from django.contrib import admin

# Register your models here.

from user.models import  WishList, BasketItems, Basket

admin.site.register([WishList, BasketItems, Basket])

