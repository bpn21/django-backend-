from django.db import models
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

# Create your models here.


class SignupForm(ModelForm):
    """user signup form"""
    class Meta:
        model = User
        fields = ('username','first_name','password','email',)


class LoginForm(forms.Form):
    """user Login Form"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())



