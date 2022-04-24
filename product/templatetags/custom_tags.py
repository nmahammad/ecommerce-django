from atexit import register
from django.template import Library
from product.models import Brand, ProductVersion, PropertyName, PropertyValue


register = Library()


@register.simple_tag
def get_brands():
 return Brand.objects.all()



@register.simple_tag
def get_propertyValueSize():
 return PropertyValue.objects.filter(property_name_id__name='Size')


@register.simple_tag
def get_propertyValueColor():
 return PropertyValue.objects.filter(property_name_id__name='Color')




