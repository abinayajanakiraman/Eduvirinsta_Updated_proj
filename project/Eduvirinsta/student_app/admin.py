from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.
from .models import *
class usermodel(UserAdmin):
    pass
# admin.site.register(Super_User)
admin.site.register(CustomUser,usermodel)
# admin.site.register(School_Admin)
# admin.site.register(student)
# admin.site.register(staff)
