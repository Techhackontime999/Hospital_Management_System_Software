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
