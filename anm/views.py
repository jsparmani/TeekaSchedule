from django.shortcuts import render
from account import models as acc_models
# Create your views here.


def get_parent_list(request):
    parent_list = acc_models.ParentUser.objects.all().filter(
        address__exact=acc_models.ANMUser.objects.get(user__username__exact=request.user.username).locality)
    print(parent_list)
    return render(request, 'anm/parent_list.html', {'parent_list': parent_list})
