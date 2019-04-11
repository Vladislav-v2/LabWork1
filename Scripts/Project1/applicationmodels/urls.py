from django.contrib import admin
from django.urls import re_path, include, path
from django.conf.urls import url
from django.template import loader
from . import views

urlpatterns = [
    path('', views.ShowAppName),
]