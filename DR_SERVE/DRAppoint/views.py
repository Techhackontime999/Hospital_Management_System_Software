from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Home(request):
    # return HttpResponse("hello hospital home")
    return render(request,'DRAppoint/Home.html')
def About(request):
    # return HttpResponse("hello hospital home")
    return render(request,'DRAppoint/About.html')

def Appointment(request):
    # return HttpResponse("hello hospital home")
    return render(request,'DRAppoint/Appointment.html')    

def SignIn(request):
    # return HttpResponse("hello hospital home")
    return render(request,'DRAppoint/SignIn.html')

def SignUp(request):
    # return HttpResponse("hello hospital home")
    return render(request,'DRAppoint/SignUp.html')

def ForgotPassword(request):
    # return HttpResponse("hello hospital home")
    return render(request,'DRAppoint/Forgot_Password.html')    


def Whats_new(request):
    # return HttpResponse("hello hospital home")
    return render(request,"DRAppoint/What's_new.html")  
def Contactus(request):
    # return HttpResponse("hello hospital home")
    return render(request,'DRAppoint/Contactus.html')  
def Make_Payment(request):
    # return HttpResponse("hello hospital home")
    return render(request,'DRAppoint/Make_Payment.html')  