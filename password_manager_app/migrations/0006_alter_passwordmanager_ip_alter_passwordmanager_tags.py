# Generated by Django 4.0.2 on 2022-03-01 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('password_manager_app', '0005_alter_passwordmanager_ip_alter_passwordmanager_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordmanager',
            name='ip',
            field=models.CharField(default='116.253.138.34', max_length=15),
        ),
        migrations.AlterField(
            model_name='passwordmanager',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='passwords', to='password_manager_app.Tag'),
        ),
    ]
