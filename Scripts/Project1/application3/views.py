from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def show(request):
    return  HttpResponse("qwerty")

def ShowMessage(request,page_number):
    return HttpResponse("You are reading reviews page "+page_number)

def First_comment(request):
    return HttpResponse("“First comment")

def ShowComment(request,comment_number):
    return HttpResponse("Your comment has number"+comment_number);