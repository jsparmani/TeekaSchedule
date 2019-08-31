from django.shortcuts import render, redirect
from . import forms
from . import models
from account import models as acc_models
from datetime import datetime
from datetime import timedelta


# Create your views here.


def add_child(request):
    if request.method == 'POST':
        form = forms.AddChildForm(request.POST)
        if form.is_valid():
            child = models.Child.objects.create(
                name=form.cleaned_data['name'],
                dob=form.cleaned_data['dob'],
            )
            child.parent = acc_models.ParentUser.objects.get(
                user__username__exact=request.user.username)
            child.save()

            vaccine_list = models.VaccinationData.objects.all()
            for vaccine in vaccine_list:
                models.Vaccine.objects.create(
                    child=child,
                    name=vaccine.name,
                    date=child.dob + timedelta(days=vaccine.duration),
                    status=False
                )

            return redirect('home')
        else:
            return redirect('fault', fault="Server error")
    else:
        form = forms.AddChildForm()
        return render(request, 'parent/add_child.html', {'form': form})


def edit_vaccine(request):
    if request.method == 'POST':
        form = forms.EditVaccineForm(request.POST)
        if form.is_valid():
            vaccine_list = models.Vaccine.objects.all().filter(
                date__lte=datetime.now(), status__exact=False, child__parent__user__username=request.user.username)
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
        form = forms.EditVaccineForm()
        return render(request, 'parent/edit_vaccine.html', {'form': form})


def set_reminder(request):

    if request.method=='POST':
        form = forms.SetReminderForm(request.POST)
        if form.is_valid():
            parent = acc_models.ParentUser.objects.get(user__username__exact=request.user.username)
            parent.reminder_days = form.cleaned_data['reminder_days']
            parent.reminder_frequency = form.cleaned_data['reminder_frequency']
            try:
                parent.save()
                return redirect('home')
            except:
                return redirect('fault', fault='Server Error')
        else:
            return redirect('fault', fault='Server Error')
    else:
        form = forms.SetReminderForm()
        return render(request, 'parent/set_reminder.html', {'form':form})
















