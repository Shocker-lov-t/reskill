from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("This is my Django Application")
def index2(request):
    return HttpResponse("This IS 2nd Page Of My Django Application")