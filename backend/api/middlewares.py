import requests
from bs4 import BeautifulSoup
from .models import Contests
from .thread import *
class MyMiddleWare:
    def __init__(self,get_response):
        self.get_response = get_response
        print('One Time Initialization')
    def __call__(self,request):
        response = self.get_response(request)
        
        if hasattr(request, 'path') and 'api/v1/ListContest/' in request.path:
            
            response = self.get_response(request)
            print('this is after view')
        return response