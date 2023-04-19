from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def hello(request):
    return HttpResponse("Hello, world!")


def witaj(request):
    return HttpResponse("<h2 > Witaj, <span style='color:red'>Wojtek</span> </h2>")


def hi(request):
    return HttpResponse("<!DOCTYPE html><html><head><body></body></head>>/html>")


def hi2(request):
    return render(request, "hi.html")