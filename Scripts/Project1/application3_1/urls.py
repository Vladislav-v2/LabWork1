from django.contrib import admin
from django.urls import re_path, include, path
from django.conf.urls import url
from django.template import loader
from . import views

urlpatterns = [
    path('',views.ShowAppsName),
    path('user/',views.index),
    path('condition/',views.view),
    path('menu/',views.menu),
    path('menu/main.html',views.ShowMain),
    path('menu/Content.html', views.ShowContent),
    path('menu/condition.html', views.view),
    path('menu/wrapper.html', views.ShowWrapper),
]