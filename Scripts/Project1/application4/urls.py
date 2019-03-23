from django.contrib import admin
from django.urls import re_path, include, path
from django.conf.urls import url
from django.template import loader
from . import  views

urlpatterns = [
    path('',views.ShowAppsName),
    path('redirect/',views.Redir),
    path('redirect/redirected/',views.ShowRedir),
    path('render-html/',views.ShowHTML),
    path('html/', views.view),
]