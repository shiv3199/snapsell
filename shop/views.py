from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def picture (request):
    products = Product.objects.order_by('-id')[:]
    return render (request, 'shop/picture.html',{'products': products})

def search (request):
    return HttpResponse("this is search")

def productview (request):
    return HttpResponse("this is product view")

def checkout (request):
    return HttpResponse("this is ceheck out")