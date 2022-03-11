from django.contrib import admin

from product.models import Product, Category, Brands, Images, ProductVersion

# Register your models here.

admin.site.register([Product,Category,Brands,Images,ProductVersion])
