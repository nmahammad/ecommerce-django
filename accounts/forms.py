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
import imp
from tkinter import Widget
from django import forms
from django.contrib.auth import get_user_model

USER = get_user_model()


class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirm Password'
            }))

    class Meta:
        model = USER
        fields = (
            'first_name',
            'last_name',
            'email',
            'password',
            'confirm_password'
        )

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            })
        }

    def clean(self):
        data = self.cleaned_data
        if data['password'] != data['confirm_password']:
            raise forms.ValidationError("password and confirm password does not match")
        return super().clean()
