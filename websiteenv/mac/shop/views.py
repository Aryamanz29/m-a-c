from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def index(request):
    return render(request,"shop/index.html")

def about(request):
    return HttpResponse("about")

def contact(request):
    return HttpResponse("contact")

def tracker(request):
    return HttpResponse("tracker")

def search(request):
    return HttpResponse()

def productview(request):
    return HttpResponse()

def checkout(request):
    return HttpResponse()