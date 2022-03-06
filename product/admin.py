from django.contrib import admin

from product.models import Praduct, Category, Brands, Images, ProductVersion

# Register your models here.

admin.site.register([Praduct,Category,Brands,Images,ProductVersion])
