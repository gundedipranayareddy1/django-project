from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

#hello worldhttp response  message
def hello(request):
    return HttpResponse("Hello Pranaya!!!.....its home page")

#fetch values using request object for POST
def homepage(request):
    
    return render(request,'home.html')

#fetch values using request object for POST
def welcomepage(request):
    firstname=request.POST['firstname']
    
    return render(request,'welcome.html', {'firstname':firstname})



#Pass values from one page to other
def indexpage(request):
    return render(request,'index.html')

    #drf test
def drfview(request):
    dict1={
        'id':1,
        'name':'pranayareddyg',
        

    }
    return JsonResponse(dict1)