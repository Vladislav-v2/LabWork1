"""Project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from django.conf.urls import url
from . import  views

urlpatterns = [
    re_path(r'^product/$',views.prd),
    re_path(r'^product/(?P<number>[\d]{3,4})/$', views.ThisYear),
    re_path(r'^product/(?P<year>[\d]{3,4})/(?P<month>[0-9]{2})/$',views.day_archive),
    #re_path(r'^item/(?P<year>[\d]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.day_archive, name='none'),

    url(r'^(?P<str>[\w]*)/$', views.long_string),
    re_path(r'^folder/product(?P<number>[\d]{1,})/$', views.SelectFolder),
    path('', views.show),
]