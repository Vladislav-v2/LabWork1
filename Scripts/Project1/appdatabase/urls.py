from django.urls import re_path, include, path
from django.conf.urls import url
from django.template import loader
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('content/', views.List.as_view(),name="human_list"),
    path('content/search/', views.List.as_view(), name = "search_list"),
]