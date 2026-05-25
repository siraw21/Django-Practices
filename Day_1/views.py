from django.http import HttpResponse
from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
   return render(request, "hello/index.html")

def login(request):
   return HttpResponse("Welcome to login page")

def greeting(request, name):
    return render(request, "hello/greet.html", {
       "name": name.capitalize()
    })

def is_it_christmas(request):
    now = datetime.datetime.now()
    
    return render(request, "hello/isItChristmas.html", {
        "month": now.month == 1 and now.day == 1
        
    })
