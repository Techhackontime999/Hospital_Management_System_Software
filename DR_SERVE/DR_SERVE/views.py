from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Home(request):
    # return HttpResponse("hello home")
    return render(request,'DR_SERVE/Home.html')


def Register(request):
    return render(request,'DR_SERVE/Register.html')
    # return HttpResponse("hello Register")

def SignIn(request):
    return render(request,'DR_SERVE/Signin.html')

def ForgotPassword(request):  
    return render(request,'DR_SERVE/Forgot_Password.html')


