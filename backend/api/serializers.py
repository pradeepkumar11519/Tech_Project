from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from .helpers import getdate,gettime
from .thread import *
from backend.settings import calender_list
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','username','password')
    def create(self, data):
        user = User.objects.create(
            email=data.get('email'),
            password = data.get('password'),
            username=data.get('username'),
            )
        user.set_password(data.get('password'))
        user.save()
        return user
    def validate(seld,data):
        user_email = User.objects.filter(email=data.get('email')).exists()
        if user_email:
            raise serializers.ValidationError({'error':'Email Already Exists Try With Another'})
        else:
            return data 

class ContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contests
        fields = '__all__'

class VerifyOTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email_is_verified","otp","email")

class CalenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calender
        fields = ('contest',)
    def create(self,data):
        user = self.context['request'].user
        calender = Calender.objects.create(
            contest = data.get("contest"),
            user = user,
            contest_name = data.get("contest").Name_Of_Contest,
            contest_link = data.get("contest").Place,
            Added_To_Calender = True,
            contest_start_time = data.get('contest').Start_Time
        )
        calender.save()
        test = Test.objects.create(
            user = user,
            contest_id = data.get("contest").id
        )
        test.save()
        return calender
    
class TestSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"
