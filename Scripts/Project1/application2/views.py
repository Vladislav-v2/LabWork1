from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.

def show(request):
    return HttpResponse("application2")

def prd(request):
    return HttpResponse("<h1>application2/product</h1>")

def day_archive(request, year, month):
    if month<='12': return HttpResponse(
        "year = "+year+"<br>"+
        "month = " + month+"<br>")
    else: return HttpResponse("invalid month")

def long_string(request, str):
    return HttpResponse("Your argument is   "+str)

def SelectFolder(request, number):
        if number!='1':
         return  HttpResponse("product page with number "+number)
        else:
         return  HttpResponse("First product page")

def ThisYear(request, number):
    if number=='2019': return  HttpResponse("<h1>It’s current year</h1>")
    else: return  HttpResponse("It’s year basic folder")
