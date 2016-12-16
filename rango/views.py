from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

def index(request):
    #return HttpResponse("Index Rango application <br/><a href='/rango/about'>About</a>")
    context_dict = {
        'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!",
        'lizard': "The Green lizard!!!"
    }
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    #return HttpResponse("Rango says here is the ABOUT PAGE <br/><br/><a href='/rango/'>Index</a>")
    context_dict = {
        'about_page': 'Page 2 ABOUT PAGE',
        'example': 'Deadpool!!'
    }
    return render(request, 'rango/about.html', context=context_dict)
