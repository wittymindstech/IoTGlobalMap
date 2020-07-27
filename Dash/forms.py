from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from leaflet.forms.widgets import LeafletWidget

from Dash.models import Device

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

from django.contrib.gis import forms

class AddDeviceForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Name", "class": "form-control"}))
    location = forms.PointField(widget= forms.OSMWidget(attrs={'map_width': 1000, 'map_height': 500}))

    class Meta:
        model = Device
        fields = ('name', 'location')
        widgets = {'location': LeafletWidget()}

    class Media:
        css = {
            'all': (
                'https://cdnjs.cloudflare.com/ajax/libs/ol3/3.20.1/ol.css',
                'gis/css/ol3.css',
            )
        }
        js = (
            'https://cdnjs.cloudflare.com/ajax/libs/ol3/3.20.1/ol.js',
            'gis/js/OLMapWidget.js',
        )
