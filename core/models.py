# import email
# from operator import mod
# from venv import create
# from django.db import models
# from django.forms import EmailField

# # Create your models here.

# class AbstractModel(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     class Meta:
#         abstract = True


# class Contact(models.Model):
#     first_name = models.CharField( 'name' ,max_length=50)
#     last_name = models.CharField('surname' , max_length=50)
#     email = models.EmailField('e-mail',max_length=30)
#     phone_number = models.IntegerField('mobile number')
#     message = models.TextField('your message' , help_text='Type your message here...')
    
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):  
#         return self.first_name + self.last_name
    


import email
from operator import mod
from pyexpat import model
from venv import create
from django.db import models
from django.forms import EmailField

# Create your models here.

class  AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class Contact(AbstractModel):
    first_name = models.CharField( 'name' ,max_length=50)
    last_name = models.CharField('surname' , max_length=50)
    email = models.EmailField('e-mail',max_length=30 , blank = True)
    phone_number = models.CharField('mobile number', max_length=200)
    message = models.TextField('your message' , help_text='Type your message here...') 
    
    def __str__(self):  
        return self.first_name + " " + self.last_name


class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):  
        return self.question


class TeamMember(AbstractModel):
    first_name = models.CharField( 'name' ,max_length=50, null=False)
    last_name = models.CharField('surname' , max_length=50)
    title = models.CharField('job title' , max_length=50 )
    description = models.TextField('description')
    avatar = models.ImageField()



class NewSubscriber(AbstractModel):
    email = models.EmailField('e-mail', max_length=30 , unique=True ,null= False , blank = True)
    is_active = models.BooleanField('Is Active', default=True)

    def __str__(self):  
        return self.email