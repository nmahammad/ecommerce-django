from dataclasses import fields
from email import message
from pyexpat import model
from tkinter import Widget
from django import forms
from product.models import Review
from core.validators import validate_gmail_account


class ReviewForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={
        'cols': 167,
        'rows': 5, 
        'placeholder': 'Write Your comment' }))

    class Meta:
        model = Review
        fields = ['email','name','subject', 'rating', 'body']



class SearchForm(forms.Form):
    search = forms.CharField(label='Your name', max_length=100)

