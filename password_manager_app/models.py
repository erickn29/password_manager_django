from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from random import randint

class Tag(models.Model):

    name = models.CharField(max_length=100, null=False, default='')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')

    def __str__(self):
        return f'{self.name}'


    def get_url(self):
        return reverse('tags', args=[self.slug])


class PasswordManager(models.Model):

    ip = models.CharField(max_length=15, null=False)
    login = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=100, null=False)
    tags = models.ManyToManyField(Tag, blank=True)


    def __str__(self):
        return f'{self.ip}'


class User(models.Model):
    user_login = models.CharField(max_length=15, default='log')
    user_password = models.CharField(max_length=24, default='pass')
    user_email = models.EmailField(max_length = 254, default='email@email.email')

    def __str__(self):
        return f'{self.user_login}'
