from django.db import models
from django.contrib.auth.models import AbstractUser


class Genre(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.slug


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.slug


class Title(models.Model):
    name = models.CharField(max_length=256)
    year = models.IntegerField(
        'Год релиза',
        help_text='Введите год релиза',
        null=True,
        blank=True
    )
    rating = models.IntegerField(
        'Рейтинг',
        help_text='Введите рейтинг произведения',
        blank=True,
        null=True
    )
    genre = models.ManyToManyField(Genre, verbose_name='Жанр', related_name='titles')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name='Категория',
        help_text='Введите категорию произведения',
        null=True,
        blank=True,
        related_name='titles'
    )
    description = models.TextField(
        null=True,
        verbose_name='Описание'
    )

    def __str__(self) -> str:
        return self.name


class Review(models.Model):
    title = models.ForeignKey(
        'Title',
        on_delete=models.CASCADE,
        related_name='reviews',
        help_text='введите произведения',
        verbose_name='Произведения',
    )
    text = models.TextField(
        help_text='введите текст отзыва',
        verbose_name='текст отзыва')
    pub_date = models.DateTimeField(
        auto_now_add=True,
        help_text='введите дату публикации ',
        verbose_name='дата публикации')
    author = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='reviews',
        help_text='введите автора',
        verbose_name='Автор',
    )
    score = models.IntegerField(
        help_text='укажите оценку произведения',
        verbose_name='оценка',
    )


class Comment(models.Model):
    review = models.ForeignKey(
        'Review',
        on_delete=models.CASCADE,
        related_name='comments',
        help_text='введите отзыв',
        verbose_name='Отзыв',
    )
    text = models.TextField(
        help_text='введите текст комментария',
        verbose_name='текст комментария')
    pub_date = models.DateTimeField(
        auto_now_add=True,
        help_text='введите дату публикации ',
        verbose_name='дата публикации')
    author = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='comments',
        help_text='введите автора',
        verbose_name='Автор',
    )


class User(AbstractUser):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'
    CHOICES = [
        (ADMIN, 'Администратор'),
        (MODERATOR, 'Модератор'),
        (USER, 'Пользователь'),
    ]
    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        unique=True,
    )
    username = models.CharField(
        verbose_name='username',
        max_length=255,
        null=True,
        unique=True,
    )
    role = models.CharField(
        max_length=16,
        choices=CHOICES,
        default='user'
    )
    bio = models.TextField(
        'Биография',
        blank=True,
    )

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_admin(self):
        return self.role == self.ADMIN

