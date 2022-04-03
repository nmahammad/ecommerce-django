from pydoc import describe
from django.db import models
from core.models import AbstractModel

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Vendor(AbstractModel):
    title = models.CharField(max_length = 50)        
    description = models.CharField(max_length = 50)
    vendor_image = models.ImageField(upload_to = 'media/vendors/')


class Discount(models.Model):
  title = models.CharField(max_length=50)
  percentage = models.IntegerField()
  value = models.IntegerField()

class Brand(AbstractModel):
    title = models.CharField(max_length=30)  
        
    def __str__(self):
        return self.title


class Category(AbstractModel):
    title = models.CharField(max_length=30)
    parent_id = models.ForeignKey('self' , on_delete = models.CASCADE )  
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'  
    
    def __str__(self):
        return self.title


class PropertyName(AbstractModel):
    category_id = models.ForeignKey(Category, on_delete = models.CASCADE )
    name = models.CharField(max_length=30)
   

class PropertyValue(AbstractModel):
    name = models.CharField(max_length = 50)
    property_name_id = models.ForeignKey(PropertyName, on_delete = models.CASCADE )


class Product(AbstractModel):
    category_id = models.ForeignKey(Category, on_delete = models.CASCADE )   
    vendor_id = models.ForeignKey(Vendor, on_delete = models.CASCADE)
    brand_id = models.ForeignKey(Brand, on_delete = models.CASCADE)
    property_value = models.ManyToManyField(PropertyValue)            


class ProductVersion(AbstractModel):
  product_id = models.ForeignKey(Product, on_delete = models.CASCADE )
  discount_id = models.ForeignKey(Discount, on_delete = models.CASCADE )
  title = models.CharField(max_length = 50)
  price = models.IntegerField('Price')
  stock = models.BooleanField('Stock')


class Review(AbstractModel):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE )
    product_id = models.ForeignKey(Product, on_delete = models.CASCADE )
    name = models.CharField( 'First Name' ,max_length=50)
    email = models.EmailField('Email',max_length=30)
    title = models.CharField('Last Name' , max_length=100)
    body = models.TextField()


class ProductImage(AbstractModel):
  product_version_id = models.ForeignKey(ProductVersion, on_delete = models.CASCADE )
  image_url = models.ImageField(upload_to='media/categories/')
  is_main = models.BooleanField('verified', default=False)


