from django import forms

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