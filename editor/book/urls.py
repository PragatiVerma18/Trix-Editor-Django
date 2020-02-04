from django.contrib import admin
from django.urls import path, include
from .views import create_book

urlpatterns = [
  path('', create_book , name='create'),
]
