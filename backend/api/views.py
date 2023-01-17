
from rest_framework.generics import *
from django.contrib.auth.models import User
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
import datetime
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .helpers import *
from .models import *
import requests
from bs4 import BeautifulSoup
import json
import sqlite3
from asgiref.sync import async_to_sync
from .thread import *
from .pagination import *
import time
# Create your views here.




class ListContest(ListAPIView):
    queryset = Contests.objects.all()
    serializer_class = ContestSerializer
    def list(self,request):
        start_time = time.time()
        Contests.objects.all().delete()
        x = CreateContestsThread(100)
        x.run()
        queryset = self.get_queryset()
        
        serializer = ContestSerializer(queryset,many=True)
        print("--- %s seconds ---" % (time.time() - start_time))
        return Response(serializer.data)

class CodeForcesContests(ListAPIView):
    
    serializer_class = ContestSerializer
    def list(self,request):
        start_time = time.time()
        Contests.objects.filter(Name_Of_Website="CodeForces").delete()
        x = CreateContestsThread(100)
        x.run_codeforces()
        queryset = Contests.objects.filter(Name_Of_Website="CodeForces")
        
        serializer = ContestSerializer(queryset,many=True)
        print("--- %s seconds ---" % (time.time() - start_time))
        return Response(serializer.data)
class ClistContests(ListAPIView):
    serializer_class = ContestSerializer
    def list(self,request):
        start_time = time.time()
        Contests.objects.filter(Name_Of_Website="Clist").delete()
        x = CreateContestsThread(100)
        x.run_clist()
        queryset = Contests.objects.filter(Name_Of_Website="Clist")
        
        serializer = ContestSerializer(queryset,many=True)
        print("--- %s seconds ---" % (time.time() - start_time))
        return Response(serializer.data)

class ListAllContest(ListAPIView):
    serializer_class = ContestSerializer
    pagination_class = MyContestPagination
    queryset = Contests.objects.all()
class ListAllClistContest(ListAPIView):
    serializer_class = ContestSerializer
    pagination_class = MyClistPagination
    def get_queryset(self):
        return Contests.objects.filter(Name_Of_Website="Clist")

class ListAllCodeForcesContest(ListAPIView):
    serializer_class = ContestSerializer
    pagination_class = MyCodeForcesPagination
    def get_queryset(self):
        return Contests.objects.filter(Name_Of_Website="CodeForces")