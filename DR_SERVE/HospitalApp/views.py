from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    # return HttpResponse("hello hospital home")
    return render(request,'HospitalApp/Home.html')
def Management(request):
    return render(request,'HospitalApp/Management.html')
def About(request):
    return render(request,'HospitalApp/About.html')
def Pricing(request):
    return render(request,'HospitalApp/Pricing.html')
def Make_Payment(request):
    return render(request,'HospitalApp/Make_payment.html')
def Register(request):
    return render(request,'HospitalApp/Register.html')


def Signin(request):
    return render(request,'HospitalApp/Signin.html')

def Forgot_Password(request):
    return render(request,'HospitalApp/Forgot_Password.html')
def Whats_new(request):
    return render(request,"HospitalApp/What's_new.html")
def Contactus(request):
    return render(request,'HospitalApp/Contactus.html')