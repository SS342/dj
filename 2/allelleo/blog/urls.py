from django.urls import path, re_path

from .views import index, about, new_article, contact, sign_in

urlpatterns = [
    path("", index, name="home"),
    path('about/', about, name="about"),
    path('new-article/', new_article, name="new_article"),
    path('contact/', contact, name="contact"),
    path('sign-in/', sign_in, name="sign_in"),
]

