from django.urls import path
from . import views

urlpatterns=[
    path('',views.userlogin),
    path('loggedin',views.loginindex),
    path('logout',views.logout),
    # path('home',views.homepage),
    # path('',views.indexpage),
    # path('welcome',views.welcomepage),

]