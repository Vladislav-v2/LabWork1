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
from django.urls import include, path

urlpatterns = [
    path('appdatabase/', include('appdatabase.urls')),
    path('applicationmodels/', include('applicationmodels.urls')),
    path('application3_1/', include('application3_1.urls')),
    path('application4/',include('application4.urls')),
    #path('application3/',include('application3.urls')),
    #path('application2/',include('application2.urls')),
    #path('application1/', include('application1.urls')),
    #path('',include('application1.urls')),
    #path('App1/',include('App1.urls')),
    path('admin/', admin.site.urls),
]