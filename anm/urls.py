from django.urls import path
from . import views

app_name = 'anm'

urlpatterns = [
    path('parent-list/', views.get_parent_list, name='get_parent_list')
]
