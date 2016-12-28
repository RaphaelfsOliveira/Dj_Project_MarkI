from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

# Create your views here.
def index(request):
    #return HttpResponse("Index Rango application <br/><a href='/rango/about'>About</a>")
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    #render the response and send it back
    return render(request, 'rango/index.html', context_dict)

def about(request):
    #return HttpResponse("Rango says here is the ABOUT PAGE <br/><br/><a href='/rango/'>Index</a>")
    context_dict = {
        'about_page': 'Page 2 ABOUT PAGE',
        'example': 'Deadpool!!'
    }
    return render(request, 'rango/about.html', context=context_dict)
