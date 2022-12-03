from django.urls import path, re_path

from .views import index, categories, categories_by_id, categories_by_year, about

urlpatterns = [
    path("", index, name="home"),
    path('about/', about),
]

