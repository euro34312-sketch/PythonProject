from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    # Поля згідно з презентацією
    title = models.CharField(max_length=200)  # Короткий текст (Обов'язковий max_length)
    content = models.TextField()  # Довгий текст для статті
    published_date = models.DateTimeField(auto_now_add=True)  # Дата створення (автоматично)

    # Зв'язок "Один-до-багатьох" (ForeignKey)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title