from django.shortcuts import render

from vacationsapi.models import Vacations

# Create your views here.
def vacations(request):
    vacations=Vacations.objects.all()
    return render(request,'vacations.html',{'vacations':vacations})


# def saveVacations(request):
#     if request.method=='POST':
#         place=request.POST['place']
#         image=request.POST['image']
#         price=request.POST['price']
#         travel=request.POST['travel']
#         food=request.POST['food']
#         accomodation=request.POST['accomodation']
#     # obj=UserRegistration.objects.create(username=username,
#     # obj.save()
        
#         users=Vacations.objects.create(first_name=first_name,last_name=last_name,username=username,
#         email=email,password=password)
#         users.save()
#         print("User created!")
#         return redirect('/login')
        
        

# def fetchVacations(request):
#     # fn=request.POST['firstname']
#     # obj=UserRegistration.objects.create(username=username,
#     # obj.save()
#     vacations=Vacations.objects.all()
#     return render(request,"vacations.html", {'vacations':vacations})
    