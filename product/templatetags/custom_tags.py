from atexit import register
from django.template import Library
from product.models import Product, ProductVersion, ProductImage

register = Library()

@register.simple_tag
def get_product_versions():
    return ProductVersion.objects.order_by('-created_at')[0:4]

@register.simple_tag
def get_products():
    return Product.objects.all()
    


# @register.simple_tag
# def get_product_version_images():
#     product_versions = ProductVersion.objects.all().image_set.all()
#     product_version_images = product_versions.image_set.all()
#     return product_version_images


# @register.simple_tag
# def get_product_version_images():
#     product_versions = ProductVersion.objects.all()
#     for product_version in product_versions:
#         for product_image in product_version.image_set.all():
#             return product_image






#ItemImage.objects.filter(main=True, item__active=True)


# @register.simple_tag
# def get_product_images():
#     return ProductVersion.image_of_version
#     #return ProductImage.objects.all().order_by('-created_at')[offset:limit]