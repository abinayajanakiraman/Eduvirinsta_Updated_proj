from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from student_app.models import CustomUser, Staffs,Students,AdminHOD

from student_app.EmailBackEnd import EmailBackEnd


def staff_home(request):
    return render(request,"staff_template/staff_home_template.html")

def staff_student(request):
    id=request.user.id
    staff=Staffs.objects.get(admin=id)
    stand=staff.stand
    Student=Students.objects.filter(stand=stand)
    print(Student)
    print(staff)
    print(id,staff,stand)
    return render(request,"staff_template/list_template.html",{'Student':Student,'admin':id})

def update_student_mark(request,student_id):
    student=Students.objects.get(admin=student_id)
    return render(request,"staff_template/edit_mark.html",{'student':student,})

def edit_mark_save(request):
    if request.method!='POST':
        HttpResponse("Method Not Allowed")
    else:
        student_id=request.POST.get("student_id")
        science=request.POST.get("science")
        Social=request.POST.get("Social")
        Maths=request.POST.get("Maths")
        English=request.POST.get("English")
        Tamil=request.POST.get("Tamil")

        try:
            user=CustomUser.objects.get(id=student_id)
            user.save()

            student_model=Students.objects.get(admin=student_id)
            student_model.science=science
            student_model.Social=Social
            student_model.Maths=Maths
            student_model.English=English
            student_model.Tamil=Tamil
            student_model.save()
        
            messages.success(request,"Successfully updated Marks")
            return HttpResponseRedirect(reverse("update_student_mark",kwargs={"student_id":student_id}))
        except:
            messages.error(request,"Failed to update Marks")
            return HttpResponseRedirect(reverse("update_student_mark",kwargs={"student_id":student_id}))

