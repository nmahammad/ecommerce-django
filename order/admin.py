from django.contrib import admin

# # Register your models here.
from order.models import Order , BillingDetail

admin.site.register([Order, BillingDetail])