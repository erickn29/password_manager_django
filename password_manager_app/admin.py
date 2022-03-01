from django.contrib import admin
from .models import PasswordManager, Tag


class PasswordManagerAdmin(admin.ModelAdmin):
    list_display = ['ip', 'login', 'password']
    list_editable = ['login', 'password']
    filter_horizontal = ['tags']


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(PasswordManager, PasswordManagerAdmin)
admin.site.register(Tag, TagAdmin)