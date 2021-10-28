from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from loginapi.models import UserLogin
from django.contrib.auth.models import auth,User

# Create your views here.
def userlogin(request):
    return render(request,'login.html')



def loginindex(request):
    print("entered loginindex method")
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,"logout.html")
        else:
            messages.info(request,"invalid credentials")
            return render(request,'login.html')
    else:
            messages.info(request,"invalid url")
            return redirect('/login')

def logout(request):
    auth.logout(request)
    return redirect('/')


    