from django.contrib import admin

# Register your models here.
from order.models import Orders , BillingDetails

admin.site.register([Orders, BillingDetails])