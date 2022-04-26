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