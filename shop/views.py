from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def picture (request):
    return render(request,'shop/picture.html')