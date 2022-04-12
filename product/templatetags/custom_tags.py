from atexit import register
from django.template import Library
from product.models import Product, ProductVersion, ProductImage

register = Library()

@register.simple_tag
def get_product_versions():
    return ProductVersion.objects.all()
    

# @register.simple_tag
# def get_product_images():
#     return ProductVersion.image_of_version
#     #return ProductImage.objects.all().order_by('-created_at')[offset:limit]