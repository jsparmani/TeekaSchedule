from django.urls import path
from . import views

app_name = 'parent'

urlpatterns = [
    path('add-child/', views.add_child, name='add_child'),
]
