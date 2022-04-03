from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
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
    flat = models.CharField('Flat' , max_length=50)
