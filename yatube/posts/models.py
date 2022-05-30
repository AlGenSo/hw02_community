from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Объявляем класс Post, наследник класса Model из пакета models


class Post(models.Model):
    # Описываем поля модели и их типы

    # Тип: TextField (текстовое поле)
    text = models.TextField(
        verbose_name='Текст публикации',
    )
    # Тип поля: DateTimeField, для хранения даты и времени;
    # параметр auto_now_add определяет, что в поле будет автоматически
    # подставлено время и дата создания новой записи
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
    )
    # Тип: ForeignKey, ссылка на модель User
    author = models.ForeignKey(
        User,
        verbose_name='Автор публикации',
        on_delete=models.CASCADE,
        related_name='posts',
    )
    # Тип: ForeignKey, ссылка на модель Group
    group = models.ForeignKey(
        'Group',
        verbose_name='Сообщество',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='posts',
    )


# Объявляем класс Group, наследник класса Model из пакета models


class Group(models.Model):
    # Описываем поля модели и их типы

    # Тип: CharField (строка с ограничением длины)
    title = models.CharField(
        verbose_name='Каста',
        max_length=200,
    )
    # Короткая метка для чего-либо,
    # содержащая только буквы, цифры,
    # подчеркивания или дефисы. Обычно используются в URL.
    slug = models.SlugField(
        verbose_name='URL - адрес',
        unique=True,
    )
    # Тип: TextField (текстовое поле)
    description = models.TextField(
        verbose_name='Заметка',
    )

    # метод __str__,
    # чтобы при печати объекта модели Group
    # выводилось поле title.
    def __str__(self) -> str:

        return self.title
