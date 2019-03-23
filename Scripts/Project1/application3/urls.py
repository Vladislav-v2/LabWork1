from django.contrib import admin
from django.urls import re_path, include, path
from django.conf.urls import url
from . import  views


new_patterns = [
    re_path(r'^comments/$', views.First_comment),
    re_path(r'^comments/(?P<comment_number>[\d]{1,})/$',views.ShowComment),
]

ACTION = [
    re_path(r'(?P<str>[\w]+)/$',views.ShowACTION),
]
urlpatterns = [
    #re_path(r'^item/(?P<year>[\d]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.day_archive, name = 'none'),

    #url(r'^(?P<str>[\w]*)/$',views.long_string),

    re_path(r'^review/page-(?P<page_number>[\d].)/$',views.ShowMessage),


    re_path(r'^product/review/page-(?P<page_number>[\d]+)/',include(ACTION)),


    path('new_patterns/', include(new_patterns)),
    path('', views.show),
]
