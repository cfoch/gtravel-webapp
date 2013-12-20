from django.forms import ModelForm
from applications.models import Application

class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        exclude = ('user', 'event', 'status')

"""
class ApplicationBankTransferForm(ModelForm):
    class Meta:
        model = BankTransfer
        exclude = ('application')


class ApplicationPayPalForm(ModelForm):
    class Meta:
        model = PayPal
        exclude = ('application')


class ApplicationCheckForm(ModelForm):
    class Meta:
        model = Application
        exclude = ('application')
"""

