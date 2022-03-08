from django import forms
from .models import User, PasswordManager


class PasswordManagerForm(forms.ModelForm):
    class Meta:
        model = PasswordManager
        fields = ['ip', 'login', 'password', 'tags']
        labels = {
            'ip': 'ip',
            'login': 'log',
            'password': 'pass',
            'tags': 'taaags'
        }