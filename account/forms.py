# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import EmailField, TextInput, PasswordInput, FileInput, Textarea

from .models import Image

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
    
        widgets = {
        "username" : forms.TextInput(attrs={
            'class' : 'form-control',
            'placeholder' : ''
        }),
        "email" : forms.EmailInput(attrs={
            'class' : 'form-control',
            'placeholder' : ''
        }),
        "password1" : forms.PasswordInput(attrs={
            'class' : 'form-control',
            'placeholder' : ''
        }),
        "password2" : forms.PasswordInput(attrs={
            'class' : 'form-control',
            'placeholder' : ''
        }),
    }
        
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = [ 'title', 'image', 'description']

        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'input-field'}),
            'image' : forms.FileInput(attrs={'class' : 'input-field'}),
            'description' : forms.Textarea(attrs={'class' : 'input-field'}),
        }
        