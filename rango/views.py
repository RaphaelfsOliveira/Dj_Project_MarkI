from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Index Rango application <br/><a href='/rango/about'>About</a>")

def about(request):
    return HttpResponse("Rango says here is the ABOUT PAGE <br/><a href='/rango/'>Index</a>")
