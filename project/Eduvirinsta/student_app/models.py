from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class CustomUser(AbstractUser):
    user_type_data=((1,"HOD"),(2,"Staff"),(3,"Student"),(4,'superuser'))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)

class AdminHOD(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    objects=models.Manager()
   

class Staffs(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address=models.CharField(max_length=25)
    stand=models.IntegerField(default=0)
    objects=models.Manager()
    

class Stand(models.Model):
    name=models.IntegerField()
   
class Students(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    stand=models.IntegerField(default=0)
    science=models.IntegerField(default=0)
    Social=models.IntegerField(default=0)
    Maths=models.IntegerField(default=0)
    English=models.IntegerField(default=0)
    Tamil=models.IntegerField(default=0)
    objects = models.Manager()

class Superuser(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    objects=models.Manager()
    
    

@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type==2:
            Staffs.objects.create(admin=instance,address="",stand=0)
        if instance.user_type==3:
            Students.objects.create(admin=instance,stand=0)
        if instance.user_type==4:
            Superuser.objects.create(admin=instance)

@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.adminhod.save()
    if instance.user_type==2:
        instance.staffs.save()
    if instance.user_type==3:
        instance.students.save()
    if instance.user_type==4:
        instance.superuser.save()




