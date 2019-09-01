from .import models


def UserList(request):
    parent_all = [u['user']
                  for u in models.ParentUser.objects.all().values('user')]
    anm_all = [u['user']
               for u in models.ANMUser.objects.all().values('user')]
    ward_all = [u['user']
                for u in models.WardUser.objects.all().values('user')]

    cluster_all = [u['user']
                   for u in models.ClusterUser.objects.all().values('user')]

    district_all = [u['user']
                    for u in models.DistrictUser.objects.all().values('user')]

    return {'parent_all': parent_all, 'anm_all': anm_all, 'ward_all': ward_all, 'cluster_all': cluster_all, 'district_all': district_all}
