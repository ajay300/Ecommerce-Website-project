from tkinter import Widget
from attr import attr
from django import forms
from .models import Customer 
from django.forms.models import ModelForm
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm , AuthenticationForm ,UsernameField , PasswordChangeForm
from django.utils.translation import gettext , gettext_lazy as _
from django.contrib.auth import password_validation

class CustomerRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2']

        labels = {
            'email':'Email',
            'password1':'Enter Password',
            'password2':'Confirm Pasword',
        }
        
        widgets = {
            'username':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'email':forms.EmailInput(attrs={
                'class':'form-control'
            }),
            'password1':forms.PasswordInput(attrs={
                'class':'form-control'
            }),
            'password2':forms.PasswordInput(attrs={
                'class':'form-control'
            }),
        }

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer 
        fields = ['name','locality','city','zipcode','state']

        widgets = {
            'name':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'locality':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'city':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'zipcode':forms.NumberInput(attrs={
                'class':'form-control'
            }),
            'state':forms.Select(attrs={
                'class':'form-control'
            }),
        }
       

class UserLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True , 'class':'form-control'}))
    password = forms.CharField(label=_('Password'),widget=forms.PasswordInput(attrs={'autocomplete':'current-password' , 'class':'form-control'}))

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_('Old_Password'),widget=forms.PasswordInput(attrs={'autocomplete':'current-password' , 'class':'form-control'}))
    new_password1 = forms.CharField(label=_('New Password'),widget=forms.PasswordInput(attrs={'autocomplete':'new-password' , 'class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_('Confirm Password'),widget=forms.PasswordInput(attrs={'autocomplete':'confirm-password' , 'class':'form-control'}))
