from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'class': 'input100',
                                'placeholder': "Name", 'required': True}))
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'class': 'input100',
                                'placeholder': "Alias", 'required': True}))
    email = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'class': 'input100', 'type':'email',
                        'placeholder': "Email", 'help_text': 'Enter a valid email address', 'required': True}))
    password1 = forms.CharField(max_length=254, widget=forms.PasswordInput(attrs={'class': 'input100',
                            'placeholder': "Password", 'required': True}))
    password2 = forms.CharField(max_length=254, widget=forms.PasswordInput(attrs={'class': 'input100',
                            'placeholder': "Confirm Password", 'required': True, 'onfocusout': "samePassword()"}))
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'input100', 'type': 'date',
                            'placeholder': "Date of Birth", 'required': True}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2',]