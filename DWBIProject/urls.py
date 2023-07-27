"""
Definition of urls for DWBIProject.
"""

from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.views.generic import TemplateView
from app.views import CustomLoginView
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.decorators import login_required as auth_login_required
from django.contrib.auth import views as auth_views

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth.decorators import user_passes_test

def is_superuser(user):
    return user.is_superuser







urlpatterns = [
    path('', CustomLoginView.as_view(), name='home'),
    #path('', login_required(views.home), name='home'),
    path('contact/', login_required(views.contact), name='contact'),
    #path('about/', login_required(views.about), name='about'),
    path('index/', login_required(views.index), name='index'),
     #path('profile/', login_required(views.profile), name='profile'),
     #path('data', views.data, name='data'),
     #path('newdata', views.newdata, name='newdata'),
    #path('login/', LoginView.as_view(
    #    template_name='app/login.html',
    #    authentication_form=forms.BootstrapAuthenticationForm,
    #    extra_context={
    #        'title': 'Log in',
    #        'year': datetime.now().year,
    #    }
    #), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    #path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
     #path('timeout/', TimeoutRedirectView.as_view(), name='timeout'),
    path('admin/',  admin.site.urls),
    path('', login_required(include('app.urls'))),
    #path('allcontactus/', login_required(views.allcontactus), name='allcontactus'),
    path('reports/', login_required(views.reports), name='reports'),
     path('allreport/', login_required(views.allreport), name='allreport'),
      path('crm/', login_required(views.crm), name='crm'),
    #path('excelupload/', login_required(views.excelupload), name='excelupload'),
    #  path('sectorupload/', login_required(views.sectorupload), name='sectorupload'),
    # path('excelupload/', staff_member_required(views.excelupload), name='excelupload'),
    #path('sectorupload/', staff_member_required(views.sectorupload), name='sectorupload'),
   path('excelupload/', user_passes_test(is_superuser)(views.excelupload), name='excelupload'),
    path('sectorupload/', user_passes_test(is_superuser)(views.sectorupload), name='sectorupload'),
 
]

