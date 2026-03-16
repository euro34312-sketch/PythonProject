from django.contrib import admin
from .models import Category, Post

admin.site.register(Category)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'published_date')
    list_filter = ('category',)
    search_fields = ('title', 'content')