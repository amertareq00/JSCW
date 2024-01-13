from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Shipment

class ShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ['from_city', 'to_city','weight', 'shipment_date']
        widgets = {
            'shipment_date': forms.DateInput(attrs={'type': 'date'}),}
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email',  'password1', 'password2']
