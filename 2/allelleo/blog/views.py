from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import Blog

menu = [
    {'title': 'Home', 'url_name': 'home'},
    {'title': 'About', 'url_name': 'about'},
    {'title': 'New Article', 'url_name': 'new_article'},
    {'title': 'Contact', 'url_name': 'contact'},
    {'title': 'Sign In', 'url_name': 'sign_in'}
]


# Create your views here.
def index(request):
    posts = Blog.objects.all()
    context = {
        "title": "Home",
        'menu': menu,
        'posts': posts,
    }
    return render(request, 'blog/index.html', context=context)


def about(request):
    context = {
        "title": "About",
        'menu': menu,
    }
    return render(request, 'blog/about.html', context=context)


def new_article(request):
    context = {
        "title": "new_article",
        'menu': menu,
    }
    return render(request, 'blog/new_article.html', context=context)


def contact(request):
    context = {
        "title": "Contact",
        'menu': menu,
    }
    return render(request, 'blog/contact.html', context=context)


def sign_in(request):
    context = {
        "title": "Sign In",
        'menu': menu,
    }
    return render(request, 'blog/sign_in.html', context=context)


def show_post(request, post_id):
    return HttpResponse(f"Post: {post_id}")


def pageNotFound(request, exception):
    return HttpResponseNotFound("404 error")
