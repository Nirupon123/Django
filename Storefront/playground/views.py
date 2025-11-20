from django.shortcuts import render
from django.http import  HttpResponse

def say_hello(request):
    #return HttpResponse("Welcome to the Playground App!")
    return render(request,'index.html')