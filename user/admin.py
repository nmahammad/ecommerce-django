from django.contrib import admin

# # Register your models here.

from user.models import BasketItem, Basket

admin.site.register([ BasketItem, Basket])

