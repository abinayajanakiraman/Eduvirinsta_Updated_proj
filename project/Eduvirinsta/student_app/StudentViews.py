from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from student_app.models import CustomUser, Staffs,Students,AdminHOD

from student_app.EmailBackEnd import EmailBackEnd


def student_home(request):
    return render(request,"student_template/student_home_template.html")

def student_view_marks(request):
    student=Students.objects.get(admin=request.user.id)
    return render(request,"student_template/student_view.html",{"student":student})
