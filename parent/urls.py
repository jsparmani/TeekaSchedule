from django.urls import path
from . import views

app_name = 'parent'

urlpatterns = [
    path('add-child/', views.add_child, name='add_child'),
    path('child-list-edit-vaccine/', views.edit_vaccine_child, name='edit_vaccine_child'),
    path('child-list-aefi/', views.report_aefi_child, name='child_list_aefi'),
    path('edit-vaccine/<int:pk>/', views.edit_vaccine, name='edit_vaccine'),
    path('set-reminder/', views.set_reminder, name='set_reminder'),
    path('list-child/', views.list_child, name='list_child'),
    path('list-child-vaccine/<int:pk>/', views.list_child_vaccine,
         name='list_child_vaccine'),
    path('report-aefi/<int:pk>/', views.report_aefi,
         name='report_aefi'),
]
