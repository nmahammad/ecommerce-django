import email
from operator import mod
from venv import create
from django.db import models
from django.forms import EmailField

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField( 'name' ,max_length=50)
    last_name = models.CharField('surname' , max_length=50)
    email = models.EmailField('e-mail',max_length=30)
    phone_number = models.IntegerField('mobile number')
    message = models.TextField('your message' , help_text='Type your message here...')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):  
        return self.first_name + self.last_name
    

