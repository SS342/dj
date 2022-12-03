from django.urls import path, re_path

from .views import index, categories, categories_by_id, categories_by_year

urlpatterns = [
    path("", index, name="home"),
    path("cats/", categories),
    path("cats/<int:catid>/", categories_by_id),
    re_path(r'^archive/(?P<year>[0-9]{4})/', categories_by_year),
]

