import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from student_app.EmailBackEnd import EmailBackEnd

def ShowDemoPage(request):
    return render(request,"demo.html")


def ShowLoginPage(request):
    return render(request,"login_page.html")

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("Method not allowded")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        print(user)
        if user!=None:
            login(request,user)
            if user.user_type=="1":
                return HttpResponseRedirect('/superuser_home')
            elif user.user_type=="2":
                return HttpResponseRedirect(reverse("staff_home"))
            elif user.user_type=='3':
                return HttpResponseRedirect(reverse("student_home"))
            else:
                return HttpResponseRedirect('/admin_home')
        else:
            messages.error(request,"Invalid Login")
            return HttpResponse("Invalid")

def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("user:"+request.user.email+"Password:"+request.user.user_type)
    else:
        return HttpResponse("please login first")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")
