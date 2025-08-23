from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput
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
        fields = ['first_name', 'last_name', 'category', 'phone', 'tall', 'weight', 'address']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'tall': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter height in cm'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter weight in kg'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter address'}),
        }
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        # Remove any non-digit characters
        phone = ''.join(filter(str.isdigit, str(phone)))
        if not phone:
            raise forms.ValidationError('Please enter a valid phone number')
        return phone

class updateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'category', 'phone', 'tall', 'weight', 'address']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'tall': forms.NumberInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }
 