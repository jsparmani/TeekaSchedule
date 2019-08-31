from django.urls import path
from . import views

app_name = 'location'

urlpatterns = [
    path('show-nearby-hospitals/', views.get_nearby_hospital,
         name='get_nearby_hospital')
]
