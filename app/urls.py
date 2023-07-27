from django.urls import path
from . import views
#from app.views import item_list

urlpatterns = [
   # path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    #path('',views.home, name='home'),
    #path('items/', views.item_list, name='item_list'),
]

