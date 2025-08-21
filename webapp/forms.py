from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import TextInput, PasswordInput
from .models import Record

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',  'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField( widget=TextInput)
    password = forms.CharField(widget=PasswordInput)

class createRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name','Category' , 'phone','tall','weight', 'address']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
             'Category': forms.Select(attrs={'class': 'form-control'}),
            'tall': forms.NumberInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }
 