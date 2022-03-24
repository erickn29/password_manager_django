from django.contrib import admin
from .models import PasswordManager, Tag


class PasswordManagerAdmin(admin.ModelAdmin):
    list_display = ['resource_name', 'ip', 'login', 'post_author']
    list_editable = []
    filter_horizontal = ['tags']
    prepopulated_fields = {'post_slug': ('ip',), 'resource_name_alias':('resource_name',)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(PasswordManager, PasswordManagerAdmin)
admin.site.register(Tag, TagAdmin)