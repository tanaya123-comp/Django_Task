from django import forms
from .models import *
from django.forms import ModelForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'
        exclude=['user','updated_at']


class RegisterForm(forms.ModelForm):
    class Meta:
         model=User
         fields=('username','first_name','last_name','email','password')



