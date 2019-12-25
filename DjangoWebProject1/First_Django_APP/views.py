from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def index(request):
    now = datetime.now()
    return render(
        request,
        "First_Django_APP/index.html",
        {
            'title':"GNLS Django!",
            'message':'WDNMD Django!',
            'content':" on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )
def about(request):
    return render(
        request,
        "First_Django_APP/about.html",
        {
            'title' : "About HelloDjangoApp",
            'content' : "Example app page for Django."
        }
    )
def hh(request):
    return HttpResponse("SHIT Django!")
