from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
from datetime import datetime
# Create your views here.

def ShowAppsName(request):
    return HttpResponse("application3_1")

def index(request):
    years = [2017, 2018, 2019, 2020, 2021]
    context ={
        "name": "Vladislav",
        "lastname": "Lohai",
        "job_year": years,
        "contact": {
            "nickname": "vlad",
            "phone": "380509467291",
            "email": "vladoss@gmail.com",
        },
        "datetime": datetime.now()
    }
    return render(request,"index.html",context)

def view(request):
    days = [1,2,3,4,5,6,7]
    context = {
        "days": days,
        "current_user": "admin",
        "day": "3",
        "status": "online",
        "email": "vlad@gmail.com"
    }
    return render(request,"condition.html",context)