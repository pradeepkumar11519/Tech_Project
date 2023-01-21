from django.apps import AppConfig

import schedule
import time





class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    

    def ready(self):
        from api.helpers import start
        from api.thread import CreateContestsThread
        from backend.settings import calender_list
        x = CreateContestsThread(100,calender_list)
        x.start()
        print("Scraping Started")
        start()