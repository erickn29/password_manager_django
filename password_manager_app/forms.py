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
            'tags': 'Выбрать теги',
        }


# class TagsForm(forms.ModelForm):
#     class Meta:
#         model = Tag
#         fields = ['name', 'slug']
#         labels = {
#             'name': 'Добавить тег',
#             'slug': ''
#         }
#
#     prepopulated_fields = {'slug': ('name',)}