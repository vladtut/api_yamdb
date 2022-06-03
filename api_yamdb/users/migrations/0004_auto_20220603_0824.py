# Generated by Django 2.2.16 on 2022-06-03 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220602_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Администратор'), ('moderator', 'Модератор'), ('user', 'Пользователь')], default='user', max_length=16),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=255, null=True, unique=True, verbose_name='username'),
        ),
    ]
