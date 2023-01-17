import threading
from .models import *
import requests
from bs4 import BeautifulSoup
from .models import *
from django.apps import AppConfig
from asgiref.sync import async_to_sync
import time 
import pandas as pd 
from selenium import webdriver 
from selenium.webdriver import Chrome 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import time 
import pandas as pd 
from selenium import webdriver 
from selenium.webdriver import Chrome 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
# Create your views here.




class CreateContestsThread(threading.Thread):
    def __init__(self,total):
        self.total = total
        threading.Thread.__init__(self)
    def codeforces(self):
            html = requests.get('https://codeforces.com/contests').text
            soup = BeautifulSoup(html, 'lxml')
            template = soup.find('table')
            hackths = template.find_all('tr')[1:]
            hackathons = []
            for hackt in hackths:
                hackathon = []
                tds = hackt.find_all('td')
                hackathon.append(tds[0].text.lstrip().rstrip()) #name of contest
                hackathon.append("Online") #place
                hackathon.append(tds[2].a.span.text.lstrip().rstrip()) #satrt time
                hackathon.append(tds[3].text.lstrip(). rstrip()) #contest duration
                if tds[4].span.span is None:
                    hackathon.append(tds[4].span.text.lstrip().rstrip()) #days remoaing for the contest to start
                else:
                    hackathon.append(tds[4].span.span.text.lstrip().rstrip())
                if(tds[5].a != None):
                    hackathon.append('Registration in Open!') #days remainig to register
                else:
                    if(tds[5].span.span is None):
                        hackathon.append(tds[5].span.text)
                    else:
                        hackathon.append(tds[5].span.span.text.lstrip().rstrip())#days remaining to register
                hackathons.append(list(hackathon))
            
            for i in range(len(hackathons)):
                
                Contests.objects.create(
                    Name_Of_Contest=hackathons[i][0], 
                    Place=hackathons[i][1],
                    Start_Time=hackathons[i][2],
                    Contest_Duration=hackathons[i][3],
                    OnGoing = False,
                    Name_Of_Website = 'CodeForces',
                    Days_Remaining_For_The_Contest_To_Start=hackathons[i][4],
                    Days_Remaining_To_Register=hackathons[i][5],
                )
    def clist(self):

        html_text = requests.get('https://clist.by').text

        soup = BeautifulSoup(html_text, 'lxml')

        ongoing = soup.findAll('div', class_='contest row running bg-success')
        coming = soup.findAll('div', class_='contest row coming')

        for data in ongoing:
            Contests.objects.create(
                Name_Of_Contest = data.find('div', class_='col-md-7 col-sm-8 event').find('a', class_='title_search').text.replace('\n', '').strip(),
                Place = data.find('div', class_='col-md-7 col-sm-8 event').find('a', class_='title_search').get('href'),
                Start_Time = data.find('div', class_='col-md-5 col-sm-12 start-time').text.replace('\n', '').strip(),
                OnGoing = True,
                Name_Of_Website = "Clist",
                Contest_Duration = data.find('div', class_='col-md-3 col-sm-6 duration').text.replace('\n', '').strip()
            )
        for data in coming:
            Contests.objects.create(
                Name_Of_Contest = data.find('div', class_='col-md-7 col-sm-8 event').find('a', class_='title_search').text.replace('\n', '').strip(),
                Place = data.find('div', class_='col-md-7 col-sm-8 event').find('a', class_='title_search').get('href'),
                OnGoing = False,
                Name_Of_Website = "Clist",
                Start_Time = data.find('div', class_='col-md-5 col-sm-12 start-time').text.replace('\n', '').strip(),
                Contest_Duration = data.find('div', class_='col-md-3 col-sm-6 duration').text.replace('\n', '').strip()
            )
    def codechef(self):


        # start by defining the options 
        options = webdriver.ChromeOptions() 
        options.headless = True # it's more scalable to work in headless mode 
        # normally, selenium waits for all resources to download 
        # we don't need it as the page also populated with the running javascript code. 
        options.page_load_strategy = 'none' 
        # this returns the path web driver downloaded 
        chrome_path = ChromeDriverManager().install() 
        chrome_service = Service(chrome_path) 
        # pass the defined options and service objects to initialize the web driver 
        driver = Chrome(options=options, service=chrome_service) 
        driver.implicitly_wait(5)

        url = "https://www.codechef.com/contests" 
        
        driver.get(url) 
        # time.sleep(20)
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, '_table__container_jhph2_249')))

        u_o_contests = driver.find_elements(By.CLASS_NAME, '_table__container_jhph2_249')

        o_c = u_o_contests[0]
        u_c = u_o_contests[1]

        open_contests = []
        upcoming_contests = []

        o_contests = o_c.find_elements(By.CLASS_NAME, '_data__container_jhph2_382')
        u_contests = u_c.find_elements(By.CLASS_NAME, '_data__container_jhph2_382')

        for c in o_contests:
            con_details = {}
            con_details['name'] = c.find_element(By.TAG_NAME, 'span').text
            con_details['ends'] = c.find_element(By.CLASS_NAME, '_timer__container_jhph2_402').text
            # print(con_details)
            open_contests.append(con_details)
            
        for c in u_contests:
            con_details = {}
            con_details['name'] = c.find_element(By.TAG_NAME, 'span').text
            time = c.find_element(By.CLASS_NAME, '_timer__container_jhph2_402').find_elements(By.TAG_NAME, 'p')
            con_details['starts'] = time[0].text + ' ' + time[1].text
            # print(con_details)
            upcoming_contests.append(con_details)
            print('open',open_contests)
            print('upcoming',upcoming_contests)
    def run_codeforces(self):
            self.codeforces()
    def run_clist(self):
            self.clist()
    def run(self):
        self.codeforces()
        self.clist()
    def join(self):
        c = threading.Thread.join(self)
