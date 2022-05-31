from django.contrib import admin
from modeltranslation.admin import TranslationAdmin


from django_reverse_admin import ReverseModelAdmin
from product.models import Product, Category, Brand, ProductImage, ProductVersion, PropertyName, Discount ,Vendor, PropertyValue, Review

# # Register your models here.

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 5

class ProductVersionAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

admin.site.register(ProductVersion, ProductVersionAdmin)


class ProductVersionAdmin(TranslationAdmin):
    inlines = [ProductImageInline]



class ProductVersionInline(admin.TabularInline):
    model = ProductVersion
    extra = 2

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductVersionInline]

admin.site.register(Product, ProductAdmin)


class ReverseProductVersion(ReverseModelAdmin):
    inline_type = 'tabular'  
    inline_reverse = ['book']  # could do [('book', {'fields': ['title', 'authors'})] if you only wanted to show certain fields in the create admin






admin.site.register([Category,Vendor,Discount,Brand,ProductImage, PropertyValue, PropertyName, Review])


