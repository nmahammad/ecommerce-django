from django import forms

from order.models import BillingDetail

class OrderForm(forms.ModelForm):

    def clean(self):
        cleaned_data = self.cleaned_data
        print( 'cleaned data:' , cleaned_data)
        return super().clean()

 
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
            'town_city',
            'create_account'
        )

        widgets = {
            'address' : forms.TextInput(attrs = {
                
                'placeholder' : 'Street address'
            
            }),
            
            'country' : forms.Select(attrs = {

            })
        }

