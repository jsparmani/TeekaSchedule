from django.urls import path
from . import views


app_name = 'analyze'

urlpatterns = [

    path('ward-level-analysis/', views.ward_level_analysis, name='ward_level_analysis'),
    path('cluster-level-analysis/', views.cluster_level_analysis, name='cluster_level_analysis'),
    path('district-level-analysis/', views.district_level_analysis, name='district_level_analysis'),

]