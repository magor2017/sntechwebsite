from django.urls import path
from . import views
from sntech import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services/',views.service,name='sevice'),
    path('realisations/',views.realisations,name='realisations'),
    path('contact/',views.contact,name='contact'),
   # path('',views.index)
]