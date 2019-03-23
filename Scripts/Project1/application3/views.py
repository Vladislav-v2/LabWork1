from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def show(request):
    return HttpResponse("application3")

def ShowMessage (request, page_number):
    return HttpResponse("You are reading reviews page "+page_number)

def First_comment(request):
    return HttpResponse("First comment")

def ShowComment(request, comment_number):
    return HttpResponse ("Your comment has number"+comment_number)

def ShowACTION(request,page_number,str):
   if str=='edit':
        return  HttpResponse("You are editing page "+page_number)
   if str=='delete':
       return HttpResponse("You are deleting page " + page_number)
   if str=='answer':
       return HttpResponse("You are discussing page " + page_number)
   else: return  HttpResponse("ERROR")
