from django.contrib import admin

from product.models import Product, Category, Brand, ProductImage, ProductVersion, PropertyName, Discount ,Vendor, PropertyValue, Review

# # Register your models here.

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 5


admin.site.register([Product,Category,Vendor,Discount,Brand,ProductImage, PropertyValue, PropertyName, Review])


class ProductVersionAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]


admin.site.register(ProductVersion, ProductVersionAdmin)

# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'price')
# admin.site.register(Book, BookAdmin)
