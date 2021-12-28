from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email', required=True)
    password1=forms.CharField(label='Password', required=True, widget=forms.PasswordInput())
    password2=forms.CharField(label='Repite Password', required=True, widget=forms.PasswordInput())

    class Meta:
        model=User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts={k:'' for k in fields}
    


