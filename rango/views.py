from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Naaaaaoo PEEEIIDAA!")

def about(request):
    return HttpResponse('Rango says here is the ABOUT PAGE')
