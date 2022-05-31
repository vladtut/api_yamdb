from django.contrib.auth.models import AbstractUser
from django.db import models

CHOICES = (
    ('user', 'пользователь'),
    ('moderator', 'модератор'),
    ('admin', 'администратор'),
)

class User(AbstractUser):
    user_role=models.CharField(
        max_length=16,
        choices=CHOICES,
        default='user'
    )


