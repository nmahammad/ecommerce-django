from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from django_reverse_admin import ReverseModelAdmin
from product.models import Product, Category, Brand, ProductImage, ProductVersion, PropertyName, Discount ,Vendor, PropertyValue, Review

### ADDING PRODUCT IMAGES FOR VERSIONS
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 5

class ProductVersionAdmin(TranslationAdmin):
    inlines = [ProductImageInline]

admin.site.register(ProductVersion, ProductVersionAdmin)

#### ADDING PRODUCT VERSIONS TO PRODUCTS ###
class ProductVersionInline(admin.TabularInline):
    model = ProductVersion
    extra = 0

class ProductAdmin(TranslationAdmin):
    inlines = [ProductVersionInline]
    list_display = ('title', 'category_id', 'brand_id', 'vendor_id', 'id')
    list_filter = ('category_id__title', 'brand_id__title' , 'vendor_id__title' )
    search_fields = ('title', 'category_id__title' , 'brand_id__title' , 'vendor_id__title')

admin.site.register(Product, ProductAdmin)

class CategoryAdmin(TranslationAdmin):
    model = Category

admin.site.register(Category, CategoryAdmin)


# class ProductVersionAdmin(TranslationAdmin):
#     model = ProductVersion

admin.site.register([Vendor,Discount,Brand,ProductImage, PropertyValue, PropertyName,  Review ])


