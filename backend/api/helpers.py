import datetime
from datetime import date
import json
from backend.settings import calender_list
from bs4 import BeautifulSoup
from apscheduler.schedulers.background import BackgroundScheduler

import requests
from .thread import *
def getdate():
    today = date.today()
    day = 23
    mydate = datetime.datetime.now()
    month = mydate.strftime("%B")
    year = today.year
    if day == 1 or day == 21 or day ==31:
        current_day = f"{day}st {month} {year}"
    elif day == 3 or day==23:
        current_day = f"{day}rd {month} {year}"
    else:
        current_day = f"{day}th {month} {year}"
    return current_day

def gettime():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    hour = int(current_time[0:2])
    if hour > 12:
        new_time = str(hour - 12) + current_time[2:] + ' pm'
    elif hour == 0:
        new_time = str(12) + current_time[2:] + ' am'
    elif hour < 12:
        new_time = str(hour) + current_time[2:] + ' am'
    elif hour == 12:
        new_time = str(12) + current_time[2:] + ' pm'
    return new_time
def get_contest_month_number(month_name):
    mydate = datetime.datetime.now()
    print(mydate.strptime(month_name, '%b').month)
    return mydate.strptime(month_name, '%b').month





def do_something():
    url = "http://127.0.0.1:8000/api/v1/Scrap_Data_And_Add_To_Data"
    api_request = requests.get(url)
    try:
        api_request.raise_for_status()
        return api_request.json()
    except Exception as e:
        return 

def start():
        scheduler = BackgroundScheduler()
        x = CreateContestsThread(100,calender_list)
        scheduler.add_job(do_something,"interval",days=1,id="Scrapping_001",replace_existing=True)
        scheduler.start()