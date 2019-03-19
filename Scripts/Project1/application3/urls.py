from django.contrib import admin
from django.urls import path
from django.urls import re_path
from django.conf.urls import url
from . import  views

urlpatterns = [

    #re_path(r'^item/(?P<year>[\d]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.day_archive, name = 'none'),

    #url(r'^(?P<str>[\w]*)/$',views.long_string),
    re_path(r'^review/page-(?P<page_number>[\d].)/$',views.ShowMessage),
    path('', views.show),
]
new_patterns = [
    re_path(r'^comments/',views.First_comment),
    re_path(r'^comments/(?P<comment_number>[\d])/$',views.ShowComment),
]