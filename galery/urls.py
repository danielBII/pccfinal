from django.contrib import admin
from django.urls import path
from .views import galery, create_post_galery

urlpatterns = [
    path('', galery, name='galery'),
    path('create/', create_post_galery),
]
