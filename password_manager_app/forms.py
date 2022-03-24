from django import forms
from .models import PasswordManager, Tag
from django.contrib.auth.models import User


class PasswordManagerForm(forms.ModelForm):

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Выберите теги'
    )

    # post_author = forms.CharField(max_length=100, disabled=False)

    class Meta:
        model = PasswordManager
        exclude = ("post_author",)
        fields = ['resource_name', 'ip', 'login', 'password', 'esia_login', 'tags']
        labels = {
            'resource_name': 'Названние ресурса',
            'ip': 'Адрес ресурса',
            'login': 'Логин',
            'esia_login': 'Вход через Госуслуги',
            'password': 'Пароль',
            'tags': 'Выберите теги',
        }

    # def save(self, commit=True):
    #     instance = super(PasswordManagerForm, self).save(commit=False)
    #     instance.post_author = User.objects.get(id=post_author)
    #     if commit:
    #         instance.save()
    #     return instance