from django.shortcuts import render, get_object_or_404

from .models import Article


def index(request):

    articles = Article.objects.all()
    return render(request, 'blog/index.html', {'posts': articles})


def post_detail(request, post_id):

    article = get_object_or_404(Article, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': article, 'comments': []})


def category_posts(request, category_name):

    filtered_posts = Article.objects.filter(title__icontains=category_name)
    return render(request, 'blog/category.html', {'posts': filtered_posts, 'category': category_name})


def search(request):
    query = request.GET.get('q', '')
    if query:

        results = Article.objects.filter(title__icontains=query) | Article.objects.filter(author__icontains=query)
    else:
        results = Article.objects.all()

    return render(request, 'blog/index.html', {
        'posts': results,
        'query_author': query
    })
