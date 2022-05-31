from asyncore import write
from dataclasses import fields
from click import password_option, style
from rest_framework import serializers

from accounts.models import User


class RegistrationSerializers(serializers.ModelSerializer):
 
 password2 = serializers.CharField(style={'input_type':'password'},write_only = True)

 class Meta:
  model = User
  fields = ['first_name','last_name','email','password','password2' ]
  extra_kwargs =  {
   'password':{'write_only': True}
  }
 
 def save(self):
  user = User(
   first_name = self.validated_data['first_name'],
   last_name = self.validated_data['last_name'],
   email = self.validated_data['email'],
  )
  password = self.validated_data['password']
  password2 = self.validated_data['password2']

  if password != password2:
   raise serializers.ValidationError({'password': 'Paswords must match.'})
  user.set_password(password)
  user.save()
  return user
