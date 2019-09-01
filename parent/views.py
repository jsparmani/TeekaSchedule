from django.shortcuts import render, redirect
from . import forms
from . import models
from account import models as acc_models
from datetime import datetime
from datetime import timedelta

import datetime as datetime_whole
from email.message import EmailMessage
import smtplib
import requests
from django.core.mail import send_mail

# Create your views here.


def add_child(request):
    if request.method == 'POST':
        form = forms.AddChildForm(request.POST)
        if form.is_valid():
            child = models.Child.objects.create(
                name=form.cleaned_data['name'],
                dob=form.cleaned_data['dob'],
                weight=form.cleaned_data['weight']
            )
            child.parent = acc_models.ParentUser.objects.get(
                user__username__exact=request.user.username)
            child.save()

            vaccine_list = models.VaccinationData.objects.all()
            for vaccine in vaccine_list:
                vac = models.Vaccine.objects.create(
                    child=child,
                    name=vaccine.name,
                    date=child.dob + timedelta(days=vaccine.duration),
                    status=False
                )
                models.ReminderANM.objects.create(
                    user=acc_models.ANMUser.objects.get(
                        locality__exact=child.parent.address),
                    vaccine=vac,
                    child=child,
                    date=child.dob + timedelta(days=vaccine.duration-7)
                )

                models.ReminderANM.objects.create(
                    user=acc_models.ANMUser.objects.get(
                        locality__exact=child.parent.address),
                    vaccine=vac,
                    child=child,
                    date=child.dob + timedelta(days=vaccine.duration)
                )

            return redirect('home')
        else:
            return redirect('fault', fault="Server error")
    else:
        form = forms.AddChildForm()
        return render(request, 'parent/add_child.html', {'form': form})


def edit_vaccine_child(request):

    child_list = models.Child.objects.all().filter(
        parent__user__username__exact=request.user.username)
    return render(request, 'parent/child_list_vaccine.html', {'child_list': child_list})


def edit_vaccine(request, pk):
    if request.method == 'POST':
        form = forms.EditVaccineForm(
            data=request.POST, user=request.user, pk=pk)
        if form.is_valid():
            vaccine_list = models.Vaccine.objects.all().filter(
                date__lte=datetime.now(), status__exact=False, child__parent__user__username=request.user.username, child__pk__exact=pk)
            for vaccine in vaccine_list:
                try:
                    status = form.cleaned_data[vaccine.name]
                    vaccine.status = status
                    vaccine.save()
                except:
                    continue
            return redirect('home')
        else:
            return redirect('fault', fault="Server Error!")
    else:
        form = forms.EditVaccineForm(user=request.user, pk=pk)
        return render(request, 'parent/edit_vaccine.html', {'form': form})


def set_reminder(request):

    if request.method == 'POST':
        form = forms.SetReminderForm(request.POST)
        if form.is_valid():
            parent = acc_models.ParentUser.objects.get(
                user__username__exact=request.user.username)
            parent.reminder_days = form.cleaned_data['reminder_days']
            parent.reminder_frequency = form.cleaned_data['reminder_frequency']

            parent.save()

            vaccine_list = models.Vaccine.objects.all().filter(child__parent__user__username=parent.user.username,
                                                               status__exact=False, date__gte=datetime.now())

            for vaccine in vaccine_list:

                for i in range(1, (int(parent.reminder_days)//int(parent.reminder_frequency))+1):
                    models.Reminder.objects.create(
                        parent=parent,
                        vaccine=vaccine,
                        date=(vaccine.date) - timedelta(days=i *
                                                        int(parent.reminder_frequency))
                    )

            return redirect('home')
        else:
            return redirect('fault', fault='Server Error')
    else:
        form = forms.SetReminderForm()
        return render(request, 'parent/set_reminder.html', {'form': form})


def list_child(request):

    children = models.Child.objects.all().filter(
        parent__user__username__exact=request.user.username)

    return render(request, 'parent/list_child.html', {'children': children})


def list_child_vaccine(request, pk):
    vaccine_list = models.Child.objects.get(pk__exact=pk).vaccinnes.all()

    return render(request, 'parent/list_child_vaccine.html', {'vaccine_list': vaccine_list})


def report_aefi_child(request):

    child_list = models.Child.objects.all().filter(
        parent__user__username__exact=request.user.username)
    return render(request, 'parent/child_list_aefi.html', {'child_list': child_list})


def report_aefi(request, pk):

    if request.method == 'POST':
        form = forms.AEFIForm(request.POST)
        if form.is_valid():

            child_age = (datetime_whole.date.today() -
                         models.Child.objects.get(pk__exact=pk).dob).days

            vaccine_min = ''
            vaccine_duration_min = 10000
            vaccine_list = models.VaccinationData.objects.all()

            for vac in vaccine_list:
                try:
                    print(models.Vaccine.objects.get(child__pk__exact=pk,
                                                     name__exact=vac.name, status__exact=True))
                except:
                    continue
                diff = child_age-vac.duration
                print(child_age, diff)
                if (diff > 0):
                    if(diff < vaccine_duration_min):
                        vaccine_min = vac.name
                        vaccine_duration_min = diff
                    elif(diff == vaccine_duration_min):
                        vaccine_min = vaccine_min + f', {vac.name}'
                    else:
                        continue
                else:
                    break

            aefi = form.save(commit=False)
            aefi.child = models.Child.objects.get(pk__exact=pk)
            aefi.vaccine = vaccine_min
            aefi.save()

            send_mail(
                'New AEFI Filed',
                f'A new AEFI has been filed by {aefi.child.parent.f_name} at {datetime.now()}.',
                'harhathkalam.ind@gmail.com',
                ['dniesters@gmail.com'],
                fail_silently=True,
            )

            return redirect('home')
        else:
            return redirect('fault', fault='Server Error')
    else:
        form = forms.AEFIForm()
        return render(request, 'parent/get_aefi_details.html', {'form': form})
