from django.forms import ModelForm
from applications.models import Application

class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        exclude = ('user', 'event', 'status')


