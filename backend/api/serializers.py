from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from .helpers import getdate,gettime
from .thread import *
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
        
    