from django import forms
from django.contrib.auth import get_user_model


USER = get_user_model()


class LoginForm(forms.Form):
 username = forms.CharField(widget=forms.TextInput(attrs={
  'class': 'form-control',
  'placeholder': 'Username'
 }))
 password = forms.CharField(widget=forms.PasswordInput(attrs={
  'class': 'form-control',
  'placeholder': 'Password'
 }))