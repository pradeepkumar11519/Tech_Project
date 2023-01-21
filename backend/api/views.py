
from rest_framework.generics import *
from django.contrib.auth.models import User
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
import datetime
from rest_framework.permissions import IsAuthenticated
from .helpers import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import *
from .thread import *
from .pagination import *
import time
from django.http import JsonResponse
from backend.settings import calender_list
from .emails import *
from rest_framework.filters import SearchFilter
# Create your views here.

print(calender_list)

class Scrap_Data_And_Add_To_Data(APIView):
    def get(self,request):
        start_time = time.time()
        Contests.objects.all().delete()
        x = CreateContestsThread(100,calender_list)
        x.run()
        print("--- %s seconds ---" % (time.time() - start_time))
        return Response("Process Done Succesfully",status=status.HTTP_200_OK)

        
class Signup(APIView):
    def post(self,request):
            data = request.data
            serializer = UserSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                send_otp_via_email(serializer.data["email"])
                return Response({"email":serializer.data["email"]},status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):
    def post(self,request):
        username = request.data['username']
        password = request.data['password']
        email = request.data['email']

        # checking for errors
        user = User.objects.filter(username=username).first()
        
        print(user)
        if user is None:
                    return Response({'error': 'invalid username or password'}, status=status.HTTP_404_NOT_FOUND)
        if not user.check_password(password):
                    return Response({'error': 'invalid username or password'},status=status.HTTP_404_NOT_FOUND)
        if user.email_is_verified==False:
            return Response({'error': 'invalid username or password'},status=status.HTTP_404_NOT_FOUND)
        else:
            if email == user.email:
                    refresh = RefreshToken.for_user(user)
                    user.last_login = datetime.datetime.now()
                    user.save()
                    choice1 = ['orange','pink','yellow','red','black','rose']
                    
                    return Response({
                        'message': 'login successfull',
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                        'username':user.username,
                        'last_login_date':getdate(),
                        'last_login_time':gettime(),
                        'email':user.email},
                        status=status.HTTP_200_OK)
                    
                    
            else:
                return Response({'errors':'email not matched'},status=status.HTTP_404_NOT_FOUND)

       
class ListAllContest(ListAPIView):
    serializer_class = ContestSerializer
    pagination_class = MyContestPagination
    filter_backends = [SearchFilter]
    search_fields = ['Contest_Mode','Contest_Type']
    queryset = Contests.objects.all()
class ListContest(ListAPIView):
    serializer_class = ContestSerializer
    filter_backends = [SearchFilter]
    search_fields = ['Contest_Mode','Contest_Type']
    queryset = Contests.objects.all()


class VerifyOTP(APIView):
    def post(self,request):
            data = request.data
            serializer = VerifyOTPSerializer(data = data)
            if serializer.is_valid():
                email = serializer.data["email"]
                otp = serializer.data["otp"]
                user = User.objects.filter(email=email)
                if not user.exists():
                    return Response("UnAuthorized",status=status.HTTP_401_UNAUTHORIZED)
                if user[0].otp != otp:
                    return Response("Wrong Otp Please Retry",status=status.HTTP_400_BAD_REQUEST)
                user = user.first()
                user.email_is_verified = True
                user.save()
            return Response('OTP Succesfully Verified',status=status.HTTP_200_OK)
            
class AddToCalender(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class =  CalenderSerializer
    queryset = Calender.objects.all()
    def list(self,request):
        user = self.request.user
        test = Test.objects.filter(user = user)
        serializer = TestSerialzier(test,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

        
class ListCalenderContests(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get_serializer_class(self):
         return CalenderSerializer
    def get_queryset(self):
        data = self.request.data
        user = self.request.user
        print(data)
        New_Date = f"{data['month'].upper()}/{data['day']}/{datetime.date.today().year}"
        print(New_Date)
        calender = Calender.objects.filter(user = user).filter(contest_start_time = New_Date).values()
        return calender
    def post(self,request):
        calender = self.get_queryset()
        json_calender = json.dumps(list(calender))
        return Response(json_calender,status=status.HTTP_200_OK)
        
class ListTodaysCalender(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CalenderSerializer
    def list(self,request):
        calender = self.get_queryset().values()
        json_calender = json.dumps(list(calender))
        return Response(json_calender,status=status.HTTP_200_OK)
    def get_queryset(self):
        user = self.request.user
        New_Date = f"{get_contest_month_name(datetime.date.today().month).upper()}/{datetime.date.today().day}/{datetime.date.today().year}"
        Calender_Contest = Calender.objects.filter(user = user).filter(contest_start_time = New_Date)
        return Calender_Contest

class SendTestData(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TestSerialzier