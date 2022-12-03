from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import Blog

menu = ["Home", "News", "New Article", "Sign In"]

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

def categories(request):
    if (request.GET):
        print(request.GET)
    return HttpResponse("<h1> Посты по категориям </h1>")


def categories_by_id(request, catid):
    return HttpResponse(f"<h1> Посты по категориям </h1><p>{catid}</p>")


def categories_by_year(request, year):
    if int(year) > 2022:
        return redirect('home', permanent=True)
        raise Http404()
    return HttpResponse(f"<h1> Посты по годам </h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("404 error")
