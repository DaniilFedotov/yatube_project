from django.contrib import admin
# Из модуля models импортируем модель Post
from .models import Post, Group


class PostAdmin(admin.ModelAdmin):
    # Перечисляем поля, отображаемые в админке
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
    )
    list_editable = ('group',)
    # Интерфейс для поиска по тексту постов
    search_fields = ('text',)
    # Возможность фильтрации по дате
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


# Источник конфигурации - класс Postadmin
admin.site.register(Post, PostAdmin)
admin.site.register(Group)
