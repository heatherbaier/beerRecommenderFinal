# import packages
from django import forms

# super simple form to take user adjectives
class SimpleForm(forms.Form):
    adj1 = forms.CharField()
    adj2 = forms.CharField()
    adj3 = forms.CharField()

    