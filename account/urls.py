from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'account'

urlpatterns = [
    path('parent-username/', views.get_parent_username,
         name='get_parent_username'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('parent-otp/<int:pk>/', views.get_parent_otp, name='get_parent_otp'),
    path('parent-details/',
         views.get_parent_details, name='get_parent_details'),

]
