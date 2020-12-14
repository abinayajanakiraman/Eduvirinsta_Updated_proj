from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from student_app.models import CustomUser, Staffs,Students,AdminHOD,Superuser

from student_app.EmailBackEnd import EmailBackEnd

def superuser_home(request):
    return render(request,"superuser_template/superuser_home_template.html")

def addsuperuser(request):
    return render(request,"superuser_template/addsuperuser.html")


def addsuperuser_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        print(first_name,last_name,username,email,password)
        print("**************************")

        try:
            user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=4)
            print(user)
            user.save()
            messages.success(request,"Successfully Added addsuperuser")
            return HttpResponseRedirect(reverse("addsuperuser"))
        except:
            messages.error(request,"Failed to Add addsuperuser")
            return HttpResponseRedirect(reverse("addsuperuser"))


def managesuperuser(request):
    superadmin=Superuser.objects.all()
    return render(request,"superuser_template/managesuperadmin.html",{"superadmin":superadmin})


def edit_superadmin(request,superadmin_id):
    superadmin=Superuser.objects.get(admin=superadmin_id)
    return render(request,"superuser_template/edit_superuser.html",{"superadmin":superadmin,"id":superadmin_id})

def edit_superuser_save(request):
    if request.method!='POST':
        HttpResponse("Method Not Allowed")
    else:
        superadmin_id=request.POST.get("superadmin_id")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        username=request.POST.get("username")
        print(superadmin_id,first_name,last_name,email,username)
        print("***********edit*****************")

        try:
            user=CustomUser.objects.get(id=superadmin_id)
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            user.username=username
            user.save()

            superadmin_model=Superuser.objects.get(admin=superadmin_id)
            superadmin_model.save()
        
            messages.success(request,"Successfully Edited SuperAdmin")
            return HttpResponseRedirect(reverse("edit_superadmin",kwargs={"superadmin_id":superadmin_id}))
        except:
            messages.error(request,"Failed to Edit Staff")
            return HttpResponseRedirect(reverse("edit_superadmin",kwargs={"superadmin_id":superadmin_id}))

def delete_superadmin(request,superadmin_id):
    superadmin=Superuser.objects.get(admin=superadmin_id)
    customer=CustomUser.objects.get(id=superadmin_id)
    superadmin.delete()
    customer.delete()
    return HttpResponseRedirect(reverse("managesuperuser"))