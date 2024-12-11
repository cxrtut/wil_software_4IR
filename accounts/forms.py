from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ContactForm(forms.Form):
    username = forms.CharField(max_length=100, label='Your Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Your Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Your Message', widget=forms.Textarea(attrs={'class': 'form-control'}))

class CheckoutForm(forms.Form):
    firstname = forms.CharField(max_length=100, label="Full Name")
    email = forms.EmailField(label="Email")
    address = forms.CharField(max_length=200, label="Address")
    city = forms.CharField(max_length=50, label="City")
    state = forms.CharField(max_length=50, label="State")
    zip = forms.CharField(max_length=20, label="Zip")
    cardname = forms.CharField(max_length=100, label="Name on Card")
    cardnumber = forms.CharField(max_length=16, label="Credit Card Number")
    expmonth = forms.CharField(max_length=20, label="Expiration Month")
    expyear = forms.CharField(max_length=4, label="Expiration Year")
    cvv = forms.CharField(max_length=4, label="CVV")