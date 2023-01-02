from django import forms

class SMSForm(forms.Form):
    phone = forms.CharField(max_length=10, required=True)
    code = forms.CharField(max_length=4, required=False)