from django.shortcuts import render
from django.http import HttpResponse

# Спільне меню для всіх сторінок
menu = """
    <hr>
    <nav>
        <a href="/">Головна</a> | 
        <a href="/about/">Про нас</a> | 
        <a href="/contact/">Контакти</a>
    </nav>
    <hr>
"""

def index(request):
    return HttpResponse(f"<h1>Головна сторінка блогу</h1><p>Вітаємо на нашому сайті!</p>{menu}")

def about(request):
    return HttpResponse(f"<h1>Про нас</h1><p>Ми створюємо найкращий контент для вас.</p>{menu}")

def contact(request):
    return HttpResponse(f"<h1>Контакти</h1><p>Зв'яжіться з нами за адресою: info@example.com</p>{menu}")