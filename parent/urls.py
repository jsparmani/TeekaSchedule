from django.urls import path
from . import views

app_name = 'parent'

urlpatterns = [
    path('add-child/', views.add_child, name='add_child'),
    path('edit-vaccine/', views.edit_vaccine, name='edit_vaccine'),
    path('set-reminder/', views.set_reminder, name='set_reminder'),
]
