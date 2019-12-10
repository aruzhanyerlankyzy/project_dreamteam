from django.shortcuts import render, redirect,reverse
from django.http import HttpResponseRedirect
from reportlab.pdfgen import canvas
from myApp.models import *
from django.http import HttpResponse
import datetime
from django.contrib.auth.models import User,auth
import hashlib
# Create your views here.
def index(request):
    return render(request, "myApp/index.html")
def login(request):
    return render(request, "myApp/login.html")
def registration(request):
    return render(request, "myApp/registration.html")
def profile(request):
    return render(request,"myApp/profile.html")
def logout_act(request):
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == 'POST':
        print(request.POST)
        # form = RegistrationForm()
        # print("FORM", form.is_valid())
        # if form.is_valid():

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
                client.save()
                return HttpResponseRedirect(reverse('login'))
        # else:
        #     return redirect('registration')
    else:
        return render(request, 'myApp/registration.html')

def profile_act(request):
    if request.method == 'POST':
        username=request.POST['username']
        package_name=request.POST['package_name']
        email=request.POST['email']
        pet=request.POST['pet']

        package=Package.objects.create(username=username,
                                       package_name=package_name,
                                       email=email,
                                       pet=pet)
        package.save()

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="receipt.pdf"'
        documentTitile = 'My receipt'
        pdf = canvas.Canvas(response)
        pdf.setTitle(documentTitile)
        pdf.drawString(30, 750, 'DREAM TEAM')
        pdf.drawString(30, 735, 'VETERINARY CLINIC')
        pdf.drawString(500, 750, "10/12/2019")
        pdf.line(480, 747, 580, 747)

        pdf.drawString(275, 725, 'YOUR PACKAGE')
        pdf.drawString(500, 725, package_name)
        pdf.line(378, 723, 580, 723)

        pdf.drawString(30, 703, 'RECEIVED BY:')
        pdf.line(120, 700, 580, 700)
        pdf.drawString(120, 703, username)

        pdf.drawString(30, 650, 'YOUR PET:')
        pdf.line(120, 642, 580, 642)
        pdf.drawString(120, 653, pet)
        pdf.showPage()
        pdf.save()
        response.write(pdf)
        return response
    else:
        return HttpResponseRedirect(reverse('profile'))

def login_act(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        if Client.objects.filter(client_username=username).exists() and Client.objects.filter(client_password=password).exists():
            return HttpResponseRedirect(reverse('profile'))
        else:
            return HttpResponseRedirect(reverse("login"))
    else:
        return HttpResponseRedirect(reverse("login"))

def add_comment(request):
    if request.method=='POST':
        text=request.POST['text']
        editor=request.POST['editor']
        doctor=request.POST['doctor']
        rating=request.POST['rating']

        comment=Comments.objects.create(comments_text=text,
                                        comments_editor=editor,
                                        comments_doctor=doctor,
                                        rating=rating)
        comment.save()
        return HttpResponseRedirect(reverse('profile'))

def rating(request,doctor):
    list=Comments.objects.filter(comments_doctor=doctor)
    sum=0
    for x in list:
        sum+=list.get(rating)
    if(sum==0):
        result=10
    else:
        result=sum/x
    return result

def show_comments(request):
    latest_comments=Comments.objects.get()
    print(latest_comments.comments_text)
    return render(request, "myApp/profile.html", {'latest_comments': latest_comments})




