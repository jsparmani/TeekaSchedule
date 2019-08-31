from django.shortcuts import render, redirect
import threading
from account import models as acc_models


def home(request):
    

    def automatic_task():
        threading.Timer(5.0, printit).start()
        parents = acc_models.ParentUser.objects.get(user__username__exact='9758940909')
        # print(parents.reminder_days, parents.reminder_frequency)
    automatic_task()
    return render(request, 'home.html')


def fault(request, fault):
    return render(request, 'fault.html', {'fault': fault})
