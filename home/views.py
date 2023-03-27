from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import contactEnquiry
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    return render(request, 'home/contact.html')


def saveenquiry(request):
    n = ''
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')
        en = contactEnquiry(name=name, email=email,
                            mobile=mobile, message=message)
        en.save()
        n = 'Message submit'
    return render(request, 'home/contact.html', {'n': n})


def signup(request):
    n = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')

        if password != confirmpassword:
            n = 'confirm password not matched'
            # return HttpResponse("no")
        else:
            my_user = User.objects.create_user(username, email, password)
            my_user.save()
            n = 'Account created successfully!!'

    return render(request, 'home/signup.html', {'n': n})


def signin(request):

    n = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            username = user.username
            return render(request, 'home/index.html', {'username': username})
        else:
            return HttpResponse('user not found')

    return render(request, 'home/signin.html')


def log_out(request):
    logout(request)
    messages.info(request, 'you logged out')
    return redirect('index')
