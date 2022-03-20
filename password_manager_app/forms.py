from django import forms
from .models import PasswordManager, Tag


class PasswordManagerForm(forms.ModelForm):

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Выберите теги'
    )

    class Meta:
        model = PasswordManager
        fields = ['ip', 'login', 'password', 'tags']
        labels = {
            'ip': 'Ресурс',
            'login': 'Логин',
            'password': 'Пароль',
            'tags': 'Выберите теги'
        }

