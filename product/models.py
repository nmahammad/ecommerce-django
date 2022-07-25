
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
from django.utils.safestring import mark_safe


# Create your models here.
class Tag(models.Model):
    title = models.CharField(max_length=100, db_index=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.title


class Vendor(AbstractModel):
    title = models.CharField(max_length=50)
    description = models.TextField()
    vendor_image = models.ImageField(upload_to='media/vendors/')

    def __str__(self):
        return self.title


class Discount(models.Model):
    title = models.CharField(max_length=50)
    percentage = models.IntegerField()

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

    image = models.ImageField(blank=True, upload_to='images/')
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):                           
        full_path = [self.title]                 
        k = self.parent_id
        while k is not None:
            full_path.append(k.title)
            k = k.parent_id
        return ' / '.join(full_path[::-1])


class Color(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10, blank=True,null=True)

    def __str__(self):
        return self.name

    def color_tag(self):
        if self.code is not None:
            return mark_safe('<p style="background-color:{}">Color </p>'.format(self.code))
        else:
            return ""


class Size(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10, blank=True,null=True)
    def __str__(self):
        return self.name


class Product(AbstractModel):

    VARIANTS = (
        ('None', 'None'),
        ('Size', 'Size'),
        ('Color', 'Color'),
        ('Size-Color', 'Size-Color'),

    )

    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True ,null=True)
    title = models.CharField(max_length=500, null=True)
    description = models.TextField(null=True)
    featured = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)
    variant=models.CharField(max_length=10,choices=VARIANTS, default='None')
    slug = models.SlugField(null=False, unique=True)

    @property
    def distinct_versions(self):
        distinct_versions = ProductVersion.objects.filter(product_id=self.id).distinct('color')
        return distinct_versions

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
    def is_featured(self):
        return self.featured

    @property
    def main_version(self):
        result = None
        product_versions = self.product_set.all()
        for pv in product_versions:
            if pv.image_set.all():
                result = pv
                break
        return result

    @property
    def biggest_off(self):
        product_versions = self.product_set.order_by('discount_id__percentage')
        return product_versions.first()
    
    def get_absolute_url(self):
        return reverse_lazy('product_detail', kwargs={
            'pk': self.id
        })

    def __str__(self):
        if self.brand_id :
            return self.brand_id.title + ' ' + str(self.category_id.parent_id) + ' ' + self.category_id.title + ' ' + self.vendor_id.title + ' ' + 'id:' + str(self.id)
        else :
             return str(self.category_id.parent_id) + ' ' + self.category_id.title + ' ' + self.vendor_id.title + ' ' + 'id:' + str(self.id)


class ProductVersion(AbstractModel):
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_set')

    discount_id = models.ForeignKey(
        Discount, on_delete=models.CASCADE, related_name='discount_set' , blank=True, null=True)
    title = models.CharField(max_length=50)
    price = models.IntegerField('Price')
    stock = models.BooleanField('Stock')
    color = models.ForeignKey(Color, on_delete=models.CASCADE,blank=True,null=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE,blank=True,null=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.title + ' ' + str(self.price) + ' ' + str(self.id)

    def main_image(self):
        return self.image_set.order_by("-is_main").first()

    def get_images(self):
        return self.image_set.all()

    def get_absolute_url(self):
        product_pk = self.id 
        return reverse_lazy('product_detail', kwargs={
            'pk': product_pk
        })

    @property
    def related_pic(self):

        other_versions = ProductVersion.objects.filter( product_id = self.product_id )

        related_versions = []
        for pv in other_versions:
            if pv.color.id == self.color.id:
                related_versions.append(pv)  
        
        for rv in related_versions:
            if rv.get_images:
                img = rv.get_images
                return img


class ProductImage(AbstractModel):
    product_version_id = models.ForeignKey(
        ProductVersion, related_name='image_set', on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='media/product_images/', null=True, blank=True)
    is_main = models.BooleanField('main pic', default=False)
    image_title = models.CharField('Image title', max_length=100, null=True)
    image_color = models.ForeignKey(Color, related_name='image_color', on_delete=models.CASCADE)


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



