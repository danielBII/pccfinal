from django.contrib import admin
from django.urls import path
from blog.views import posts, posts_edit, posts_del, posts_create


urlpatterns = [
    path('create/', posts_create, name="postcreate"),
    path('<slug:slug>/', posts, name="postunique"),
    path('<slug:slug>/edit/', posts_edit, name="postedit"),
    path('<slug:slug>/delete/', posts_del, name="postedel"),
]
