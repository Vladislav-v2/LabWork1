from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
# Create your views here.

def ShowAppName(request):
    return HttpResponse("applicatinmodels")