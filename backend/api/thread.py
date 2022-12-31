import threading
from .models import *
import requests
from bs4 import BeautifulSoup
from .models import *
from django.apps import AppConfig
from asgiref.sync import async_to_sync
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
    def run(self):
            self.codeforces()
            self.clist()
    def join(self):
        c = threading.Thread.join(self)