"""TeekASchedule URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls', namespace='account')),
    path('parent/', include('parent.urls', namespace='parent')),
    path('location/', include('location.urls', namespace='location')),
    path('anm/', include('anm.urls', namespace='anm')),
    path('analyze/', include('analyze.urls', namespace='analyze')),
    path('', views.home, name='home'),
    path('', include('pwa.urls')),
    path('script/', views.script, name='script'),
    path('faq/', views.faq, name='faq'),
    path('info/', views.info, name='info'),
    path('fault/<str:fault>/', views.fault, name='fault'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
