from django.contrib import admin
from django.urls import path
from .views import course_unique

urlpatterns = [
    path('<slug:slug>/', course_unique)
]
