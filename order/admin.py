from django.contrib import admin

# # Register your models here.
from order.models import  Order , BillingDetail, Cart, CartItem

admin.site.register([Order, BillingDetail, CartItem, Cart ])
