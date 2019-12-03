from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from myApp.forms import *
from django.contrib.auth.models import User,auth
import hashlib
# Create your views here.
def index(request):
    return render(request, "myApp/index.html")
def login(request):
    return render(request, "myApp/login.html")
def registration(request):
    return render(request, "myApp/registration.html")

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username=request.POST['client_username']
            first_name = request.POST['client_name']
            last_name = request.POST['client_name']
            pet= request.POST['client_pet']
            telephone=request.POST['client_telephone']
            email=request.POST['client_email']
            password1=request.POST['password1']
            password2 = request.POST['password2']

            if password1==password2:
                if Client.objects.filter(client_surname=username).exists():
                    print('Username taken')
                elif Client.objects.filter(client_email=email).exists():
                        print('Email taken')
                else:
                    client=Client.objects.create(client_username=username,
                                                 client_name=first_name,
                                                 client_surname=last_name,
                                                 client_pet=pet,
                                                 client_telephone=telephone,
                                                 client_email=email,
                                                 client_password=password1)
                    form.save()
                    return redirect("login/")
        else:
            return redirect('registration')
    else:
        return render(request, 'myApp/registration.html')

def profile_premium(request):
    return render(request, "myApp/premium.html")

def login_act(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("myApp/index.html")
        else:
            return redirect("myApp/index.html")
    else:
        return render(request,"myApp/index.html")
