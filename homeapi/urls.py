from django.urls import path
from . import views

urlpatterns=[
    path('hello',views.hello),
    path('',views.homepage),
    path('index',views.indexpage),
    path('welcome',views.welcomepage),
    path('drf',views.drfview),
   

]