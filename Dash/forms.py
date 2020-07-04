from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",
                "class": "form-control"
            }
        ))

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class AddDeviceForm(forms.Form):
    device_name = forms.CharField(
        required=True,
        label='Device Name',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    location = forms.CharField(
        required=False,
        label='Location',
        max_length=50,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    device_type = forms.CharField(
        required = False,
        label = 'Device Type',
        max_length = 100,
        widget= forms.TextInput(attrs={'class': 'form-control'})
    )