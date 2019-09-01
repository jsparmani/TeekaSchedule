from django.shortcuts import render
from location import models as loc_models
from account import models as acc_models
from parent import models as parent_models

from datetime import datetime
import json

# Create your views here.


def ward_level_analysis(request):
    ward_user = acc_models.WardUser.objects.get(user__username__exact=request.user.username)
    ward = ward_user.ward
    locality_list = ward.localities.all()
    data_series = [u['name'] for u in locality_list.values('name') ]
    labels = ['Vaccinated','Unvaccinated']
    data = [[],[]]

    for locality in locality_list:
        data[0].append(parent_models.Vaccine.objects.all().filter(child__parent__address__exact=locality, date__lte=datetime.now(), status__exact=True).count())
        data[1].append(parent_models.Vaccine.objects.all().filter(child__parent__address__exact=locality, date__lte=datetime.now(), status__exact=False).count())

    


    data_dict = []

    i=0
    for label in labels:
        data_dict.append({'name':label, 'data':data[i]})
        i+=1



    jsondata = {'data_series': data_series, 'data_dict':data_dict}

    jsondata = json.dumps(jsondata)

    return render(request, 'analyze/graph.html', {'jsondata': jsondata})



def cluster_level_analysis(request):
    cluster_user = acc_models.ClusterUser.objects.get(user__username__exact=request.user.username)
    cluster = cluster_user.cluster
    ward_list = cluster.wards.all()
    data_series = [u['ward_id'] for u in ward_list.values('ward_id') ]
    labels = ['Vaccinated','Unvaccinated']
    data = [[],[]]

    locality_list = []

    data_pie = []

    for ward in ward_list:
        locality_list=[]
        localities = ward.localities.all()
        for loc in localities:
            locality_list.append(loc.pk)
        data[0].append(parent_models.Vaccine.objects.all().filter(child__parent__address__in=locality_list, date__lte=datetime.now(), status__exact=True).count())
        data[1].append(parent_models.Vaccine.objects.all().filter(child__parent__address__in=locality_list, date__lte=datetime.now(), status__exact=False).count())
        data_pie.append({'name': f'Ward {ward.ward_id}', 'y':data[0][-1]})

        

    

    
    data_dict = []

    i=0
    for label in labels:
        data_dict.append({'name':label, 'data':data[i]})
        i+=1



    jsondata = {'data_series': data_series, 'data_dict':data_dict, 'data_pie':data_pie}

    jsondata = json.dumps(jsondata)

    return render(request, 'analyze/graph.html', {'jsondata': jsondata})


def ward_level_indirect_analysis(request, pk):
    ward = loc_models.Ward.objects.get(pk__exact=pk)
    locality_list = ward.localities.all()
    data_series = [u['name'] for u in locality_list.values('name')]
    labels = ['Vaccinated', 'Unvaccinated']
    data = [[], []]

    for locality in locality_list:
        data[0].append(parent_models.Vaccine.objects.all().filter(
            child__parent__address__exact=locality, date__lte=datetime.now(), status__exact=True).count())
        data[1].append(parent_models.Vaccine.objects.all().filter(
            child__parent__address__exact=locality, date__lte=datetime.now(), status__exact=False).count())

    data_dict = []

    i = 0
    for label in labels:
        data_dict.append({'name': label, 'data': data[i]})
        i += 1

    jsondata = {'data_series': data_series, 'data_dict': data_dict}

    jsondata = json.dumps(jsondata)

    return render(request, 'analyze/graph.html', {'jsondata': jsondata})


def ward_list(request):
    cluster_user = acc_models.ClusterUser.objects.get(
        user__username__exact=request.user.username)
    cluster = cluster_user.cluster
    ward_list = cluster.wards.all()
    return render(request, 'analyze/ward_list.html', {'ward_list': ward_list})


def district_level_analysis(request):
    district_user = acc_models.DistrictUser.objects.get(user__username__exact=request.user.username)
    district = district_user.district
    cluster_list = district.clusters.all()
    data_series = [u['cluster_id'] for u in cluster_list.values('cluster_id') ]
    labels = ['Vaccinated','Unvaccinated']
    data = [[],[]]

    locality_list = []


    for cluster in cluster_list:
        locality_list = []
        ward_list = cluster.wards.all()
        for ward in ward_list:
            localities = ward.localities.all()
            for loc in localities:
                locality_list.append(loc.pk)
        data[0].append(parent_models.Vaccine.objects.all().filter(child__parent__address__in=locality_list, date__lte=datetime.now(), status__exact=True).count())
        data[1].append(parent_models.Vaccine.objects.all().filter(child__parent__address__in=locality_list, date__lte=datetime.now(), status__exact=False).count())
            
        

    

    
    data_dict = []

    i=0
    for label in labels:
        data_dict.append({'name':label, 'data':data[i]})
        i+=1



    jsondata = {'data_series': data_series, 'data_dict':data_dict}

    jsondata = json.dumps(jsondata)

    return render(request, 'analyze/graph.html', {'jsondata': jsondata})



