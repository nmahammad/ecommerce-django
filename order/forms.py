from django import forms
from order.models import BillingDetail

class OrderForm(forms.ModelForm):

    class Meta:
        model = BillingDetail
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'country',
            'address',
            'state',
            'postal_code',
            'city_town',

        )
        widgets = {
            'address': forms.TextInput(attrs={
                    
                    'placeholder': 'Street Address'
            }),
            
            'country': forms.Select(attrs={
                
            })
        } 