from django import forms
from django.forms import fields
from .models import Contact

class ContactForm(forms.ModelForm):
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
    phone=forms.CharField(widget=forms.TextInput(attrs={
        'class':"form-control" ,
        'placeholder':"Your phone"
    }))
    message =forms.CharField(widget=forms.Textarea(attrs={
        'class':"form-control" ,
        'placeholder':"Say something about us"
    }))

    class Meta:
        model=Contact
        fields= ['first_name','last_name','email','phone','message']