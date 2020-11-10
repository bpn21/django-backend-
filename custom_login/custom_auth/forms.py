"""lets create simple forms for user to register and login.
 Note that we are not focused on designing the form with css."""

from django import forms
from django.contrib.auth import get_user_model


class SignupForm(forms.ModelForm):
    """user signup form"""
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ('email', 'name', 'password',)


class LoginForm(forms.Form):
    """user login form"""
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

""" in Modelforms Meta class we don’t initialise user model 
via importing from models.py as usual but
 instead we are referring to settings.py initialisation.
  Hence we called get_user_model() method which in turn returns our custom user class.
   This is the recommended best practise to follow. 
   This can be same in any other app where user model is to be instantiated.
    Further we return the views based on the user action. Lets code for views in views.py"""