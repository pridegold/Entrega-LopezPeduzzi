from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PlacasForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    marca = forms.CharField(max_length=40)

class FuentesForm(forms.Form):
    Watts = forms.CharField(max_length=40)
    marca = forms.CharField(max_length=40)

class PerifericosForm(forms.Form):
    tipo = forms.CharField(max_length=40)
    marca = forms.CharField(max_length=40)
    modelo = forms.CharField(max_length=40)

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]


class UserEditForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]
        help_texts = {k: "" for k in fields}


