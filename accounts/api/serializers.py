from asyncore import write
from dataclasses import fields
from click import password_option, style
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



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



User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
        )


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs=attrs)
        user_serializer = UserSerializer(self.user)
        data.update(user_serializer.data)
        return data