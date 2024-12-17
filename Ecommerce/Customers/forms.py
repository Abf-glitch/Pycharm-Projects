from django import forms

from Customers.models import Customer


class CustomerForm(forms.Form):
    name = forms.CharField(required=True,max_length=20,label='Name:')
    email = forms.EmailField(required=True,label='Email:',min_length=10, max_length=30)
    phone = forms.IntegerField(required=True,label='Phone Number:')
    address = forms.CharField(required=True,max_length=10,label='Address:')

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'