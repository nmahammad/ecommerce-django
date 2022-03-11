from pydoc import describe
from django.db import models

# Create your models here.
class Data(models.Model):
 created_at = models.DateTimeField(auto_now_add=True)
 updated_at = models.DateTimeField(auto_now=True)
  
 class Meta:
  abstract = True


class Product (Data):
 description = models.CharField('Description', max_length=250)
 details = models.CharField('Details', max_length=250)
 
 class Meta:
  verbose_name = 'Product'
  verbose_name_plural = 'Product'

 def __str__(self):
  return self.description


class Category(Data):
 title = models.CharField(max_length=30)

 class Meta:
  verbose_name = 'Category'
  verbose_name_plural = 'Categories'

 def __str__(self):
  return self.title


class Brands(Data):
 title = models.CharField(max_length=30)

 class Meta:
  verbose_name = 'Brands'
  verbose_name_plural = 'Brands'

 def __str__(self):
  return self.title


class Images(Data): 
 title = models.CharField(max_length=30)
 image = models.ImageField(upload_to='media/categories/')
 is_main = models.BooleanField('verified', default=False)

 class Meta:
  verbose_name = 'Images'
  verbose_name_plural = 'Images'

 def __str__(self): 
  return self.title


class ProductVersion(Data): 
 title = models.CharField(max_length=30)
 price = models.IntegerField('Price')
 stock = models.IntegerField('Stock')

 class Meta:
  verbose_name = 'ProductVersion'
  verbose_name_plural = 'ProductVersion'

 def __str__(self): 
  return self.title