from django.shortcuts import render, redirect
from . import forms
import random
from . import models
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from datetime import datetime
# Create your views here.


def get_parent_username(request):

    if request.method == 'POST':
        form = forms.ParentUsernameForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            otp = random.randint(111111, 999999)
            try:
                otp_user = models.OTP.objects.create(
                    username=username,
                    otp=otp,
                    created_at=datetime.now()
                )
            except:
                return redirect('fault', fault="Server Error!")

            print(otp)

            return redirect('account:get_parent_otp', pk=otp_user.pk)

        else:
            return redirect('fault', fault="Server Error!")
    else:
        form = forms.ParentUsernameForm()
        return render(request, 'account/get_parent_username.html', {'form': form})


def get_parent_otp(request, pk):
    otp_user = models.OTP.objects.get(pk__exact=pk)

    if request.method == 'POST':
        form = forms.ParentOTPForm(request.POST)
        if form.is_valid():
            otp = form.cleaned_data['otp']
            if otp == otp_user.otp:
                user = authenticate(request, username=otp_user.username,
                                    password='testpassword')
                if user:
                    auth_login(request, user)
                    return redirect('home')
                else:
                    user = User.objects.create_user(
                        username=otp_user.username,
                        password='testpassword'
                    )
                    user.save()
                    models.ParentUser.objects.create(
                        user=user
                    )
                    user = authenticate(request, username=otp_user.username,
                                        password='testpassword')
                    auth_login(request, user)
                    return redirect('home')
            else:
                return redirect('fault', fault="Invalid Credentials!")
        else:
            return redirect('fault', fault="Server Error!")
    else:
        form = forms.ParentOTPForm()
        return render(request, 'account/get_parent_otp.html', {'form': form})


def get_parent_details(request):
    if request.method == 'POST':
        form = forms.ParentDetailsForm(request.POST)
        if form.is_valid():
            f_name = form.cleaned_data['f_name']
            m_name = form.cleaned_data['m_name']
            f_dob = form.cleaned_data['f_dob']
            m_dob = form.cleaned_data['m_dob']

            print(request.user.username)
            try:
                user = models.ParentUser.objects.get(
                    user__username__exact=request.user.username)
            except:
                return redirect('fault', fault="Server Error")
            user.f_name = f_name
            user.m_name = m_name
            user.f_dob = f_dob
            user.m_dob = m_dob

            user.save()

            return redirect('home')
        else:
            return redirect('fault', fault="Server Error!")
    else:
        form = forms.ParentDetailsForm()
        return render(request, 'account/get_parent_details.html', {'form': form})
