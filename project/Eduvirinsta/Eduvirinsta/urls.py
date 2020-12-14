"""Eduvirinsta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

from student_app import views
from Eduvirinsta import settings
from student_app import HodViews
from student_app import StudentViews
from student_app import StaffViews
from student_app import superuserViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo',views.ShowDemoPage),
    path('',views.ShowLoginPage,name="show_login"),
    path('doLogin',views.doLogin,name="do_login"),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user,name="logout"),
    path('admin_home',HodViews.admin_home,name="admin_home"),
    path('add_staff',HodViews.add_staff,name="add_staff"),
    path('add_staff_save',HodViews.add_staff_save,name="add_staff_save"),
    path('add_student', HodViews.add_student,name="add_student"),
    path('add_student_save', HodViews.add_student_save,name="add_student_save"),
    
    path('manage_staff', HodViews.manage_staff,name="manage_staff"),
    path('manage_student', HodViews.manage_student,name="manage_student"),
    path('edit_staff/<str:staff_id>', HodViews.edit_staff,name="edit_staff"),
    path('edit_staff_save', HodViews.edit_staff_save,name="edit_staff_save"),
    path('edit_student/<str:student_id>', HodViews.edit_student,name="edit_student"),
    path('edit_student_save', HodViews.edit_student_save,name="edit_student_save"),
    path('delete_student/<str:student_id>',HodViews.delete_student,name="delete_student"),
    path('delete_staff/<str:staff_id>',HodViews.delete_staff,name="delete_staff"),
    
    path('staff_home', StaffViews.staff_home, name="staff_home"),
    path('staff_student',StaffViews.staff_student,name="staff_student"),
    path('update_student_mark/<str:student_id>',StaffViews.update_student_mark,name="update_student_mark"),
    path('edit_mark_save',StaffViews.edit_mark_save,name="edit_mark_save"),
    


    path('student_home', StudentViews.student_home, name="student_home"),
    path('student_view_marks',StudentViews.student_view_marks,name="student_view_marks"),
    

    path('superuser_home',superuserViews.superuser_home,name="superuser_home"),
    path('addsuperuser',superuserViews.addsuperuser,name="addsuperuser"),
    path('addsuperuser_save',superuserViews.addsuperuser_save,name="addsuperuser_save"),
    path('managesuperuser',superuserViews.managesuperuser,name="managesuperuser"),
    path('edit_superadmin/<str:superadmin_id>',superuserViews.edit_superadmin,name="edit_superadmin"),
    path('edit_superuser_save',superuserViews.edit_superuser_save,name="edit_superuser_save"),
    path('delete_superadmin/<str:superadmin_id>',superuserViews.delete_superadmin,name="delete_superadmin"),
    

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)