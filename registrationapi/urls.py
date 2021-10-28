from django.urls import path
from . import views

urlpatterns=[
    path('',views.registeruser),
    path('displayusers',views.fetchUserDetails),
    path('welcomeuser',views.registerUserDetails)
    # path('home',views.homepage),
    # path('',views.indexpage),
    # path('welcome',views.welcomepage),

]