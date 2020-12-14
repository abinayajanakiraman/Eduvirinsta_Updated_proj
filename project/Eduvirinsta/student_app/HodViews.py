from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from student_app.models import CustomUser, Staffs,Students,AdminHOD

from student_app.EmailBackEnd import EmailBackEnd


def admin_home(request):
    return render(request,"hod_template/home_content.html")

def add_staff(request):
    return render(request,"hod_template/add_staff_template.html")

def add_staff_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        address=request.POST.get("address")
        stand=request.POST.get("stand")
        print(first_name,last_name,username,email,password,stand,address)
        print("**************************")

        try:
            user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=2)
            print(user)
            user.staffs.address=address
            user.staffs.stand=stand
            user.save()
            messages.success(request,"Successfully Added Staff")
            return HttpResponseRedirect(reverse("add_staff"))
        except:
            messages.error(request,"Failed to Add Staff")
            return HttpResponseRedirect(reverse("add_staff"))

def add_student(request):
    return render(request,"hod_template/add_student_template.html")
def add_student_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        stand=request.POST.get("stand")
        print(first_name,last_name,username,email,password,stand)
        print("**************************")

        try:
            user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=3)
            print(user)
            user.students.stand=stand
            user.save()
            messages.success(request,"Successfully Added Student")
            return HttpResponseRedirect(reverse("add_student"))
        except:
            messages.error(request,"Failed to Add Student")
            return HttpResponseRedirect(reverse("add_student"))
def delete_student(request,student_id):
    p1=Students.objects.get(admin=student_id)
    p2=CustomUser.objects.get(id=student_id)
    p1.delete()
    p2.delete()
    return HttpResponseRedirect(reverse("manage_student"))

def manage_staff(request):
    staffs=Staffs.objects.all()
    return render(request,"hod_template/manage_staff_template.html",{"staffs":staffs})

def manage_student(request):
    students=Students.objects.all()
    return render(request,"hod_template/manage_student_template.html",{"students":students})

def edit_staff(request,staff_id):
    staff=Staffs.objects.get(admin=staff_id)
    return render(request,"hod_template/edit_staff_template.html",{"staff":staff,"id":staff_id})

def edit_staff_save(request):
    if request.method!='POST':
        HttpResponse("Method Not Allowed")
    else:
        staff_id=request.POST.get("staff_id")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        username=request.POST.get("username")
        address=request.POST.get("address")
        stand=request.POST.get("stand")
        print(staff_id,first_name,last_name,email,username,address,stand)
        print("***********edit*****************")

        try:
            user=CustomUser.objects.get(id=staff_id)
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            user.username=username
            user.save()

            staff_model=Staffs.objects.get(admin=staff_id)
            staff_model.address=address
            staff_model.stand=stand
            staff_model.save()
        
            messages.success(request,"Successfully Edited Staff")
            return HttpResponseRedirect(reverse("edit_staff",kwargs={"staff_id":staff_id}))
        except:
            messages.error(request,"Failed to Edit Staff")
            return HttpResponseRedirect(reverse("edit_staff",kwargs={"staff_id":staff_id}))

def delete_staff(request,staff_id):
    staff=Staffs.objects.get(admin=staff_id)
    customer=CustomUser.objects.get(id=staff_id)
    staff.delete()
    customer.delete()
    return HttpResponseRedirect(reverse("manage_staff"))


def edit_student(request,student_id):
    student=Students.objects.get(admin=student_id)
    return render(request,"hod_template/edit_student_template.html",{'student':student,'id':student_id})

def edit_student_save(request):
    if request.method!='POST':
        HttpResponse("Method Not Allowed")
    else:
        student_id=request.POST.get("student_id")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        username=request.POST.get("username")
        stand=request.POST.get("stand")
        print(student_id,first_name,last_name,email,username,stand)
        print("***********edit*****************")

        try:
            user=CustomUser.objects.get(id=student_id)
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            user.username=username
            print("****",user.first_name,user.last_name,user.email,user.username)
            user.save()

            student_model=Students.objects.get(admin=student_id)
            student_model.stand=stand
            print("************",student_model.stand)
            student_model.save()
        
            messages.success(request,"Successfully Edited Student")
            return HttpResponseRedirect(reverse("edit_student",kwargs={"student_id":student_id}))
        except:
            messages.error(request,"Failed to Edit Student")
            return HttpResponseRedirect(reverse("edit_student",kwargs={"student_id":student_id}))
