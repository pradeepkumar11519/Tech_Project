from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    email_is_verified = models.BooleanField(null=True,default=False,blank=True)
    otp = models.CharField(max_length=10,null=True,blank=True,default=None)
    
    REQUIRED_FIELDS = []
    
class Contests(models.Model):
    id = models.IntegerField(primary_key=True,unique=True)
    Name_Of_Contest = models.CharField(null=True,blank=True,default="-", max_length=225)
    Place = models.CharField(null=True,blank=True,default="Online", max_length=225)
    Start_Time = models.CharField(null=True,blank=True,default="-", max_length=225)
    Name_Of_Website = models.CharField(null=True,blank=True,default="-", max_length=225)
    OnGoing = models.BooleanField(null=True,blank=True,default="-")
    Start_Date = models.CharField(null=True,blank=True,default="-", max_length=225)
    Contest_Type = models.CharField(null=True,blank=True,default=None,max_length=225)
    Contest_Mode = models.CharField(null=True,blank=True,default=None,max_length=225)
    Contest_Duration = models.CharField(null=True,blank=True,default="-", max_length=225)
    Remaining_Time = models.CharField(null=True,blank=True,default="-", max_length=225)
    Days_Remaining_For_The_Contest_To_Start = models.CharField(null=True,blank=True,default="-", max_length=225)
    Days_Remaining_To_Register = models.CharField(null=True,blank=True,default="-", max_length=225)
    Entry_Price = models.IntegerField(null=True,blank=True,default=0)
    Price_Pool = models.IntegerField(null=True,blank=True,default=0)
class Calender(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,to_field="username")
    contest = models.ForeignKey(Contests,on_delete=models.CASCADE)
    Added_To_Calender = models.BooleanField(null=True,default=False,blank=True)
    contest_name = models.CharField(null=True,blank=True,default=None,max_length=225)
    contest_link = models.URLField(null=True,blank=True,default=None)
    contest_start_time = models.CharField(null=True,blank=True,default=None,max_length=225)

class Test(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,to_field="username")
    contest_id = models.IntegerField(null=True,blank=True,default=None)

