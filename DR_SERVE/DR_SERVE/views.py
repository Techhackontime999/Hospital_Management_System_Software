from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Home(request):
    # return HttpResponse("hello home")
    return render(request,'DR_SERVE/Home.html')

def About(request):
    return render(request,'DR_SERVE/About.html')

def Pricing(request):
    return render(request,'DR_SERVE/Pricing.html')

def Contactus(request):
    return render(request,'DR_SERVE/Contactus.html')

def Whats_new(request):
    return render(request,"DR_SERVE/What's_new.html")


def Learn_more(request):
    return render(request,"DR_SERVE/Learn_more.html")



