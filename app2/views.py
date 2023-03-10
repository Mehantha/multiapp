from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first(request):
    return HttpResponse('<h1>First fun in app2')

def second(request):
    return HttpResponse('<h2><marquee>Second fun in app2</marquee></h2>')

