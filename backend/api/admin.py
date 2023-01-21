from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Contests)
class ContestAdmin(admin.ModelAdmin):
    list_display = ['id','Place','Name_Of_Contest']
@admin.register(User)
class ContestAdmin(admin.ModelAdmin):
    list_display = ['id',"username","email","otp"]

@admin.register(Calender)
class CalenderAdmin(admin.ModelAdmin):
    list_display = ["id",'user','contest','Added_To_Calender']
@admin.register(Test)
class CalenderAdmin(admin.ModelAdmin):
    list_display = ["user","contest_id"]