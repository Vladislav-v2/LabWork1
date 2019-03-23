from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect

# Create your views here.
def view(request):
    list = [0,232,45,123,0,4,53423,54,23]
    context = {
        "text": "TEXT!",
        "list":list,
        "name":"Adam",
        "surname":"Smith",
        "coords":{
            "x":"x coords",
            "y":"y coords",
        },
    }

    return render(request,"htmlFile.html",context)

def ShowAppsName(request):
    return HttpResponse("application4")
def Redir(request):
    return redirect("redirected/")

def ShowRedir(request):
    return HttpResponse("You were redirected")

def ShowHTML(request):
    html = """
     <html>
     <head><title>TITLE</title>
     <body>
     <h1>HTML!<h1>
     </body>
     </html>
     """
    return  HttpResponse(html)

