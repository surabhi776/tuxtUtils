from django.http import HttpResponse
from django.shortcuts import render

#WE HAVE CREATE FUNCTION
#def index(request):
    #return HttpResponse('''<h1>Surabhi</h1> <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> Django codewithHarry</a>>''')

def index(request):
    return render(request, )
   # return HttpResponse("Home")

def removepunc(request):
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse("capitize first")

def newline(request):
    return HttpResponse("new one items are added")

def space(request):
    return HttpResponse("you are an space")
