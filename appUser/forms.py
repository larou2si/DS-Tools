from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'class': 'input100', 'required': True}))
    email = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'class': 'input100',
                            'help_text': 'Enter a valid email address', 'required': True}))
    password1 = forms.CharField(max_length=254, widget=forms.PasswordInput(attrs={'class': 'input100',
                            'placeholder': "Password", 'required': True}))
    password2 = forms.CharField(max_length=254, widget=forms.PasswordInput(attrs={'class': 'input100',
                            'placeholder': "Password", 'required': True}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2',]
        widgets = {
            '': forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Enter your username'}),
        }