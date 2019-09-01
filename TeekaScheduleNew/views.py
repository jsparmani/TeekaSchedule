from django.shortcuts import render, redirect
import threading
from account import models as acc_models
from parent import models as parent_models
from location import models as loc_models
from datetime import datetime
import requests
from django.contrib.auth.models import User


def home(request):

    def automatic_task():
        threading.Timer(86400.0, automatic_task).start()
        reminders = parent_models.Reminder.objects.all().filter(date__exact=datetime.now())

        # SEND MESSAGE TO PARENTS

        for reminder in reminders:
            # link = f'https://2factor.in/API/R1/?module=TRANS_SMS&apikey=563c8dff-70b3-11e9-ade6-0200cd936042&to={reminder.parent.user.username}&from=TKSCHD&templatename=VaccinationReminder&var1={reminder.vaccine.child.name}&var2={reminder.vaccine.date}&var3={reminder.vaccine.name}'
            # requests.get(link)
            reminder.delete()

        reminders_anm = parent_models.ReminderANM.objects.all().filter(
            date__exact=datetime.now())

        for reminder in reminders_anm:
            # print(reminder.user.phone)
            # print(reminder.child.name,
            #       reminder.child.parent.f_name,
            #       reminder.vaccine.name,
            #       reminder.vaccine.date)

            # link = f'https://2factor.in/API/R1/?module=TRANS_SMS&apikey=563c8dff-70b3-11e9-ade6-0200cd936042&to={reminder.user.phone}&from=TKSCHD&templatename=Vaccination+Reminder+ANM&var1={reminder.child.name}&var2={reminder.child.parent.f_name}&var3={reminder.vaccine.name}&var4={reminder.vaccine.date}'
            # requests.get(link)
            reminder.delete()

        vacs = parent_models.Vaccine.objects.all().filter(
            status__exact=False, date__lte=datetime.now())

        for v in vacs:
            pass
            # print(acc_models.ANMUser.objects.get(
            #     locality__exact=v.child.parent.address).phone,
            #     v.child.name,
            #     v.child.parent.f_name,
            #     v.date
            # )

            #link = f'https://2factor.in/API/R1/?module=TRANS_SMS&apikey=563c8dff-70b3-11e9-ade6-0200cd936042&to={acc_models.ANMUser.objects.get(locality__exact=v.child.parent.address).phone}&from=TKSCHD&templatename=Reminders+for+ANM+Missing&var1={v.child.name}&var2={v.child.parent.f_name}&var3={v.name}&var4={v.date}'
            # requests.get(link)

    automatic_task()
    return render(request, 'home.html')


def fault(request, fault):
    return render(request, 'fault.html', {'fault': fault})


def info(request):
    return render(request, 'info.html')


def script(request):

    username = ['8128990569', '7486089677', '6388278796',
                '9758940909', '8279617019', '7896541231']
    for i in range(2, 8):
        user = User.objects.create_user(
            username=f'ANM{i-1}',
            password='testpassword'
        )

        user.save()
        acc_models.ANMUser.objects.create(
            user=user,
            locality=loc_models.Locality.objects.get(pk__exact=i),
            phone=username[i-2]
        )
