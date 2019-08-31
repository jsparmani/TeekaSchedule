from django.shortcuts import render, redirect
import threading
from account import models as acc_models
from parent import models as parent_models
from datetime import datetime


def home(request):
    

    def automatic_task():
        threading.Timer(5.0, automatic_task).start()
        reminders = parent_models.Reminder.objects.all().filter(date__exact = '2019-10-04')
        
        # SEND MESSAGE


        for reminder in reminders:
            reminder.delete()

    automatic_task()
    return render(request, 'home.html')


def fault(request, fault):
    return render(request, 'fault.html', {'fault': fault})
