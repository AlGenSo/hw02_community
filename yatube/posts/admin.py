from django.contrib import admin
from .models import Post, Group

# Создание класса PostAdmin, наследник модели admin.ModelAdmin


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    # Перечисляем поля, которые должны отображаться в админке
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
    )
    # Список групп
    list_editable = ('group',)
    # Интерфейс для поиска по тексту постов
    search_fields = ('text',)
    # Возможность фильтрации по дате
    list_filter = ('pub_date',)
    # Это свойство сработает для всех колонок: где пусто — там будет эта строка
    empty_value_display = '-пусто-'


admin.site.register(Group)
