from django.contrib import admin
from .models import Article

#
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_published') # Поля у списку
    search_fields = ('title', 'content')                  # Пошук
    list_filter = ('is_published', 'created_at')          # Фільтри збоку
    list_editable = ('is_published',)                     # Швидке редагування

# Реєструємо модель разом із налаштуваннями
admin.site.register(Article, ArticleAdmin)