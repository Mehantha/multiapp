from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def first(request):
    return HttpResponse('<h1>First function in app1</h1>')

def second(request):
    return HttpResponse('<marquee> Second fun in app1</marquee>')

