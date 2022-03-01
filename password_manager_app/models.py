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

    ip = models.CharField(max_length=15, null=False, default=f'{randint(1,255)}.{randint(1,255)}.{randint(1,255)}.{randint(1,255)}')
    login = models.CharField(max_length=100, null=False, default='login')
    password = models.CharField(max_length=100, null=False, default='password')
    tags = models.ManyToManyField(Tag, blank=True)


    def __str__(self):
        return f'{self.ip}'
