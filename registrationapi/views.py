from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import auth,User
from django.contrib import messages

from registrationapi.models import UserRegistration

# Create your views here.
def registeruser(request):
    return render(request,'registration.html')

    #fetch values using request object for POST
def registerUserDetails(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['confirmpassword']
    # obj=UserRegistration.objects.create(username=username,
    # obj.save()
        if password==password2:
            if User.objects.filter(username=username).exists():
                print("username taken")
                messages.info(request,"username taken")
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                print("email taken")
                messages.info(request,"email taken")
                return redirect('/register')
            else:

                users=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,
                email=email,password=password)
                users.save()
                print("User created!")
                return redirect('/login')
                
        else:
            print("password taken")
            messages.info(request,"password taken")
            return redirect('/register')
        
        

def fetchUserDetails(request):
    # fn=request.POST['firstname']
    # obj=UserRegistration.objects.create(username=username,
    # obj.save()
    users=User.objects.all()
    return render(request,"userlist.html", {'users':users})
    
   

