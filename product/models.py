from pydoc import describe
import re
from django.db import models
from core.models import AbstractModel

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Vendor(AbstractModel):
    title = models.CharField(max_length = 50)        
    description = models.TextField(null=True)
    vendor_image = models.ImageField(upload_to = 'media/vendors/' , blank = True ,  null = True)

    def __str__(self):
        return self.title


class Discount(models.Model):
    title = models.CharField(max_length=50)
    percentage = models.IntegerField()
    value = models.IntegerField( null = True )
  
    def __str__(self):
        return self.title + ' ' + str(self.percentage) + '%'



class Brand(AbstractModel):
    title = models.CharField(max_length=30)  
        
    def __str__(self):
        return self.title


class Category(AbstractModel):
    subcategory=models.ForeignKey('self',related_name='categories', default='', on_delete=models.CASCADE, null=True, blank=True)
    title=models.CharField('title',max_length=70)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class PropertyName(AbstractModel):
    category_id = models.ForeignKey(Category, on_delete = models.CASCADE )
    name = models.CharField(max_length=30)

    
    def __str__(self):
        return self.name
   

class PropertyValue(AbstractModel):
    name = models.CharField(max_length = 50)
    property_name_id = models.ForeignKey(PropertyName, on_delete = models.CASCADE )

    
    def __str__(self):
        return self.name + ' '


class Product(AbstractModel):
    category_id = models.ForeignKey(Category, on_delete = models.CASCADE )   
    vendor_id = models.ForeignKey(Vendor, on_delete = models.CASCADE)
    brand_id = models.ForeignKey(Brand, on_delete = models.CASCADE)    
    

class ProductVersion(AbstractModel):
    product_id = models.ForeignKey(Product, on_delete = models.CASCADE )
    property_value = models.ManyToManyField(PropertyValue)    
    discount_id = models.ForeignKey(Discount, on_delete = models.CASCADE , blank=True ,null=True)
    title = models.CharField(max_length = 50)
    price = models.CharField('Price' , max_length=50)
    stock = models.BooleanField('Stock')

    def __str__(self):
        return self.title + ' ' + str(self.price) 

    def main_image(self):
        return self.productimage.all().order_by('is_main').first()    



class Review(AbstractModel):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE )
    product_id = models.ForeignKey(Product, on_delete = models.CASCADE )
    name = models.CharField( 'First Name' ,max_length=50)
    email = models.EmailField('Email',max_length=30)
    title = models.CharField('Last Name' , max_length=100)
    body = models.TextField()


class ProductImage(AbstractModel):
    product_version_id = models.ForeignKey(ProductVersion, related_name='image_set' , on_delete = models.CASCADE )
    image = models.ImageField(upload_to='media/product_images/', null = True , blank = True)
    is_main = models.BooleanField('main pic', default=False)

    def __str__(self):
        return self.product_version_id.title + ' ' + self.product_version_id.price






