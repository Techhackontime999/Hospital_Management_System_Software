from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Home(request):
    # return HttpResponse("hello hospital home")
    return render(request,'DR_BLOG/Home.html')
def About(request):
    return render(request,'DR_BLOG/About.html')

