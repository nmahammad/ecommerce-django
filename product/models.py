
from ast import Break
import email
# from asyncio.windows_events import NULL
from pydoc import describe
from turtle import title
from django.db.models import Avg, Count
from django.db import models
from django.forms import ModelForm
from core.models import AbstractModel
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Vendor(AbstractModel):
    title = models.CharField(max_length = 50)        
    description = models.TextField()
    vendor_image = models.ImageField(upload_to = 'media/vendors/')

    def __str__(self):
        return self.title


class Discount(models.Model):
    title = models.CharField(max_length=50)
    percentage = models.IntegerField()
    value = models.IntegerField(null=True)

    def __str__(self):
        return self.title + ' ' + str(self.percentage) + '%'


class Brand(AbstractModel):
    title = models.CharField(max_length=30)

    class Meta:
            verbose_name = _('Brand')
            verbose_name_plural = _('Brands')

    def __str__(self):
        return self.title


class Category(AbstractModel):
    parent_id = models.ForeignKey(
        'self', related_name='categories', default='', on_delete=models.CASCADE, null=True, blank=True)  # parent_id
    title = models.CharField('title', max_length=70)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        if self.parent_id is not None:
            return self.title + '('  + str(self.parent_id) + ')'
        else:
            return self.title


class PropertyName(AbstractModel):
    category_id = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='category_property_name', null=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name + ' ' + str(self.category_id)

class PropertyValue(AbstractModel):
    name = models.CharField(max_length=50)
    property_name_id = models.ForeignKey(
        PropertyName, on_delete=models.CASCADE, related_name='property_name_property_value')

    def __str__(self):
        return self.name + ' - ' + self.property_name_id.name + ' ' + '(' + self.property_name_id.category_id.title + ')'

    class Meta:
        verbose_name = 'Property values'
        verbose_name_plural = 'Property values'


class Product(AbstractModel):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, null=True)
    description = models.TextField(null=True)

    @property
    def avaregereview(self):
        reviews = Review.objects.filter(product_id__id=self.id).aggregate(avarage=Avg('rating'))
        avg=0
        if reviews["avarage"] is not None:
            avg=float(reviews["avarage"])
        return avg

    @property
    def review_count(self):
        reviews = Review.objects.filter(product_id__id=self.id).aggregate(count=Count('rating'))
        count=0
        if reviews["count"] is not None:
            count=float(reviews["count"])
        return count


    
    @property
    def main_version(self):
        return self.product_set.first()

    def get_absolute_url(self):
        return reverse_lazy('product_detail', kwargs={
            'pk': self.id
        })

    def __str__(self):
        return self.brand_id.title + ' ' + str(self.category_id.parent_id) + ' ' + self.category_id.title + ' ' + self.vendor_id.title + ' ' + 'id:' + str(self.id)


class ProductVersion(AbstractModel):
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_set')
    property_value = models.ManyToManyField(PropertyValue)
    discount_id = models.ForeignKey(
        Discount, on_delete=models.CASCADE, related_name='discount_set' , blank=True, null=True)
    title = models.CharField(max_length=50)
    price = models.IntegerField('Price')
    stock = models.BooleanField('Stock')

    def __str__(self):
        return self.title + ' ' + str(self.price) + ' ' + str(self.id)
    
    def get_color(self):
        return self.property_value.filter(property_name_id__name='Color')  

    def main_image(self):
        return self.image_set.order_by("-is_main").first()

    def get_images(self):
        return self.image_set.all()

    def get_absolute_url(self):
        product_pk = self.kwargs['pk'] 
        return reverse_lazy('productdetail', kwargs={
            'pk': product_pk
        })


class ProductImage(AbstractModel):
    product_version_id = models.ForeignKey(
        ProductVersion, related_name='image_set', on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='media/product_images/', null=True, blank=True)
    is_main = models.BooleanField('main pic', default=False)
    image_title = models.CharField('Image title', max_length=100, null=True)

    def __str__(self):
        return str(self.image_title) + ' ' + str(self.product_version_id.price)


class Review(AbstractModel):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_review')
    name = models.CharField('First Name', max_length=50)
    email = models.EmailField('Email', max_length=30)
    subject = models.CharField('Subject', max_length=100, null=True)
    body = models.TextField()

    rating = models.IntegerField(default=1)

    def __str__(self):
        return str(self.name) + ' -- ' + str(self.product_id.title)








