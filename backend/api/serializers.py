from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from .helpers import getdate,gettime
from .thread import *
class ContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contests
        fields = '__all__'
        
    