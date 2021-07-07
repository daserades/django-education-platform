from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={
        'class':"form-control" ,
        'placeholder':"Username"
    }))
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'class':"form-control" ,
        'placeholder':"Password"
    }))
    class Meta:
        model=User
        fields= ['username','password']

class RegisterForm(UserCreationForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={
        'class':"form-control" ,
        'placeholder':"Your firstname"
    }))
    last_name=forms.CharField(widget=forms.TextInput(attrs={
        'class':"form-control" ,
        'placeholder':"Your lastname"
    }))
    email=forms.EmailField(widget=forms.EmailInput(attrs={
        'class':"form-control" ,
        'placeholder':"Your email"
    }))
    username=forms.CharField(widget=forms.TextInput(attrs={
        'class':"form-control" ,
        'placeholder':"Username"
    }))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={
        'class':"form-control" ,
        'placeholder':"Password"
    }))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={
        'class':"form-control" ,
        'placeholder':"Confirm Password"
    }))
    class Meta:
        model=User
        fields= ['first_name','last_name','email','username','password1','password2']

