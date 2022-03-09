from django import forms
from .models import User, PasswordManager, Tag


class PasswordManagerForm(forms.ModelForm):

    class Meta:
        model = PasswordManager
        fields = ['ip', 'login', 'password', 'tags']
        labels = {
            'ip': 'Ресурс',
            'login': 'Логин',
            'password': 'Пароль',
            'tags': 'Выберите теги',
        }

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )