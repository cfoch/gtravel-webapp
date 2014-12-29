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

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
