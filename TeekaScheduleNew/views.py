from django.shortcuts import render, redirect
import threading
from account import models as acc_models
from parent import models as parent_models
from datetime import datetime
import requests


def home(request):

    def automatic_task():
        threading.Timer(5.0, automatic_task).start()
        reminders = parent_models.Reminder.objects.all().filter(date__exact='2019-10-04')

        # SEND MESSAGE TO PARENTS

        for reminder in reminders:
            reminder.delete()

        reminders_anm = parent_models.ReminderANM.objects.all().filter(
            date__exact='2019-10-17')

        api_key = '292a8d1f-295e-11e9-9ee8-0200cd936042'

        for reminder in reminders_anm:
            print(reminder.user.phone)
            print(reminder.child.name,
                reminder.child.parent.f_name,
                reminder.vaccine.name,
                reminder.vaccine.date)

            # link = f'https://2factor.in/API/R1/?module=TRANS_SMS&apikey={api_key}&to={phone_num}&from=TKSCHD&templatename={template_name}&var1={name}&var2={complaint_type}&var3={}'
            # requests.get(link)
            reminder.delete()

        vacs = parent_models.Vaccine.objects.all().filter(
            status__exact=False, date__lte=datetime.now())

        for v in vacs:
            print(acc_models.ANMUser.objects.get(
                locality__exact=v.child.parent.address).phone,
                v.child.name,
                v.child.parent.f_name,
                v.date
            )

    automatic_task()
    return render(request, 'home.html')


def fault(request, fault):
    return render(request, 'fault.html', {'fault': fault})
