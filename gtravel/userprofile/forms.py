from django.forms import ModelForm
from django import forms
from userprofile.models import Persona


class SignUpForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Persona
        fields = [
            'username',
            'email',
            'password',
            'password2',
            'first_name',
            'last_name'
            ]

