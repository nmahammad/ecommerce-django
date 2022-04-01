from django.contrib import admin

from product.models import Product, Category, Brand, ProductImage, ProductVersion, PropertyName, Discount ,Vendor, PropertyValue, Review

# Register your models here.

admin.site.register([Product,Category,Vendor,Discount,Brand,ProductImage,ProductVersion, PropertyValue, PropertyName, Review])
