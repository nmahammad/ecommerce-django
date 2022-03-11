from itertools import count, product
from django.db import models

# Create your models here.


class WishList(models.Model):
    product_id = models.IntegerField('product id')
    user_id = models.IntegerField("user id")


class Basket(models.Model):
    user_id = models.IntegerField('basket id') 

class BasketItems(models.Model):
    price = models.IntegerField('price')
    product_id = models.IntegerField
    basket_id = models.IntegerField
    count = models.IntegerField("number of items")

