from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import Blog

menu = [
    {'title': 'Home', 'url_name': 'home'},
    {'title': 'News', 'url_name': 'news'},
    {'title': 'New Article', 'url_name': 'new_article'},
    {'title': 'Contact', 'url_name': 'contact'},
    {'title': 'Sign In', 'url_name': 'sign_in'}
]


# Create your views here.
def index(request):
    posts = Blog.objects.all()
    return render(request, 'blog/index.html', {
        "title": "Home",
        'menu': menu,
        'posts': posts,
    })


def about(request):
    return render(request, 'blog/about.html', {
        "title": "About",
        'menu': menu,
    })

def news(request):
    return render(request, 'blog/news.html', {
        "title": "news",
        'menu': menu,
    })

def new_article(request):
    return render(request, 'blog/new_article.html', {
        "title": "new_article",
        'menu': menu,
    })

def contact(request):
    return render(request, 'blog/contact.html', {
        "title": "contact",
        'menu': menu,
    })

def sign_in(request):
    return render(request, 'blog/sign_in.html', {
        "title": "sign_in",
        'menu': menu,
    })


def pageNotFound(request, exception):
    return HttpResponseNotFound("404 error")
