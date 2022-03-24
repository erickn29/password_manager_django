from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
from encrypted_model_fields.fields import EncryptedCharField


class Tag(models.Model):

    name = models.CharField(max_length=100, null=False, default='')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')

    def __str__(self):
        return f'{self.name}'


    def get_url(self):
        return reverse('tags', args=[self.slug])


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)


# class New_tags(TagModel):
#     class TagMeta:
#         # Tag options
#         initial = "tag1, tag2, tag3"
#         force_lowercase = True
#         # autocomplete_view = 'myapp.views.hobbies_autocomplete'

class PasswordManager(models.Model):

    resource_name = models.CharField(max_length=100, blank=True, default='')
    resource_name_alias = models.CharField(max_length=100, blank=True, default='')
    esia_login = models.BooleanField(default=False)
    ip = models.CharField(max_length=100, null=True, blank=False)
    login = models.CharField(max_length=100, null=False, blank=True)
    password = EncryptedCharField(max_length=100)
    tags = models.ManyToManyField(Tag, blank=True)
    # tags = TagField(to=New_tags)
    post_slug = models.SlugField(max_length=100, unique=False, default='dflt')
    post_time = models.DateTimeField(auto_now=True)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.ip}'


    def get_url(self):
        return reverse('edit_post', args=[self.post_slug,])


    def save(self, *args, **kwargs):
        self.post_slug = f'{slugify(self.ip)}_{self.login}'
        self.resource_name_alias = str(self.resource_name).lower()
        super(PasswordManager, self).save(*args, **kwargs)



'''Перезаписать данные после миграции'''
# for item in PasswordManager.objects.all():
#     item.save()