from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("hello,mekdi")
def mekdi(request):
    return HttpResponse("I love mekdi")
def happy(request):
    return HttpResponse("I love my happy")