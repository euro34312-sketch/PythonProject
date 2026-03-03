from django.shortcuts import render
from django.http import HttpResponse

POSTS = [
    {
        'id': 1,
        'title': 'Вступ до Django',
        'slug': 'vstup-do-django',
        'content': 'Django - це чудовий веб-фреймворк на Python...',
        'category': 'python',
        'author': 'Іван',
        'date': '2025-01-15'
    },
    {
        'id': 2,
        'title': 'Основи Python',
        'slug': 'osnovy-python',
        'content': 'Python - одна з найпопулярніших мов програмування...',
        'category': 'python',
        'author': 'Марія',
        'date': '2025-01-10'
    },
    {
        'id': 3,
        'title': 'HTML та CSS',
        'slug': 'html-ta-css',
        'content': 'HTML використовується для структури, CSS - для стилів...',
        'category': 'web',
        'author': 'Петро',
        'date': '2025-01-20'
    },
    {
        'id': 4,
        'title': 'JavaScript для початківців',
        'slug': 'javascript-dlya-pochatkivtsiv',
        'content': 'JavaScript робить веб-сторінки інтерактивними...',
        'category': 'web',
        'author': 'Олена',
        'date': '2024-12-25'
    },
    {
        'id': 5,
        'title': 'Робота з базами даних',
        'slug': 'robota-z-bazamy-danyh',
        'content': 'Бази даних зберігають інформацію...',
        'category': 'database',
        'author': 'Іван',
        'date': '2024-11-30'
    },
]

COMMENTS = [
    {'id': 1, 'post_id': 1, 'author':'t', 'text': 'Дуже корисна стаття!'},
    {'id': 2, 'post_id': 1, 'author':'te' , 'text': 'Дякую за роз’яснення.'},
    {'id': 3, 'post_id': 2, 'author': 'ex', 'text': 'Python справді легкий.'},
]


def index(request):
    query_author = request.GET.get('q')
    results = [p for p in POSTS if p['author'] == query_author] if query_author else POSTS
    return render(request, 'blog/index.html', {'posts': results, 'query_author': query_author})


def post_detail(request, post_id):
    post = next((p for p in POSTS if p['id'] == post_id), None)
    if not post:
        return HttpResponse("Статтю не знайдено", status=404)

    post_comments = [c for c in COMMENTS if c['post_id'] == post_id]
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': post_comments})


def category_posts(request, category_name):
    filtered_posts = [p for p in POSTS if p['category'] == category_name]
    return render(request, 'blog/category.html', {'posts': filtered_posts, 'category': category_name})