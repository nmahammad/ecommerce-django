from django.db import models
import django 
# Create your models here.
from core.models import AbstractModel 
from user.models import Basket


class BillingDetail(AbstractModel):
    user_name = models.CharField( 'name' ,max_length=50)
    first_name = models.CharField( 'name' ,max_length=50)
    last_name = models.CharField('surname' , max_length=50)
    email = models.EmailField('e-mail',max_length=30)
    phone_number = models.BigIntegerField('mobile number')

    country_choices = (
        ('1' , 'India'),
        ('2' , 'South Africa'),
        ('3' , 'United States'),
        ('4' , 'Australia')

    )

    country = models.TextField('Country' , choices=country_choices )
    city_town = models.CharField('City/Town' , max_length=50 , help_text="City/Town"  )
    address = models.CharField('Address' , max_length=150 , help_text="Street Address")
    state = models.CharField('State/Country' , max_length=50)
    postal_code = models.CharField('Postal Code' , max_length=30)


    def __str__(self):  
        return self.first_name + ' ' + self.last_name + ' ' + self.country
        
    
class Order(AbstractModel):
    basket_id = models.ForeignKey(Basket, on_delete = models.CASCADE)
    total_payment = models.FloatField('total payment for order', max_length = 50)
