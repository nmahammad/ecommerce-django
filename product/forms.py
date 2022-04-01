from dataclasses import fields
from email import message
from tkinter import Widget
from django import forms
from product.models import Review
from core.validators import validate_gmail_account


class ReviewForm(forms.ModelForm):
    # first_name = forms.CharField(max_lenght=40, widget=forms.TextInput(attrs={
    #  'class': 'form-control',
    #  'placeholder': 'Enter Your name'
    # }))
    body = forms.CharField(
        validators=[validate_gmail_account],
        widget=forms.Textarea(
            attrs={
                "cols": 95,
                "rows": 5,
                # 'class': 'form-control',
                "placeholder": "Write Your Message",
            }
        ),
    )

    class Meta:
        model = Review
        fields = (
            "name",
            "email",
            "title",
            "body",
        )
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Your name"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Email"}
            ),
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your number"}
            ),
        }


class SearchForm(forms.Form):
    search = forms.CharField(label='Your name', max_length=100)

