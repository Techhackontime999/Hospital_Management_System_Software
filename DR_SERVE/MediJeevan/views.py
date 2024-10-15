from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Home(request):
    # return HttpResponse("hello hospital home")
    return render(request,'MediJeevan/Home.html')
def About(request):
    return render(request,'MediJeevan/About.html')