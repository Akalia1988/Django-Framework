# i have created this file - Arsh
from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request, 'index.html')


    #return HttpResponse("Home")

def removepunc(request):
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("capitalize first")


def spaceremove(request):
    return HttpResponse("space remover <a href='/'>back</a>")

def charcount(request):
    return HttpResponse("charcount ")

