from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    '''Объявляем класс Post, наследник класса Model из пакета models'''
    '''Описываем поля модели и их типы'''

    text = models.TextField(
        verbose_name='Текст публикации',
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор публикации',
        on_delete=models.CASCADE,
        related_name='posts',
    )
    group = models.ForeignKey(
        'Group',
        verbose_name='Сообщество',
        blank=True,
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts',
    )

    class Meta:
        '''Контейнер класса Post с фильтром даты'''
        ordering = ('-pub_date',)


class Group(models.Model):
    '''Объявляем класс Group, наследник класса Model из пакета models'''
    '''Описываем поля модели и их типы'''

    title = models.CharField(
        verbose_name='Сообщество',
        max_length=200,
    )
    slug = models.SlugField(
        verbose_name='URL - адрес',
        unique=True,
    )
    description = models.TextField(
        verbose_name='Описание',
    )

    def __str__(self) -> str:
        return self.title
