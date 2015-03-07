from django import forms
from django.forms import ModelForm
from applications.models import Application
from django.contrib.admin import widgets 


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        exclude = ('user', 'event', 'status', 'reimbursement_amount')
        widgets = {
            'employment': forms.TextInput(attrs={'placeholder': 'Employment'}),
            'years_using_gnome': forms.NumberInput(attrs={'placeholder': 'Years using GNOME'}),
            'statement_of_interest': forms.Textarea(attrs={'placeholder': 'Statement of interest: '})
        }
    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        self.fields['membership_status'].empty_label = "Membership status"
        self.fields['date_of_arrival'].widget = widgets.AdminDateWidget()



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

