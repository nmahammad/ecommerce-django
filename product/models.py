from django.db import models

# Create your models here.

class Discounts(models.Model):
    title = models.CharField(max_length=50)
    percentage = models.IntegerField()
    value = models.IntegerField()
    product_id = models.IntegerField('product id')    
    