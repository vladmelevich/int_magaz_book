from django import forms
from . import models

class KnigForm(forms.ModelForm):
    class Meta:
        model = models.books
        fields = ['name','im','har','price','kol','kat','nam']

class PoiskForm(forms.Form):
    poisk = forms.CharField(max_length=45)

class ZakarForm(forms.ModelForm):
    class Meta:
        model = models.za
        fields = ['nmb','user_name','sur_name','kol','goro','yl','adre']
