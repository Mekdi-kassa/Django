from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"hello/index.html")
def mekdi(request):
    return HttpResponse("I love mekdi")
def happy(request):
    return HttpResponse("I love my happy")
def greet(request,name):
    return render(request,"hello/greet.html",{"name":name})