from dataclasses import fields
from email import message
from tkinter import Widget
from django import forms
from core.models import Contact
from core.validators import validate_gmail_account




class ContactForm(forms.ModelForm):
 # first_name = forms.CharField(max_lenght=40, widget=forms.TextInput(attrs={
 #  'class': 'form-control',
 #  'placeholder': 'Enter Your name'
 # }))
 message = forms.CharField(validators=[validate_gmail_account],widget=forms.Textarea(attrs={
  'cols': 167,
  'rows': 5,
  # 'class': 'form-control', 
  'placeholder': 'Write Your Message'
 }))
 class Meta:
  model = Contact
  fields = (
   'first_name',
   'last_name',
   'email',
   'phone_number',
   'message'
  )
  widgets = {
   'first_name': forms.TextInput(attrs={
    'class': 'form-control',
    'placeholder': 'Enter Your name'
   }),

   'last_name': forms.TextInput(attrs={
    'class': 'form-control',
    'placeholder': 'Enter Your Last name'
   }),

   'email': forms.EmailInput(attrs={
    'class': 'form-control',
    'placeholder': 'Email'
   }),


   'phone_number': forms.TextInput(attrs={
    'class': 'form-control',
    'placeholder': 'Enter your number'
   })
  }
from django import forms

from core.models import Subscriber

class SubscriberForm(forms.ModelForm):
     class Meta:
        model = Subscriber
        fields = (
            'email',
        )
        widgets = {
            'email': forms.TextInput(attrs={
                    
                    'placeholder': 'Enter your email'
            }),

        } 
