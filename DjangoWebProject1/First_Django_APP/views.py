from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("FUCK Django!")

def hh(request):
    return HttpResponse("SHIT Django!")
