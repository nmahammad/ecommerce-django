from django.db import models

# Create your models here.


class Orders(models.Model):
    basket_id = models.IntegerField('basket id')    
    created_at = models.DateTimeField(auto_now_add=True)

class BillingDetails(models.Model):
    first_name = models.CharField( 'name' ,max_length=50)
    last_name = models.CharField('surname' , max_length=50)
    email = models.EmailField('e-mail',max_length=30)
    phone_number = models.IntegerField('mobile number')

    country_choices = (
        ('1' , 'India'),
        ('2' , 'South Africa'),
        ('3' , 'United States'),
        ('4' , 'Australia')

    )
    country = models.TextField('Country' , choices=country_choices )
    address = models.CharField('Address' , max_length=150 , help_text="Street Address")
    state = models.CharField('State/Country' , max_length=50)
    postal_code = models.IntegerField('Postal Code')


    def __str__(self):  
        return self.first_name + self.last_name