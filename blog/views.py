from django.shortcuts import render
from django.http import HttpResponse

POSTS = [
    {'id': 1, 'title': 'Вступ до Django', 'author': 'Іван', 'content': 'Django — це круто!'},
    {'id': 2, 'title': 'Python для початківців', 'author': 'Марія', 'content': 'Вчимо основи Python.'},
    {'id': 3, 'title': 'Поради по розробці', 'author': 'Іван', 'content': 'Пишіть чистий код.'},
]


def index(request):
    query_author = request.GET.get('q')
    results = POSTS
    if query_author:
        results = [p for p in POSTS if p['author'].lower() == query_author.lower()]

    return render(request, 'blog/index.html', {'posts': results})


def post_detail(request, post_id):
    post_found = next((p for p in POSTS if p['id'] == post_id), None)
    if post_found:
        return render(request, 'blog/post_detail.html', {'post': post_found})
    return HttpResponse("Статтю не знайдено", status=404)


def category_posts(request, category_name):
    return HttpResponse(f"Категорія: {category_name}")