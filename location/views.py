from django.shortcuts import render
from . import models
from account import models as acc_models
# Create your views here.


def get_nearby_hospital(request):
    return render(request, 'location/get_nearby_hospital.html')
